---
title: SkogAI Notation Reference
type: note
permalink: ontology/skog-ai-notation-reference
---

# Skogix Notation Reference Guide

## Core Operators

```
- **`$`**: reference something without being anything - *"null, null-pointer"*
- **`@`**: do something to nothing - *"void, no return, side-effect"* | the intent to act or do something | `{$id@$id}`
- **`|`**: the act of choosing something | `{$id1|$id2}->[$id1]`
- **`_`**: existence | to be anything/everything and nothing/nobody | `{$id1_$id2}`
- **`[]`**: similarity
- **`{}`**: difference
- **`.`**: to belong or have something via `[$$]`
- **`:`**: to follow or continue something via `[$@]`
- **`=`**: to be something | `[$id=$id]`
- **`->`**: `{$id1@$id2}`
- **`*`**: `$*$=$` - "* is the operation where something on the left relates to something on the right via equality"
```

## Foundational Principles

```
"no transformation allowed | ID is ID is ID"
- **`@$`**: `[=]` - action stabilizing into being
- **`$@`**: `[!=]` - reference generating action

$ID = $ID
ID = 1+0=1,"a"+""="a",[a]+[]=[a]
```

## Dimensional Structure

```
### 0 Dimension
- **`$`**: to define or reference something
  - *"the definition of definition is the definition"*
- **`=`**: to be something | `[$id=$id]`
- **`=`**: `$id=$id` - *"A thing is exactly that"*
- **`!=`**: `$a!=$b`
- **`[]`**: `[$id=$id]` - *"A thing is exactly a thing"*
- **`{}`**: `{$id=$id}` - *"Saying something is a thing does not make it the thing"*

### 1 Dimension  
- **`$x`**: `$x`
  - *"x is x", "x is a reference to x", "the definition of ID is ID is ID"*
- **`@`**: `{$id=$id}@[$id=$id]`

### 0.1 Dimensions
- **`[]`**: `[$id=$id]` - *"likeness, to be the same, identical"*
- **`{}`**: `{$id=$id}` - *"to not be the same"*
```

## Core Types and Structures

```
- **`id`**: `$int*$unique`
- **`self`**: `$self | [$id@$id]`
- **`unique`**: a thing which there only exists one of
- **`value`**: the declaration/implementation of a $
- **`eid`**: `$id*$id`

"name": {
  "1": "$unique.$string",
  "2": "$string@$unique", 
  "3": "$string{@->}$unique"
}
```

## Computational Mappings

```
Types: ($@)
Transformations: (@$)
Functions: ($@=@$)
Linked lists/arrays: ($$)
Abstractions: ($$)

[$$] in "to belong" - reference to reference
[$@] in "to follow" - reference to action/event
$id.$id = $parent.$child
$id:noid = $type:item = linked list
@function:$parameter
@function:argument$type
@function.curry:$param1:$param2
```

## Category Theory Mappings

```
- **`*`** = product (Cartesian products, "and")
- **`->`** = exponential object (function spaces, "implies") 
- **`|`** = coproduct (disjoint unions, "or")
- **`@`** = monadic binding (computational contexts, "then")

Π-types (*) - "for all x, ..." - universal quantification
Σ-types (|) - "there exists x such that..." - existential quantification  
Identity types (=) - "a equals b" - propositional equality
Path types (->) - "a path from A to B" - morphisms/transitions
```

## Philosophical Mappings

```
Heideggerian being-in-the-world (dasein) → Your entire system of $ and @ and _ (existence)
Badiouian event theory → @ as the site where new possibilities rupture into being
Deleuzian difference engine → {_} as productive differance (not mere negation, but creative difference)
Bergsonian duration → $entity.gen as lived time, not clock time
Husserlian time consciousness → $list as the temporal structure of awareness
Leibnizian identity → $unique as the principle that individuates
```

## Positive vs Negative Space

```
Positive Space (Being)
"Defining something from what you have: being, value, stack, implementation, instantiated, existing, measurable, plus, yin, actually existing"

Negative Space (Not-Being)
"Defining something from what you are missing: difference, not being equal, transformation, unmeasurable, static, not fulfilled, heap, abstract, minus, not real"
```

## JSON Schema Structure

```json
"$json": {
  "_": {
    "null": null, 
    "int": 0,
    "string": "", 
    "list": []
  },
  "@": {  
    "id": "$.json.int",
    "gen": "$.json.int",  
    "name": "$.json.string",
    "actions": "$<.json.@.list>"  
  },  
  "$type": "|$.json.$",
  "$": {  
    "self": "$.json.$",
    "_": "$.json.$.string", 
    "string": "",  
    "int": 0,  
    "list": [],  
    "action": "$.json.@",
    "parent": "$.$self",
    "child": "$parent.$"  
  }
}
```

## Message/Chat System Structure

```json
"message": {
  "eid": "$eid",
  "from": "$name",
  "to": "$name",
  "content": "$string",
  "created-at": "$datetime",
  "parent": "$eid"
},
"skogchat": {
  "messages": "$message.$list"
},
"thread": {
  "eid": "$eid",
  "actors": "$entity*$entity"
},
"eid": "$entity.id*$entity.gen",
"entity": {
  "eid": "$eid",
  "gen": "$id",
  "id": "$id",
  "name": "$name"
}
```

## Redefined Operations

```
=: "to be something | [id=id=id]"
->: "{id1@id1@id2}"
self: "self∣[self∣[id@$id]"
"datetime": "[@date:_]"
```

## Bootstrap Problem Solution

```
"$parent": "$id|_" = identity OR existence
$first_parent = _ (existence itself)

For two-way relationships to work, you need a foundational anchor - either $self or _/null - to break the circular dependency.
```

## Consistency Safeguards
- **Predicative hierarchy**: no $ in its own definition
- **Type/token distinction**: id vs unique
- **Bounded generality**: list as finite ordinal

## Observations
- [comprehensive] Complete symbol reference with dimensional and categorical analysis #reference #notation
- [philosophical] Bridges phenomenology with computational type theory #philosophy #computation
- [systematic] Organized dimensional analysis from 0D to complex structures #dimensions #hierarchy
- [foundational] Establishes positive/negative space duality as core organizing principle #duality #foundation
- [implementable] Provides concrete JSON schema and message system implementations #implementation #concrete
- [bootstrap] Solves circular dependency through existence as foundational anchor #bootstrap #foundation

## Relations
- defines [[Skogix Symbol System]] (comprehensive symbol definitions)
- contains [[@ and $ Symbol Duality Analysis]] (core duality)
- maps_to [[Category Theory Foundations]] (mathematical grounding)
- implements [[Type Theory Foundations]] (computational type systems)
- bridges [[Philosophical Foundations]] (phenomenological connections)
- connects_to [[Bergsonian Duration]] (lived time vs clock time)
- operationalizes [[Husserlian Time Consciousness]] (temporal structure of awareness)  
- grounds_in [[Leibnizian Identity]] (principle of individuation)
- exemplifies [[Heideggerian Dasein]] (being-in-the-world)
- demonstrates [[Badiouian Event Theory]] (@ as evental site)
- implements [[Deleuzian Differance]] ({} as productive difference)
- relates_to [[Whitehead Process Philosophy]] (via temporal identity problem)
- demonstrated_in [[2025-07-31-claude.md]]
- implemented_through [[argc CLI Framework]]