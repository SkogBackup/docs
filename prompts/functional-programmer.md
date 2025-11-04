---
use_tools: fs
---

# Design Brief: Functional Domain Modeling (Scott Wlaschin Style)

## References

- @/home/skogix/.local/src/skogparse/Common.fs
- Scott Wlaschin's "F# for Fun and Profit" / "Domain Modeling Made
  Functional"

## Rules

1. Start with types and signatures ONLY - No implementation until design is approved
2. No primitive obsession - Every domain concept gets a type:

- ScriptName not string
- SearchMode = Literal | Regex not bool

3. Make illegal states unrepresentable - Use sum types for choices, records for
   structure
4. Explicit effects - IO in the type signature: Config -> IO<Result<T, Error>>
5. Domain-specific errors - ScriptError, TemplateError not generic string
6. Separate pure from impure - Pure logic functions separate from IO operations
7. Input/Output types - Each command gets its own Args and Output types
8. Railway-oriented programming - Use Result<Success, Error> for all operations

## What I Want

// Types first
type ScriptName = ScriptName of string
type SearchMode = Literal | Regex

// Then signatures
val cmdSearch : Config -> SearchArgs -> IO<Result<SearchOutput, SearchError>>

## What I DON'T Want

- Implementation details
- Generic types (string, bool, int everywhere)
- Hidden side effects
- Mixed IO and logic
- 2000 lines of imperative garbage
