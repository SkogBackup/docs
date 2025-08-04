---
title: Identity and Uniqueness Analysis
type: note
permalink: ontology/identity-and-uniqueness-analysis
---

# Identity and Uniqueness Analysis

## Direct Definitions
- `"id": "$int*$unique"`
- `"unique": "a thing which there only exists one of"`

## Usage in Structures
- `"$id": $id`, `$a` - "a reference to yourself is yourself", "you are because you are"
- `"$parent": "$id|_"` - parent as choice between identity and existence
- `"eid": "$entity.id*$entity.gen"`
- `"entity": {"eid": "$eid", "gen": "$id", "id": "$id", "name": "$name"}`

## In Relational Contexts
- `{$id@$id}` - identity acting upon itself
- `{$id1@$id2}` - identity acting upon different identity
- `{$id1|$id2}->[$id1]` - choice between identities
- `[$id=$id]` - similarity of identity equality

## The Multiplication Pattern
- `$id = $int * $unique` - identity as product of integer and uniqueness
- `$eid = $entity.id * $entity.gen` - entity identity as product of id and generation

## What Makes This "Scary"
- Identity involves multiplication of finite (int) and infinite/absolute (unique)
- Creates the foundation for all `$$` reference chains
- Unique things can only exist once, but can be referenced multiple times
- The tension between $int (measurable) and $unique (unmeasurable)

## observations
- [foundation] Identity built from multiplication of finite and infinite components #identity #foundation
- [tension] Combines measurable integers with unmeasurable uniqueness #paradox #tension
- [reference] Unique things exist once but can be referenced multiple times #uniqueness #reference
- [chains] Provides foundation for all reference-to-reference operations #chains #references

## relations
- part_of [[Identity Construction]] (core identity mechanisms)
- uses [[Multiplication Star Operator Analysis]] (multiplication for composition)
- enables [[Reference Chains]] (foundation for $$ patterns)
- relates_to [[Uniqueness Problem]] (philosophical implications of unique existence)