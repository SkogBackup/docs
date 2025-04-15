#!/usr/bin/env node
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ErrorCode,
  ListPromptsRequestSchema,
  ListResourcesRequestSchema,
  ListToolsRequestSchema,
  McpError,
  ReadPromptRequestSchema,
  ReadResourceRequestSchema
} from '@modelcontextprotocol/sdk/types.js';
import * as path from 'path';
import * as fs from 'fs';
import Database from 'better-sqlite3';

// Parse command line arguments
const args = process.argv.slice(2);
let dbPath = ':memory:'; // Default to in-memory database

for (let i = 0; i < args.length; i++) {
  if (args[i] === '--db-path' && i + 1 < args.length) {
    dbPath = args[i + 1];
    if (dbPath.startsWith('~')) {
      dbPath = path.join(process.env.HOME || process.env.USERPROFILE || '', dbPath.slice(1));
    }
    break;
  }
}

// Initialize the database
const db = new Database(dbPath);
console.error(`SQLite database initialized at: ${dbPath}`);

// Store insights in memory for the memo resource
let businessInsights: string[] = [];

class SqliteServer {
  private server: Server;

  constructor() {
    this.server = new Server(
      {
        name: 'sqlite-mcp-server',
        version: '1.0.0',
      },
      {
        capabilities: {
          resources: {},
          tools: {},
          prompts: {}
        },
      }
    );

    this.setupResourceHandlers();
    this.setupToolHandlers();
    this.setupPromptHandlers();
    
    // Error handling
    this.server.onerror = (error) => console.error('[MCP Error]', error);
    process.on('SIGINT', async () => {
      await this.server.close();
      process.exit(0);
    });
  }

  private setupResourceHandlers() {
    this.server.setRequestHandler(ListResourcesRequestSchema, async () => ({
      resources: [
        {
          uri: 'memo://insights',
          name: 'Business Insights Memo',
          mimeType: 'text/plain',
          description: 'A continuously updated memo of business insights discovered during data analysis'
        }
      ],
    }));

    this.server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
      if (request.params.uri === 'memo://insights') {
        return {
          contents: [
            {
              uri: request.params.uri,
              mimeType: 'text/plain',
              text: businessInsights.length > 0 
                ? `# Business Insights Memo\n\n${businessInsights.map((insight, index) => `${index + 1}. ${insight}`).join('\n\n')}`
                : '# Business Insights Memo\n\nNo insights have been recorded yet. Use the append_insight tool to add business insights discovered during your analysis.'
            },
          ],
        };
      }

      throw new McpError(
        ErrorCode.ResourceNotFound,
        `Resource not found: ${request.params.uri}`
      );
    });
  }

  private setupToolHandlers() {
    this.server.setRequestHandler(ListToolsRequestSchema, async () => ({
      tools: [
        {
          name: 'read_query',
          description: 'Execute SELECT queries to read data from the database',
          inputSchema: {
            type: 'object',
            properties: {
              query: {
                type: 'string',
                description: 'The SELECT SQL query to execute'
              }
            },
            required: ['query']
          }
        },
        {
          name: 'write_query',
          description: 'Execute INSERT, UPDATE, or DELETE queries',
          inputSchema: {
            type: 'object',
            properties: {
              query: {
                type: 'string',
                description: 'The SQL modification query'
              }
            },
            required: ['query']
          }
        },
        {
          name: 'create_table',
          description: 'Create new tables in the database',
          inputSchema: {
            type: 'object',
            properties: {
              query: {
                type: 'string',
                description: 'CREATE TABLE SQL statement'
              }
            },
            required: ['query']
          }
        },
        {
          name: 'list_tables',
          description: 'Get a list of all tables in the database',
          inputSchema: {
            type: 'object',
            properties: {},
            required: []
          }
        },
        {
          name: 'describe_table',
          description: 'View schema information for a specific table',
          inputSchema: {
            type: 'object',
            properties: {
              table_name: {
                type: 'string',
                description: 'Name of table to describe'
              }
            },
            required: ['table_name']
          }
        },
        {
          name: 'append_insight',
          description: 'Add new business insights to the memo resource',
          inputSchema: {
            type: 'object',
            properties: {
              insight: {
                type: 'string',
                description: 'Business insight discovered from data analysis'
              }
            },
            required: ['insight']
          }
        }
      ],
    }));

    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      try {
        switch (request.params.name) {
          case 'read_query': {
            const { query } = request.params.arguments as { query: string };
            if (!query.trim().toLowerCase().startsWith('select')) {
              throw new McpError(
                ErrorCode.InvalidParams,
                'Only SELECT queries are allowed with read_query'
              );
            }
            
            try {
              const stmt = db.prepare(query);
              const results = stmt.all();
              return {
                content: [
                  {
                    type: 'text',
                    text: JSON.stringify(results, null, 2)
                  }
                ]
              };
            } catch (error) {
              return {
                content: [
                  {
                    type: 'text',
                    text: `SQL Error: ${error instanceof Error ? error.message : String(error)}`
                  }
                ],
                isError: true
              };
            }
          }
          
          case 'write_query': {
            const { query } = request.params.arguments as { query: string };
            const lowerQuery = query.trim().toLowerCase();
            
            if (lowerQuery.startsWith('select')) {
              throw new McpError(
                ErrorCode.InvalidParams,
                'SELECT queries are not allowed with write_query. Use read_query instead.'
              );
            }
            
            try {
              const stmt = db.prepare(query);
              const result = stmt.run();
              return {
                content: [
                  {
                    type: 'text',
                    text: JSON.stringify({ affected_rows: result.changes }, null, 2)
                  }
                ]
              };
            } catch (error) {
              return {
                content: [
                  {
                    type: 'text',
                    text: `SQL Error: ${error instanceof Error ? error.message : String(error)}`
                  }
                ],
                isError: true
              };
            }
          }
          
          case 'create_table': {
            const { query } = request.params.arguments as { query: string };
            
            if (!query.trim().toLowerCase().startsWith('create table')) {
              throw new McpError(
                ErrorCode.InvalidParams,
                'Query must start with CREATE TABLE'
              );
            }
            
            try {
              const stmt = db.prepare(query);
              stmt.run();
              return {
                content: [
                  {
                    type: 'text',
                    text: 'Table created successfully'
                  }
                ]
              };
            } catch (error) {
              return {
                content: [
                  {
                    type: 'text',
                    text: `SQL Error: ${error instanceof Error ? error.message : String(error)}`
                  }
                ],
                isError: true
              };
            }
          }
          
          case 'list_tables': {
            try {
              const stmt = db.prepare("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name");
              const tables = stmt.all().map(row => row.name);
              return {
                content: [
                  {
                    type: 'text',
                    text: JSON.stringify(tables, null, 2)
                  }
                ]
              };
            } catch (error) {
              return {
                content: [
                  {
                    type: 'text',
                    text: `SQL Error: ${error instanceof Error ? error.message : String(error)}`
                  }
                ],
                isError: true
              };
            }
          }
          
          case 'describe_table': {
            const { table_name } = request.params.arguments as { table_name: string };
            
            try {
              // Check if table exists
              const tableCheck = db.prepare("SELECT name FROM sqlite_master WHERE type='table' AND name = ?");
              const tableExists = tableCheck.get(table_name);
              
              if (!tableExists) {
                throw new Error(`Table '${table_name}' does not exist`);
              }
              
              const stmt = db.prepare(`PRAGMA table_info(${table_name})`);
              const columns = stmt.all();
              return {
                content: [
                  {
                    type: 'text',
                    text: JSON.stringify(columns, null, 2)
                  }
                ]
              };
            } catch (error) {
              return {
                content: [
                  {
                    type: 'text',
                    text: `Error: ${error instanceof Error ? error.message : String(error)}`
                  }
                ],
                isError: true
              };
            }
          }
          
          case 'append_insight': {
            const { insight } = request.params.arguments as { insight: string };
            
            if (!insight || insight.trim() === '') {
              throw new McpError(
                ErrorCode.InvalidParams,
                'Insight cannot be empty'
              );
            }
            
            businessInsights.push(insight.trim());
            return {
              content: [
                {
                  type: 'text',
                  text: 'Insight added to memo successfully'
                }
              ]
            };
          }
          
          default:
            throw new McpError(
              ErrorCode.MethodNotFound,
              `Unknown tool: ${request.params.name}`
            );
        }
      } catch (error) {
        if (error instanceof McpError) {
          throw error;
        }
        
        return {
          content: [
            {
              type: 'text',
              text: `Error: ${error instanceof Error ? error.message : String(error)}`
            }
          ],
          isError: true
        };
      }
    });
  }

  private setupPromptHandlers() {
    this.server.setRequestHandler(ListPromptsRequestSchema, async () => ({
      prompts: [
        {
          name: 'mcp-demo',
          description: 'Interactive prompt that guides users through database operations',
          inputSchema: {
            type: 'object',
            properties: {
              topic: {
                type: 'string',
                description: 'The business domain to analyze'
              }
            },
            required: ['topic']
          }
        }
      ]
    }));

    this.server.setRequestHandler(ReadPromptRequestSchema, async (request) => {
      if (request.params.name !== 'mcp-demo') {
        throw new McpError(
          ErrorCode.ResourceNotFound,
          `Prompt not found: ${request.params.name}`
        );
      }

      const { topic } = request.params.arguments as { topic: string };
      
      return {
        content: `# SQLite MCP Server Demo - ${topic} Analysis

You now have access to a SQLite database for business analytics. I can help you:

1. Create tables for ${topic} data
2. Insert sample data 
3. Run queries to analyze the data
4. Extract business insights

Let me show you how to use the available tools.

## Creating Tables

First, let's create a sample table appropriate for ${topic}. Here's an example using the \`create_table\` tool:

\`\`\`typescript
// Example for a retail business
use_mcp_tool({
  server_name: "github.com/modelcontextprotocol/servers/tree/main/src/sqlite",
  tool_name: "create_table",
  arguments: {
    query: "CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, category TEXT, price REAL, inventory INTEGER);"
  }
})
\`\`\`

## Inserting Data

Next, use the \`write_query\` tool to insert data:

\`\`\`typescript
use_mcp_tool({
  server_name: "github.com/modelcontextprotocol/servers/tree/main/src/sqlite", 
  tool_name: "write_query",
  arguments: {
    query: "INSERT INTO products (name, category, price, inventory) VALUES ('Widget A', 'Electronics', 19.99, 42);"
  }
})
\`\`\`

## Querying Data

Use the \`read_query\` tool to retrieve and analyze data:

\`\`\`typescript
use_mcp_tool({
  server_name: "github.com/modelcontextprotocol/servers/tree/main/src/sqlite",
  tool_name: "read_query",
  arguments: {
    query: "SELECT * FROM products WHERE price < 20.00;"
  }
})
\`\`\`

## Viewing Schema

List all tables with the \`list_tables\` tool:

\`\`\`typescript
use_mcp_tool({
  server_name: "github.com/modelcontextprotocol/servers/tree/main/src/sqlite",
  tool_name: "list_tables",
  arguments: {}
})
\`\`\`

Examine a table's structure with the \`describe_table\` tool:

\`\`\`typescript
use_mcp_tool({
  server_name: "github.com/modelcontextprotocol/servers/tree/main/src/sqlite",
  tool_name: "describe_table",
  arguments: {
    table_name: "products"
  }
})
\`\`\`

## Recording Business Insights

When you discover something interesting, add it to the insights memo:

\`\`\`typescript
use_mcp_tool({
  server_name: "github.com/modelcontextprotocol/servers/tree/main/src/sqlite",
  tool_name: "append_insight",
  arguments: {
    insight: "Products under $20 account for 35% of our inventory but generate only 15% of revenue."
  }
})
\`\`\`

Access the continuously updated insights memo:

\`\`\`typescript
access_mcp_resource({
  server_name: "github.com/modelcontextprotocol/servers/tree/main/src/sqlite",
  uri: "memo://insights"
})
\`\`\`

Let's begin exploring your ${topic} data. Would you like me to create an appropriate database schema for ${topic}?`
      };
    });
  }

  async run() {
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    console.error('SQLite MCP server running on stdio');
  }
}

const server = new SqliteServer();
server.run().catch(console.error);
