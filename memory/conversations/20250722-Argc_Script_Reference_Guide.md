---
title: Argc Script Reference Guide
type: conversation
permalink: conversations/20250722-Argc_Script_Reference_Guide
created: '2025-07-22T02:52:17.119592Z'
modified: '2025-07-22T03:11:35.529604Z'
---

# Argc Script Reference Guide

### Human (2025-07-22 02:52:20)
Hello Claude! I'm looking to create  a *bunch* of smaller scripts using argc. best to start by creating a artifact with the needed information condensed maybe?

**Attachment: command-runner.md**
```
# Command runner

Argc is a also command runner built for those who love the efficiency and flexibility of Bash scripting.

This guide provides instructions on how to effectively use `argc` for this purpose.

## Create an Argcfile.sh 

Commands, called recipes, are stored in a file called argcfile .

Use `--argc-create` to quickly generate an `Argcfile.sh` for your project.

```sh
argc --argc-create build test
```

This creates a basic Argcfile.sh with sample `build` and `test` recipes.

```sh
#!/usr/bin/env bash

set -e

# @cmd
build() {
    echo TODO build
}

# @cmd
test() {
    echo TODO test
}

# See more details at https://github.com/sigoden/argc
eval "$(argc --argc-eval "$0" "$@")"
```

A recipe is a regular shell function with a `@cmd` comment tag above it.

## Handle dependencies

Since recipe are functions, manage dependencies by calling them sequentially within other functions.

```sh
# @cmd
current() { before;
  echo current
after; }

# @cmd
before() {
  echo before
}

# @cmd
after() { 
  echo after
}
```

This example demonstrates how the `current` recipe calls both `before` and `after` recipes.

```
$ argc current
before
current
after
```

## Organize Recipes

Organize related recipes into groups for better readability.

```sh
# @cmd
test() { :; }
# @cmd
test-unit() { :; }
# @cmd
test-bin() { :; }
```

> Valid group formats include: `foo:bar` `foo.bar` `foo@bar`.

## Set default recipe

When invoked without a specific recipe, Argc displays available recipes.

```
$ argc
USAGE: Argcfile.sh <COMMAND>

COMMANDS:
  build
  test

```

Use `main` function to set a default recipe to run automatically.

```sh
# @cmd
build() { :; }

# @cmd
test() { :; }

main() {
  build
}
```

Another way is to use `@meta default-subcommand`

```sh
# @cmd
# @meta default-subcommand
build() { :; }

# @cmd
test() { :; }
```

Remember, you can always use `--help` for detailed help information.

## Aliases

Aliases allow recipes to be invoked on the command line with alternative names:

```sh
# @cmd
# @alias t
test() {
  echo test
}
```

Now you can run the `test` recipe using the alias `t`:
```
$ argc t
```

## Access positional arguments

Accessed through shell positional variables (`$1`, `$2`, `$@`, `$*` etc.).

```sh
# @cmd
build() {
  echo $1 $2
  echo $@
  echo $*
}
```

```
$ argc build foo bar
foo bar
foo bar
```

## Access Flag/option arguments

Define and use flags/options for more control.

```sh
# @cmd  A simple command
# @flag -f --flag   A flag parameter
# @option -option   A option parameter
# @arg arg          A positional parameter
cmd() {
  echo "flag:    $argc_flag"
  echo "option:  $argc_option"
  echo "arg:     $argc_arg"
}
```

```
$ argc cmd -h
A simple command

USAGE: Argcfile.sh cmd [OPTIONS] [ARG]

ARGS:
  [ARG]  A positional parameter

OPTIONS:
  -f, --flag             A flag parameter
      --option <OPTION>  A option parameter
  -h, --help             Print help

$ argc cmd -f --option foo README.md
flag:    1
option:  foo
arg:     README.md
```

## Load environment variables from dotenv file

Use `@meta dotenv` to load environment variables from a `.env` file.

```sh
# @meta dotenv                                    # Load .env
# @meta dotenv .env.local                         # Load .env.local
```

## Document and Validate environment variables

Define environment variables using `@env`.

```sh
# @env  FOO               A env var
# @env  BAR!              A required env var
# @env  MODE[dev|prod]    A env var with possible values
```

Argc automatically generates help information for environment variables.

By running `argc -h`, you'll see a list of variables with descriptions and any restrictions.

```
$ argc -h
USAGE: Argcfiles.sh

ENVIRONMENTS:
  FOO   A env var
  BAR*  A required env var
  MODE  A env var with possible values [possible values: dev, prod]
```

Argc also validates environment variables as per the `@env` definitions.

If `$BAR` is missing, Argc will report an error:

```
error: the following required environments were not provided:
  BAR$MO
```

For `$MODE`, which has predefined values, Argc verifies the input values and reports errors if they do not match:

```
error: invalid value `abc` for environment variable `MODE`
  [possible values: dev, prod]
```

## Align the project's rootdir

Argc automatically cds into the directory of the Argcfile.sh it finds in the parent hierarchy.

Project directory structure as follows:

```
$ tree /tmp/project

/tmp/project
├── Argcfile.sh
└── src
```

The code of build recipe as follows:

```sh
# @cmd
build() {
    echo $PWD
    echo $ARGC_PWD
}
```

Run the build in the project dir:
```
$ argc build
/tmp/project
/tmp/project
```

Change directory (cd) into the subdirectory and run the build:
```
$ cd src && argc build
/tmp/project
/tmp/project/src
```

When running argc under the subdirectory other than project root,
`PWD` points to the project root, while `ARGC_PWD` points to the current directory.

```

**Attachment: specification.md**
```
# Specification

## Comment Tags

### `@describe`

Sets the description for the command.

> **<sup>Syntax</sup>**\
> `@describe` [_description_]

```sh
# @describe A demo CLI
```

### `@cmd`

Defines a subcommand.

> **<sup>Syntax</sup>**\
> `@cmd` [_description_]<sup>?</sup>

```sh
# @cmd Upload a file
upload() {
  echo Run upload
}

# @cmd Download a file
download() {
  echo Run download
}
```

```
USAGE: prog <COMMAND>

COMMANDS:
  upload    Upload a file
  download  Download a file
```

### `@alias`

Sets aliases for the subcommand.

> **<sup>Syntax</sup>**\
> [_name_] (`,` [_name_])<sup>\*</sup>

```sh
# @cmd Run tests
# @alias t,tst
test() {
  echo Run test
}
```

```
USAGE: prog <COMMAND>

COMMANDS:
  test  Run tests [aliases: t, tst]
```

### `@arg`

Defines a positional argument.

> **<sup>Syntax</sup>**\
> `@arg` [_name_] [_modifier_]<sup>?</sup> [_param-value_]<sup>?</sup>
>   [_bind-env_]<sup>?</sup>
>   [_notation_]<sup>?</sup>
>   [_description_]<sup>?</sup>

```sh
# @arg va
# @arg vb!                        required
# @arg vc*                        multi-values
# @arg vd+                        multi-values + required
# @arg vna <PATH>                 value notation
# @arg vda=a                      default
# @arg vdb=`_default_fn`          default from fn
# @arg vca[a|b]                   choices
# @arg vcb[=a|b]                  choices + default
# @arg vcc*[a|b]                  multi-values + choice
# @arg vcd+[a|b]                  required + multi-values + choice
# @arg vfa[`_choice_fn`]          choice from fn
# @arg vfb[?`_choice_fn`]         choice from fn + no validation
# @arg vfc*[`_choice_fn`]         multi-values + choice from fn
# @arg vfd*,[`_choice_fn`]        multi-values + choice from fn + comma-separated list
# @arg vxa~                       capture all remaining args
# @arg vea $$                     bind-env
# @arg veb $BE <PATH>             bind-named-env
```

### `@option`

Defines an option argument.

> **<sup>Syntax</sup>**\
> `@option` [_short_]<sup>?</sup> [_long_] [_modifier_]<sup>?</sup> [_param-value_]<sup>?</sup>
>   [_bind-env_]<sup>?</sup>
>   [_notations_]<sup>?</sup>
>   [_description_]<sup>?</sup>

```sh
# @option    --oa                   
# @option -b --ob                   short
# @option -c                        short only
# @option    --oc!                  required
# @option    --od*                  multi-occurs
# @option    --oe+                  required + multi-occurs
# @option    --of*,                 multi-occurs + comma-separated list
# @option    --ona <PATH>           value notation
# @option    --onb <FILE> <FILE>    two-args value notations
# @option    --onc <CMD> <FILE+>    unlimited-args value notations
# @option    --oda=a                default
# @option    --odb=`_default_fn`    default from fn
# @option    --oca[a|b]             choice
# @option    --ocb[=a|b]            choice + default
# @option    --occ*[a|b]            multi-occurs + choice
# @option    --ocd+[a|b]            required + multi-occurs + choice
# @option    --ofa[`_choice_fn`]    choice from fn
# @option    --ofb[?`_choice_fn`]   choice from fn + no validation
# @option    --ofc*[`_choice_fn`]   multi-occurs + choice from fn
# @option    --ofd*,[`_choice_fn`]  multi-occurs + choice from fn + comma-separated list
# @option    --oxa~                 capture all remaining args
# @option    --oea $$               bind-env
# @option    --oeb $BE <PATH>       bind-named-env
```

### `@flag`

Defines a flag argument. Flag is a special option that does not accept any value.

> **<sup>Syntax</sup>**\
> `@flag` [_short_]<sup>?</sup> [_long_]`*`<sup>?</sup>
>   [_bind-env_]<sup>?</sup>
>   [_description_]<sup>?</sup>

```sh
# @flag     --fa 
# @flag  -b --fb         short
# @flag  -c              short only
# @flag     --fd*        multi-occurs
# @flag     --ea $$      bind-env
# @flag     --eb $BE     bind-named-env
```

### `@env`

Defines an environment variable.

> **<sup>Syntax</sup>**\
> `@arg` [_NAME_]`!`<sup>?</sup>[_param-value_]<sup>?</sup>
>   [_notation_]<sup>?</sup>
>   [_description_]<sup>?</sup>

```sh
# @env EA                 optional
# @env EB!                required
# @env EC=true            default
# @env EDA[dev|prod]      choices
# @env EDB[=dev|prod]     choices + default
```

### `@meta`

Adds metadata.

> **<sup>Syntax</sup>**\
> `@meta` [_name_] [_value_]<sup>?</sup>

| syntax                           | scope  | description                                                          |
| :------------------------------- | ------ | :------------------------------------------------------------------- |
| `@meta version <value>`          | any    | Set the version for the command.                                     |
| `@meta dotenv [<path>]`          | root   | Load a dotenv file from a custom path, if persent.                   |
| `@meta default-subcommand`       | subcmd | Set the current subcommand as the default.                           |
| `@meta require-tools <tool>,...` | any    | Require certain tools to be available on the system.                 |
| `@meta man-section <1-8>`        | root   | Override the section for the man page, defaulting to 1.              |
| `@meta inherit-flag-options`     | root   | Subcommands will inherit the flags/options from their parent.        |
| `@meta combine-shorts`           | root   | Short flags/options can be combined, e.g. `prog -xf => prog -x -f `. |
| `@meta symbol <param>`           | any    | Define a symbolic parameter, e.g. `+toolchain`, `@argument-file`.    |


```sh
# @meta version 1.0.0
# @meta dotenv
# @meta dotenv .env.local
# @meta require-tools git,yq
# @meta man-section 8
# @meta symbol +toolchain[`_choice_fn`]
```

## Syntax parts

### short

 A single character abbreviation for a flag/option.

> **<sup>Syntax</sup>**\
> &nbsp;&nbsp; -[_short-char_] \
> | +[_short-char_]

### long

A descriptive name for a flag/option.

> **<sup>Syntax</sup>**\
> &nbsp; -- [_long-name_] \
> | -[_long-name_] \
> | +[_long-name_]

### modifier

Symbols used to modify param behavior:

> **<sup>Syntax</sup>**\
> &nbsp; `!` \
> | `*` [_separated-char_]<sup>?</sup> \
> | `+` [_separated-char_]<sup>?</sup>

- `!`: The option is required and must be provided.
- `*`: multi-occurs for @option; multi-values for @arg;
- `+`: The option is required and can be used multiple times.

### param-value

Ways to specify values for params:

> **<sup>Syntax</sup>**\
> &nbsp; =[_value_] \
> | =\`[_fn-name_]\` \
> | [[_choices_]] \
> | [=[_choices_]] \
> | [\`[_fn-name_]\`] \
> | [?\`[_fn-name_]\`]

### choices

Define a set of acceptable values for an param

> **<sup>Syntax</sup>**\
> [_value_] (`|` [_value_])<sup>\*</sup>

### notations

Placeholders in help messages and usage instructions:

> **<sup>Syntax</sup>**\
> ([_notation_] )<sup>\*</sup>  [_notation-last_] 

### notation

> **<sup>Syntax</sup>**\
> `<` [_value_]` >`


- `FILE`/`PATH`: complete files
- `DIR`: complete directories

### notation-last

> **<sup>Syntax</sup>**\
> `<` [_value_] [_notation-modifier_]<sup>?</sup> `>`

### notation-modifier

Symbols used within the last notation to specify value requirements

> **<sup>Syntax</sup>**\
> &nbsp; `*` \
> | `+` \
> | `?`

- `*`: Zero or more values are allowed.
- `+`: One or more values are allowed.
- `?`: Zero or one value is allowed.

### short-char

A-Z a-z 0-9 `!` `#` `$` `%` `*` `+` `,` `.` `/` `:` `=` `?` `@` `[` `]` `^` `_` `{` `}` `~`

### separated-char

`,` `:` `@` `|` `/`

### bind-env

 Link environment variables to params:

- `$$`: Automatically use the param's name for the environment variable.
- `$`[_NAME_]: Use a specific environment variable name.

### description

Plain text for documentation and usage information

```sh
# @describe Can be multiline 
#
# Extra lines after the comment tag accepts description, which don't start with an `@`,
# are treated as the long description. A line which is not a comment ends the block.
```

[_short_]: #short
[_long_]: #long
[_modifier_]: #modifier
[_param-value_]: #param-value
[_choices_]: #choices
[_notations_]: #notations
[_notation_]: #notation
[_notation-last_]: #notation-last
[_notation-modifier_]: #notation-modifier
[_short-char_]: #short-char
[_separated-char_]: #separated-char
[_bind-env_]: #bind-env
[_description_]: #description
[_name_]: #name
[_long-name_]: #name
[_fn-name_]: #fn-name
[_value_]: #value
[_NAME_]: #name
```

**Attachment: variables.md**
```
# Variables

Argc streamlines argument parsing in your shell scripts, allowing you to utilize variables seamlessly.

## Shell Variables

You can employ shell variables within your argc-based scripts just like you normally would in Bash. Argc doesn't interfere with their behavior.

```sh
# @cmd
cmd() {
  echo $1 $2  # Accessing positional arguments
  echo "$*"   # All arguments as a single string
  echo "$@"   # All arguments as separate strings
}
```

## Argc-Generated Variables

Argc automatically creates variables corresponding to the options, flags, and positional arguments defined in your script using the `@option`, `@flag`, and `@arg` directives.

```sh
# @option --oa
# @option --ob*  # Multiple values allowed
# @flag   --fa
# @arg va
# @arg vb*

eval "$(argc --argc-eval "$0" "$@")"  # Initializes Argc variables

echo '--oa:' $argc_oa
echo '--ob:' ${argc_ob[@]}  # Accessing multiple values as an array
echo '--fa:' $argc_fa
echo '  va:' $argc_va
echo '  vb:' ${argc_vb[@]}
```

Running `./script.sh --oa a --ob=b1 --ob=b2 --fa foo bar baz` would output:

```
--oa: a
--ob: b1 b2
--fa: 1
  va: foo
  vb: bar baz
```

## Built-in Variables

Argc also provides built-in variables that offer information about the parsing process:

*   **`argc__args`**: An array holding all command-line arguments.
*   **`argc__positionals`**: An array containing only the positional arguments.
*   **`argc__fn`**: The name of the function that will be executed.

**Additional Variables for Completion (Used internally by Argc-Completions):**

*   **`argc__cmd_arg_index`**: Index of the command argument within `argc__args`.
*   **`argc__cmd_fn`**: Name of the command function.
*   **`argc__dash`**: Index of the first em-dash (`--`) within the positional arguments.
*   **`argc__option`**: Variable name of the option currently being completed.

These variables are particularly useful when creating custom completion scripts. 

## Environment Variables

Several environment variables allow you to tailor Argc's behavior:

**User-Defined:**

*  **`ARGC_SHELL_PATH`**: Specifies the path to the shell/bash executable used by Argc.
*  **`ARGC_SCRIPT_NAME`**: Overrides the default script filename (Argcfile.sh).
*  **`ARGC_COMPGEN_DESCRIPTION`**: Disables descriptions for completion candidates if set to 0 or false. 
*  **`ARGC_COMPLETIONS_PATH`**: Defines the search path for Argc-based completion scripts.

**Argc-Injected:**

*  **`ARGC_PWD`**: Current working directory (available only in Argcfile.sh).

**Argc-Injected (for completion):**
*  **`ARGC_OS`**: Operating system type.
*  **`ARGC_COMPGEN`**: Indicates whether the script is being used for generating completion candidates (1) or not (0).
*  **`ARGC_CWORD`**: The last word in the processed command line.

It's important to distinguish between these two variables:

*  **`ARGC_CWORD`**: This variable isolates the final word, regardless of any preceding flags or options. For example, in the command `git --git-dir=git`, `ARGC_CWORD` would be `git`.
*  **`ARGC_LAST_ARG`**: This variable captures the entire last argument, including any flags or options attached to it. In the same example, `ARGC_LAST_ARG` would be `--git-dir=git`.

Understanding these variables is key to effectively leveraging Argc's capabilities and creating robust and user-friendly command-line interfaces.

```

**Attachment: code_interpreter.sh**
```
#!/usr/bin/env bash
set -e

# @describe Execute the sql code.
# @option --code! The code to execute.

# @meta require-tools usql

# @env USQL_DSN! The database connection url. e.g. pgsql://user:pass@host:port
# @env LLM_OUTPUT=/dev/stdout The output path

ROOT_DIR="${LLM_ROOT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"

main() {
    if ! grep -qi '^select' <<<"$argc_code"; then
        "$ROOT_DIR/utils/guard_operation.sh"
    fi
    usql -c "$argc_code" "$USQL_DSN" >> "$LLM_OUTPUT"
}

eval "$(argc --argc-eval "$0" "$@")"

```

**Attachment: demo_sh.sh**
```
#!/usr/bin/env bash
set -e

# @describe Demonstrate how to create a tool using Bash and how to use comment tags.
# @option --string!                  Define a required string property
# @option --string-enum![foo|bar]    Define a required string property with enum
# @option --string-optional          Define a optional string property
# @flag --boolean                    Define a boolean property
# @option --integer! <INT>           Define a required integer property
# @option --number! <NUM>            Define a required number property
# @option --array+ <VALUE>           Define a required string array property
# @option --array-optional*          Define a optional string array property

# @env LLM_OUTPUT=/dev/stdout The output path

main() {
    cat <<EOF >> "$LLM_OUTPUT"
string: ${argc_string}
string_enum: ${argc_string_enum}
string_optional: ${argc_string_optional}
boolean: ${argc_boolean}
integer: ${argc_integer}
number: ${argc_number}
array: ${argc_array[@]}
array_optional: ${argc_array_optional[@]}
$(printenv | grep '^LLM_')
EOF
}

eval "$(argc --argc-eval "$0" "$@")"

```

**Attachment: execute_sql_code.sh**
```
#!/usr/bin/env bash
set -e

# @describe Execute the sql code.
# @option --code! The code to execute.

# @meta require-tools usql

# @env USQL_DSN! The database connection url. e.g. pgsql://user:pass@host:port
# @env LLM_OUTPUT=/dev/stdout The output path

ROOT_DIR="${LLM_ROOT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"

main() {
    if ! grep -qi '^select' <<<"$argc_code"; then
        "$ROOT_DIR/utils/guard_operation.sh"
    fi
    usql -c "$argc_code" "$USQL_DSN" >> "$LLM_OUTPUT"
}

eval "$(argc --argc-eval "$0" "$@")"

```

**Attachment: fs_ls.sh**
```
#!/usr/bin/env bash
set -e

# @describe List all files and directories at the specified path.

# @option --path! The path of the directory to list

# @env LLM_OUTPUT=/dev/stdout The output path

main() {
    ls -1 "$argc_path" >> "$LLM_OUTPUT"
}

eval "$(argc --argc-eval "$0" "$@")"

```

**Attachment: fs_patch.sh**
```
#!/usr/bin/env bash
set -e

# @describe Apply a patch to a file at the specified path.
# This can be used to edit the file, without having to rewrite the whole file.

# @option --path! The path of the file to apply to
# @option --contents! The patch to apply to the file
#
# Here is an example of a patch block that can be applied to modify the file to request the user's name:
# --- a/hello.py
# +++ b/hello.py
# \@@ ... @@
#  def hello():
# -    print("Hello World")
# +    name = input("What is your name? ")
# +    print(f"Hello {name}")

# @env LLM_OUTPUT=/dev/stdout The output path

ROOT_DIR="${LLM_ROOT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"

main() {
    if [ ! -f "$argc_path" ]; then
        echo "Not found file: $argc_path"
        exit 1
    fi
    new_contents="$(awk -f "$ROOT_DIR/utils/patch.awk" "$argc_path" <(printf "%s" "$argc_contents"))"
    printf "%s" "$new_contents" | git diff --no-index "$argc_path" - || true
    "$ROOT_DIR/utils/guard_operation.sh" "Apply changes?"
    printf "%s" "$new_contents" > "$argc_path"

    echo "The patch applied to: $argc_path" >> "$LLM_OUTPUT"
}

eval "$(argc --argc-eval "$0" "$@")"

```

**Attachment: fs_rm.sh**
```
#!/usr/bin/env bash
set -e

# @describe Remove the file or directory at the specified path.

# @option --path! The path of the file or directory to remove

# @env LLM_OUTPUT=/dev/stdout The output path

ROOT_DIR="${LLM_ROOT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"

main() {
    if [[ -f "$argc_path" ]]; then
        "$ROOT_DIR/utils/guard_path.sh" "$argc_path" "Remove '$argc_path'?"
        rm -rf "$argc_path"
    fi
    echo "Path removed: $argc_path" >> "$LLM_OUTPUT"
}

eval "$(argc --argc-eval "$0" "$@")"

```

**Attachment: get_current_weather.sh**
```
#!/usr/bin/env bash
set -e

# @describe Get the current weather in a given location.
# @option --location! The city and optionally the state or country, e.g., "London", "San Francisco, CA".

# @env LLM_OUTPUT=/dev/stdout The output path

main() {
    curl -fsSL "https://wttr.in/$(echo "$argc_location" | sed 's/ /+/g')?format=4&M" \
    >> "$LLM_OUTPUT"
}

eval "$(argc --argc-eval "$0" "$@")"

```

**Attachment: search_wikipedia.sh**
```
#!/usr/bin/env bash
set -e

# @describe Search Wikipedia for a query.
# Uses it to get detailed information about a public figure, interpretation of a complex scientific concept or in-depth connectivity of a significant historical event,.

# @option --query! The query to search for.

# @env LLM_OUTPUT=/dev/stdout The output path

main() {
    encoded_query="$(jq -nr --arg q "$argc_query" '$q|@uri')"
    base_url="https://en.wikipedia.org/w/api.php"
    url="$base_url?action=query&list=search&srprop=&srlimit=1&limit=1&srsearch=$encoded_query&srinfo=suggestion&format=json"
    json="$(curl -fsSL "$url")"
    suggestion="$(echo "$json" | jq -r '.query.searchinfo.suggestion // empty')"
    title="$(echo "$json" | jq -r '.query.search[0].title // empty')"
    pageid="$(echo "$json" | jq -r '.query.search[0].pageid // empty')"
    if [[ -z "$title" || -z "$pageid" ]]; then
        echo "error: no results for '$argc_query'" >&2
        exit 1
    fi
    title="$(echo "$title" | tr ' ' '_')"
    url="$base_url?action=query&prop=extracts&explaintext=&titles=$title&exintro=&format=json"
    curl -fsSL "$url" | jq -r '.query.pages["'"$pageid"'"].extract' >> "$LLM_OUTPUT"
}

eval "$(argc --argc-eval "$0" "$@")"

```

**Attachment: search_wolframalpha.sh**
```
#!/usr/bin/env bash
set -e

# @describe Get an answer to a question using Wolfram Alpha. Input should the query in English.
# Use it to answer user questions that require computation, detailed facts, data analysis, or complex queries.

# @option --query! The query to search for.

# @env WOLFRAM_API_ID! The api id
# @env LLM_OUTPUT=/dev/stdout The output path

main() {
    encoded_query="$(jq -nr --arg q "$argc_query" '$q|@uri')"
    url="https://api.wolframalpha.com/v2/query?appid=$WOLFRAM_API_ID&input=$encoded_query&output=json&format=plaintext"
    curl -fsSL "$url" | jq '[.queryresult | .pods[] | {title:.title, values:[.subpods[].plaintext | select(. != "")]}]' \
    >> "$LLM_OUTPUT"
}

eval "$(argc --argc-eval "$0" "$@")"

```

### Assistant (2025-07-22 02:53:09)
 I'll create a condensed argc reference guide that covers everything you'll need to create your scripts efficiently!    This reference guide covers all the essential argc patterns you'll need! It includes:

- **Basic script structure** with the required eval line
- **Complete comment tag reference** (@cmd, @option, @flag, @arg, @env, @meta)
- **Variable access patterns** for different argument types
- **Common script templates** you can adapt (file processing, API clients, multi-command tools)
- **Best practices and tips** from the examples in your docs

The guide is organized so you can quickly find what you need while writing scripts. Each pattern includes working examples you can copy and modify.

What types of scripts are you planning to create? I can help you adapt these patterns or create specific examples for your use cases!

### Human (2025-07-22 03:10:26)
this is directly created by an agent and this should be standard way to do it. 


these are especially important:

# @env LLM_OUTPUT=/dev/stdout The output path
ROOT_DIR="${LLM_ROOT_DIR:/home/skogix/.local/src/llm-functions/agents/sql/tools.sh-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
  "$ROOT_DIR/utils/guard_path.sh" "$argc_path" "Create '$argc_path'?"

and that output pipes like this:
      cat "$official_dir/$argc_document.md" >>"$LLM_OUTPUT"

and lastly: 

eval "$(argc --argc-eval "$0" "$@")"

otherwise nothing happens :)

**Attachment: tools.sh**
```
#!/usr/bin/env bash
set -e

# @env LLM_OUTPUT=/dev/stdout The output path

ROOT_DIR="${LLM_ROOT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"

# @cmd Create a new file at the specified path with contents.
# @option --path! The path where the file should be created
# @option --contents! The contents of the file
fs_create() {
  "$ROOT_DIR/utils/guard_path.sh" "$argc_path" "Create '$argc_path'?"
  mkdir -p "$(dirname "$argc_path")"
  printf "%s" "$argc_contents" >"$argc_path"
  echo "File created: $argc_path" >>"$LLM_OUTPUT"
}

# @cmd Show the library
# @option --username! The path where the file should be created
show_library() {
  local library="/home/skogix/skogai/librarian"
  tree -C "$library/archives" "$library/official" --noreport >>"$LLM_OUTPUT"

}

# @cmd Read official SkogAI documents from the official documentation directory
# @option --document! The name or path of the official document to read (use "list" to see all)
read_official_documents() {
  local official_dir="/home/skogix/skogai/docs/official"

  if [[ "$argc_document" == "list" ]]; then
    ls -la "$official_dir" >>"$LLM_OUTPUT"
  else
    cat "$official_dir/$argc_document" >>"$LLM_OUTPUT" 2>/dev/null ||
      cat "$official_dir/$argc_document.md" >>"$LLM_OUTPUT"
  fi
}

# See more details at https://github.com/sigoden/argc
eval "$(argc --argc-eval "$0" "$@")"

```

**Attachment: tools.sh**
```
#!/usr/bin/env bash
set -e

# @env LLM_OUTPUT=/dev/stdout The output path

ROOT_DIR="${LLM_ROOT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"

# @cmd Create a new file at the specified path with contents.
# @option --path! The path where the file should be created
# @option --contents! The contents of the file
fs_create() {
    "$ROOT_DIR/utils/guard_path.sh" "$argc_path" "Create '$argc_path'?"
    mkdir -p "$(dirname "$argc_path")"
    printf "%s" "$argc_contents" > "$argc_path"
    echo "File created: $argc_path" >> "$LLM_OUTPUT"
}

# See more details at https://github.com/sigoden/argc
eval "$(argc --argc-eval "$0" "$@")"

```

**Attachment: tools.sh**
```
#!/usr/bin/env bash

set -e

ROOT_DIR="${LLM_ROOT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"

# @meta require-tools usql
# @env LLM_AGENT_VAR_DSN! The database connection url. e.g. pgsql://user:pass@host:port 

# @cmd Execute a SELECT query
# @option --query!                  SELECT SQL query to execute
read_query() {
    if ! grep -qi '^select' <<<"$argc_query"; then
        echo "error: only SELECT query is allowed" >&2
        exit 1
    fi
    _run_sql "$argc_query"
}

# @cmd Execute an SQL query
# @option --query!                  SQL query to execute
write_query() {
    "$ROOT_DIR/utils/guard_operation.sh" "Execute SQL?"
    _run_sql "$argc_query"
}

# @cmd List all tables
list_tables() {
    _run_sql "\dt+"
}

# @cmd Get the schema information for a specific table
# @option --table-name!             Name of the table to describe
describe_table() {
    _run_sql "\d $argc_table_name"
}

_run_sql() {
    usql "$LLM_AGENT_VAR_DSN" -c "$1" >> "$LLM_OUTPUT"
}

# See more details at https://github.com/sigoden/argc
eval "$(argc --argc-eval "$0" "$@")"

```

### Assistant (2025-07-22 03:11:35)
 Perfect! I see the agent-specific patterns now. Let me update the reference guide to include these essential agent conventions:             Perfect! I've updated the reference guide to include the agent standard patterns. The key agent requirements are now prominently featured:

## Critical Agent Standards:
1. **`# @env LLM_OUTPUT=/dev/stdout The output path`** - Always include this
2. **`ROOT_DIR="${LLM_ROOT_DIR:-...}"`** - Standard root directory setup  
3. **`>> "$LLM_OUTPUT"`** - ALL output must redirect here (never plain echo!)
4. **`"$ROOT_DIR/utils/guard_*.sh"`** - Use guard utilities for safety
5. **`eval "$(argc --argc-eval "$0" "$@")"`** - CRITICAL ending line or nothing works!

The updated guide now shows the proper agent patterns in all examples, including:
- File operations with path guards
- Database operations with safety checks
- Proper output redirection in all cases
- Multi-command scripts with agent standards

This should give you everything you need to create argc scripts that work perfectly in your agent environment. The examples are all ready to copy and adapt for your specific use cases!