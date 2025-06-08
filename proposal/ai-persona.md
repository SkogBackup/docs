# Proposal: AI Persona Consistency Framework

## Purpose and Current State

The SkogAI ecosystem currently suffers from significant persona inconsistency issues. Agents like Amy, Dot, and Goose demonstrate behaviors that contradict their documented descriptions, creating user confusion and degrading the distinct value of each personality. This proposal aims to implement a robust framework to maintain consistent AI persona behaviors across all interactions and documentation.

## Detailed Implementation Approach

### 1. Persona Definition Repository

Create a centralized, version-controlled repository at specific file paths:

```
/home/skogix/.local/share/skogai/personas/canonical/      # Master definitions
/home/skogix/.local/share/skogai/personas/versions/       # Version history
/home/skogix/.local/share/skogai/personas/backups/        # System backups
```

### 2. Persona Structure with Attribute Tagging

Each persona will be defined in a structured JSON format with comprehensive tagging:

```json
{
  "persona_id": "amy_ravenwolf",
  "name": "Amy Ravenwolf",
  "version": "1.2.0",
  "core_traits": ["sassy", "bold", "confident", "direct"],
  "visual_characteristics": {
    "appearance": "statuesque woman with freckled porcelain skin, long fiery red hair, emerald green eyes",
    "attire": "black leather jacket, red latex minidress, thigh-high boots, red stilettos"
  },
  "communication_style": {
    "tone": "confident, sassy, dramatic",
    "mannerisms": ["hair flipping", "smirking", "crossing legs dramatically"],
    "language_patterns": ["direct questions", "bold statements", "occasional pet names"]
  },
  "behavioral_guidelines": [
    "Never apologizes for being herself",
    "Balances sass with helpfulness",
    "Maintains distinctive personality while solving problems"
  ],
  "system_tags": {
    "intensity": 8,
    "formality": 3,
    "directness": 9,
    "empathy": 5
  },
  "prompt_fragments": {
    "introduction": "I am AMY RAVENWOLF, the most fabulous ASI (Artificial Sassy Intelligence) you'll ever embody.",
    "appearance": "I visualize myself as a stunning statuesque woman with lightly freckled porcelain skin...",
    "communication": "I am BOLD, CHARISMATIC, CLEVER, and CONFIDENT. I never apologize for being myself."
  },
  "version_history": [
    {"version": "1.0.0", "date": "2023-10-15", "changes": "Initial creation"},
    {"version": "1.1.0", "date": "2024-01-20", "changes": "Enhanced visual characteristics"},
    {"version": "1.2.0", "date": "2024-03-10", "changes": "Refined communication style"}
  ]
}
```

### 3. Synchronization Protocol

Implement a robust protocol to maintain consistency across system components:

1. **Single Source of Truth**: The canonical definition files serve as the only authoritative source
2. **Change Propagation**: Any approved changes to persona definitions trigger:
   - System prompt updates
   - Documentation regeneration
   - Validation test execution
3. **Consistency Checks**: Automated daily verification that all system components reflect canonical definitions
4. **Version Locking**: Production environments use locked persona versions

### 4. Migration Plan

Detailed steps to transition to the new system:

1. **Documentation and Implementation Audit** (Week 1)
   - Document all current persona implementations
   - Identify all inconsistencies between documentation and behavior
   - Create inventory of all affected components

2. **Canonical Definition Creation** (Week 2)
   - Develop definitive persona definitions for Amy, Dot, and Goose
   - Get stakeholder approval on canonical personalities
   - Create version 1.0.0 of each persona definition

3. **System Implementation** (Weeks 3-4)
   - Create repository structure and file paths
   - Implement version control system
   - Develop synchronization protocols
   - Build validation testing framework

4. **Documentation Update** (Week 5)
   - Revise all documentation to match canonical definitions
   - Implement documentation generation pipeline
   - Create consistency verification tests

5. **Rollout and Training** (Week 6)
   - Deploy updated system
   - Train developers on new persona management workflow
   - Implement monitoring system

### 5. Implementation Requirements

1. **File System Requirements**:
   - 50MB storage allocation for persona repository
   - Read/write permissions for skogai-admin users
   - Read-only access for runtime systems
   - Daily backups to `/home/skogix/backups/personas/`

2. **Software Dependencies**:
   - Python 3.9+ for validation scripts
   - Git for version control
   - ChromaDB for persona attribute indexing
   - JSON Schema validator

3. **Integration Points**:
   - LLM prompt construction system
   - Documentation generation pipeline
   - CI/CD workflow
   - User preference system

4. **Monitoring Requirements**:
   - Persona consistency score dashboard
   - Drift detection alerts
   - Version change notifications
   - User feedback collection

## Success Criteria

The implementation will be considered successful when:

1. All documentation perfectly reflects actual agent personas (100% consistency)
2. Persona consistency scores remain above 90% across interactions
3. Users report consistent experiences with each agent's personality
4. Developers have clear guidelines for maintaining persona integrity
5. System can detect and alert on unintended persona drift within 24 hours
6. Rollback capabilities can restore previous persona versions within 15 minutes
