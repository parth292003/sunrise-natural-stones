from build_pages import hero, prose, faq, links, cta, esc

DATE = "2026-10-04"
IMG = "/assets/images"


def figure(src, alt, caption):
    return (f'<figure class="pg-figure" style="margin:26px 0;"><img src="{src}" alt="{esc(alt)}" '
            f'width="1100" height="825" loading="lazy" /><figcaption>{esc(caption)}</figcaption></figure>')


def tbl(headers, rows):
    head = "".join(f"<th scope=\"col\">{h}</th>" for h in headers)
    body = "".join("<tr>" + "".join(
        (f"<th scope=\"row\">{c}</th>" if i == 0 else f"<td>{c}</td>") for i, c in enumerate(r)) + "</tr>"
        for r in rows)
    return f'<div class="pg-table-wrap"><table class="pg-table"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'


def byline():
    return f'By Sunrise Natural Stones, Udaipur. <time datetime="{DATE}">4 October 2026</time>'


# ───────────────────────── Bathtub guide ─────────────────────────
tub_faq = [
    ("Is a single-block marble bathtub really carved from one piece?",
     "Yes. The tub is hollowed out of one block of marble. There are no joints, adhesives or bonded "
     "sections, so the veining runs unbroken around the outside and through the basin."),
    ("How heavy is a solid marble bathtub?",
     "Marble weighs about 2.7 tonnes per cubic metre. A freestanding tub around 170 cm long often weighs "
     "between 0.8 and 1.5 tonnes empty, depending on the stone, the shape and the wall thickness. Filled "
     "with water and a bather, add roughly another 300 to 450 kg. We give the exact figure with the quotation."),
    ("Does a stone bathtub keep water warm?",
     "Yes. Thick stone has a lot of thermal mass. Once the stone has warmed up, it holds the water's heat "
     "longer than thin acrylic or steel."),
    ("How do you clean and maintain a marble bathtub?",
     "Use pH-neutral cleaners only and rinse after use. Re-seal the stone periodically as your "
     "installer advises. Acidic products, bath bombs with citric acid and abrasive pads will etch or dull marble."),
    ("Can you carve a tub to an architect's drawing?",
     "Yes. Send dimensioned drawings, and we will confirm what can be achieved from the blocks available "
     "in your chosen stone before you commit."),
]

tub_guide = {
    "file": "blog/single-block-marble-bathtubs.html",
    "path": "/blog/single-block-marble-bathtubs",
    "title": "Single-Block Marble Bathtubs: A Guide for Luxury Homes",
    "description": "How solid marble bathtubs are carved from one block, what they weigh, which stones to choose, floor loading, care and cost. A guide for designers.",
    "h1": "Single-block marble bathtubs: a guide for architects and designers",
    "crumbs": [("Journal", "/blog/"), ("Single-block marble bathtubs", "/blog/single-block-marble-bathtubs")],
    "og_image": "/assets/images/og/blog-marble-bathtubs.jpg",
    "og_source": "/assets/images/bespoke/bathtub-bespoke.webp",
    "faq": tub_faq,
    "article": {"date": DATE},
}
tub_guide["sections"] = [
    hero("Journal", tub_guide["h1"],
         "A solid stone bathtub is often the most expensive object in a bathroom, and the heaviest. Here is "
         "what to know before you specify one for a luxury residence, villa or hotel suite.",
         tub_guide["crumbs"], byline()),
    prose("", "", f"""
<p class="pg-lede">A single-block bathtub is hollowed out of one solid piece of marble. Nothing is glued or
assembled, so the veining wraps unbroken around the tub. That is why designers of ultra-luxury homes
specify them, and why they cost what they do.</p>

<h2>What "single block" means</h2>
<p>Many stone tubs on the market are built from slabs bonded at the corners, or cast from crushed stone and
resin. A single-block tub starts as one quarried block, larger than the finished tub on every side. The
outside is shaped first, then the basin is cut away until the walls reach their final thickness.</p>
<p>Because the tub is one piece, the block must be sound all the way through. A crack hidden in the middle
of a block can ruin weeks of work, so selection at the quarry matters more than anything that happens
in the workshop.</p>
{figure(f"{IMG}/bespoke/bathtub-bespoke.webp", "Freestanding white marble bathtub in a luxury bathroom",
        "A freestanding tub carved from one block of white marble.")}

<h2>Choosing the stone</h2>
{tbl(["Stone", "Character", "Good for"],
     [["White marble (Nirzerna, Panda White)", "Pale grounds, soft or bold veining", "Contemporary and minimal bathrooms"],
      ["Cream marble (Aagaria)", "Warm cream with grey-gold movement", "Classical interiors, hotels, spas"],
      ["Green marble (Verde Guatemala)", "Deep green with white veining; dense", "Statement bathrooms; among the most durable marbles in water"],
      ["Black granite", "Uniform black, very hard", "Maximum durability; dramatic modern spaces"]])}
<p>Denser stones tolerate daily water contact best. Very soft or heavily veined marbles look spectacular but
need more care, and veins can be lines of weakness in a thin wall. We advise on each block, not just the
variety.</p>

<h2>Size and weight</h2>
<p>Weight is the governing constraint. Marble weighs about 2.7 tonnes per cubic metre, so even a hollowed tub
is heavy. A freestanding tub around 170 cm long often weighs <strong>0.8 to 1.5 tonnes empty</strong>. Filled
with water and a bather, add another 300 to 450 kg.</p>
<ul class="pg-list">
  <li><strong>Floor loading:</strong> have a structural engineer confirm the floor can take the point load,
  especially on upper floors and in timber-framed houses.</li>
  <li><strong>Access route:</strong> check door widths, stairs, lifts and corners from the street to the
  bathroom. Many projects place the tub before walls or glazing are closed, or lift it in by crane.</li>
  <li><strong>Plumbing:</strong> fix the waste position and the type of overflow early. The drain is carved
  into the stone, so it cannot be moved later.</li>
</ul>

<h2>Shape, walls and finish</h2>
<p>Oval and rounded forms are the most common, because their curves spread stress evenly. Rectangular and
tapered forms are possible from suitable blocks. Wall thickness is a balance: thinner walls look refined and
weigh less; thicker walls are stronger and hold heat longer.</p>
<p>Finishes are usually honed inside, which is less slippery, and polished or honed outside. Some designers
choose a textured or hand-chiselled exterior to contrast with a smooth interior.</p>

<h2>Care and longevity</h2>
<p>Marble is calcium carbonate, so acids etch it. Use pH-neutral cleaners only, rinse after bathing and
re-seal the stone periodically. Avoid bath products containing citric acid. Looked after properly, a solid
stone tub lasts for generations, and minor wear can be honed out.</p>

<h2>What drives the price</h2>
<p>The finished tub may be less than half the volume of the block it came from. The rest becomes offcuts.
Price therefore depends on:</p>
<ul class="pg-list">
  <li>The size and rarity of a sound block in the chosen stone</li>
  <li>The complexity of the form and how thin the walls are</li>
  <li>Hours of carving and hand finishing</li>
  <li>Crating and freight for a single heavy piece</li>
</ul>

<h2>How we work with designers</h2>
<ol class="pg-list">
  <li>You send drawings or a reference and the project location.</li>
  <li>We propose suitable blocks and send photographs before anything is cut.</li>
  <li>The tub is carved and finished in Udaipur, with progress photos.</li>
  <li>It is crated in a braced, ISPM-15 timber crate and shipped to your port.</li>
</ol>
<p>See the tubs we make on our <a href="/stone-bathtubs">marble bathtubs page</a>, or our
<a href="/luxury-stone-sinks">carved basins</a> made from the same stones.</p>
"""),
    faq(tub_faq),
    cta("Working on a residence or hotel? Send us the drawings for a quotation on a single-block tub."),
]


# ───────────────────────── Import guide ─────────────────────────
import_faq = [
    ("What is the difference between FOB, CFR and CIF?",
     "Under FOB the seller loads the goods on the ship at the Indian port and the buyer pays ocean freight "
     "and insurance. Under CFR the seller also pays freight to your port. Under CIF the seller pays freight "
     "and minimum insurance. Under all three, risk passes to the buyer once the goods are on board in India."),
    ("Can I order less than a full container?",
     "Yes. Through your freight forwarder, smaller orders can travel as shared-container (LCL) cargo. "
     "It costs more per tonne, but works for single projects or special pieces such as bathtubs."),
    ("How do I check quality before the stone leaves India?",
     "Ask for photographs and video of the actual slabs or blocks, numbered against the packing list. "
     "You can also visit or appoint an inspection agent."),
]

import_guide = {
    "file": "blog/import-granite-marble-from-india.html",
    "path": "/blog/import-granite-marble-from-india",
    "title": "How to Import Granite and Marble from India: A Buyer's Guide",
    "description": "Step-by-step guide to importing granite and marble from India to the USA, UK, Europe, Australia and NZ: samples, Incoterms, inspection, documents, customs.",
    "h1": "How to import granite and marble from India",
    "crumbs": [("Journal", "/blog/"), ("Importing stone from India", "/blog/import-granite-marble-from-india")],
    "og_image": "/assets/images/og/blog-import-guide.jpg",
    "og_source": "/assets/images/capabilities/cap-block.webp",
    "faq": import_faq,
    "article": {"date": DATE},
}
import_guide["sections"] = [
    hero("Journal", import_guide["h1"],
         "A practical, step-by-step guide for importers, fabricators and builders buying Indian stone for "
         "the first time.", import_guide["crumbs"], byline()),
    prose("", "", f"""
<p class="pg-lede">India is one of the world's largest producers of granite and marble. Buying direct from an
Indian exporter can cut costs and widen your range. The process is simple once you know the steps.</p>

<h2>1. Define what you need</h2>
<p>Start with the stone, the format (blocks, full slabs or cut-to-size), the thickness, the finish, the
quantity and your destination port. The clearer the brief, the more accurate the quotation.</p>

<h2>2. Samples and photographs</h2>
<p>Ask for samples to check colour and finish. Natural stone varies, so for slabs and blocks ask for photos
and video of the actual material you will receive, numbered against the packing list.</p>

<h2>3. Agree the Incoterm</h2>
{tbl(["Term", "Seller pays", "Buyer pays"],
     [["FOB (Free on Board)", "Loading on the vessel at the Indian port", "Ocean freight, insurance, import clearance, delivery"],
      ["CFR (Cost and Freight)", "Loading plus ocean freight to your port", "Insurance, import clearance, delivery"],
      ["CIF (Cost, Insurance, Freight)", "Loading, freight and minimum insurance to your port", "Import clearance, delivery"]])}
<p>Under all three terms, risk passes to the buyer once the goods are on board in India. Many buyers take
CIF for their first order and switch to FOB once they have a forwarder they trust.</p>

<h2>4. Payment and production</h2>
<p>Common arrangements in the stone trade are an advance payment with the balance against a copy of the
bill of lading, or a letter of credit for larger orders. Lead time depends on the product: full slabs from
stock ship fastest, while cut-to-size work and carved pieces take longer.</p>

<h2>5. Inspection and packing</h2>
<p>Before packing, ask for a final set of photos covering thickness, finish, edges and any defects. Stone
should travel in ISPM-15 treated timber crates or A-frames, braced so nothing can shift in the container.</p>

<h2>6. Documents</h2>
<p>A standard export set is the commercial invoice, packing list, certificate of origin, fumigation
certificate and bill of lading. Your customs broker or forwarder uses these to clear the goods.</p>

<h2>7. Customs by market</h2>
{tbl(["Market", "What to know"],
     [["<a href='/usa'>USA</a>", "A customs broker files the entry; ISF (10+2) data must be filed before loading. Duty rates on Indian goods have changed since 2025, so confirm with your broker."],
      ["<a href='/uk'>United Kingdom</a>", "EORI number and customs declaration, usually through your forwarder."],
      ["<a href='/europe'>European Union</a>", "EORI number and import declaration; CE marking and a declaration of performance depending on the product's end use."],
      ["<a href='/australia'>Australia</a>", "ISPM-15 packaging and biosecurity inspection at the department's discretion. Engineered stone has been banned since 1 July 2024; natural stone is permitted."],
      ["<a href='/new-zealand'>New Zealand</a>", "MPI biosecurity rules for timber packaging and container cleanliness."]])}
<p class="pg-note">This guide is general information, not customs or legal advice. Rules change, so confirm
the current requirements with your broker before you ship.</p>

<h2>8. Receiving the shipment</h2>
<p>Unload carefully with suitable equipment. Check the bundles against the packing list, and photograph any
damage before signing for delivery.</p>
{figure(f"{IMG}/capabilities/cap-slab.webp", "Polished stone slabs on A-frames",
        "Slabs are packed on A-frames, numbered against the packing list.")}
<p>Ready to start? See our <a href="/granite-slabs">granite slabs</a>, <a href="/marble-slabs">marble
slabs</a> and <a href="/marble-blocks">marble blocks</a>, or send us an enquiry.</p>
"""),
    faq(import_faq),
    cta("Planning your first import from India? Tell us what you need and we will walk you through it."),
]


# ───────────────────────── Terms guide ─────────────────────────
terms_faq = [
    ("Is a countertop the same as a worktop or a benchtop?",
     "Yes. Countertop is the American term, worktop the British one, and benchtop is used in Australia and "
     "New Zealand. They all mean the kitchen work surface."),
    ("What thickness should a granite countertop be?",
     "In the US, 3 cm is standard for kitchens and 2 cm for vanities. In the UK, 20 mm and 30 mm are both "
     "common. In Australia and New Zealand, 20 mm with a mitred apron for a thicker edge is popular."),
]

terms_guide = {
    "file": "blog/countertops-worktops-benchtops.html",
    "path": "/blog/countertops-worktops-benchtops",
    "title": "Countertops, Worktops or Benchtops? Granite Specs by Country",
    "description": "Countertop, worktop and benchtop mean the same thing in the US, UK and Australia, but sizes differ. Granite and marble specifications compared by market.",
    "h1": "Countertops, worktops or benchtops? Stone specs by country",
    "crumbs": [("Journal", "/blog/"), ("Countertops, worktops, benchtops", "/blog/countertops-worktops-benchtops")],
    "og_image": "/assets/images/og/blog-countertops.jpg",
    "og_source": "/assets/images/bespoke/countertop-bespoke.webp",
    "faq": terms_faq,
    "article": {"date": DATE},
}
terms_guide["sections"] = [
    hero("Journal", terms_guide["h1"],
         "Three names for one product, with different standard sizes in each market. Here is what buyers in "
         "each country expect.", terms_guide["crumbs"], byline()),
    prose("", "", f"""
<p class="pg-lede">An American fabricator orders countertops, a London kitchen studio orders worktops and a
Sydney builder orders benchtops. It is the same slab of granite, cut to slightly different conventions.</p>

{tbl(["", "USA and Canada", "UK and Ireland", "Australia and NZ"],
     [["Name", "Countertop", "Worktop", "Benchtop"],
      ["Units", "Inches, square feet", "Millimetres, square metres", "Millimetres, square metres"],
      ["Common thickness", "3 cm kitchens, 2 cm vanities", "20 mm and 30 mm", "20 mm and 30 mm; 40 mm+ mitred aprons"],
      ["Typical depth", "25 to 26 inches", "600 to 650 mm", "600 to 650 mm"],
      ["Matching pieces", "Backsplash", "Upstands, splashbacks", "Splashbacks"],
      ["Market note", "Large prefab and slab trade", "Template-and-fit kitchen studios", "Natural stone demand up since the 2024 engineered stone ban"]])}

<h2>Which stone for which market?</h2>
<p>Black granite is popular everywhere. White and grey granites such as Alaska White sell strongly in the
US and Australia. In the UK, polished black and darker granites remain common, while honed and leathered
finishes are growing in all three markets.</p>
<p>Marble worktops are chosen for looks rather than toughness. They suit bathrooms, bars and kitchens where
the owner accepts a patina. Denser marbles such as Indian green hold up better than soft whites.</p>
{figure(f"{IMG}/bespoke/countertop-bespoke.webp", "Granite kitchen island countertop",
        "Granite island with a mitred waterfall end.")}

<h2>Ordering from India</h2>
<p>Whatever you call it, send us drawings or a cutting list in your own units and we will cut to them. See
<a href="/granite-countertops">granite countertops</a>, or the market pages for the
<a href="/usa">USA</a>, <a href="/uk">UK</a>, <a href="/australia">Australia</a> and
<a href="/new-zealand">New Zealand</a>.</p>
"""),
    faq(terms_faq),
    cta("Send your drawings in inches or millimetres and we will quote finished tops."),
]


# ───────────────────────── Journal index ─────────────────────────
POSTS = [tub_guide, import_guide, terms_guide]

posts_html = "".join(
    f'<a class="pg-post" href="{p["path"]}"><h2>{p["h1"]}</h2><p>{esc(p["description"])}</p>'
    f'<time datetime="{DATE}">4 October 2026</time></a>' for p in POSTS
)

journal_index = {
    "file": "blog/index.html",
    "path": "/blog/",
    "title": "Journal | Natural Stone Guides from Sunrise Natural Stones",
    "description": "Guides for architects, designers and importers: single-block marble bathtubs, importing stone from India, and countertop specifications by country.",
    "h1": "Journal",
    "crumbs": [("Journal", "/blog/")],
    "og_image": "/assets/images/og/blog.jpg",
    "og_source": "/assets/images/hero/hero-photo-3.webp",
    "faq": [],
    "schema": [{
        "@type": "Blog",
        "name": "Sunrise Natural Stones Journal",
        "url": "https://www.sunrisenaturalstones.com/blog/",
        "publisher": {"@id": "https://www.sunrisenaturalstones.com/#organization"},
        "blogPost": [{"@type": "BlogPosting", "headline": p["title"],
                      "url": "https://www.sunrisenaturalstones.com" + p["path"],
                      "datePublished": DATE} for p in POSTS],
    }],
}
journal_index["sections"] = [
    hero("Guides and notes", "Journal",
         "Practical guides on specifying, buying and importing natural stone, written by our team in Udaipur.",
         journal_index["crumbs"]),
    prose("", "", f'<div class="pg-posts">{posts_html}</div>'),
    cta("Have a question about stone that isn't answered here? Ask us directly."),
]

JOURNAL_PAGES = [journal_index] + POSTS
