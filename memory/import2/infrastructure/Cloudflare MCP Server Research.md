---
title: Cloudflare MCP Server Research
type: note
permalink: infrastructure/cloudflare-mcp-server-research
---

# Cloudflare MCP Server Research

## Key Findings

### Official Cloudflare MCP Servers (14+)
- All are **remote servers** using OAuth 2.1 authentication
- No local installation required
- Hosted at specific URLs (e.g., `https://observability.mcp.cloudflare.com/sse`)

**Available Services:**
- **Developer Platform**: Workers Bindings, Builds, Container Server, Documentation
- **Security & Observability**: Audit Logs, DEX, CASB, Observability  
- **Analytics**: DNS Analytics, Radar, AI Gateway, Logpush

### Missing Official Services
- **Cloudflare Tunnels/cloudflared** - No dedicated tunnel management MCP
- **Direct DNS record management** - Only analytics available
- **CDN/Cache configuration** - No direct cache rule management
- **Zero Trust policy management** - Limited to CASB

### Community Solutions
- `@gutmutcode/mcp-server-cloudflare` (npm) - Comprehensive API access
- Requires stdio/local installation with API token
- Covers Workers, KV, R2, D1, domain analytics
- Still no tunnel functionality

### Installation Methods
**Remote (Official):**
```json
{
  "mcpServers": {
    "cloudflare-observability": {
      "command": "npx",
      "args": ["mcp-remote", "https://observability.mcp.cloudflare.com/sse"]
    }
  }
}
```

**Stdio/Local (Community):**
```json
{
  "mcpServers": {
    "cloudflare-api": {
      "command": "npx", 
      "args": ["-y", "@gutmutcode/mcp-server-cloudflare"],
      "env": {
        "CLOUDFLARE_API_TOKEN": "your-api-token"
      }
    }
  }
}
```

## Tunnel Management Gap

For Cloudflare Tunnels, would need custom stdio-based MCP server because:
- Requires local `cloudflared` daemon access
- Security constraints prevent remote tunnel management
- No existing implementation found

## Next Steps
- Could build custom tunnel MCP server wrapping `cloudflared` CLI
- Monitor for official tunnel MCP server release
- Test community servers for current functionality

## Relations
- relates_to [[MCP Development Tools]]
- follows_up_on [[Cloudflare API Integration]]