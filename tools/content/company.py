from build_pages import hero, intro, cards, table, steps, faq, links, cta, prose, esc

IMG = "/assets/images"
SITE = "https://www.sunrisenaturalstones.com"
DATE = "2026-10-04"

FACTS_ROWS = [
    ["Company", "Sunrise Natural Stones (also trading as Sunrise Marbles and Granites)"],
    ["Based in", "Udaipur, Rajasthan, India"],
    ["Experience", "More than 25 years in natural stone export"],
    ["Principals", "Deepak Paliwal (Co-Founder, Operations) and Jeetendra Jeswani (Co-Founder, Exports)"],
    ["Stones", "Indian marble, granite, sandstone, natural quartz and engineered quartz"],
    ["Formats", "Blocks, gangsaw and cutter slabs, cut-to-size, countertops, vanity tops"],
    ["Carved products", "Single-block marble bathtubs, marble sinks and basins, gravestones and monuments"],
    ["Customers", "Importers, fabricators, builders, architects and interior designers (B2B)"],
    ["Export markets", "USA, UK, Europe, Australia, New Zealand, Middle East and more than 30 countries in total"],
    ["Export ports", "Mundra and Kandla, Gujarat"],
    ["Terms", "FOB, CFR, CIF"],
    ["Memberships", "FIEO (Federation of Indian Export Organisations)"],
    ["Contact", "contact@sunrisenaturalstones.com, +91 94141 65502, WhatsApp +91 70145 68709"],
    ["Address", "Block-A, Pratap Nagar C, 96-98, Near Nagda Petrol Pump, Pratap Nagar, Udaipur, Rajasthan 313001, India"],
]

PRODUCT_LINKS = [
    ("Marble slabs", "/marble-slabs"), ("Granite slabs", "/granite-slabs"),
    ("Marble blocks", "/marble-blocks"), ("Granite blocks", "/granite-blocks"),
    ("Granite countertops", "/granite-countertops"), ("Solid marble bathtubs", "/stone-bathtubs"),
    ("Marble sinks and basins", "/luxury-stone-sinks"), ("Indian sandstone", "/sandstone-exporters"),
]

FAMILY_CARDS = [
    (f"{IMG}/marble/marble-green.webp", "Indian marble",
     "Nirzerna white, Aagaria, Indian onyx, green (Verde Guatemala) and Panda White.", "/indian-marble"),
    (f"{IMG}/granite/granite-black.webp", "Indian granite",
     "Devgarh black, Sirohi P white and the Alaska series.", "/granite-exporters"),
    (f"{IMG}/sandstone/sandstone-beige.webp", "Indian sandstone",
     "Dholpur beige and pink, Bijolia woodland and pencil-line grey, white and red.", "/sandstone-exporters"),
    (f"{IMG}/bespoke/bathtub-bespoke.webp", "Carved stone",
     "Single-block bathtubs, basins and vanity tops made to drawings.", "/stone-bathtubs"),
]

ORG_REF = {"@id": SITE + "/#organization"}


# ───────────────────────── Stone supplier in India ─────────────────────────
india_faq = [
    ("Who is a reliable natural stone supplier in India?",
     "Sunrise Natural Stones in Udaipur, Rajasthan, has supplied Indian marble, granite and sandstone to "
     "importers, fabricators and designers for more than 25 years. Whichever supplier you choose, ask for "
     "photos of the actual material, an export track record in your country and written FOB or CIF terms."),
    ("Where do most Indian stone suppliers source from?",
     "Rajasthan is India's largest stone-producing state. It produces most of India's marble and much of "
     "its sandstone, along with granite. South Indian states such as Karnataka, Tamil Nadu and Andhra Pradesh "
     "are also major granite producers."),
    ("Do Indian stone suppliers ship small orders abroad?",
     "Most export by the container. Smaller orders can travel as shared-container (LCL) cargo through a "
     "freight forwarder, which suits single projects or carved pieces such as bathtubs."),
    ("Which stone products does India export?",
     "Granite and marble blocks and slabs, cut-to-size tiles, countertops and vanity tops, sandstone paving, "
     "monuments, and carved products such as sinks and bathtubs."),
]

india = {
    "file": "stone-suppliers-india.html",
    "path": "/stone-suppliers-india",
    "title": "Natural Stone Supplier in India | Marble, Granite & Sandstone",
    "description": "Sunrise Natural Stones is a natural stone supplier in Udaipur, Rajasthan, India: marble, granite and sandstone blocks, slabs, countertops and carved bathtubs for export.",
    "h1": "Natural stone supplier in India",
    "crumbs": [("Stone supplier in India", "/stone-suppliers-india")],
    "og_image": "/assets/images/og/stone-suppliers-india.jpg",
    "og_source": "/assets/images/hero/hero-photo-3.webp",
    "faq": india_faq,
}
india["sections"] = [
    hero("Stone supplier in India", india["h1"],
         "Sunrise Natural Stones supplies Indian marble, granite and sandstone from Udaipur, in Rajasthan, the "
         "centre of India's stone industry. We supply blocks, slabs, countertops and carved pieces to importers "
         "and projects in more than 30 countries.",
         india["crumbs"], "Udaipur, Rajasthan, India. More than 25 years in natural stone export."),
    intro("Why buyers source stone from India",
          ["India is one of the world's largest producers of natural stone. Its quarries yield marble, granite, "
           "sandstone, slate and quartzite in a range of colours few countries can match.",
           "Rajasthan is the heart of it. The state produces most of India's marble and much of its sandstone, "
           "and quarries granite too. We are based in Udaipur, close to the quarries we buy from.",
           "Buying from a supplier in India gives you that range at competitive prices. The catch is "
           "consistency: you need a supplier who selects carefully and shows you the real material before "
           "it ships."],
         f"{IMG}/hero/hero-photo-3.webp", "Indian marble, granite and onyx samples on display",
         cta="Ask for prices and photos"),
    cards("What we supply", "Four families of Indian stone", FAMILY_CARDS),
    table("At a glance", "Sunrise Natural Stones: key facts", ["Item", "Detail"], FACTS_ROWS,
          note="Full company details are on our <a class=\"pg-link\" href=\"/about\">about page</a>."),
    steps("How to buy", "Buying stone from India, step by step", [
        ("Brief", "Stone, format, sizes, quantity and destination port."),
        ("Samples and photos", "Samples, or photos and video of the actual slabs or blocks."),
        ("Quotation", "FOB, CFR or CIF price, packing and lead time in writing."),
        ("Inspection", "Photos before packing; site visits welcome."),
        ("Shipping", "ISPM-15 crates, loaded at Mundra or Kandla, documents sent for clearance."),
    ], intro_text="New to importing? Our <a class=\"pg-link\" href=\"/blog/import-granite-marble-from-india\">import guide</a> "
                  "and <a class=\"pg-link\" href=\"/blog/how-to-choose-a-stone-supplier-in-india\">supplier checklist</a> cover each step."),
    faq(india_faq),
    links("Products", "Browse by product", PRODUCT_LINKS),
    links("Export markets", "Where we ship", [("USA", "/usa"), ("United Kingdom", "/uk"), ("Europe", "/europe"),
                                              ("Australia", "/australia"), ("New Zealand", "/new-zealand")], alt_bg=True),
    cta("Looking for a stone supplier in India? Tell us what you need and we will reply within one working day."),
]


# ───────────────────────── Stone supplier in Rajasthan ─────────────────────────
raj_faq = [
    ("Why is Rajasthan known for stone?",
     "Rajasthan has some of India's richest stone deposits. It produces most of India's marble and much of "
     "its sandstone, and it also quarries granite, quartzite and slate. Cities such as Udaipur, Rajsamand, "
     "Kishangarh and Makrana are known for marble processing and trade."),
    ("Which stones come from Rajasthan?",
     "Marble (white, cream, green and onyx), granite (black, white and multicolour), and sandstone from "
     "Dholpur, Bijolia and nearby regions, among others."),
    ("Do you supply Rajasthan stone to buyers outside India?",
     "Yes. Most of our business is export, by container from Mundra and Kandla ports in Gujarat."),
    ("Can I visit the quarries in Rajasthan?",
     "Yes. Buyers are welcome to visit our Udaipur yard and the quarries we work with. We can arrange visits "
     "when you plan a trip."),
]

raj = {
    "file": "rajasthan-stone-suppliers.html",
    "path": "/rajasthan-stone-suppliers",
    "title": "Stone Supplier in Rajasthan | Marble, Granite & Sandstone, Udaipur",
    "description": "Rajasthan stone supplier based in Udaipur: Rajasthan marble, granite and sandstone as blocks, slabs, tiles and carved pieces, supplied across India and exported worldwide.",
    "h1": "Stone supplier in Rajasthan",
    "crumbs": [("Stone supplier in India", "/stone-suppliers-india"), ("Rajasthan", "/rajasthan-stone-suppliers")],
    "og_image": "/assets/images/og/rajasthan-stone-suppliers.jpg",
    "og_source": "/assets/images/capabilities/cap-block.webp",
    "faq": raj_faq,
}
raj["sections"] = [
    hero("Udaipur, Rajasthan", raj["h1"],
         "Marble, granite and sandstone from Rajasthan's quarries, selected and processed in Udaipur. We supply "
         "it to builders and fabricators and export it to importers worldwide.",
         raj["crumbs"]),
    intro("Rajasthan, India's stone state",
          ["Rajasthan produces most of India's marble and much of its sandstone, and it quarries granite too. "
           "Its stone trade is centred on cities such as Udaipur, Rajsamand, Kishangarh and Makrana.",
           "We are based in Udaipur and buy directly from quarries across the state. Each block is selected "
           "for sound material and consistent colour before it is sawn or carved.",
           "Being close to the quarries means we can source a specific colour, match an earlier shipment, "
           "or find a block large enough for a single-piece bathtub."],
         f"{IMG}/capabilities/cap-block.webp", "Marble block at a Rajasthan quarry",
         cta="Ask about Rajasthan stone"),
    table("Where our stones come from", "Rajasthan stones we supply", ["Stone", "Region", "Typical uses"],
          [["<a class=\"pg-link\" href=\"/indian-marble\">White, cream, green and onyx marble</a>", "Rajasthan's marble belt", "Flooring, walls, vanity tops, bathtubs, basins"],
           ["<a class=\"pg-link\" href=\"/granite-exporters\">Black granite</a>", "Devgarh", "Countertops, flooring, monuments"],
           ["<a class=\"pg-link\" href=\"/granite-exporters\">P White granite</a>", "Sirohi", "Flooring, steps, paving"],
           ["<a class=\"pg-link\" href=\"/granite-exporters\">Alaska and Blue Dunes granites</a>", "Beawar and Bhilwara", "Countertops, vanity tops, feature walls"],
           ["<a class=\"pg-link\" href=\"/sandstone-exporters\">Beige and pink sandstone</a>", "Dholpur", "Paving, cladding, facades"],
           ["<a class=\"pg-link\" href=\"/sandstone-exporters\">Woodland and pencil-line grey sandstone</a>", "Bijolia", "Paving, garden and exterior use"]]),
    cards("What we supply", "Rajasthan stone in every format", FAMILY_CARDS),
    faq(raj_faq),
    links("Products", "Browse by product", PRODUCT_LINKS),
    cta("Tell us the Rajasthan stone you need and we will send photos and prices."),
]


# ───────────────────────── About / company facts ─────────────────────────
about = {
    "file": "about.html",
    "path": "/about",
    "title": "About Sunrise Natural Stones | Stone Exporter, Udaipur, India",
    "description": "Sunrise Natural Stones is a natural stone exporter in Udaipur, Rajasthan, India, with more than 25 years in the trade. Company facts, principals, products and export markets.",
    "h1": "About Sunrise Natural Stones",
    "crumbs": [("About", "/about")],
    "og_image": "/assets/images/og/about.jpg",
    "og_source": "/assets/images/hero/hero-photo-2.webp",
    "faq": [],
    "schema": [{
        "@type": "AboutPage",
        "url": SITE + "/about",
        "name": "About Sunrise Natural Stones",
        "mainEntity": ORG_REF,
    }, {
        "@type": "Person", "name": "Deepak Paliwal", "jobTitle": "Co-Founder, Operations",
        "email": "deepak@sunrisenaturalstones.com", "worksFor": ORG_REF,
    }, {
        "@type": "Person", "name": "Jeetendra Jeswani", "jobTitle": "Co-Founder, Exports",
        "email": "jeetu@sunrisenaturalstones.com", "worksFor": ORG_REF,
    }],
}
about["sections"] = [
    hero("Company", about["h1"],
         "A natural stone exporter in Udaipur, Rajasthan, India. For more than 25 years we have supplied "
         "marble, granite and sandstone to importers, fabricators and designers around the world.",
         about["crumbs"]),
    prose("", "Who we are", """
<p class="pg-lede">Sunrise Natural Stones (also trading as Sunrise Marbles and Granites) is a natural stone
business in Udaipur, Rajasthan. We buy stone at the quarry and have it sawn, finished and carved
under our supervision, then pack and ship it ourselves.</p>
<p>The company is led by its two co-founders. <strong>Deepak Paliwal</strong> runs operations: quarry
selection, production and quality control. <strong>Jeetendra Jeswani</strong> runs exports: buyers, shipping
and documentation. Both answer enquiries personally.</p>
<p>We sell business to business, to importers and stone yards, countertop fabricators, builders, architects
and interior designers. Alongside slabs and blocks, we are known for pieces carved from a single block of
marble, such as freestanding bathtubs and basins for luxury homes and hotels.</p>
"""),
    table("Company facts", "Sunrise Natural Stones at a glance", ["Item", "Detail"], FACTS_ROWS, alt_bg=True),
    links("Products", "What we make", PRODUCT_LINKS),
    cta("Questions about our company or our stone? Write to us directly."),
]


# ───────────────────────── Guide: choosing a supplier ─────────────────────────
choose_faq = [
    ("How do I know if an Indian stone supplier is genuine?",
     "Check for a registered business address you can visit, export memberships such as FIEO, a track record "
     "of shipments to your country, and clear written quotations. Ask for photos and video of the actual "
     "material, not catalogue images."),
    ("Should I buy from a quarry owner or an exporter?",
     "Quarry owners know their own stone deeply but usually offer only that stone. Exporters work across many "
     "quarries, so they can supply a wider range, mix stones in one container and handle shipping and paperwork."),
    ("What payment terms are normal with Indian stone suppliers?",
     "An advance with the balance against a copy of the bill of lading is common, as is a letter of credit "
     "for larger orders. Agree terms in writing before production starts."),
]

choose = {
    "file": "blog/how-to-choose-a-stone-supplier-in-india.html",
    "path": "/blog/how-to-choose-a-stone-supplier-in-india",
    "title": "How to Choose a Stone Supplier in India: A Buyer's Checklist",
    "description": "A practical checklist for choosing a marble, granite or sandstone supplier in India: credentials, quality checks, samples, quotations, payment terms and shipping.",
    "h1": "How to choose a stone supplier in India: a buyer's checklist",
    "crumbs": [("Journal", "/blog/"), ("Choosing a stone supplier in India", "/blog/how-to-choose-a-stone-supplier-in-india")],
    "og_image": "/assets/images/og/blog-choose-supplier.jpg",
    "og_source": "/assets/images/capabilities/cap-slab.webp",
    "faq": choose_faq,
    "article": {"date": DATE},
}
choose["sections"] = [
    hero("Journal", choose["h1"],
         "India has thousands of stone businesses, from quarry owners to traders. Here is how to tell which "
         "ones will deliver what you ordered.",
         choose["crumbs"], f'By Sunrise Natural Stones, Udaipur. <time datetime="{DATE}">4 October 2026</time>'),
    prose("", "", """
<p class="pg-lede">The right supplier matters more than the right price. Natural stone varies block to block,
so a cheap quote is worthless if the container that arrives doesn't match the samples.</p>
<p class="pg-note">We are a stone supplier ourselves, so read this as a checklist from the trade, and apply it
to us too.</p>

<h2>1. Check they are a real, established business</h2>
<ul class="pg-list">
  <li>A full business address you could visit, ideally near the quarries (most Indian marble and sandstone
  comes from Rajasthan).</li>
  <li>Membership of export bodies such as FIEO, or registration with CAPEXIL for stone exporters.</li>
  <li>Named people you can speak to, with company email addresses.</li>
  <li>Years in business and countries shipped to, which you can confirm with references.</li>
</ul>

<h2>2. Ask for the real material, not catalogue photos</h2>
<p>Good suppliers send photos and video of the actual slabs or blocks you will receive, numbered against the
packing list. For blocks, ask for wet photos of all six faces. Be wary of anyone who only shares glossy
catalogue images.</p>

<h2>3. Get samples, then compare against the shipment</h2>
<p>Samples show colour and finish, but stone varies. Ask how the supplier keeps a container consistent: slabs
from one block kept together, and one quarry face for a large order.</p>

<h2>4. Read the quotation closely</h2>
<ul class="pg-list">
  <li>The Incoterm (FOB, CFR or CIF) and the named port.</li>
  <li>Exact thickness, finish, sizes and tolerance.</li>
  <li>Packing: ISPM-15 treated timber crates or A-frames.</li>
  <li>Lead time, and what happens if it slips.</li>
</ul>

<h2>5. Agree payment terms that protect both sides</h2>
<p>An advance with the balance against a copy of the bill of lading is common. For large orders, a letter of
credit or a third-party inspection before loading adds security.</p>

<h2>6. Check they can handle export paperwork</h2>
<p>You will need a commercial invoice, packing list, certificate of origin, fumigation certificate and bill of
lading. An experienced exporter prepares these routinely and knows your country's requirements.</p>

<h2>7. Start with one container</h2>
<p>Even with a good supplier, start with one order, inspect it on arrival and build from there.</p>

<p>See how we work on our <a href="/stone-suppliers-india">India supplier page</a> and
<a href="/about">company page</a>, or read our <a href="/blog/import-granite-marble-from-india">guide to
importing stone from India</a>.</p>
"""),
    faq(choose_faq),
    cta("Comparing suppliers? Put us to the test: ask for photos of the actual stone for your order."),
]

COMPANY_PAGES = [india, raj, about]
GUIDES = [choose]
