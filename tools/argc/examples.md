---
title: argc examples
type: tool
permalink: docs/tools/argc/examples.md
tags: [argc, examples, patterns, recipes]
---

# argc practical examples

real-world patterns and complete examples.

## basic cli examples

### simple file processor

```sh
#!/usr/bin/env bash
# @describe Process text files with various operations
# @meta version 1.0.0

# @option -i --input! <FILE>  Input file
# @option -o --output <FILE>  Output file (default: stdout)
# @option --format[upper|lower|title]=lower  Text transformation
# @flag -v --verbose  Verbose output

eval "$(argc --argc-eval "$0" "$@")"

[[ $argc_verbose -eq 1 ]] && echo "processing $argc_input" >&2

case $argc_format in
    upper) transform='tr "[:lower:]" "[:upper:]"' ;;
    lower) transform='tr "[:upper:]" "[:lower:]"' ;;
    title) transform='sed "s/\b\(.\)/\u\1/g"' ;;
esac

if [[ -n "$argc_output" ]]; then
    eval "$transform" < "$argc_input" > "$argc_output"
    [[ $argc_verbose -eq 1 ]] && echo "output written to $argc_output" >&2
else
    eval "$transform" < "$argc_input"
fi
```

usage:
```sh
./process.sh -i input.txt --format upper -o output.txt -v
```

### configuration manager

```sh
#!/usr/bin/env bash
# @describe Manage application configuration

# @cmd show current configuration
# @option --format[json|yaml|env]=json  Output format
show() {
    case $argc_format in
        json) cat config.json ;;
        yaml) yq eval config.json ;;
        env) jq -r 'to_entries|.[]|"\(.key)=\(.value)"' config.json ;;
    esac
}

# @cmd get configuration value
# @arg key!  Configuration key (dot notation)
get() {
    jq -r ".$argc_key" config.json
}

# @cmd set configuration value
# @arg key!  Configuration key
# @arg value!  New value
set() {
    jq ".$argc_key = \"$argc_value\"" config.json > config.json.tmp
    mv config.json.tmp config.json
    echo "set $argc_key = $argc_value"
}

# @cmd delete configuration key
# @arg key!  Configuration key
delete() {
    jq "del(.$argc_key)" config.json > config.json.tmp
    mv config.json.tmp config.json
    echo "deleted $argc_key"
}

eval "$(argc --argc-eval "$0" "$@")"
```

usage:
```sh
./config.sh show --format yaml
./config.sh get database.host
./config.sh set database.port 5432
./config.sh delete cache.enabled
```

### git workflow helper

```sh
#!/usr/bin/env bash
# @describe Git workflow automation

# @cmd create feature branch
# @arg name!  Feature name
feature() {
    local branch="feature/$argc_name"
    git checkout -b "$branch"
    echo "created and switched to $branch"
}

# @cmd create hotfix branch
# @arg name!  Hotfix name
hotfix() {
    local branch="hotfix/$argc_name"
    git checkout main
    git pull origin main
    git checkout -b "$branch"
    echo "created hotfix branch $branch from main"
}

# @cmd finish branch and create PR
# @flag -d --draft  Create as draft PR
# @arg title  PR title (default: branch name)
finish() {
    local branch=$(git branch --show-current)
    local title="${argc_title:-$branch}"

    git push -u origin "$branch"

    if [[ $argc_draft -eq 1 ]]; then
        gh pr create --title "$title" --draft
    else
        gh pr create --title "$title"
    fi
}

# @cmd sync with main
sync() {
    local current=$(git branch --show-current)
    git checkout main
    git pull origin main
    git checkout "$current"
    git merge main
    echo "synced $current with main"
}

eval "$(argc --argc-eval "$0" "$@")"
```

usage:
```sh
./git-flow.sh feature user-authentication
./git-flow.sh hotfix security-patch
./git-flow.sh sync
./git-flow.sh finish "Add user authentication" --draft
```

## argcfile.sh examples

### node.js project

```sh
#!/usr/bin/env bash
# @describe Node.js project automation
set -e

# @cmd install dependencies
install() {
    npm install
}

# @cmd run development server
# @flag -w --watch  Enable watch mode
# @option --port=3000  Server port
dev() {
    local args=""
    [[ $argc_watch -eq 1 ]] && args="--watch"
    PORT=$argc_port npm run dev $args
}

# @cmd run type checker
# @flag -w --watch  Watch mode
typecheck() {
    [[ $argc_watch -eq 1 ]] && flags="--watch" || flags="--noEmit"
    tsc $flags
}

# @cmd run linter
# @flag -f --fix  Auto-fix issues
lint() {
    [[ $argc_fix -eq 1 ]] && flags="--fix" || flags=""
    eslint src/ $flags
}

# @cmd run tests
# @flag -w --watch  Watch mode
# @flag -c --coverage  Generate coverage
# @arg pattern  Test pattern
test() {
    local args=""
    [[ $argc_watch -eq 1 ]] && args="--watch"
    [[ $argc_coverage -eq 1 ]] && args="$args --coverage"
    [[ -n "$argc_pattern" ]] && args="$args $argc_pattern"
    jest $args
}

# @cmd build for production
build() {
    typecheck
    lint
    test
    npm run build
}

# @cmd clean generated files
clean() {
    rm -rf dist/ node_modules/ coverage/ .next/
}

# @cmd run full CI pipeline
ci() {
    install
    build
}

eval "$(argc --argc-eval "$0" "$@")"
```

usage:
```sh
argc install
argc dev --port 8080 --watch
argc test -w
argc build
argc ci
```

### rust project

```sh
#!/usr/bin/env bash
# @describe Rust project automation
set -e

# @cmd build project
# @flag -r --release  Release build
# @option --target  Target triple
build() {
    local args=""
    [[ $argc_release -eq 1 ]] && args="--release"
    [[ -n "$argc_target" ]] && args="$args --target $argc_target"
    cargo build $args
}

# @cmd run project
# @flag -r --release  Run release build
# @arg args~  Arguments to pass
run() {
    [[ $argc_release -eq 1 ]] && flags="--release" || flags=""
    cargo run $flags -- ${argc_args[@]}
}

# @cmd run tests
# @flag --doc  Run doc tests only
# @flag --integration  Run integration tests only
# @arg pattern  Test pattern
test() {
    local args=""
    [[ $argc_doc -eq 1 ]] && args="--doc"
    [[ $argc_integration -eq 1 ]] && args="--test '*'"
    [[ -n "$argc_pattern" ]] && args="$args $argc_pattern"
    cargo test $args
}

# @cmd run benchmarks
bench() {
    cargo bench
}

# @cmd check code without building
check() {
    cargo check --all-targets
}

# @cmd run clippy
# @flag -f --fix  Auto-fix issues
clippy() {
    [[ $argc_fix -eq 1 ]] && flags="--fix" || flags=""
    cargo clippy --all-targets -- -D warnings $flags
}

# @cmd format code
# @flag -c --check  Check formatting without modifying
fmt() {
    [[ $argc_check -eq 1 ]] && flags="--check" || flags=""
    cargo fmt --all $flags
}

# @cmd clean build artifacts
clean() {
    cargo clean
}

# @cmd full ci pipeline
ci() {
    fmt --check
    clippy
    test
    build --release
}

# @cmd publish to crates.io
# @flag -n --dry-run  Dry run
publish() {
    [[ $argc_dry_run -eq 1 ]] && flags="--dry-run" || flags=""
    cargo publish $flags
}

eval "$(argc --argc-eval "$0" "$@")"
```

usage:
```sh
argc build --release
argc test --integration
argc clippy --fix
argc ci
argc publish --dry-run
```

### docker project

```sh
#!/usr/bin/env bash
# @describe Docker project management
set -e

# @cmd
docker() { :; }

# @cmd build images
# @flag --no-cache  Build without cache
# @arg services*  Specific services (default: all)
docker::build() {
    local args=""
    [[ $argc_no_cache -eq 1 ]] && args="--no-cache"
    docker-compose build $args ${argc_services[@]}
}

# @cmd start services
# @flag -d --detach  Run in background
# @arg services*  Specific services (default: all)
docker::up() {
    docker::build ${argc_services[@]}
    [[ $argc_detach -eq 1 ]] && flags="-d" || flags=""
    docker-compose up $flags ${argc_services[@]}
}

# @cmd stop services
# @arg services*  Specific services (default: all)
docker::down() {
    docker-compose down ${argc_services[@]}
}

# @cmd restart services
# @arg services*  Specific services (default: all)
docker::restart() {
    docker-compose restart ${argc_services[@]}
}

# @cmd view logs
# @flag -f --follow  Follow logs
# @option -n --tail=100  Number of lines
# @arg services*  Specific services (default: all)
docker::logs() {
    local args="--tail $argc_tail"
    [[ $argc_follow -eq 1 ]] && args="$args -f"
    docker-compose logs $args ${argc_services[@]}
}

# @cmd execute command in service
# @arg service!  Service name
# @arg cmd~  Command to execute
docker::exec() {
    docker-compose exec $argc_service ${argc_cmd[@]}
}

# @cmd show running containers
docker::ps() {
    docker-compose ps
}

# @cmd
db() { :; }

# @cmd backup database
# @option --output=backup.sql  Backup file
db::backup() {
    docker-compose exec -T db pg_dump -U postgres myapp > "$argc_output"
    echo "database backed up to $argc_output"
}

# @cmd restore database
# @arg file!  Backup file
db::restore() {
    docker-compose exec -T db psql -U postgres myapp < "$argc_file"
    echo "database restored from $argc_file"
}

# @cmd reset database
# @flag -f --force  Skip confirmation
db::reset() {
    if [[ $argc_force -eq 1 ]]; then
        confirmed=y
    else
        read -p "reset database? (y/N) " -n 1 -r confirmed
        echo
    fi

    if [[ $confirmed =~ ^[Yy]$ ]]; then
        docker-compose exec db psql -U postgres -c "DROP DATABASE IF EXISTS myapp"
        docker-compose exec db psql -U postgres -c "CREATE DATABASE myapp"
        echo "database reset"
    fi
}

eval "$(argc --argc-eval "$0" "$@")"
```

usage:
```sh
argc docker build web api
argc docker up -d
argc docker logs -f web
argc docker exec web bash
argc db backup --output prod-backup.sql
argc db restore prod-backup.sql
```

## advanced patterns

### multi-environment deployment

```sh
#!/usr/bin/env bash
# @describe Deploy application to various environments
# @meta dotenv

# @cmd deploy application
# @arg env[dev|staging|prod]!  Target environment
# @flag --skip-tests  Skip test suite
# @flag --skip-build  Skip build step
# @env DEPLOY_KEY!  Deployment key
# @env DEPLOY_HOST!  Deployment host
deploy() {
    echo "deploying to $argc_env environment..."

    # load env-specific config
    source ".env.$argc_env"

    # run tests
    if [[ $argc_skip_tests -eq 0 ]]; then
        echo "running tests..."
        npm test || { echo "tests failed" >&2; exit 1; }
    fi

    # build
    if [[ $argc_skip_build -eq 0 ]]; then
        echo "building..."
        NODE_ENV=$argc_env npm run build
    fi

    # deploy
    echo "deploying to $argc_DEPLOY_HOST..."
    rsync -avz --delete dist/ "deploy@$argc_DEPLOY_HOST:/var/www/app/"

    # restart service
    ssh "deploy@$argc_DEPLOY_HOST" "sudo systemctl restart app"

    echo "deployment to $argc_env complete"
}

# @cmd rollback deployment
# @arg env[dev|staging|prod]!  Target environment
# @arg version!  Version to rollback to
rollback() {
    source ".env.$argc_env"
    ssh "deploy@$argc_DEPLOY_HOST" "cd /var/www/app && git checkout v$argc_version && sudo systemctl restart app"
    echo "rolled back $argc_env to version $argc_version"
}

eval "$(argc --argc-eval "$0" "$@")"
```

### database migration tool

```sh
#!/usr/bin/env bash
# @describe Database migration management

# @cmd create new migration
# @arg name!  Migration name
create() {
    local timestamp=$(date +%Y%m%d%H%M%S)
    local filename="migrations/${timestamp}_${argc_name}.sql"

    mkdir -p migrations
    cat > "$filename" <<-EOF
-- migration: $argc_name
-- created: $(date)

-- up
BEGIN;

-- add your migration here

COMMIT;

-- down
BEGIN;

-- add rollback here

COMMIT;
EOF
    echo "created migration: $filename"
}

# @cmd run pending migrations
# @flag -n --dry-run  Show what would run
# @env DATABASE_URL!  Database connection
migrate() {
    local migrations=(migrations/*.sql)

    for migration in "${migrations[@]}"; do
        local name=$(basename "$migration")

        # check if already applied
        if psql "$argc_DATABASE_URL" -tAc \
           "SELECT 1 FROM migrations WHERE name='$name'" | grep -q 1; then
            continue
        fi

        if [[ $argc_dry_run -eq 1 ]]; then
            echo "would run: $name"
        else
            echo "running: $name"
            psql "$argc_DATABASE_URL" <<-SQL
                BEGIN;
                $(sed -n '/-- up/,/-- down/p' "$migration" | grep -v -- '-- down')
                INSERT INTO migrations (name, applied_at) VALUES ('$name', NOW());
                COMMIT;
SQL
            echo "applied: $name"
        fi
    done
}

# @cmd rollback last migration
# @flag -f --force  Skip confirmation
rollback() {
    local last=$(psql "$argc_DATABASE_URL" -tAc \
                 "SELECT name FROM migrations ORDER BY applied_at DESC LIMIT 1")

    if [[ -z "$last" ]]; then
        echo "no migrations to rollback" >&2
        exit 1
    fi

    if [[ $argc_force -eq 0 ]]; then
        read -p "rollback $last? (y/N) " -n 1 -r
        echo
        [[ ! $REPLY =~ ^[Yy]$ ]] && exit 0
    fi

    echo "rolling back: $last"
    psql "$argc_DATABASE_URL" <<-SQL
        BEGIN;
        $(sed -n '/-- down/,\$p' "migrations/$last" | tail -n +2)
        DELETE FROM migrations WHERE name='$last';
        COMMIT;
SQL
    echo "rolled back: $last"
}

# @cmd show migration status
status() {
    echo "applied migrations:"
    psql "$argc_DATABASE_URL" -c "SELECT * FROM migrations ORDER BY applied_at"

    echo -e "\npending migrations:"
    local applied=$(psql "$argc_DATABASE_URL" -tAc "SELECT name FROM migrations")
    for migration in migrations/*.sql; do
        local name=$(basename "$migration")
        echo "$applied" | grep -q "$name" || echo "  $name"
    done
}

eval "$(argc --argc-eval "$0" "$@")"
```

## completion examples

### dynamic git branch completion

```sh
#!/usr/bin/env bash
# @describe Git branch operations

# @cmd checkout branch
# @arg branch[`_choice_branches`]!  Branch to checkout
checkout() {
    git checkout "$argc_branch"
}

# @cmd delete branch
# @arg branches+[`_choice_branches`]  Branches to delete
# @flag -f --force  Force delete
delete() {
    [[ $argc_force -eq 1 ]] && flags="-D" || flags="-d"
    for branch in "${argc_branches[@]}"; do
        git branch $flags "$branch"
    done
}

_choice_branches() {
    git branch -a | cut -c3- | sed 's/^remotes\///'
}

eval "$(argc --argc-eval "$0" "$@")"
```

### service management with descriptions

```sh
#!/usr/bin/env bash
# @describe Manage application services

# @cmd start service
# @arg service[`_choice_services`]!  Service to start
start() {
    systemctl start "$argc_service"
}

_choice_services() {
    cat <<-'EOF'
web	Web server (nginx)
api	API server (node)
worker	Background worker (celery)
db	Database (postgres)
cache	Redis cache
queue	Message queue (rabbitmq)
EOF
}

eval "$(argc --argc-eval "$0" "$@")"
```

## references

- more examples: `@src/argc/examples/`
- cli authoring: `@docs/tools/argc/cli-authoring.md`
- task automation: `@docs/tools/argc/task-automation.md`
- completions: `@docs/tools/argc/completions.md`
