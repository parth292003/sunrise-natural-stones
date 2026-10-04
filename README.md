# Sunrise Natural Stones — Official Website

Premium Indian natural stone exporter website showcasing marble, sandstone, granite, quartz, and engineered quartz.

🌐 **Live Site**: [sunrisenaturalstones.com](https://sunrisenaturalstones.com)

---

## 🗂️ Project Structure

```
├── index.html                  # Homepage
├── *.html                      # Product, collection and export-market pages (clean URLs, e.g. /marble-slabs)
├── blog/                       # Journal: index + guides
├── assets/
│   ├── css/style.css           # All styles
│   ├── js/main.js              # Shared script: nav, enquiry form, advisor, translations
│   ├── video/hero.mp4          # Hero video (720p, ~1.4 MB)
│   └── images/                 # WebP images; og/ holds 1200x630 social share images
├── tools/
│   ├── build_pages.py          # Generates the product, market and journal pages
│   └── content/                # Copy for those pages (products.py, markets.py, journal.py)
├── sitemap.xml, robots.txt     # Search engine files
└── llms.txt                    # Plain-text business summary for AI assistants
```

## ✏️ Editing generated pages

The marble/granite slab and block pages, the market pages (/usa, /uk, /europe, /australia,
/new-zealand) and everything under /blog are generated. Edit the copy in `tools/content/`, then run:

```
python3 tools/build_pages.py
```

The script takes the nav, contact section, enquiry modal and footer from `stone-bathtubs.html`,
so change those there and re-run it. Add any new page to `sitemap.xml` and `llms.txt`.

## 📨 Enquiry form

The enquiry form posts to [FormSubmit](https://formsubmit.co) and is delivered to
contact@sunrisenaturalstones.com. The first submission sends an activation email to that address,
which must be confirmed once. If the service is unreachable, the form falls back to opening the
visitor's email app.

## 🚀 Deployment (GitHub Pages)

1. Push this repository to GitHub
2. Go to **Settings → Pages**
3. Under **Source**, select `main` branch and `/ (root)` folder
4. Click **Save**
5. Your site will be live at `https://<username>.github.io/<repo-name>/`

## ⚡ Tech Stack

- **Pure HTML, CSS, JavaScript**, no frameworks; a small Python script generates some pages
- Fully static — works with any static hosting provider
- Responsive design with mobile-first approach
- Client-side translation (EN, HI, AR, DE, FR, IT, ES and more)

---

© 2026 Sunrise Natural Stones. All rights reserved.
