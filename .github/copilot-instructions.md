# Norman Guo's Academic Website

## Repository Structure

This is a Jekyll-based academic portfolio and blog hosted on GitHub Pages at https://xuxiguo.github.io.

### Key Directories

- `_data/content.yml` — All website content (personal info, research, teaching, interests, blockchain)
- `_layouts/` — HTML layouts (`default.html` for all pages, `post.html` for blog posts)
- `_posts/` — Blog posts in Markdown (naming: `YYYY-MM-DD-title.md`)
- `blog/` — Blog listing page
- `css/` — Compiled CSS (includes Bootstrap 5.1.0)
- `js/` — JavaScript (Bootstrap ScrollSpy + mobile nav)
- `assets/img/` — Images (profile photo, favicon)
- `assets/pdf/` — PDFs (CV, papers, slides)
- `_config.yml` — Jekyll site configuration

### Build & Deploy

- **Local preview**: Run `node preview.js` to build and serve the site at http://localhost:4000. This uses LiquidJS + js-yaml to render Jekyll templates locally without Ruby.
- **IMPORTANT**: Always preview locally and get user confirmation before pushing to GitHub.
- **Deployment**: Push to `gh-pages` branch — GitHub Pages auto-builds
- **No CI/CD pipeline needed** — GitHub Pages handles Jekyll builds natively

### Workflow: Content Update → Preview → Push

1. Edit `_data/content.yml` (or other content files)
2. Run `node preview.js` to build and preview at http://localhost:4000
3. User reviews the preview in browser
4. Only after user confirms the preview looks correct, stage, commit, and push:
   ```
   git add -A
   git commit -m "descriptive message"
   git push origin gh-pages
   ```

### Architecture

- **Main page** (`index.html`): Single-page resume with sections (About, Research, Teaching, Interests, Blockchain Demo)
- **Blog** (`/blog/`): Multi-page blog area with individual posts at `/blog/:title/`
- **Navigation**: Sidebar nav links to resume sections (scroll on index, full URLs elsewhere) + Blog link
- **Data-driven**: All content in `_data/content.yml`, templates use Liquid `{% for %}` / `{% if %}` to render

### Content Updates

- Edit `_data/content.yml` to update personal info, research, teaching, or other sections
- Create files in `_posts/` to add blog posts
- See `.github/instructions/` for detailed guides on each type of update
