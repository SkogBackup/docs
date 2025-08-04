---
title: Clean Symbolic Tests
type: note
permalink: tests/clean-symbolic-tests
---

$ id
$ unique
$ claude
$ entity.id
$ message.eid
$ int*$ unique
$ entity.id*$ entity.gen
$ name.1
[@hello:Claude]
[@date:now]
{"player": {"x": $ int, "y": $ int}, "health": $ int*$ unique}
{"game_state": $ entity.eid, "score": $ int*$ int}
[$ entity.id, $ entity.gen, $ unique]
[$ claude, $ message.from, $ message.to]
{"entities": [$ entity, $ entity], "messages": [$ message]}
$ name.2
$ name.3
$ entity.name
$ nonexistent.key
$ missing.reference
{"world": {"entities": [{"id": $ entity.id, "pos": [$ int, $ int]}, {"id": $ entity.gen, "pos": [$ int*$ unique, $ int]}]}, "player": $ claude, "time": $ datetime}
$ json.self
"$ literally just the dollar sign"