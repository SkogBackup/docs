# SkogAI Memory Validation Checklist

Use this checklist to verify that memory entries meet all requirements and standards for the SkogAI Memory system.

## Basic Structure

- [ ] **Filename follows standards**
  - Uses lowercase letters
  - Uses hyphens for word separation (kebab-case)
  - Avoids spaces, underscores, and special characters
  - Is concise but descriptive

- [ ] **Has required sections**
  - Title as first heading (# Title)
  - Summary section
  - Main content
  - Observations section
  - Relations section

- [ ] **Frontmatter (if used)**
  - Contains title that matches H1 heading
  - Contains type field
  - Contains permalink and/or tags if applicable

## Content Quality

- [ ] **Title is appropriate**
  - Clear and descriptive
  - Focuses on primary topic
  - Consistent with related documents
  - Usually 2-6 words in length

- [ ] **Summary is effective**
  - Provides quick understanding in 1-3 sentences
  - Highlights most important aspects
  - Includes key terminology for searchability

- [ ] **Main content is well-structured**
  - Uses appropriate heading levels (H2, H3, etc.)
  - Organizes information logically
  - Uses lists, tables, and formatting appropriately
  - Presents information clearly and concisely

## Observations Section

- [ ] **Contains 3-5+ observations**
  - Each observation is a single idea or fact
  - Observations cover different aspects of the topic
  - Observations represent different categories

- [ ] **Proper formatting**
  - Each observation starts with a category in brackets: [category]
  - Each observation includes at least one hashtag
  - Optional context is included in parentheses where helpful

- [ ] **Category diversity**
  - Uses appropriate categories for the content type
  - Includes a mix of different categories (facts, principles, techniques, etc.)
  - Categories accurately reflect the nature of each observation

- [ ] **Effective tagging**
  - Tags are relevant to the content
  - Tags use established terminology when possible
  - Tags will facilitate discovery of the content

## Relations Section

- [ ] **Contains 2-3+ relations**
  - Relations are to relevant documents
  - Relations use specific types rather than generic ones
  - Relations include context descriptions where helpful

- [ ] **Proper formatting**
  - Each relation starts with a relation type
  - Target documents are in double brackets: [[document-name]]
  - Optional context is included in parentheses where helpful

- [ ] **Relation types**
  - Uses specific relation types appropriate to the connection
  - Avoids overuse of generic "relates_to" when more specific types apply
  - Relation types accurately reflect the nature of the connection

- [ ] **Knowledge graph connectivity**
  - Creates meaningful connections to existing documents
  - Establishes forward references for topics that should exist
  - Contributes to a cohesive knowledge network

## Overall Assessment

- [ ] **Semantic density**
  - Provides sufficient detail and connections
  - Contains enough observations to be valuable
  - Establishes enough relations to be discoverable

- [ ] **Formatting correctness**
  - Follows markdown syntax correctly
  - Adheres to SkogAI Memory formatting standards
  - Is consistent in formatting throughout

- [ ] **Content value**
  - Adds meaningful information to the knowledge base
  - Will be discoverable through searches and relations
  - Integrates well with existing content

## Validation Outcome

- [ ] **Fully compliant** - Meets all requirements without issues
- [ ] **Minor issues** - Has minor formatting or content issues that should be addressed
- [ ] **Major issues** - Has significant structural or content problems requiring substantial revision

## Notes on Improvements

_If there are issues or opportunities for enhancement, list specific recommendations here:_

- Improvement suggestion 1
- Improvement suggestion 2
- Improvement suggestion 3

## observations

- [fact] This checklist covers all mandatory elements of SkogAI Memory entries #validation #requirements
- [technique] Using this checklist helps ensure consistent quality across the knowledge base #quality-control
- [principle] Regular validation maintains system integrity and usefulness #maintenance
- [requirement] All memory entries must pass this validation to be considered complete #standards

## relations

- implements [[skogai-memory-rules]] (practical application of standards)
- part_of [[quality-assurance-process]] (component of ensuring system quality)
- supports [[memory-agent]] (provides evaluation criteria)
- relates_to [[content-creation-workflow]] (validation step in content process)