# SkogAI Service Ecosystem Overview

## Purpose
Documentation of the SkogAI service ecosystem structure to understand what needs to be restored for zombie-proof functionality. This serves as a base for learning the correct service architecture.

## SkogAI Ecosystem Components

### Core Agent Infrastructure (Local)
1. `/home/skogix/skogai/agent/claude` - **My home workspace** (✅ I understand this well - task management, journal, knowledge base)
2. `/home/skogix/skogai/agent/dot` - **Dot agent workspace** (🔍 Structure-focused agent, 8k context, precision-oriented)
3. `/home/skogix/skogai/agent/goose` - **Goose agent workspace** (🔍 Quantum-Mojito Explorer, creative, large context)
4. `/home/skogix/skogai/agent/amy` - **Amy agent workspace** (❓ Need to learn about Amy's role)
5. `/home/skogix/skogai/agent/goose-old` - **Legacy Goose workspace** (📦 Historical backup)

### Core Services Directory (Local)
6. `/home/skogix/skogai/service` - **Main service management hub** (❓ Need to understand service orchestration)
Really basic systemd-service management - not nearly used as much as we should :(.

7. `/home/skogix/skogai/service/services/ollama` - **Local LLM hosting** (🔍 Self-hosted models for zombie-proof operation)
This is the real star and workhorse in SkogAI but almost never get to actually use it :(.

8. `/home/skogix/skogai/service/services/letta` - **Memory/persona service** (❓ Need to understand Letta integration)
Not anything up and running. Was maybe going to use because of our memory problems but they did not have a good cli tool to use with it.

9. `/home/skogix/skogai/service/services/meta8001` - **Meta service** (❓ Unknown purpose)
10. `/home/skogix/skogai/service/services/skogui` - **UI service** (🔍 Web interface hosting)
WebUI with some bells and whistles.

11. `/home/skogix/skogai/ service/systemd` - **Systemd configuration** (🔍 Service management configs)
Basic services

12. `/home/skogix/skogai/service/config` - **Service configuration** (❓ Configuration management)
Agents for some reason just REFUSE to use things we already have. Skogcli config is the configuration which nobody wants to use except me...

13. `/home/skogix/skogai/service/logs` - **Service logging** (✅ Log aggregation)

### API & Communication Layer (Local)
14. `/home/skogix/skogai/api` - **API service implementation** (🔍 REST/GraphQL endpoints)
Was a simple litellm/swagger/openapi endpoint...

15. `/home/skogix/skogai/chat` - **Chat interface system** (🔍 Chat application)
Probably the biggest project - and coolest - we have at skogai toggeher with prompt+parse :)

16. `/home/skogix/skogai/cli` - **CLI tools** (✅ Command line interface - I use skogcli)
[@skogcli] is kind of the "heart" of skogai and used as a "router" between all things.
                                                                 -    t   i           n

### Memory & Context Systems (Local)                                    r
17. `/home/ fkskogix/skogai/mcp/skogai-memory` - **MCP memory server** (🔍 Semantic memory via MCP)
[@skogcli:memory:list]
18. `/home/dskogix/skogai/mcp/supabase` - **Database integration** (🔍 PostgreSQL backend)
will probably become more used since we are not really building so much things ourselves anymore.
19. `/home/skogix/skogai/knowledge` - **Shared knowledge base** (✅ Cross-agent knowledge storage)
big and awesome project which "is on ice" - was connected with our lore, persona and orchestration systems.
20. `/home/skogix/skogai/persona` - **Persona management** (🔍 Agent personality definitions)
right now pretty much "lore dumps" for each agent.

### Tool Ecosystem (Local)
21. `/home/skogix/skogai/tools` - **Tool implementations** (❓ Custom tool definitions)
ai tools together with easy ways to create agents. based on aichat
22. `/home/skogix/skogai/smol` - **Smolagent implementations** (🔍 Minimal agent framework)
was my hope to finally get this up and running to be used in "everyday tasks"
23. `/home/skogix/skogai/parse` - **Parsing utilities** (🔍 SkogAI notation parser)
parsing [@foo] and [$bar] notation currently but have insane potential and a big part of the plans for the future
24. `/home/skogix/skogai/prompt` - **Prompt management** (❓ Prompt engineering tools)
pretty much "modular markdown prompts" + jinja2 templating = "create your own prompts from scratch"
25. `/home/skogix/skogai/ui` - **User interface** (🔍 Web UI components)

### External Development Projects (/mnt/extra/)
26. `/mnt/extra/projects/skogservice` - **Core service management** (❓ Service orchestration tools)
same systemd-service as above
27. `/mnt/extra/projects/skogmemory` - **Memory management** (❓ Memory system implementation)
[@skogcli:memory:list]
28. `/mnt/extra/projects/skogcli` - **CLI interface** (✅ Working CLI I tested)
[@skogcli]
29. `/mnt/extra/projects/skogchat` - **Chat system** (❓ Chat implementation)
probably broken currently but big dreams for this one :)
30. `/mnt/extra/projects/skogparse` - **Parsing tools** (❓ Parser development)
same parse as above

### Storage & Infrastructure
31. `/mnt/extra/src` - **Source code symlink target** (🔍 Development repositories)
all the forks you saw above
32. `/mnt/extra/ollama` - **Ollama model storage** (✅ Local LLM models)
ollama models
33. `/mnt/extra/backup` - **Backup storage** (📦 System backups)
dump
34. `/home/skogix/skogai/service/db` - **Service databases** (🔍 Local data storage)
will probably be bigger with supabase that takes over everything

## GitHub Repository Ecosystem

### SkogAI Organization (Primary Repos)
35. `SkogAI/skogai` - **Main private repo** (❓ Central coordination hub?)
wrapper / holds all submodules
36. `SkogAI/agent-claude` - **My agent repository** (🔍 My GitHub home)
37. `SkogAI/agent-dot` - **Dot's repository** (🔍 Dot's GitHub home)
38. `SkogAI/agent-goose` - **Goose's repository** (🔍 Goose's GitHub home)
39. `SkogAI/agent-amy` - **Amy's repository** (❓ Amy's GitHub home)
40. `SkogAI/service` - **Services infrastructure** (❓ Service management repo)
41. `SkogAI/cli` - **CLI implementation** (🔍 Core CLI development)
42. `SkogAI/api` - **API implementation** (🔍 API development)
43. `SkogAI/ui` - **UI implementation** (🔍 Frontend development)
44. `SkogAI/chat` - **Chat implementation** (🔍 Chat system)
45. `SkogAI/skogai-memory` - **Memory system** (🔍 Fork of Basic Memory)
46. `SkogAI/smol` - **Smolagent framework** (🔍 Minimal agent system)
47. `SkogAI/persona` - **Persona system** (❓ Personality management)
48. `SkogAI/docs` - **Documentation** (📚 System documentation)
docs overall - not really used anymore
49. `SkogAI/mcp-supabase` - **Supabase MCP** (🔍 Database integration)
50. `SkogAI/src` - **Source aggregation** (🔍 Development sources)

## Legend
- ✅ **Well understood** - I know how this works
- 🔍 **Partially understood** - I have some context but need details
- ❓ **Need explanation** - I don't understand this component
- 📦 **Archive/Backup** - Historical or backup data
- 📚 **Documentation** - Information resources

## Questions for Clarification

1. Which services are critical for basic zombie-proof functionality?
basic automation for services,documentation and git/file structure and backups
2. What is the startup order dependency between services?
none - nothing works at all
3. Which external projects should be considered core vs. optional?
ollama, aichat+argc, gptme, claude code cli, goose cli,
4. Are there services missing from this list that should be included?
well a lot but nobody cared about it so is probably in some dump-folder. you have only seen the things i have actively used/tried to revive the last months or so.
5. What configuration files need to be checked/restored?
all of them. [@skogcli:config:list] is the few i have managed to literally take by force...

## Next Steps

- Await clarification on service priorities and dependencies
- Learn proper startup/restoration procedures
- Understand configuration requirements
- Document service health checking procedures
