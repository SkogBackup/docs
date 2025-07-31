---
title: List
type: project_doc
permalink: Parttrap/docs/List
created: '2025-07-10T09:20:48.570418+00:00'
modified: '2025-07-10T09:19:45.577376+00:00'
project_name: Parttrap
project_uuid: 0197f3a2-3da8-7118-a06d-b9978df9e253
doc_uuid: 70ad9807-b6b0-4cda-b9fa-9b5e454c5495
---

# Task List Format Documentation

## Standard Format
```
- [ ] full/path/from/project/root/filename.ext - action description
```

## Example
```
- [ ] Headless/PT.Headless.Content.WebApi/Controllers/AttributesController.cs - map GET /attributes/{slug} to GetBySlug action
```

## Components
- `- [ ]` - checkbox for task tracking
- Full file path from project root directory
- Hyphen separator ` - `
- Specific action to perform on that file

## Use Cases
- Implementation step lists
- Code review checklists
- Feature development tasks
- Bug fix action items