#!/bin/bash
# Setup script for SkogAI Documentation Frontmatter Automation
# This script sets up the environment, installs dependencies, and configures the service

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$(dirname "$SCRIPT_DIR")")"
VENV_PATH="$PROJECT_ROOT/.venv"
REQUIREMENTS="$SCRIPT_DIR/../requirements.txt"
SYSTEMD_SERVICE="$HOME/.config/systemd/user/docgen-watcher.service"
DEFAULT_MODEL="qwen3:4b"

echo -e "${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║   SkogAI Documentation Frontmatter Automation Setup        ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Function to print status
status() {
  echo -e "${GREEN}[✓]${NC} $1"
}

warn() {
  echo -e "${YELLOW}[!]${NC} $1"
}

error() {
  echo -e "${RED}[✗]${NC} $1"
}

info() {
  echo -e "${BLUE}[i]${NC} $1"
}

# Check Python version
check_python() {
  echo -e "\n${BLUE}Checking Python...${NC}"
  if command -v python3 &>/dev/null; then
    PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    if (($(echo "$PYTHON_VERSION >= 3.10" | bc -l))); then
      status "Python $PYTHON_VERSION found"
      return 0
    else
      error "Python 3.10+ required, found $PYTHON_VERSION"
      return 1
    fi
  else
    error "Python3 not found"
    return 1
  fi
}

# Check Ollama
check_ollama() {
  echo -e "\n${BLUE}Checking Ollama...${NC}"
  if command -v ollama &>/dev/null; then
    status "Ollama installed"

    # Check if Ollama is running
    if curl -s http://localhost:11434/api/tags &>/dev/null; then
      status "Ollama server is running"
    else
      warn "Ollama is installed but server is not running"
      info "Start it with: ollama serve"
      return 1
    fi
    return 0
  else
    error "Ollama not found"
    info "Install from: https://ollama.ai/download"
    return 1
  fi
}

# Setup Python virtual environment
setup_venv() {
  echo -e "\n${BLUE}Setting up Python virtual environment...${NC}"

  if [ -d "$VENV_PATH" ]; then
    status "Virtual environment exists at $VENV_PATH"
  else
    info "Creating virtual environment..."
    python3 -m venv "$VENV_PATH"
    status "Created virtual environment at $VENV_PATH"
  fi

  # Activate and install dependencies
  source "$VENV_PATH/bin/activate"

  info "Installing dependencies..."
  pip install --upgrade pip -q
  pip install -r "$REQUIREMENTS" -q
  status "Dependencies installed"
}

# Pull Ollama model
setup_model() {
  echo -e "\n${BLUE}Setting up Ollama model...${NC}"

  MODEL="${1:-$DEFAULT_MODEL}"

  # Check if model exists
  if ollama list | grep -q "$MODEL"; then
    status "Model '$MODEL' already available"
  else
    info "Pulling model '$MODEL'... (this may take a few minutes)"
    ollama pull "$MODEL"
    status "Model '$MODEL' pulled successfully"
  fi
}

# Configure systemd service
setup_service() {
  echo -e "\n${BLUE}Setting up systemd service...${NC}"

  # Ensure user systemd directory exists
  mkdir -p "$HOME/.config/systemd/user"

  # Check if service file exists
  if [ -f "$SYSTEMD_SERVICE" ]; then
    status "Service file exists at $SYSTEMD_SERVICE"
  else
    warn "Service file not found at $SYSTEMD_SERVICE"
    info "Copy the template from the project:"
    echo "  cp ~/.config/systemd/user/docgen-watcher.service.template $SYSTEMD_SERVICE"
    return 1
  fi

  # Update the ExecStart path in service file
  sed -i "s|ExecStart=.*|ExecStart=$VENV_PATH/bin/python $SCRIPT_DIR/frontmatter-daemon.py|g" "$SYSTEMD_SERVICE"
  sed -i "s|WorkingDirectory=.*|WorkingDirectory=$PROJECT_ROOT|g" "$SYSTEMD_SERVICE"

  # Reload systemd
  systemctl --user daemon-reload
  status "Systemd configuration reloaded"

  info "To enable and start the service:"
  echo "  systemctl --user enable docgen-watcher"
  echo "  systemctl --user start docgen-watcher"
}

# Test the setup
test_setup() {
  echo -e "\n${BLUE}Testing setup...${NC}"

  source "$VENV_PATH/bin/activate"

  # Test imports
  if python3 -c "from .docgen.scripts import models, llm, writer" 2>/dev/null; then
    status "Python modules import correctly"
  else
    warn "Module import test skipped (run from project root)"
  fi

  # Test Ollama connection
  if python3 -c "import ollama; print(ollama.list())" &>/dev/null; then
    status "Ollama Python client works"
  else
    error "Ollama Python client failed"
    return 1
  fi

  status "Setup tests passed"
}

# Print usage instructions
print_usage() {
  echo -e "\n${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
  echo -e "${BLUE}║                      Usage Instructions                     ║${NC}"
  echo -e "${BLUE}╚════════════════════════════════════════════════════════════╝${NC}"
  echo ""
  echo "Quick Start:"
  echo ""
  echo "  1. Run the daemon manually:"
  echo "     ${GREEN}$VENV_PATH/bin/python $SCRIPT_DIR/frontmatter-daemon.py${NC}"
  echo ""
  echo "  2. Or enable the systemd service:"
  echo "     ${GREEN}systemctl --user enable --now docgen-watcher${NC}"
  echo ""
  echo "  3. Check service status:"
  echo "     ${GREEN}systemctl --user status docgen-watcher${NC}"
  echo ""
  echo "  4. View logs:"
  echo "     ${GREEN}journalctl --user -u docgen-watcher -f${NC}"
  echo ""
  echo "Options:"
  echo "  --dirs \"./agents,./skogix\"   Watch specific directories"
  echo "  --model llama3.1:8b          Use a different model"
  echo "  --workers 4                   Use more concurrent workers"
  echo "  --scan-existing              Process existing files on startup"
  echo ""
  echo "Environment Variables:"
  echo "  DOCGEN_MODEL      Model to use (default: qwen3:4b)"
  echo "  DOCGEN_WORKERS    Number of workers (default: 2)"
  echo "  DOCGEN_DEBOUNCE   Debounce delay in seconds (default: 0.5)"
  echo "  DOCGEN_DIRS       Comma-separated directories to watch"
  echo ""
}

# Main
main() {
  cd "$PROJECT_ROOT"

  check_python || exit 1
  check_ollama || warn "Continue anyway? (y/n) " && read -r && [[ $REPLY =~ ^[Yy]$ ]]
  setup_venv
  setup_model "${1:-$DEFAULT_MODEL}"
  setup_service
  test_setup
  print_usage

  echo -e "\n${GREEN}Setup complete!${NC}"
}

# Run if executed directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  main "$@"
fi
