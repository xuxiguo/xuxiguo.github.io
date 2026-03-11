---
applyTo: "_posts/**"
---

# Blog Post Creation Guide

## Creating a New Blog Post

### File Location & Naming

Create new posts in `_posts/` with the naming convention:

```
_posts/YYYY-MM-DD-title-with-dashes.md
```

Example: `_posts/2026-03-18-transformer-models-in-finance.md`

### Front Matter Template

Every post MUST start with YAML front matter:

```yaml
---
title: "Your Post Title Here"
date: YYYY-MM-DD
categories: [Category1, Category2]
---
```

### Recommended Categories

Use these categories to organize posts:

- **AI Thoughts** — Weekly AI commentary and insights
- **Research Updates** — Progress on academic papers
- **Finance** — Market analysis, investment insights
- **Teaching** — Course reflections, educational content
- **FinTech** — Technology in finance industry

### Content Guidelines

- Write in Markdown
- Use `##` for section headers within posts (h2)
- Keep paragraphs concise and readable
- Add images with: `![Alt text](/assets/img/blog/image-name.jpg)`
  - Store blog images in `assets/img/blog/`

### Example Post

```markdown
---
title: "How LLMs Are Reshaping Financial Analysis"
date: 2026-03-18
categories: [AI Thoughts, Finance]
---

Opening paragraph that hooks the reader...

## Main Point 1

Content...

## Main Point 2

Content...

## Conclusion

Closing thoughts...
```

### Build & Preview

- Local preview: `bundle exec jekyll serve` then visit `http://localhost:4000/blog/`
- Deploy: Push to `gh-pages` branch — GitHub Pages auto-builds
- New posts appear automatically on the blog listing page at `/blog/`
- Each post gets its own URL at `/blog/title-with-dashes/`
