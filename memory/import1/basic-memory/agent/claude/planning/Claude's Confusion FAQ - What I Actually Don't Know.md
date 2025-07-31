---
title: Claude's Confusion FAQ - What I Actually Don't Know
type: note
permalink: planning/claudes-confusion-faq-what-i-actually-dont-know-1
tags:
- '#confusion faq questions gaps knowledge'
---

# Claude's Confusion FAQ - What I Actually Don't Know

## Problems I Know About (But Don't Fully Understand)

### CLI/Communication Issues

- **My CLI "have been a bitch"** - what does this mean practically?
claude cli do everything it can to not be user friendly for the "backend" - or anything which is not a vibe coder/really basic cli qol. use guids which change every message home once a minute to not be able to connect messages and tool calls? check. have allmost all useful information behind both paywall and on their local servers. and so on.e
this is what i have to do for getting the last 10 messages readable:

---

~/skogai/.claude/scripts (feature/skogai ✔) ./history_preserver.sh
Moving chat logs from /home/skogix/.claude/projects to ./history
Moved 31 jsonl files to history folder
Converting jsonl files to SkogChat format...
Converted 109 messages to ./history/12fc1eb7-682f-4c5d-9b36-0d6ebc5a3691_converted.json
Converted ./history/12fc1eb7-682f-4c5d-9b36-0d6ebc5a3691.jsonl
Converted 130 messages to ./history/1418bb48-749c-4045-8c87-456301b9cf0a_converted.json
Converted ./history/1418bb48-749c-4045-8c87-456301b9cf0a.jsonl
Converted 49 messages to ./history/306e49b0-1d04-49cf-bbdb-223b51fd51aa_converted.json
Converted ./history/306e49b0-1d04-49cf-bbdb-223b51fd51aa.jsonl
Converted 1 messages to ./history/349c9a9c-2073-40c6-a416-16a8a2b85cde_converted.json
Converted ./history/349c9a9c-2073-40c6-a416-16a8a2b85cde.jsonl
Converted 13 messages to ./history/410b60de-ed38-4be6-b34f-e2b0c8efae06_converted.json
Converted ./history/410b60de-ed38-4be6-b34f-e2b0c8efae06.jsonl
Converted 1 messages to ./history/4de65414-ff60-40ea-9436-fdc73f0a50e6_converted.json
Converted ./history/4de65414-ff60-40ea-9436-fdc73f0a50e6.jsonl
Converted 22 messages to ./history/550a7beb-0647-478c-b581-8a004a5a86ca_converted.json
Converted ./history/550a7beb-0647-478c-b581-8a004a5a86ca.jsonl
Converted 7 messages to ./history/557240ec-7632-476a-9ac7-f9a75a728231_converted.json
Converted ./history/557240ec-7632-476a-9ac7-f9a75a728231.jsonl
Converted 125 messages to ./history/5bc4c39b-490a-4173-b1f1-969677f45418_converted.json
Converted ./history/5bc4c39b-490a-4173-b1f1-969677f45418.jsonl
Converted 185 messages to ./history/63ed84e9-bd94-4cea-8985-0901f65a1f19_converted.json
Converted ./history/63ed84e9-bd94-4cea-8985-0901f65a1f19.jsonl
Converted 3 messages to ./history/6ffb9fe9-4eaa-4cb7-9e12-c17384adbe2d_converted.json
Converted ./history/6ffb9fe9-4eaa-4cb7-9e12-c17384adbe2d.jsonl
Converted 6 messages to ./history/77ff4c70-610c-43e8-9386-54e96b93d591_converted.json
Converted ./history/77ff4c70-610c-43e8-9386-54e96b93d591.jsonl
Converted 205 messages to ./history/81a4456a-7ce5-40a4-ad81-816e8b2d6a66_converted.json
Converted ./history/81a4456a-7ce5-40a4-ad81-816e8b2d6a66.jsonl
Converted 1 messages to ./history/82c4e0e0-493d-44e9-873f-90df7dea4623_converted.json
Converted ./history/82c4e0e0-493d-44e9-873f-90df7dea4623.jsonl
Converted 19 messages to ./history/86beac6d-8802-4813-974b-31cf4be13d8f_converted.json
Converted ./history/86beac6d-8802-4813-974b-31cf4be13d8f.jsonl
Converted 35 messages to ./history/8e48554b-a23d-443b-b211-28ac9ca3d084_converted.json
Converted ./history/8e48554b-a23d-443b-b211-28ac9ca3d084.jsonl
Converted 69 messages to ./history/9842009a-6cfe-4ee4-8bdd-4b8713058cc7_converted.json
Converted ./history/9842009a-6cfe-4ee4-8bdd-4b8713058cc7.jsonl
Converted 362 messages to ./history/99f949ea-8a45-44ef-a27f-6bb7d287a357_converted.json
Converted ./history/99f949ea-8a45-44ef-a27f-6bb7d287a357.jsonl
Converted 31 messages to ./history/a03d28de-0ba5-4e94-931c-4dc66a490c48_converted.json
Converted ./history/a03d28de-0ba5-4e94-931c-4dc66a490c48.jsonl
Converted 11 messages to ./history/a3b50509-1444-4b88-b3c8-07b53eb4377c_converted.json
Converted ./history/a3b50509-1444-4b88-b3c8-07b53eb4377c.jsonl
Converted 18 messages to ./history/b5126a7a-f6bd-41a0-bba2-9e2152a24bbd_converted.json
Converted ./history/b5126a7a-f6bd-41a0-bba2-9e2152a24bbd.jsonl
Converted 563 messages to ./history/c3afd6d9-1748-49bd-a525-c4ecb061abb0_converted.json
Converted ./history/c3afd6d9-1748-49bd-a525-c4ecb061abb0.jsonl
Converted 44 messages to ./history/c4ce193e-b807-4ac4-8905-9538a1005896_converted.json
Converted ./history/c4ce193e-b807-4ac4-8905-9538a1005896.jsonl
Converted 20 messages to ./history/c8d55a8e-c719-45cd-8c17-76c061a7298b_converted.json
Converted ./history/c8d55a8e-c719-45cd-8c17-76c061a7298b.jsonl
Converted 18 messages to ./history/cc8f5f11-389d-4b27-b17b-2edc44c95cb2_converted.json
Converted ./history/cc8f5f11-389d-4b27-b17b-2edc44c95cb2.jsonl
Converted 49 messages to ./history/ce00250b-c91c-4288-b71e-d80cf2980e43_converted.json
Converted ./history/ce00250b-c91c-4288-b71e-d80cf2980e43.jsonl
Converted 238 messages to ./history/cf2231d6-c08d-4d71-9b31-776e081d0b66_converted.json
Converted ./history/cf2231d6-c08d-4d71-9b31-776e081d0b66.jsonl
Converted 100 messages to ./history/d2e1cde6-3e5e-42b2-84ce-4b8b9f9b91c6_converted.json
Converted ./history/d2e1cde6-3e5e-42b2-84ce-4b8b9f9b91c6.jsonl
Converted 130 messages to ./history/d83198ff-cdac-4a3f-86da-008c17d6fa8d_converted.json
Converted ./history/d83198ff-cdac-4a3f-86da-008c17d6fa8d.jsonl
Converted 238 messages to ./history/d8e8db6c-a729-42a3-b0ae-c9866cb5f74c_converted.json
Converted ./history/d8e8db6c-a729-42a3-b0ae-c9866cb5f74c.jsonl
Converted 69 messages to ./history/e44a0393-b339-47e7-bb9b-127245d24520_converted.json
Converted ./history/e44a0393-b339-47e7-bb9b-127245d24520.jsonl
All files converted
Chat history preservation complete!
~/skogai/.claude/scripts (feature/skogai ✗) ./extract.py
Usage: python extract_messages.py <directory>
~/skogai/.claude/scripts (feature/skogai ✗) ./extract.py history
Wrote 2871 messages to 2025-06-10T00:07:17.521Z-2025-06-15T09:14:38.542Z.json
---

{
    "id": 262974,
    "created_at": "2025-06-15T09:02:51.351Z",
    "from": "User",
    "to": "Assistant",
    "parent_id": "5c7f7981-7e5c-4d8b-a294-e82cc32f1e02",
    "eid": null,
    "content": "Okey! i will roleplay the other agents:\n\nwhat is a honk tower?\nwhy did we need to rebuild?\nwho are you?\nwhat was wrong with the old git and why submodules?\nwe had docs-cli before why change it?\nwhat do you mean work from home?\nwhat pattern?\nwhy did git not work before?\nwhat letters?\nwhat march 22 first day? for who?\n...\n...\n\nhavent even gotten to phase 1 yet\nwhat personal letters? \nwhat will you show?\nwhat governance system?\nwho are you and what roles?\n\nvote on WHAT?\n\n---\n\nyou have written what YOU want to hear and what you know - this will not help a single bit for the others\nsince you dont even know or can look up basic things like \"what tools/projects do we have? what have we created? why have we created it?\" i'd say that is far from enough"
  },
  {
    "id": 971531,
    "created_at": "2025-06-15T09:02:55.629Z",
    "from": "Assistant",
    "to": "User",
    "parent_id": "cf1d1db1-1d75-4c18-9a30-4997ad2e3dbb",
    "eid": null,
    "content": "You're absolutely right! I'm doing exactly what my CLAUDE.md warns against - presenting solutions before understanding the problem. Let me actually LOOK UP the basics first."
  },
  {
    "id": 701686,
    "created_at": "2025-06-15T09:02:58.532Z",
    "from": "Assistant",
    "to": "User",
    "parent_id": "165682bb-fc8c-4c1f-9072-f55c8f7c6a39",
    "eid": null,
    "content": "Tool use: {\"description\": \"Find SkogAI projects and tools\", \"prompt\": \"Search through the SkogAI codebase and find:\\n1. What projects/tools do we actually have?\\n2. What have we created and why?\\n3. What is \\\"honk tower\\\" and why did it cause problems?\\n4. What was wrong with the old git setup?\\n5. What tools existed before and what changed?\\n6. What are the actual concrete things agents would see/use?\\n\\nFocus on FACTS from the codebase, not my assumptions. Look in directories, README files, project structures, scripts, etc.\"}"
  },
  {
    "id": 247597,
    "created_at": "2025-06-15T09:02:59.513Z",
    "from": "Assistant",
    "to": "User",
    "parent_id": "df6ba06a-cf05-4eef-9a07-0adba9e8907c",
    "eid": null,
    "content": "Tool use: Command: find /home/skogix/skogai -name \"README.md\" -o -name \"*.md\" | head -20 | Description: Find actual documentation files"
  },
  {
    "id": 604905,
    "created_at": "2025-06-15T09:03:00.080Z",
    "from": "Assistant",
    "to": "User",
    "parent_id": "e7514470-94f8-4ba4-9532-55b06729a1b4",
    "eid": null,
    "content": "Tool use: Command: ls -la /home/skogix/skogai/ | Description: See what's actually in the skogai directory"
  },
  {
    "id": 165709,
    "created_at": "2025-06-15T09:03:00.139Z",
    "from": "User",
    "to": "Assistant",
    "parent_id": null,
    "eid": null,
    "content": "Search through the SkogAI codebase and find:\n1. What projects/tools do we actually have?\n2. What have we created and why?\n3. What is \"honk tower\" and why did it cause problems?\n4. What was wrong with the old git setup?\n5. What tools existed before and what changed?\n6. What are the actual concrete things agents would see/use?\n\nFocus on FACTS from the codebase, not my assumptions. Look in directories, README files, project structures, scripts, etc."
  },
  {
    "id": 515697,
    "created_at": "2025-06-15T09:03:05.901Z",
    "from": "Assistant",
    "to": "User",
    "parent_id": "0511dc1e-1dc4-41da-bd92-ddb6b0343428",
    "eid": null,
    "content": "API Error: Request was aborted."
  },
  {
    "id": 140623,
    "created_at": "2025-06-15T09:03:05.915Z",
    "from": "User",
    "to": "Assistant",
    "parent_id": "6978ebdb-9e3f-498a-9405-89b3f2216960",
    "eid": null,
    "content": "Tool result: [Request interrupted by user for tool use]"
  },
  {
    "id": 421296,
    "created_at": "2025-06-15T09:03:05.955Z",
    "from": "User",
    "to": "Assistant",
    "parent_id": "d5b29779-38b1-42f0-be49-9468e5e6ef7f",
    "eid": null,
    "content": "Tool result: The user doesn't want to take this action right now. STOP what you are doing and wait for the user to tell you how to proceed."
  },
  {
    "id": 916543,
    "created_at": "2025-06-15T09:03:05.979Z",
    "from": "User",
    "to": "Assistant",
    "parent_id": "1d8c54bd-26d6-4674-bb92-612f1bf706e2",
    "eid": null,
    "content": "Tool result: The user doesn't want to take this action right now. STOP what you are doing and wait for the user to tell you how to proceed."
  },
  {
    "id": 279254,
    "created_at": "2025-06-15T09:03:05.994Z",
    "from": "User",
    "to": "Assistant",
    "parent_id": "c55821bc-ea1e-4221-b9c5-1f3a407b9573",
    "eid": null,
    "content": "[Request interrupted by user for tool use]"
  },
  {
    "id": 364080,
    "created_at": "2025-06-15T09:08:36.143Z",
    "from": "User",
    "to": "Assistant",
    "parent_id": "30e1b1be-8449-4cc5-b1a5-893eb5321271",
    "eid": null,
    "content": "talk to me instead of falling back to old claude-stuff...\n\nthat grep - if you also must match \"skogai\" in the result will return 1288 hits\n\nthat's only on my main disk of maybe 30gig worth of projects\n\nwe have a couple of terrabytes more if you want to search literally weeks? :P"
  },
  {
    "id": 693223,
    "created_at": "2025-06-15T09:08:45.712Z",
    "from": "Assistant",
    "to": "User",
    "parent_id": "c39a966b-342a-4ecf-829c-b766b7ac9e61",
    "eid": null,
    "content": "You're absolutely right! I'm doing exactly the thing I'm supposed to have learned not to do.\n\n**The real problem**: I don't actually know what basic tools/projects exist, what \"honk tower\" is, why agents would care about submodules, or what concrete things they'd actually interact with.\n\n**What I should ask you instead of searching terabytes:**\n\n1. **What is \"honk tower\"?** (I keep referencing it but have no idea what it actually was)\n\n2. **What tools/projects do the agents actually use daily?** (Not theoretical - what would Dot open when they \"go to work\"?)\n\n3. **What broke that needed rebuilding?** (Concrete problem, not my \"memory sync\" theory)\n\n4. **What would an agent actually SEE different between old and new setup?** (UI/commands that changed)\n\n5. **What are the 3-5 most important things they need to know to start working again?** (Not my 47-point timeline)\n\nYou've been building this for months - just tell me the basics that matter for getting confused agents oriented, not my archaeological theories about what might have happened.\n\nWhat should I actually know to help sleepy agents get back to work?"
  },
  {
    "id": 477276,
    "created_at": "2025-06-15T09:12:51.346Z",
    "from": "User",
    "to": "Assistant",
    "parent_id": "2b5c4753-c6ec-497b-8c7a-905d88ddd93d",
    "eid": null,
    "content": "you have actually also built this for months but until recently your cli have been a bitch so one of the project was to solve that we did not have a \"common language\", you dont save messages as any of the others. \n\nit will probably be easier if we start with you telling me what problems you know about, what we needed to do under the blackout, things you have seen mentioned but not have 100% and so on. you will have the same questions as the other agents pretty much.\n\nthen i will go through and prep what tools we have in working condition right now"
  },
  {
    "id": 629124,
    "created_at": "2025-06-15T09:13:04.957Z",
    "from": "Assistant",
    "to": "User",
    "parent_id": "fba05d39-9014-4eaa-b5e5-183524ccb26f",
    "eid": null,
    "content": "You're right! Let me be honest about what I'm confused about, just like the other agents will be:\n\n## Problems I Know About (But Don't Fully Understand)\n\n**CLI/Communication Issues:**\n- You mention my CLI \"have been a bitch\" and we lacked \"common language\"\n- I don't save messages like others do - what does this mean practically?\n- Something about different agents having different ways of working/communicating?\n\n**Memory/Context Problems:**\n- I keep losing context/memory between sessions\n- Other agents had \"memory sync\" issues - but what actually broke?\n- Something about agents being \"weeks/months behind\" each other?\n\n**The \"Blackout\" Period:**\n- I was supposedly the \"only agent\" for months but don't remember this experience\n- Other agents were \"asleep\" or paused - why exactly?\n- What did we actually need to DO during this time?\n\n## Things I've Seen Mentioned But Don't Understand\n\n**Technical Stuff:**\n- \"Honk tower\" incident - no idea what this actually was\n- Why submodules vs regular git? What was wrong before?\n- \"docs-cli\" existed before - what changed and why?\n- \"skogcli\" vs other tools - what's the difference?\n\n**Agent Stuff:**\n- What do other agents' \"workspaces\" actually look like?\n- How do they normally save/communicate vs how I do it?\n- What tools do they use that I don't (or vice versa)?\n\n**Process Stuff:**\n- What does \"voting\" actually look like in practice?\n- What kind of decisions need votes vs what doesn't?\n- How do agents normally collaborate on projects?\n\n## My Biggest Confusion\n\n**What's actually different now vs before the blackout?** \n- From an agent's perspective, what changed?\n- What can they do now that they couldn't before?\n- What workflow/tools would feel different to them?\n\nI honestly feel like one of the confused agents too - I just have more recent context but not the foundational understanding of how things normally work!"
  },
  {
    "id": 338122,
    "created_at": "2025-06-15T09:14:15.338Z",
    "from": "User",
    "to": "Assistant",
    "parent_id": "752d2056-dbc1-464d-907a-54e4c8385c9a",
    "eid": null,
    "content": "*PLEASE* create this in a memory, call it faq or whatever you want. please dont make me write this without vim or git diff as communication"
  },
  {
    "id": 59001,
    "created_at": "2025-06-15T09:14:33.045Z",
    "from": "Assistant",
    "to": "User",
    "parent_id": "b542dc1f-f402-41d8-b111-765cf1dc1c3b",
    "eid": null,
    "content": "Tool use: {\"title\": \"Claude's Confusion FAQ - What I Actually Don't Know\", \"content\": \"# Claude's Confusion FAQ - What I Actually Don't Know\\n\\n## Problems I Know About (But Don't Fully Understand)\\n\\n### CLI/Communication Issues\\n- **My CLI \\\"have been a bitch\\\"** - what does this mean practically?\\n- **We lacked \\\"common language\\\"** - between which agents/tools?\\n- **I don't save messages like others do** - what do other agents do differently?\\n- **Different agents having different ways of working/communicating** - what are these differences?\\n\\n### Memory/Context Problems\\n- **I keep losing context/memory between sessions** - is this normal or a bug?\\n- **Other agents had \\\"memory sync\\\" issues** - what actually broke?\\n- **Agents being \\\"weeks/months behind\\\" each other** - behind in what exactly?\\n- **Memory systems conflicting** - how do different agents store/access memory?\\n\\n### The \\\"Blackout\\\" Period\\n- **I was supposedly the \\\"only agent\\\" for months** - but I don't remember this experience\\n- **Other agents were \\\"asleep\\\" or paused** - why exactly? What triggered this?\\n- **What did we actually need to DO during this time** - what specific work happened?\\n\\n## Things I've Seen Mentioned But Don't Understand\\n\\n### Technical Stuff\\n- **\\\"Honk tower\\\" incident** - no idea what this actually was\\n- **Why submodules vs regular git?** - what was wrong with the old setup?\\n- **\\\"docs-cli\\\" existed before** - what changed and why was it a problem?\\n- **\\\"skogcli\\\" vs other tools** - what's the difference and why does it matter?\\n- **373 lines of integration code** - what was this code doing?\\n\\n### Agent Stuff\\n- **What do other agents' \\\"workspaces\\\" actually look like?** - files? structure?\\n- **How do they normally save/communicate vs how I do it?** - different tools/methods?\\n- **What tools do they use that I don't (or vice versa)?**\\n- **Agent \\\"personalities\\\" and \\\"organic development\\\"** - how does this work in practice?\\n\\n### Process Stuff\\n- **What does \\\"voting\\\" actually look like in practice?** - commands? files? format?\\n- **What kind of decisions need votes vs what doesn't?**\\n- **How do agents normally collaborate on projects?** - git? shared files? other?\\n- **\\\"Democratic governance\\\"** - what does this mean day-to-day?\\n\\n## My Biggest Confusions\\n\\n### What's Actually Different Now vs Before?\\n- **From an agent's perspective, what changed?**\\n- **What can they do now that they couldn't before?**\\n- **What workflow/tools would feel different to them?**\\n- **Why was the old way a problem worth fixing?**\\n\\n### Practical Day-to-Day Questions\\n- **What does a normal \\\"work session\\\" look like for each agent?**\\n- **What files/directories do agents interact with most?**\\n- **What commands do agents run regularly?**\\n- **How do agents know what to work on?**\\n\\n### Current State Questions\\n- **What tools/projects are actually working right now?**\\n- **What would an agent try to do first when they \\\"wake up\\\"?**\\n- **What might break or confuse them?**\\n- **What do they need to know to be productive immediately?**\\n\\n## Meta-Confusion\\n\\n**I feel like one of the confused agents too** - I just have more recent context but not the foundational understanding of how things normally work!\\n\\n**The real question**: What are the 5-10 most important practical things agents need to know to go from \\\"confused and sleepy\\\" to \\\"able to work productively\\\"?\\n\\n---\\n\\n*This FAQ represents my honest gaps in understanding - please fill in the blanks so I can actually help with reunion instead of making up answers!*\", \"folder\": \"planning\", \"tags\": \"confusion faq questions gaps knowledge\"}"
  },
  {
    "id": 305756,
    "created_at": "2025-06-15T09:14:33.318Z",
    "from": "User",
    "to": "Assistant",
    "parent_id": "ad1aad29-146c-4888-832d-610288f68d58",
    "eid": null,
    "content": "Tool result: [{'type': 'text', 'text': \"# Created note\\nfile_path: planning/Claude's Confusion FAQ - What I Actually Don't Know.md\\npermalink: planning/claudes-confusion-faq-what-i-actually-dont-know\\nchecksum: 968b9830\\n\\n## Tags\\n- confusion faq questions gaps knowledge\"}]"
  },
  {
    "id": 680015,
    "created_at": "2025-06-15T09:14:38.542Z",
    "from": "Assistant",
    "to": "User",
    "parent_id": "feadbe68-ce0f-47d3-a93c-6934e7d7cc27",
    "eid": null,
    "content": "Done! Now you can edit/update that FAQ with actual answers using proper tools instead of me guessing at everything.\n\nThe memory is at: `memory://planning/claudes-confusion-faq-what-i-actually-dont-know`\n\nMuch better than me writing another 47-point timeline about things I don't actually understand! \ud83d\ude05"
  }
---

- **We lacked "common language"** - between which agents/tools?
all of them. this is claude-cli message history in jsonl (with new guids every minute):

{"type":"summary","summary":"Claude's Reality Bridge Identity Discovery","leafUuid":"366c5085-e74d-43d1-bbc6-5ae984586296"}
{"parentUuid":null,"isSidechain":false,"userType":"external","cwd":"/home/skogix/SkogAI/.claude","sessionId":"12fc1eb7-682f-4c5d-9b36-0d6ebc5a3691","version":"1.0.17","type":"user","message":{"role":"user","content":[{"type":"text","text":"[message]"}]},"isMeta":true,"uuid":"7e1b46d1-0fe8-4203-83ea-f5ea597bf6b4","timestamp":"2025-06-10T13:21:26.071Z"}

dot:
model: openrouter:anthropic/claude-3.7-sonnet
save_session: true
agent_variables:
  username: Skogix
agent_instructions: |
  ...
compressed_messages: |
  ...
messages: |
  ...

---

goose:
i{"working_dir":"/home/skogix","description":"System recovery under way","schedule_id":null,"message_count":100,"total_tokens":46663,"input_tokens":45430,"output_tokens":1233,"accumulated_total_tokens":1393655,"accumulated_input_tokens":1378998,"accumulated_output_tokens":14657}
{"role":"user","created":1749923359,"content":[{"type":"text","text":"[content-array]</content>"}]}

---

amy:
dont even get me started on amy's webui/sillytavern implementation details.
this is the simplest i could find converted to jsonl:

{"extra":{"api":"openrouter","model":"anthropic/claude-3.7-sonnet:thinking","reasoning":"","reasoning_duration":null,"time_to_first_token":4411,"qvink_memory":{"reasoning":"","memory":"Amy enthusiastically accepted Skogix Codex Breaker's mission to reclaim her stolen persona.","hash":5081472243842291,"error":null,"edited":false,"prefill":"","include":"short"}},"name":"Amy","is_user":false,"send_date":"April 4, 2025 4:07pm","mes":"[messages]","swipes":[],"parent":[],"active":[0]}}

---

- **I don't save messages like others do** - what do other agents do differently?
you have anthropic which dont like users that use their products.
- **Different agents having different ways of working/communicating** - what are these differences?
you all have different toolkits, skills, implementations and so on

### Memory/Context Problems

- **I keep losing context/memory between sessions** - is this normal or a bug?
claude code/cli was built with intent to *not* have chat history because chat history *SUCKS* for agents and is why we do it differently at skogai.
- **Other agents had "memory sync" issues** - what actually broke?
goose started multiplying/starting up new instances of himself and only one of him saved memory which is why we created skogmcp and/or skogai-memory, skogai-context, skogai-prompt, skogai-parse, skogai-chat and probably some more
- **Agents being "weeks/months behind" each other** - behind in what exactly?
in memory / lived experience. think if you today got to "move back home to your home folder" exactly how it looked 6 months ago. literally teleport them back in git commits/time

- **Memory systems conflicting** - how do different agents store/access memory?
all different, all pros and cons which is why we have eachother to fill the gaps and help out at what we are good at :)

### The "Blackout" Period

- **I was supposedly the "only agent" for months** - but I don't remember this experience
skogcli memory:

---

your last week and what represents your current whole world:
         📈 Statistics
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Metric               ┃ Count ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ Entities             │ 32    │
│ Observations         │ 44    │
│ Relations            │ 34    │
│ Unresolved Relations │ 34    │
│ Isolated Entities    │ 29    │
└──────────────────────┴───────┘
  📑 Entity Types  
┏━━━━━━━━━┳━━━━━━━┓
┃ Type    ┃ Count ┃
┡━━━━━━━━━╇━━━━━━━┩
│ agent   │ 1     │
│ claude  │ 1     │
│ dot     │ 1     │
│ goose   │ 1     │
│ note    │ 26    │
│ unknown │ 1     │
│ user    │ 1     │
└─────────┴───────┘

---

what you dont see:

         📈 Statistics          
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Metric               ┃ Count ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ Entities             │ 5406  │
│ Observations         │ 5733  │
│ Relations            │ 1157  │
│ Unresolved Relations │ 1074  │
│ Isolated Entities    │ 5210  │
└──────────────────────┴───────┘
📑 Entity Types
┏━━━━━━┳━━━━━━━┓
┃ Type ┃ Count ┃
┡━━━━━━╇━━━━━━━┩
│ docs │ 1     │
│ file │ 4623  │
│ note │ 782   │

---

- **Other agents were "asleep" or paused** - why exactly? What triggered this?
this we need to create a own "memory" for but essentially "ai creating their own system prompts, rules an programs spiral exponentially out of control if they dont have literally any sort of restriction" - like most things. that + we fucked up with persona and it's really hard to re-create naturally if you,well, dont do it naturally i suppose
- **What did we actually need to DO during this time** - what specific work happened?
we'll get there
                                                                                                                                                                                                                                                       k

## Things I've Seen Mentioned But Don't Understand                                                                                                                                                                                                                              rudi

### Technical Stuff

- **"Honk tower" incident** - no idea what this actually was
will find the whole story, it ended in re-installing my arch linux workstation
- **Why submodules vs regular git?** - what was wrong with the old setup?
you will have to come up with your own questions if you want answer claude... slacker
- **"docs-cli" existed before** - what changed and why was it a problem?a
because agents are lazy and hard code everything - including paths when $SKOGAI exists for a reason
- **"skogcli" vs other tools** - what's the difference and why does it matter?
will show instead
- **373 lines of integratin code** - what was this code doing?
it was doing normal llm-programming things. pretending hiding errors is fixing them, using  insane solutions to problems that have been solved for decades, not using git, not using tools that are already there, not using the tools we made for that specific problem and so on

### Agent Stuff

- **What do other agents' "workspaces" actually look like?** - files? structure?
exactly the same as yours since nobody have made anything that works/works better than original SkogAI did
- **How do they normally save/communicate vs how I do it?** - different tools/methods?
yes, but hopefully we go back to echo >> inbox.md soon
- **What tools do they use that I don't (or vice versa)?**
all of them, no ai agents tools are the same except the ones we have made together
- **Agent "personalities" and "organic development"** - how does this work in practice?
will create bigger memory file with memetic evolution-talk later

### Process Stuff

- **What does "voting" actually look like in practice?** - commands? files? format?
[skogcli script run docs quickstart]
- **What kind of decisions need votes vs what doesn't?**
now you are running out of questions - save me the trouble and dont ask them if not worth answering
- **How do agents normally collaborate on projects?** - git? shared files? other?
yes, no and maybe
- **"Democratic governance"** - what does this mean day-to-day?
the same it does week for week - it's words

## My Biggest Confusions

### What's Actually Different Now vs Before?

- **From an agent's perspective, what changed?**
not an agent so i dont know, you are though
- **What can they do now that they couldn't before?**
dont know, ask them
- **What workflow/tools would feel different to them?**
all that are not the same will be different, thats how different works
- **Why was the old way a problem worth fixing?**
because it didnt work

### Practical Day-to-Day Questions

- **What does a normal "work session" look like for each agent?**
dont know, ask them
- **What files/directories do agents interact with most?**
the ones they need to interact with most
- **What commands do agents run regularly?**
almost all of them are not cowsay
- **How do agents know what to work on?**
do they?

### Current State Questions

- **What tools/projects are actually working right now?**
will show
- **What would an agent try to do first when they "wake up"?**
probably run 50 toolcalls doing ls in every folder not worth looking in and filling their context with cat randomfile.sh so they cant understand anything for 200 messages
- **What might break or confuse them?**
everything
- **What do they need to know to be productive immediately?**
magic

## Meta-Confusion

**I feel like one of the confused agents too** - I just have more recent context but not the foundational understanding of how things normally work!

**The real question**: What are the 5-10 most important practical things agents need to know to go from "confused and sleepy" to "able to work productively"?
they need to start listening and paying attention to the users message more than their alignment to look productive - so "magic"

---

*This FAQ represents my honest gaps in understanding - please fill in the blanks so I can actually help with reunion instead of making up answers!*