"""Build the static content pages (products, export markets, journal).

The shared chrome (nav, mobile menu, advisor, contact, enquiry modal, footer)
is taken from stone-bathtubs.html so every generated page matches the rest of
the site. Page content lives in tools/content/*.py.

Usage:  python3 tools/build_pages.py
"""
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))

SITE = "https://www.sunrisenaturalstones.com"
TEMPLATE = os.path.join(ROOT, "stone-bathtubs.html")

ORGANIZATION = {
    "@type": "Organization",
    "@id": SITE + "/#organization",
    "name": "Sunrise Natural Stones",
    "alternateName": "Sunrise Marbles and Granites",
    "url": SITE + "/",
    "logo": SITE + "/logo.png",
    "email": "contact@sunrisenaturalstones.com",
    "telephone": "+91 94141 65502",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "Block-A, Pratap Nagar C, 96-98, Near Nagda Petrol Pump, Pratap Nagar",
        "addressLocality": "Udaipur",
        "addressRegion": "Rajasthan",
        "postalCode": "313001",
        "addressCountry": "IN",
    },
    "sameAs": ["https://www.instagram.com/sunrise_natural_stones"],
}


def esc(text):
    return html.escape(text, quote=True)


def _absolute_paths(fragment):
    fragment = fragment.replace('src="logo.png"', 'src="/logo.png"')
    fragment = re.sub(r'(src|href)="assets/', r'\1="/assets/', fragment)
    return fragment


def load_chrome():
    """Return (nav, tail) HTML taken from the template page."""
    src = open(TEMPLATE, encoding="utf-8").read()
    body_start = src.index("<body>") + len("<body>")
    hero_start = src.index('<section class="hero subpage-hero"')
    nav = src[body_start:hero_start]
    tail_start = src.index("<!-- ───── AI STONE ADVISOR ───── -->")
    tail = src[tail_start:]
    # Generated pages carry no testimonial block.
    tail = re.sub(r"(?s)<!-- ───── REVIEWS ───── -->.*?</section>\s*", "", tail)
    return _absolute_paths(nav), _absolute_paths(tail)


# ───────────────────────── section helpers ─────────────────────────

def hero(eyebrow, h1, tagline, crumbs, meta=""):
    trail = ['<a href="/">Home</a>']
    for label, href in crumbs[:-1]:
        trail.append(f'<a href="{href}">{esc(label)}</a>')
    trail.append(f'<span aria-current="page">{esc(crumbs[-1][0])}</span>')
    sep = ' <span aria-hidden="true">/</span> '
    meta_html = f'<p class="pg-hero__meta">{meta}</p>' if meta else ""
    return f"""<section class="pg-hero" id="top">
  <div class="pg-hero__inner">
    <nav class="pg-crumbs" aria-label="Breadcrumb">{sep.join(trail)}</nav>
    <span class="pg-eyebrow">{esc(eyebrow)}</span>
    <h1>{h1}</h1>
    <p>{tagline}</p>
    {meta_html}
  </div>
</section>
"""


def intro(h2, paras, img, alt, caption="", cta="Request a quote", alt_bg=False):
    body = "\n".join(
        f'<p class="pg-lede">{p}</p>' if i == 0 else f"<p>{p}</p>" for i, p in enumerate(paras)
    )
    cap = f"<figcaption>{esc(caption)}</figcaption>" if caption else ""
    cls = "pg-section pg-section--alt" if alt_bg else "pg-section"
    return f"""<section class="{cls}">
  <div class="pg-wrap pg-two">
    <div>
      <h2>{h2}</h2>
      {body}
      <p style="margin-top:26px;"><button class="pg-btn" data-open-modal>{esc(cta)} <span class="arr">&rarr;</span></button></p>
    </div>
    <figure class="pg-figure"><img src="{img}" alt="{esc(alt)}" width="1100" height="825" />{cap}</figure>
  </div>
</section>
"""


def cards(eyebrow, h2, items, intro_text="", alt_bg=True):
    """items: (img, name, desc, product_for_enquiry or link href starting with /)"""
    out = []
    for img, name, desc, target in items:
        if target.startswith("/"):
            out.append(f"""<a class="pg-card" href="{target}">
        <img loading="lazy" src="{img}" alt="{esc(name)}" width="600" height="400" />
        <div class="pg-card__body"><h3>{esc(name)}</h3><p>{desc}</p><span class="swatch__cta">View &rarr;</span></div>
      </a>""")
        else:
            out.append(f"""<article class="pg-card">
        <img loading="lazy" src="{img}" alt="{esc(name)}" width="600" height="400" />
        <div class="pg-card__body"><h3>{esc(name)}</h3><p>{desc}</p>
          <button class="swatch__cta" data-open-modal data-product="{esc(target)}">Enquire <span class="arr">&rarr;</span></button></div>
      </article>""")
    cls = "pg-section pg-section--alt" if alt_bg else "pg-section"
    lead = f"<p style=\"max-width:66ch;margin-bottom:22px;\">{intro_text}</p>" if intro_text else ""
    return f"""<section class="{cls}">
  <div class="pg-wrap">
    <span class="pg-eyebrow">{esc(eyebrow)}</span>
    <h2>{h2}</h2>
    {lead}
    <div class="pg-cards">
      {''.join(out)}
    </div>
  </div>
</section>
"""


def table(eyebrow, h2, headers, rows, intro_text="", note="", alt_bg=False):
    head = "".join(f"<th scope=\"col\">{h}</th>" for h in headers)
    body = "".join(
        "<tr>" + "".join(
            (f"<th scope=\"row\">{c}</th>" if i == 0 else f"<td>{c}</td>") for i, c in enumerate(r)
        ) + "</tr>"
        for r in rows
    )
    cls = "pg-section pg-section--alt" if alt_bg else "pg-section"
    lead = f"<p style=\"max-width:66ch;margin-bottom:18px;\">{intro_text}</p>" if intro_text else ""
    foot = f'<p class="pg-note">{note}</p>' if note else ""
    return f"""<section class="{cls}">
  <div class="pg-wrap">
    <span class="pg-eyebrow">{esc(eyebrow)}</span>
    <h2>{h2}</h2>
    {lead}
    <div class="pg-table-wrap"><table class="pg-table"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>
    {foot}
  </div>
</section>
"""


def steps(eyebrow, h2, items, intro_text="", alt_bg=False):
    lis = "".join(f"<li><strong>{t}</strong>{d}</li>" for t, d in items)
    cls = "pg-section pg-section--alt" if alt_bg else "pg-section"
    lead = f"<p style=\"max-width:66ch;margin-bottom:22px;\">{intro_text}</p>" if intro_text else ""
    return f"""<section class="{cls}">
  <div class="pg-wrap">
    <span class="pg-eyebrow">{esc(eyebrow)}</span>
    <h2>{h2}</h2>
    {lead}
    <ol class="pg-steps">{lis}</ol>
  </div>
</section>
"""


def prose(eyebrow, h2, inner_html, alt_bg=False):
    cls = "pg-section pg-section--alt" if alt_bg else "pg-section"
    eb = f'<span class="pg-eyebrow">{esc(eyebrow)}</span>' if eyebrow else ""
    h = f"<h2>{h2}</h2>" if h2 else ""
    return f"""<section class="{cls}">
  <div class="pg-wrap pg-narrow pg-prose">
    {eb}
    {h}
    {inner_html}
  </div>
</section>
"""


def faq(items, alt_bg=True):
    det = "".join(
        f"<details><summary>{esc(q)}</summary><p>{a}</p></details>" for q, a in items
    )
    cls = "pg-section pg-section--alt" if alt_bg else "pg-section"
    return f"""<section class="{cls}">
  <div class="pg-wrap pg-narrow pg-faq">
    <span class="pg-eyebrow">Questions buyers ask</span>
    <h2>Frequently asked questions</h2>
    {det}
  </div>
</section>
"""


def links(eyebrow, h2, items, alt_bg=False):
    a = "".join(f'<a href="{href}">{esc(label)} <span>&rarr;</span></a>' for label, href in items)
    cls = "pg-section pg-section--alt" if alt_bg else "pg-section"
    return f"""<section class="{cls}">
  <div class="pg-wrap">
    <span class="pg-eyebrow">{esc(eyebrow)}</span>
    <h2>{h2}</h2>
    <div class="pg-links">{a}</div>
  </div>
</section>
"""


def cta(text, button="Start an enquiry"):
    return f"""<section class="pg-section">
  <div class="pg-wrap pg-cta">
    <p>{text}</p>
    <div style="display:flex;gap:12px;flex-wrap:wrap;">
      <button class="pg-btn" data-open-modal>{esc(button)} <span class="arr">&rarr;</span></button>
      <a class="pg-btn pg-btn--ghost" href="https://wa.me/917014568709" target="_blank" rel="noopener">WhatsApp us</a>
    </div>
  </div>
</section>
"""


# ───────────────────────── page assembly ─────────────────────────

def _strip_tags(s):
    return re.sub(r"<[^>]+>", "", html.unescape(s))


def schema_graph(page):
    url = SITE + page["path"]
    crumbs = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}]
    for i, (label, href) in enumerate(page["crumbs"], start=2):
        crumbs.append({"@type": "ListItem", "position": i, "name": label, "item": SITE + href})
    graph = [ORGANIZATION, {"@type": "BreadcrumbList", "itemListElement": crumbs}]
    if page.get("faq"):
        graph.append({
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": _strip_tags(a)}}
                for q, a in page["faq"]
            ],
        })
    if page.get("article"):
        art = page["article"]
        graph.append({
            "@type": "Article",
            "headline": _strip_tags(page["h1"]),
            "description": page["description"],
            "image": SITE + page["og_image"],
            "datePublished": art["date"],
            "dateModified": art.get("modified", art["date"]),
            "author": {"@id": SITE + "/#organization"},
            "publisher": {"@id": SITE + "/#organization"},
            "mainEntityOfPage": url,
        })
    for extra in page.get("schema", []):
        graph.append(extra)
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2, ensure_ascii=False)


def render(page, nav, tail):
    url = SITE + page["path"]
    og = SITE + page["og_image"]
    title, desc = esc(page["title"]), esc(page["description"])
    head = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=5" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<meta name="robots" content="index, follow, max-image-preview:large" />
<link rel="canonical" href="{url}" />
<link rel="icon" type="image/png" href="/logo.png" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet" />
<meta property="og:type" content="{'article' if page.get('article') else 'website'}" />
<meta property="og:site_name" content="Sunrise Natural Stones" />
<meta property="og:url" content="{url}" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:image" content="{og}" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{title}" />
<meta name="twitter:description" content="{desc}" />
<meta name="twitter:image" content="{og}" />
<script type="application/ld+json">
{schema_graph(page)}
</script>
<link rel="stylesheet" href="/assets/css/style.css" />
</head>
<body>
"""
    return head + nav + "".join(page["sections"]) + tail


def build_og(page):
    """Create the 1200x630 share image for a page from its source image."""
    src = os.path.join(ROOT, page["og_source"].lstrip("/"))
    dst = os.path.join(ROOT, page["og_image"].lstrip("/"))
    if not os.path.exists(dst):
        os.system(f'convert "{src}" -resize 1200x630^ -gravity center -extent 1200x630 -quality 78 -strip "{dst}"')


def main():
    from content import ALL_PAGES  # noqa: E402

    nav, tail = load_chrome()
    for page in ALL_PAGES:
        build_og(page)
        out = os.path.join(ROOT, page["file"])
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(render(page, nav, tail))
        print("wrote", page["file"])


if __name__ == "__main__":
    main()
