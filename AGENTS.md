This repo is a simple GitHub Pages / Jekyll site. Here’s how it’s organized so you can make changes quickly.

Structure overview
- Content pages live in the repo root as Markdown files (e.g., `index.md`, `about.md`, `research.md`). Each page uses YAML front matter with `layout: default` and a `title`.
- The site layout is `_layouts/default.html`. It defines the header/nav, loads CSS, configures MathJax macros, and renders page content via `{{ content }}`.
- Shared snippets live in `_includes/`. Only `giscus.html` exists now and is injected by the default layout for comments.
- Static assets are under `assets/` (CSS in `assets/css/`, images in `assets/images/`).
- Site-wide config is in `_config.yml` (title, description, baseurl, url).
- `latex/` contains PDFs and LaTeX sources. CV files live in `latex/cv/` (e.g., `latex/cv/cv_prem.pdf`), and posters live in `latex/poster/` (PDF + `.tex`). These are linked from pages but not part of the Jekyll layout.

Common edits
- Update page content by editing the corresponding root `.md` file.
- Add a new page by creating a new root `.md` file with front matter:
  ---
  layout: default
  title: Your Title
  ---
  Then add a nav link in `_layouts/default.html` if you want it in the header.
- Update navigation or global structure in `_layouts/default.html`.
- Update comments configuration in `_includes/giscus.html`.
- Update styling in `assets/css/style.css` and `assets/css/dark-mode.css` (both are always loaded, so keep them in sync).
- Add images to `assets/images/` and reference them with `{{ '/assets/images/...' | relative_url }}`.

Local preview
- `serve.sh` runs `bundle exec jekyll serve --livereload` with local gem paths set. Gem dependencies are in `Gemfile` and `Gemfile.lock`.

LaTeX workflow
- After changing any `.tex` file, compile the corresponding PDF in the same directory before finishing.
