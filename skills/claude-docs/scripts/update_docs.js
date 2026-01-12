#!/usr/bin/env node

/**
 * update_docs.js
 *
 * Fetches the latest Claude Code documentation from docs.claude.com
 * and saves it to the references/ directory.
 *
 * Usage: node scripts/update_docs.js
 */

const https = require("https");
const fs = require("fs");
const path = require("path");

// const LLMS_TXT_URL = "https://platform.claude.com/llms.txt";
const LLMS_TXT_URL = "https://code.claude.com/docs/llms.txt";
//https://code.claude.com/docs/llms.txt

// Currently fetches Developer Guide sections:
// - claude-code: CLI tool documentation
// - agent-sdk: SDK reference (Python/TypeScript)
// - agents-and-tools: Tool use, skills, MCP connectors
//
// Other available sections (not currently fetched):
// - /docs/en/api/: API reference (messages, batches, models, admin, etc.)
// - /docs/en/build-with-claude/: Building guides (prompt engineering, streaming, etc.)
// - /docs/en/about-claude/: General info (models, pricing, glossary)
// - /docs/en/resources/: Prompt library and use case guides
// - /docs/en/test-and-evaluate/: Testing and evaluation guides
// - /docs/en/release-notes/: Release notes
//
// Alternative approach: Use https://platform.claude.com/llms-full.txt
// which contains all documentation already rendered as markdown in a single file
//
// https://code.claude.com/docs/en/overview
// const CLAUDE_CODE_PATTERN =
// /https:\/\/platform\.claude\.com\/docs\/en\/(?:claude-code|resources|build-with-claude|agent-sdk|agents-and-tools)\/[^\s)]+\.md/g;
const CLAUDE_CODE_PATTERN = /https:\/\/code\.claude\.com\/docs\/[^\s)]+\.md/g;
const REFERENCES_DIR = path.join(__dirname, "..", "references");

/**
 * Fetch content from a URL using https module
 */
function fetchUrl(url) {
  return new Promise((resolve, reject) => {
    https
      .get(url, (res) => {
        let data = "";
        res.on("data", (chunk) => (data += chunk));
        res.on("end", () => {
          if (res.statusCode >= 200 && res.statusCode < 300) {
            resolve(data);
          } else {
            reject(new Error(`HTTP ${res.statusCode}: ${res.statusMessage}`));
          }
        });
      })
      .on("error", reject);
  });
}

/**
 * Extract Claude Code doc URLs from llms.txt
 */
async function getClaudeCodeUrls() {
  console.log("📥 Fetching llms.txt...");
  const content = await fetchUrl(LLMS_TXT_URL);

  const urls = new Set();
  const matches = content.matchAll(CLAUDE_CODE_PATTERN);

  for (const match of matches) {
    urls.add(match[0]);
  }

  return Array.from(urls).sort();
}

/**
 * Extract subdirectory path from URL
 * Example: https://platform.claude.com/docs/en/claude-code/hooks.md
 *   -> claude-code
 * Example: https://platform.claude.com/docs/en/resources/prompt-library/git-gud.md
 *   -> resources/prompt-library
 */
function getSubdirFromUrl(url) {
  const match = url.match(/\/docs\/en\/(.+?)\/[^\/]+\.md$/);
  return match ? match[1] : "";
}

/**
 * Fetch and save a single documentation page
 */
async function fetchAndSaveDoc(url) {
  const filename = path.basename(url);
  const subdir = getSubdirFromUrl(url);
  const targetDir = subdir ? path.join(REFERENCES_DIR, subdir) : REFERENCES_DIR;
  const filepath = path.join(targetDir, filename);

  try {
    // Ensure subdirectory exists
    if (subdir && !fs.existsSync(targetDir)) {
      fs.mkdirSync(targetDir, { recursive: true });
    }

    const displayPath = subdir ? `${subdir}/${filename}` : filename;
    console.log(`  Fetching ${displayPath}...`);
    const content = await fetchUrl(url);
    fs.writeFileSync(filepath, content, "utf8");
    return { url, filename, success: true };
  } catch (error) {
    const displayPath = subdir ? `${subdir}/${filename}` : filename;
    console.error(`  ❌ Failed to fetch ${displayPath}: ${error.message}`);
    return { url, filename, success: false, error: error.message };
  }
}

/**
 * Main execution
 */
async function main() {
  console.log("🚀 Claude Code Documentation Updater\n");

  // Ensure references directory exists
  if (!fs.existsSync(REFERENCES_DIR)) {
    fs.mkdirSync(REFERENCES_DIR, { recursive: true });
  }

  // Get all Claude Code documentation URLs
  const urls = await getClaudeCodeUrls();
  console.log(`✅ Found ${urls.length} Claude Code documentation pages\n`);

  // Fetch all documentation pages
  console.log("📥 Downloading documentation...");
  const results = [];
  for (const url of urls) {
    const result = await fetchAndSaveDoc(url);
    results.push(result);
    // Small delay to be nice to the server
    await new Promise((resolve) => setTimeout(resolve, 100));
  }

  // Summary
  const successful = results.filter((r) => r.success).length;
  const failed = results.filter((r) => !r.success).length;

  console.log(`\n✅ Documentation update complete!`);
  console.log(`   ${successful} files downloaded successfully`);
  if (failed > 0) {
    console.log(`   ${failed} files failed to download`);
  }
  console.log(`\n📁 Documentation saved to: ${REFERENCES_DIR}`);
}

// Run if called directly
if (require.main === module) {
  main().catch((error) => {
    console.error("❌ Error:", error.message);
    process.exit(1);
  });
}

module.exports = { getClaudeCodeUrls, fetchAndSaveDoc };
