i *literally* included the commands

---

skogcli misc run create-persona help
SkogAI Persona Creation Tool

Usage: /home/skogix/.config/skogcli/scripts/create-persona.sh [command] [options]

Commands:
  create     Create a new persona
  list       List all available personas
  show ID    Display details about a specific persona
  edit ID    Edit a persona
  delete ID  Delete a persona
  help       Show this help message

Examples:
  /home/skogix/.config/skogcli/scripts/create-persona.sh create "Forest Guardian" "A magical protector" "compassionate,wise,gentle" "serene"
  /home/skogix/.config/skogcli/scripts/create-persona.sh list
  /home/skogix/.config/skogcli/scripts/create-persona.sh show persona_1234567890

---

 ✘ skogix@skogix-workstation  ~/skogai   master  ./generate-agent-lore.py --help
usage: generate-agent-lore.py [-h] --agent-type AGENT_TYPE
                              [--description DESCRIPTION]
                              [--model MODEL]
                              [--persona PERSONA]
                              [--create-persona]
                              [--export EXPORT]

Generate specialized lore for agents

options:
  -h, --help            show this help message and exit
  --agent-type AGENT_TYPE
                        Type of agent (writer, researcher,
                        planner, etc.)
  --description DESCRIPTION
                        Description of the agent's purpose
  --model MODEL         Ollama model to use
  --persona PERSONA     Link to existing persona ID
  --create-persona      Create a new persona for this agent
                        type
  --export EXPORT       Export as SillyTavern lorebook to
                        this path

---

 skogix@skogix-workstation  ~/skogai/tools   master  ./llama-lore-integrator.sh
Llama Lore Integrator - Analyze and integrate existing content into lore/persona system

Usage: ./llama-lore-integrator.sh [model_name] [command] [options]

Commands:
  extract-lore file.txt [json/lore]      Extract lore from a text file
  create-entries "analysis text" [book_id]  Create entries from analysis
  create-persona file.txt                Create a persona from text file
  analyze-connections book_id            Find connections between entries
  import-directory dir "Title" "Desc"    Create lorebook from directory
  help                                   Show this help message

Example:
  ./llama-lore-integrator.sh llama3 extract-lore story.txt json
  ./llama-lore-integrator.sh llama3 create-persona character.txt
  ./llama-lore-integrator.sh llama3 import-directory /path/to/world "My Fantasy World" "A rich fantasy setting"
 skogix@skogix-workstation  ~/skogai/tools   master  ./llama-lore-creator.sh
Llama Lore Creator - Generate lore content using local LLM

Usage: ./llama-lore-creator.sh [model_name] [command] [options]

Commands:
  entry "Title" "category"            Generate a lore entry
  persona "Name" "Description"       Generate a persona with traits
  lorebook "Title" "Desc" count      Generate a lorebook with entries
  link persona_id [book_count]         Link persona to lore books
  help                                 Show this help message

Example:
  ./llama-lore-creator.sh llama3 entry "The Crystal Forest" "place"
  ./llama-lore-creator.sh mistral persona "Elara" "An elven sorceress"
  ./llama-lore-creator.sh llama3 lorebook "Eldoria" "A magical realm" 5
 skogix@skogix-workstation  ~/skogai/tools   master  ./manage-lore.sh --help
SkogAI Lore Management Tool

Usage: ./manage-lore.sh [command] [options]

Commands:
  create-entry     Create a new lore entry
  create-book      Create a new lore book
  list-entries     List all lore entries
  list-books       List all lore books
  show-entry ID    Display a specific lore entry
  show-book ID     Display a specific lore book
  add-to-book      Add an entry to a book
  link-to-persona  Associate a lore book with a persona
  search           Search lore entries by keyword
  help             Show this help message

For more information, see the documentation in knowledge/core/lore/
