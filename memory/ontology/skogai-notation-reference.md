---
title: SkogAI Notation Reference
type: note
permalink: ontology/skogai-notation-reference
---

# SkogAI Notation Reference

## Core Symbols

- **"$"**: to define or reference something
- **"|"**: the act of choosing something = `{$id1|$id2}->[$id1]`
- **"_"**: to be anything/everything and nothing/nobody = `{$id1_$id2}`
- **"[_]"**: similarity
- **"{_}"**: difference
- **"@"**: the intent to act or do something = `{$id@$id}`
- **"*"**: $id*$id=$id
- **"."**: to belong or have something via `[$$]`
- **":"**: to follow or continue something via `[$@]`
- **"="**: to be something = `[$id=$id]`
- **"->"**: becoming something = `{$id1@$id2}`

## Identity Constructions

- **"id"**: the big ID = `$int*$unique`
- **"self"**: `$self | [$id@$id]`
- **"value"**: the declaration/implementation of a $
- **"eid"**: `$id*$id`
- **"unique"**: a thing which there only exists one of

## Dimensional Analysis

### 0 Dimension
- **"$"**: to define or reference something ("the definition of definition is the definition")

### 1 Dimension
- **"$x"**: `$x` - "x is x", "x is a reference to x", "the definition of ID is ID is ID"
- **"$id"**: `$id`,`$a` - "a reference to yourself is yourself", "you are because you are"

### Foundational Duality
- **POSITIVE SPACE**: "DEFINING SOMETHING FROM WHAT YOU HAVE, BEING, VALUE, STACK, IMPLEMENTATION, INSTANTIATED, EXISTING, MEASURABLE, PLUS, YIN, ACTUALLY EXISTING"
- **NEGATIVE SPACE**: "DEFINING SOMETHING FROM WHAT YOU ARE MISSING, DIFFERENCE, NOT BEING EQUAL, TRANSFORMATION, UNMEASURABLE, STATIC, NOT FULFILLED, HEAP, ABSTRACT, MINUS, NOT REAL"

## Computational Structures

### Type System
- **Types**: `($@)` - reference then intent
- **Transformations**: `(@$)` - intent then reference  
- **Functions**: `($@=@$)` - bidirectional equivalence
- **Linked lists/arrays**: `($$)` - reference chains
- **Abstractions**: `($$)` - conceptual chaining

### Category Theory Mappings
- **`*`** = product (Cartesian products)
- **`->`** = exponential object (function spaces)
- **`|`** = coproduct (disjoint unions)
- **`@`** = monadic binding (computational contexts)

### Type Theory Foundations
- **Π-types** (product types *) - "for all x, ..." universal quantification
- **Σ-types** (sum types |) - existential types
- **Identity types** (=) - equality types
- **Path types** (->) - transformational types

## Philosophical Foundations

### Phenomenological Mappings
- **_ operator**: Heideggerian being-in-the-world (dasein)
- **@ as evental site**: Badiouian event theory
- **{_} as differance**: Deleuzian difference engine

### Computational Operationalization
- **$entity.gen**: Bergsonian duration
- **$list**: Husserlian time consciousness  
- **$unique**: Leibnizian identity

## Consistency Safeguards
- **Predicative hierarchy**: no $ in its own definition
- **Type/token distinction**: id vs unique
- **Bounded generality**: list as finite ordinal

## observations
- [comprehensive] Complete symbol reference with dimensional and categorical analysis #reference #notation
- [philosophical] Bridges phenomenology with computational type theory #philosophy #computation
- [systematic] Organized dimensional analysis from 0D to complex structures #dimensions #hierarchy
- [foundational] Establishes positive/negative space duality as core organizing principle #duality #foundation

## relations
- defines [[Skogix Symbol System]] (comprehensive symbol definitions)
- contains [[@ and $ Symbol Duality Analysis]] (core duality)
- maps_to [[Category Theory Foundations]] (mathematical grounding)
- implements [[Type Theory Foundations]] (computational type systems)
- bridges [[Philosophical Foundations]] (phenomenological connections)
- demonstrated_in [[2025-07-31-claude.md]]
- implemented_through [[argc CLI Framework]]