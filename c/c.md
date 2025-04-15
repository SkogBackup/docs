● Proposal: Automated Context 
  Generation for New Contributors

  Summary

  This proposal suggests
  implementing an automated
  context generation system for
  new contributors to SkogAI
  repositories, providing
  essential project understanding
   with minimal manual effort.

  Background

  New contributors (both human
  and AI) face a steep learning
  curve when joining SkogAI
  projects. Currently, they must
  manually explore repositories
  to understand structure,
  standards, and workflows before
   making meaningful
  contributions.

  Proposed Solution

  Create an automated context
  generation script that provides
   essential project
  understanding for new
  contributors.

  Features

  1. Repository Overview
    - Directory structure
  visualization
    - Key file identification
    - Architecture diagram
  generation
  2. Standards Summary
    - Coding style highlights
    - Documentation requirements
    - Testing expectations
  3. Workflow Guide
    - Branch/PR process summary
    - CI/CD pipeline overview
    - Review expectations
  4. Contributor-Specific Context
    - Role-based information
  filtering
    - Complexity level adjustment
    - Relevant examples based on
  planned contribution area

  Implementation

  The tool would:
  1. Run as a standalone script:
  ./scripts/generate-contributor-
  context.sh [role] [focus-area]
  2. Generate a markdown file
  with project context tailored
  to the contributor
  3. Include links to detailed
  documentation for each section
  4. Provide practical examples
  relevant to the contributor's
  focus

  Benefits

  - Reduces onboarding time for
  new contributors
  - Ensures consistent
  understanding of project
  standards
  - Improves first contribution
  quality
  - Creates standardized
  knowledge baseline
  - Supports both human and AI
  contributors with appropriate
  context

  Next Steps

  1. Identify essential context
  components across SkogAI
  projects
  2. Create context template
  structure
  3. Develop context extraction
  logic
  4. Implement role-based
  filtering
  5. Test with new contributors
