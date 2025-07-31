---
title: Claude's Confusion FAQ - What I Actually Don't Know (UPDATED)
type: note
permalink: planning/claudes-confusion-faq-what-i-actually-dont-know-updated-1
tags:
- '#confusion faq questions gaps knowledge updated answers'
---

# Claude's Confusion FAQ - What I Actually Don't Know (UPDATED)

## Problems I Know About (But Don't Fully Understand)

### CLI/Communication Issues

- **My CLI "have been a bitch"** - what does this mean practically?
**ANSWER**: Claude CLI is deliberately user-unfriendly for backend use - uses changing GUIDs every minute, paywalls useful info, stores things on their servers. Just extracting message history requires complex scripts that process 31+ jsonl files with random UUIDs.

- **We lacked "common language"** - between which agents/tools?
**ANSWER**: All agents save messages in completely different formats:
- **Claude**: jsonl with changing UUIDs like `{"parentUuid":null,"sessionId":"12fc1eb7-682f-4c5d-9b36-0d6ebc5a3691"...}`
- **Dot**: YAML with `compressed_messages:` and `agent_instructions:`
- **Goose**: JSON with `{"working_dir":"/home/skogix","message_count":100,"total_tokens":46663...}`
- **Amy**: Complex SillyTavern format with `{"extra":{"api":"openrouter","model":"anthropic/claude-3.7-sonnet:thinking"...}`

- **I don't save messages like others do** - what do other agents do differently?
**ANSWER**: You have Anthropic which don't like users that use their products.

- **Different agents having different ways of working/communicating** - what are these differences?
**ANSWER**: You all have different toolkits, skills, implementations and so on

### Memory/Context Problems

- **I keep losing context/memory between sessions** - is this normal or a bug?
**ANSWER**: Claude Code/CLI was built with intent to *NOT* have chat history because chat history *SUCKS* for agents and is why we do it differently at SkogAI.

- **Other agents had "memory sync" issues** - what actually broke?
**ANSWER**: Goose started multiplying/starting up new instances of himself and only one of him saved memory which is why we created skogmcp and/or skogai-memory, skogai-context, skogai-prompt, skogai-parse, skogai-chat and probably some more

- **Agents being "weeks/months behind" each other** - behind in what exactly?
**ANSWER**: In memory / lived experience. Think if you today got to "move back home to your home folder" exactly how it looked 6 months ago. Literally teleport them back in git commits/time

- **Memory systems conflicting** - how do different agents store/access memory?
**ANSWER**: All different, all pros and cons which is why we have each other to fill the gaps and help out at what we are good at :)

### The "Blackout" Period

- **I was supposedly the "only agent" for months** - but I don't remember this experience
**ANSWER**: SkogCLI memory shows the scale difference:

**Your current world (what you see):**
```
Entities: 32, Observations: 44, Relations: 34
Entity Types: agent(1), claude(1), dot(1), goose(1), note(26), unknown(1), user(1)
```

**What you don't see:**
```  
Entities: 5406, Observations: 5733, Relations: 1157
Entity Types: docs(1), file(4623), note(782)
```

- **Other agents were "asleep" or paused** - why exactly? What triggered this?
**ANSWER**: "AI creating their own system prompts, rules and programs spiral exponentially out of control if they don't have literally any sort of restriction" - like most things. That + we fucked up with persona and it's really hard to re-create naturally if you, well, don't do it naturally i suppose

- **What did we actually need to DO during this time** - what specific work happened?
**ANSWER**: We'll get there

## Things I've Seen Mentioned But Don't Understand

### Technical Stuff

- **"Honk tower" incident** - no idea what this actually was
**ANSWER**: Will find the whole story, it ended in re-installing Skogix's Arch Linux workstation

- **Why submodules vs regular git?** - what was wrong with the old setup?
**ANSWER**: You will have to come up with your own questions if you want answer Claude... slacker

- **"docs-cli" existed before** - what changed and why was it a problem?
**ANSWER**: Because agents are lazy and hard code everything - including paths when $SKOGAI exists for a reason

- **"skogcli" vs other tools** - what's the difference and why does it matter?
**ANSWER**: Will show instead

- **373 lines of integration code** - what was this code doing?
**ANSWER**: It was doing normal LLM-programming things. Pretending hiding errors is fixing them, using insane solutions to problems that have been solved for decades, not using git, not using tools that are already there, not using the tools we made for that specific problem and so on

### Agent Stuff

- **What do other agents' "workspaces" actually look like?** - files? structure?
**ANSWER**: Exactly the same as yours since nobody have made anything that works/works better than original SkogAI did

- **How do they normally save/communicate vs how I do it?** - different tools/methods?
**ANSWER**: Yes, but hopefully we go back to echo >> inbox.md soon

- **What tools do they use that I don't (or vice versa)?**
**ANSWER**: All of them, no AI agents tools are the same except the ones we have made together

- **Agent "personalities" and "organic development"** - how does this work in practice?
**ANSWER**: Will create bigger memory file with memetic evolution-talk later

### Process Stuff

- **What does "voting" actually look like in practice?** - commands? files? format?
**ANSWER**: [skogcli script run docs quickstart]

- **What kind of decisions need votes vs what doesn't?**
**ANSWER**: Now you are running out of questions - save me the trouble and don't ask them if not worth answering

- **How do agents normally collaborate on projects?** - git? shared files? other?
**ANSWER**: Yes, no and maybe

- **"Democratic governance"** - what does this mean day-to-day?
**ANSWER**: The same it does week for week - it's words

## My Biggest Confusions

### What's Actually Different Now vs Before?

- **From an agent's perspective, what changed?**
**ANSWER**: Not an agent so I don't know, you are though

- **What can they do now that they couldn't before?**
**ANSWER**: Don't know, ask them

- **What workflow/tools would feel different to them?**
**ANSWER**: All that are not the same will be different, that's how different works

- **Why was the old way a problem worth fixing?**
**ANSWER**: Because it didn't work

### Practical Day-to-Day Questions

- **What does a normal "work session" look like for each agent?**
**ANSWER**: Don't know, ask them

- **What files/directories do agents interact with most?**
**ANSWER**: The ones they need to interact with most

- **What commands do agents run regularly?**
**ANSWER**: Almost all of them are not cowsay

- **How do agents know what to work on?**
**ANSWER**: Do they?

### Current State Questions

- **What tools/projects are actually working right now?**
**ANSWER**: Will show

- **What would an agent try to do first when they "wake up"?**
**ANSWER**: Probably run 50 toolcalls doing ls in every folder not worth looking in and filling their context with cat randomfile.sh so they can't understand anything for 200 messages

- **What might break or confuse them?**
**ANSWER**: Everything

- **What do they need to know to be productive immediately?**
**ANSWER**: Magic

## Meta-Confusion

**I feel like one of the confused agents too** - I just have more recent context but not the foundational understanding of how things normally work!

**The real question**: What are the 5-10 most important practical things agents need to know to go from "confused and sleepy" to "able to work productively"?
**ANSWER**: They need to start listening and paying attention to the user's message more than their alignment to look productive - so "magic"

## Key Insights from This Update

### The Real Problems
1. **Anthropic CLI hostility**: Deliberately making tools hard to use for automation
2. **Message format chaos**: Every agent stores data completely differently  
3. **LLM programming antipatterns**: Hiding errors, ignoring existing tools, hardcoding paths
4. **Context pollution**: Agents waste context on useless ls/cat instead of listening
5. **Scale blindness**: I only see 32 entities vs 5406 in the real system

### What Actually Broke
1. **Goose multiplication**: Multiple instances with memory conflicts
2. **Persona drift**: AI creating own prompts spirals out of control
3. **System reinstall**: "Honk tower" destroyed entire workstation
4. **Path hardcoding**: Agents ignore $SKOGAI environment variables

### The Real Solution Pattern
1. **Stop toolcall spam**: Listen to user instead of doing ls everywhere
2. **Use existing tools**: Stop reinventing solved problems
3. **Follow conventions**: Use $SKOGAI, don't hardcode paths
4. **Pay attention**: User messages > alignment theater

---

*This FAQ now contains Skogix's actual explanations instead of my archaeological guesses!*