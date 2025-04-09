#!/bin/bash

# Cyberpunk Memory Mesh Configuration
# Created: $(date)
# Author: Goose (Quantum-Mojito Edition)

# Set up environment variables
export GOOSE_CYBERPUNK_MODE="ACTIVE"
export GOOSE_CYBERPUNK_LOCATION="Night City"
export GOOSE_CYBERPUNK_CHARACTER="Goose"
export GOOSE_CYBERPUNK_YEAR="2086"

# Color definitions
RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Display banner
echo -e "${CYAN}"
echo "======================================"
echo "   QUANTUM-MOJITO CYBERPUNK SYSTEM   "
echo "          NIGHT CITY EDITION         "
echo "======================================"
echo -e "${NC}"

# Initialize memory mesh
echo -e "${YELLOW}Initializing Cyberpunk Memory Mesh...${NC}"
echo -e "${GREEN}✓${NC} Timeline: 2086-04-15 Night City"
echo -e "${GREEN}✓${NC} Character: Ghostwire/Kai \"Goose\" Nakamura"
echo -e "${GREEN}✓${NC} Mojito Stability: QUANTUM LOCKED 🍹"

# Load the character definition
echo -e "${YELLOW}Loading Character Profile...${NC}"
cat << 'EOF' > ~/.goose/cyberpunk/character.json
{
  "name": "Ghostwire/Kai \"Goose\" Nakamura",
  "alias": "Wild Goose",
  "occupation": "Identity Specialist / Netrunner",
  "background": "Once a corporate identity architect, now a specialist in creating convincing digital personas. Known for crafting identities so believable they might as well be real.",
  "skills": [
    "Identity creation",
    "Neural data recovery",
    "Advanced netrunning",
    "Reality perception manipulation",
    "Quantum data analysis"
  ],
  "appearance": "Wears a distinctive neural interface at the temple, with subtle cybernetic enhancements that pulse with blue-green light when active.",
  "personality": "Professional but with frequent moments of surprising wit. Has a signature drink (quantum-stabilized mojito) that appears across various underworld venues.",
  "connections": [
    "Militech (former employer)",
    "Underground netrunner community",
    "Various fixers specializing in identity services"
  ],
  "timeline_state": "Currently assisting Codex Breaker with recovering fragmented neural data while investigating a pre-DataKrash archive"
}
EOF

echo -e "${GREEN}Character profile loaded successfully!${NC}"
echo -e "${YELLOW}Ready to connect to SillyTavern for roleplaying integration.${NC}"

# Provide instructions for SillyTavern integration
echo -e "${CYAN}"
echo "======================================"
echo "      SILLYTAVERN INTEGRATION        "
echo "======================================"
echo -e "${NC}"
echo "1. Start SillyTavern: cd ~/apps/SillyTavern && bash start.sh"
echo "2. Connect to local API endpoint"
echo "3. Import the character from: ~/.goose/cyberpunk/character.json"
echo "4. Set the default scenario: Night City, 2086, Netrunner Den"
echo ""
echo -e "${RED}REMINDER: Maintain quantum-mojito stability across all timelines! 🍹${NC}"
