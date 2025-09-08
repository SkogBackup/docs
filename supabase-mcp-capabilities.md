# Supabase MCP Server Capabilities

## Overview
The Supabase MCP server provides direct access to manage and interact with your Supabase projects through Claude.

## Available Functions

### Project Management

#### `list_projects()`
Lists all Supabase projects in your account.
- **Use when**: You need to see all projects or find a project ID
- **Returns**: Project details including ID, name, region, status

#### `get_project(id)`
Gets detailed information about a specific project.
- **Use when**: You need project status, database version, or connection details
- **Parameters**: `id` - The project ID

#### `create_project(name, region, organization_id, confirm_cost_id)`
Creates a new Supabase project.
- **Use when**: Setting up a new application database
- **Note**: Requires cost confirmation first via `confirm_cost()`

#### `pause_project(project_id)` / `restore_project(project_id)`
Pauses or restores a project to manage costs.
- **Use when**: Temporarily stopping unused projects or reactivating them

### Database Operations

#### `list_tables(project_id, schemas=['public'])`
Lists all tables in specified schemas.
- **Use when**: Exploring database structure
- **Returns**: Table names, columns, data types, constraints, RLS status

#### `execute_sql(project_id, query)`
Executes raw SQL queries (SELECT, INSERT, UPDATE, DELETE).
- **Use when**: Querying or modifying data
- **Note**: Use `apply_migration()` for DDL operations

#### `apply_migration(project_id, name, query)`
Applies DDL migrations (CREATE, ALTER, DROP).
- **Use when**: Creating/modifying tables, indexes, functions
- **Best practice**: Use snake_case names for migrations

#### `list_migrations(project_id)`
Shows all applied migrations.
- **Use when**: Checking migration history

#### `generate_typescript_types(project_id)`
Generates TypeScript types from database schema.
- **Use when**: Building type-safe frontend applications

### Extensions & Configuration

#### `list_extensions(project_id)`
Lists all PostgreSQL extensions.
- **Use when**: Checking available database capabilities

#### `get_project_url(project_id)` / `get_anon_key(project_id)`
Gets API endpoint and anonymous key.
- **Use when**: Configuring client applications

### Edge Functions

#### `list_edge_functions(project_id)`
Lists all deployed Edge Functions.

#### `deploy_edge_function(project_id, name, files, entrypoint_path='index.ts')`
Deploys serverless functions.
- **Use when**: Creating API endpoints, webhooks, or background jobs
- **Example structure**:
  ```typescript
  import "jsr:@supabase/functions-js/edge-runtime.d.ts";
  
  Deno.serve(async (req: Request) => {
    return new Response(JSON.stringify({ message: "Hello" }), {
      headers: { 'Content-Type': 'application/json' }
    });
  });
  ```

### Branching (Development)

#### `create_branch(project_id, name='develop', confirm_cost_id)`
Creates a development branch with fresh database.
- **Use when**: Testing migrations before production
- **Note**: Branches get their own project_id

#### `list_branches(project_id)`
Shows all branches and their status.

#### `merge_branch(branch_id)`
Merges branch migrations to production.
- **Use when**: Deploying tested changes

#### `reset_branch(branch_id)` / `rebase_branch(branch_id)`
Resets or rebases branch to handle drift.

### Monitoring & Debugging

#### `get_logs(project_id, service)`
Fetches recent logs (last minute).
- **Services**: 'api', 'postgres', 'edge-function', 'auth', 'storage', 'realtime'
- **Use when**: Debugging errors or monitoring activity

#### `get_advisors(project_id, type)`
Gets security and performance recommendations.
- **Types**: 'security', 'performance'
- **Use when**: After schema changes to catch issues (missing RLS, indexes)
- **Important**: Run regularly, especially after DDL changes

### Cost Management

#### `get_cost(organization_id, type)`
Gets pricing for creating projects/branches.
- **Types**: 'project', 'branch'

#### `confirm_cost(type, recurrence, amount)`
Confirms understanding of costs before creation.
- **Returns**: confirmation ID for create operations

### Documentation

#### `search_docs(graphql_query)`
Searches Supabase documentation using GraphQL.
- **Use when**: Looking up how to implement features
- **Example query**:
  ```graphql
  query {
    searchDocs(query: "row level security", limit: 5) {
      nodes {
        title
        href
        content
      }
    }
  }
  ```

## Common Workflows

### 1. Database Setup
```
1. list_projects() - Find project
2. list_tables(project_id) - Explore structure
3. apply_migration() - Create tables
4. get_advisors(project_id, 'security') - Check for issues
```

### 2. Data Operations
```
1. execute_sql() - Query/modify data
2. get_logs(project_id, 'postgres') - Monitor queries
```

### 3. Safe Deployment
```
1. create_branch() - Test environment
2. apply_migration() on branch - Test changes
3. merge_branch() - Deploy to production
```

### 4. Client Setup
```
1. get_project_url() - Get API endpoint
2. get_anon_key() - Get public key
3. generate_typescript_types() - Get types
```

## Best Practices

1. **Always use migrations** for schema changes (not execute_sql)
2. **Run advisors** after schema changes to catch security issues
3. **Use branches** for testing destructive changes
4. **Check logs** when debugging issues (only shows last minute)
5. **Document migrations** with descriptive names
6. **Enable RLS** on tables with user data
7. **Use TypeScript types** for type-safe development

## Connection Strings

- **Direct**: For persistent connections (servers)
- **Transaction Pooler**: For serverless functions  
- **Session Pooler**: For IPv4 networks

## Important Notes

- Migrations are permanent once applied
- Branch data doesn't copy from production
- Logs only show last 60 seconds
- RLS policies are critical for security
- Edge Functions run on Deno runtime