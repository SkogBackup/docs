---
title: Data Folder Cleanup Plan
type: note
permalink: tasks/data-folder-cleanup-plan
---

# Data Folder Cleanup Plan

## Summary

This document outlines the systematic approach for processing and migrating content from the temporary `/data` folder to appropriate locations within the structured SkogAI system. The goal is to preserve valuable information while eliminating redundancy and improving organization.

## Current Status

The `/data` folder contains approximately 85 files covering various aspects of the SkogAI system, including:

- Duplicated documentation from the root directory
- Journal entries from March and June 2025
- Knowledge base documents on various topics
- Project-specific information
- People profiles and documentation
- Task definitions and templates
- Temporary files and archived correspondence

## Content Migration Strategy

### Core Documentation

1. **System Architecture and Structure**
   - Key information from ARCHITECTURE.md, ABOUT.md, README.md consolidated
   - Created structured note in system/SkogAI System Architecture
   - Created structured note in system/SkogAI Workspace Structure

2. **Historical Events**
   - CHAOS RED ALARM incident documentation created
   - March and June 2025 journal entries consolidated
   - Event timeline and analysis preserved

3. **Conceptual Framework**
   - Quantum-Mojito Theory documented
   - Agent Family structure preserved
   - Tool evolution and relationships clarified

### Remaining Content Categories

For the remaining content, we will apply the following approach:

1. **Journal Entries**
   - Consolidate by month and theme
   - Preserve in history/ folder with appropriate metadata
   - Extract key insights for inclusion in relevant concepts

2. **Knowledge Content**
   - Categorize by domain (git workflow, integration, etc.)
   - Create structured notes in knowledge/ folder
   - Cross-reference related concepts

3. **Project Documentation**
   - Organize by project name
   - Create structured notes in projects/ folder
   - Preserve implementation details and requirements

4. **People Profiles**
   - Consolidate information about key individuals
   - Create profiles in appropriate format
   - Store in agents/ folder for AI agents, people/ for human collaborators

5. **Task Documentation**
   - Review against current task files
   - Update task files with relevant information
   - Archive completed task documentation appropriately

6. **Templates and Standards**
   - Extract and organize templates
   - Document standards in appropriate location
   - Create reference materials for consistent application

7. **Correspondence and Archives**
   - Review for historical context
   - Extract relevant information
   - Archive or delete as appropriate

## Implementation Approach

1. **Batch Processing**: Process files in batches by category
2. **Content Extraction**: Focus on preserving valuable unique information
3. **De-duplication**: Eliminate redundant content across files
4. **Structural Improvement**: Organize information more logically
5. **Cross-referencing**: Create links between related information

## Success Criteria

The cleanup will be considered successful when:

1. All valuable information has been preserved in structured format
2. The /data folder has been emptied
3. Information is logically organized and easily accessible
4. Redundancy has been eliminated
5. Cross-references connect related information

## Progress Tracking

As files are processed, this document will be updated to track progress. Files will be removed from the /data folder once their content has been appropriately migrated or determined to be redundant.