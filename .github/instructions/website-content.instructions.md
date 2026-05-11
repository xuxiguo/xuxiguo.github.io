---
applyTo: "_data/**"
---

# Website Content Update Guide

## File: `_data/content.yml`

This file contains ALL website content. Changes here are reflected on the site after Jekyll rebuild.

## Section Reference

### `personal`
- `firstName`, `lastName`, `displayName` — Name as displayed
- `title` — Academic title
- `institution`, `location` — Current position
- `email` — Contact email
- `profileImage` — Path to profile photo (in `assets/img/`)
- `cv` — Path to CV PDF (in `assets/pdf/`)

### `research.publications[]`
Each publication has:
- `title` — Paper title
- `authors[]` — Array of `{name, url}` objects (coauthors only, not the site owner)
- `year` — Publication year
- `journal` — Journal name
- `description` — Brief abstract

### `research.workingPapers[]`
Each working paper has:
- `title` — Paper title
- `authors[]` — Array of `{name, url}` objects (optional, omit for solo papers)
- `paperUrl` — Link to paper (SSRN URL or local PDF path like `assets/pdf/filename.pdf`)
- `status` — Current status string. Examples:
  - `"Under review"`
  - `"Forthcoming, Journal of Financial Stability"`
  - `"Revising for invited re-submission at Journal of Finance"`
- `description` — Brief abstract

**Do NOT include** `presentations` or `slideUrl` fields — these were intentionally removed.

### `teaching[]`
Each course has:
- `course` — Course name
- `institution` — University name
- `period` — Date range (e.g., `"2022 - Present"`)
- `description` — Optional course description
- `topics[]` — Optional list of course topics

### `navigation[]`
- `id` — Section HTML id (used for scroll navigation on the index page)
- `label` — Display text in sidebar

### `socialLinks[]`
- `platform` — Identifier (e.g., `"github"`, `"linkedin"`)
- `url` — Profile URL
- `icon` — Font Awesome class (e.g., `"fab fa-github"`)

## Common Operations

**Add a new publication**: Add an entry to `research.publications[]` with `title`, `authors`, `year`, `journal`, `description`.

**Promote working paper to publication**: Move the entry from `workingPapers[]` to `publications[]`, add `year` and `journal` fields, remove `status` and `paperUrl`.

**Update paper status**: Change the `status` field (e.g., from `"Under review"` to `"Forthcoming, Journal Name"`).

**Add a coauthor**: Add a `{name, url}` object to the paper's `authors[]` array.

**Add a new course**: Add an entry to `teaching[]` with `course`, `institution`, `period`, and optionally `description` and `topics[]`.
