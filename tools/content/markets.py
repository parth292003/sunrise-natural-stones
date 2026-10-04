from build_pages import hero, intro, cards, table, steps, faq, links, cta, prose

IMG = "/assets/images"

PRODUCT_CARDS = {
    "slabs": (f"{IMG}/capabilities/cap-slab.webp", "Marble and granite slabs",
              "Gangsaw slabs in 2 cm and 3 cm, polished, honed or leathered.", "/granite-slabs"),
    "marble": (f"{IMG}/marble/marble-nirzerna.webp", "Indian marble slabs",
               "Nirzerna, Aagaria, onyx, green and Panda White marble.", "/marble-slabs"),
    "blocks": (f"{IMG}/capabilities/cap-block.webp", "Marble and granite blocks",
               "Quarry blocks for processors, priced per cubic metre.", "/marble-blocks"),
    "counter": (f"{IMG}/bespoke/countertop-bespoke.webp", "Countertops",
                "Granite and marble tops cut to size with finished edges.", "/granite-countertops"),
    "tubs": (f"{IMG}/bespoke/bathtub-bespoke.webp", "Solid marble bathtubs",
             "Freestanding tubs carved from a single block of stone.", "/stone-bathtubs"),
    "sinks": (f"{IMG}/bespoke/sink-bespoke.webp", "Stone sinks and basins",
              "Vessel and undermount basins carved from one piece.", "/luxury-stone-sinks"),
    "vanity": (f"{IMG}/bespoke/vanity-bespoke.webp", "Vanity tops",
               "Marble and granite vanity tops with basin cut-outs.", "/stone-vanity-tops"),
}


def product_cards(keys, title_word):
    return cards("What we ship", f"Stone products for {title_word} buyers",
                 [PRODUCT_CARDS[k] for k in keys])


OTHER_MARKETS = [("USA", "/usa"), ("United Kingdom", "/uk"), ("Europe", "/europe"),
                 ("Australia", "/australia"), ("New Zealand", "/new-zealand")]


def other_markets(path):
    return links("Other markets", "We also ship to", [m for m in OTHER_MARKETS if m[1] != path])


GUIDE_LINKS = [
    ("How to import stone from India", "/blog/import-granite-marble-from-india"),
    ("Countertops, worktops or benchtops?", "/blog/countertops-worktops-benchtops"),
    ("Single-block marble bathtubs: a guide", "/blog/single-block-marble-bathtubs"),
]

PROCESS = [
    ("Enquiry", "Tell us the stone, format, sizes and quantity, plus your destination port."),
    ("Samples and photos", "We send samples, or photos and video of the actual slabs or blocks."),
    ("Quotation", "FOB, CFR or CIF price, packing details and lead time in writing."),
    ("Production and inspection", "Cutting and finishing to your specification, with photos before packing."),
    ("Shipping", "Fumigated crates, container loading at Mundra or Kandla, documents sent for clearance."),
]


# ───────────────────────── USA ─────────────────────────
usa_faq = [
    ("Do you ship granite and marble directly to the USA?",
     "Yes. We ship by container to US East and West Coast and Gulf ports, and quote FOB, CFR or CIF to "
     "the port you name. Your customs broker handles entry and the final delivery."),
    ("Do you make prefabricated granite countertops for the US market?",
     "Yes. We cut granite and marble countertops, island tops and vanity tops to US sizes in inches, "
     "with your choice of edge profile and sink cut-outs."),
    ("What about US import duties on stone from India?",
     "US duty rates on goods from India have changed several times since 2025. We quote FOB or CIF, "
     "and your customs broker confirms the duty that applies at the time of entry."),
    ("Do you sell to homeowners in the USA?",
     "We sell by the container to importers, distributors, fabricators, builders and designers. "
     "For a single piece, such as a marble bathtub for a residence, we ship through your designer, "
     "contractor or a freight forwarder."),
]

usa = {
    "file": "usa.html",
    "path": "/usa",
    "title": "Granite & Marble Supplier to the USA | Slabs & Countertops",
    "description": "Indian granite and marble for US importers and fabricators: 2 cm and 3 cm slabs, prefab countertops, vanity tops and solid marble bathtubs, shipped to US ports.",
    "h1": "Indian granite and marble for US importers and fabricators",
    "crumbs": [("Export markets", "/natural-stone-exporters"), ("USA", "/usa")],
    "og_image": "/assets/images/og/usa.jpg",
    "og_source": "/assets/images/bespoke/countertop-bespoke.webp",
    "faq": usa_faq,
}
usa["sections"] = [
    hero("Exporting to the United States", usa["h1"],
         "Slabs, prefabricated countertops, vanity tops, blocks and carved marble bathtubs, made in Udaipur "
         "to US sizes and shipped by container to the port you choose.",
         usa["crumbs"]),
    intro("Built for the way the US market buys stone",
          ["US fabricators work in inches and square feet, mostly in 3 cm granite. Importers want "
           "consistent colour from one container to the next. We plan production around both.",
           "We cut countertops and vanity tops to standard US dimensions or to your drawings. Full slabs "
           "go out in A-frame bundles, numbered against the packing list so your yard can check them in quickly.",
           "Interior designers and architects working on high-end residences also come to us for "
           "single-block marble bathtubs and carved basins, pieces that are hard to source in the US."],
         f"{IMG}/bespoke/countertop-bespoke.webp", "Granite kitchen countertop with waterfall edge",
         cta="Request a US quotation"),
    product_cards(["slabs", "counter", "vanity", "tubs", "sinks", "blocks"], "US"),
    table("US specifications", "Common US formats", ["Product", "Typical specification"],
          [["Granite slabs", "3 cm (1&#8540;\") for countertops; 2 cm (&frac34;\") for vanities and walls"],
           ["Prefab kitchen countertops", "Standard lengths such as 96\" and 108\", 26\" depth; islands to your drawing"],
           ["Vanity tops", "Common widths 25\", 31\", 37\", 49\" and 61\", with single or double basin cut-outs"],
           ["Edge profiles", "Eased, bevel, half bullnose, full bullnose, ogee, mitred"],
           ["Marble bathtubs", "Freestanding, carved from one block, made to your dimensions"]],
          note="We follow your shop drawings. Dimensions are confirmed in writing before cutting."),
    table("Shipping", "Shipping to the United States", ["Item", "Detail"],
          [["Destination ports", "East Coast (for example New York/New Jersey, Savannah), Gulf (Houston) and West Coast (Los Angeles/Long Beach)"],
           ["Incoterms", "FOB Mundra or Kandla, CFR or CIF to your US port"],
           ["Customs", "Your customs broker files the entry; ISF (10+2) data is sent before the vessel sails"],
           ["Packing", "ISPM-15 fumigated wooden crates and A-frames"],
           ["Documents", "Commercial invoice, packing list, certificate of origin, fumigation certificate, bill of lading"]],
          alt_bg=True),
    steps("How it works", "Ordering from India, step by step", PROCESS),
    faq(usa_faq),
    links("Guides", "Useful reading", GUIDE_LINKS),
    other_markets("/usa"),
    cta("Send your colours, formats and port, and we will reply with photos and a US quotation."),
]


# ───────────────────────── UK ─────────────────────────
uk_faq = [
    ("Do you supply granite worktops to the UK?",
     "Yes. We cut granite and marble worktops in 20 mm and 30 mm to your templates, with upstands, "
     "splashbacks and window sills from the same slabs, and ship them by container to UK ports."),
    ("Can you supply full slabs to UK fabricators?",
     "Yes. Full gangsaw slabs in 20 mm and 30 mm, packed in numbered bundles, for fabricators and "
     "stone yards that cut their own worktops."),
    ("What paperwork do I need to import stone into the UK?",
     "You need an EORI number and a customs declaration, usually made by your freight forwarder or "
     "customs agent. We supply the commercial invoice, packing list, certificate of origin and "
     "fumigation certificate."),
    ("Do you supply marble basins and bathtubs in the UK?",
     "Yes. We carve vessel basins and freestanding bathtubs from single blocks of marble for UK "
     "designers, developers and hotel projects."),
]

uk = {
    "file": "uk.html",
    "path": "/uk",
    "title": "Granite Worktops and Marble Supplier UK | Indian Stone Exporter",
    "description": "Granite and marble worktops, slabs, basins and bathtubs for UK fabricators and kitchen studios. 20 and 30 mm, cut to template and shipped to UK ports.",
    "h1": "Granite worktops and marble for the UK trade",
    "crumbs": [("Export markets", "/natural-stone-exporters"), ("United Kingdom", "/uk")],
    "og_image": "/assets/images/og/uk.jpg",
    "og_source": "/assets/images/capabilities/cap-thick.webp",
    "faq": uk_faq,
}
uk["sections"] = [
    hero("Exporting to the United Kingdom", uk["h1"],
         "Worktops, full slabs, upstands, basins and bathtubs in Indian granite and marble. Cut to template "
         "in Udaipur and shipped by container to UK ports.",
         uk["crumbs"]),
    intro("Worktops, not countertops",
          ["UK buyers search for granite worktops, so that is what we call them here. We cut worktops in "
           "20 mm and 30 mm, with matching upstands, splashbacks and sills from the same slabs so the "
           "colour matches.",
           "Fabricators can buy full slabs instead and cut locally. Kitchen studios and developers often "
           "prefer finished pieces cut to their templates, which saves workshop time in the UK.",
           "For bathrooms we carve marble basins and freestanding baths from single blocks. These are "
           "specified by interior designers for high-end homes and hotels."],
         f"{IMG}/capabilities/cap-thick.webp", "Thick green marble kitchen worktop",
         cta="Request a UK quotation"),
    product_cards(["slabs", "counter", "vanity", "sinks", "tubs", "marble"], "UK"),
    table("UK specifications", "Common UK formats", ["Product", "Typical specification"],
          [["Granite and marble worktops", "20 mm and 30 mm, lengths to template, with sink and hob cut-outs"],
           ["Upstands and splashbacks", "Cut from the same slabs as the worktops so the colour matches"],
           ["Full slabs", "20 mm and 30 mm gangsaw slabs in numbered bundles"],
           ["Edges", "Pencil round, bevel, half bullnose, full bullnose, mitred apron"],
           ["Bathroom", "Vanity tops, vessel basins, freestanding single-block bathtubs"]]),
    table("Shipping", "Shipping to the UK", ["Item", "Detail"],
          [["Destination ports", "Felixstowe, Southampton, London Gateway, or the port you name"],
           ["Incoterms", "FOB Mundra or Kandla, CFR or CIF to your UK port"],
           ["Customs", "EORI number and customs declaration through your forwarder or agent"],
           ["Packing", "ISPM-15 fumigated wooden crates and A-frames"],
           ["Documents", "Commercial invoice, packing list, certificate of origin, fumigation certificate, bill of lading"]],
          note="Where your product type needs UKCA or CE marking, for example flooring or cladding, tell us when you enquire.",
          alt_bg=True),
    steps("How it works", "Ordering from India, step by step", PROCESS),
    faq(uk_faq),
    links("Guides", "Useful reading", GUIDE_LINKS),
    other_markets("/uk"),
    cta("Send your templates or a cutting list, and we will reply with a UK quotation."),
]


# ───────────────────────── Australia ─────────────────────────
au_faq = [
    ("Can I still use stone benchtops in Australia after the engineered stone ban?",
     "Yes. Australia banned engineered stone benchtops, panels and slabs from 1 July 2024. Natural stone "
     "such as granite and marble is not covered by the ban. Fabricators must still control silica dust "
     "when cutting any stone."),
    ("What thickness are your granite benchtops?",
     "20 mm and 30 mm slabs are standard. For a thick look we supply mitred aprons, so a 20 mm benchtop "
     "reads as 40 mm or more along the edge."),
    ("How do you meet Australian biosecurity rules?",
     "All timber packaging is ISPM-15 heat-treated or fumigated and marked, and we supply the fumigation "
     "certificate with the shipping documents. Containers can still be inspected on arrival at the "
     "department's discretion."),
    ("Which Australian ports do you ship to?",
     "Sydney (Port Botany), Melbourne, Brisbane, Fremantle and Adelaide, or any port your forwarder "
     "names."),
]

australia = {
    "file": "australia.html",
    "path": "/australia",
    "title": "Granite & Marble Benchtops Supplier Australia | From India",
    "description": "Natural granite and marble benchtops, slabs, basins and bathtubs for Australian fabricators and builders. ISPM-15 packed, shipped to all major ports.",
    "h1": "Natural stone benchtops and slabs for Australia",
    "crumbs": [("Export markets", "/natural-stone-exporters"), ("Australia", "/australia")],
    "og_image": "/assets/images/og/australia.jpg",
    "og_source": "/assets/images/bespoke/sink-granite-bespoke.webp",
    "faq": au_faq,
}
australia["sections"] = [
    hero("Exporting to Australia", australia["h1"],
         "Granite and marble benchtops, full slabs, vanity tops, basins and bathtubs. Natural stone only, "
         "packed to Australian biosecurity rules and shipped to every major port.",
         australia["crumbs"]),
    intro("Natural stone, now the benchtop of choice",
          ["Australia banned engineered stone benchtops, panels and slabs from 1 July 2024. Since then, "
           "builders and kitchen companies have turned to natural granite and marble. That is what we "
           "quarry and cut.",
           "We supply benchtops in 20 mm and 30 mm with mitred aprons for a thick edge. Full slabs go to "
           "fabricators who cut locally, and vanity tops are cut to the sizes Australian builders use.",
           "For luxury homes we carve freestanding bathtubs and basins from single blocks of marble."],
         f"{IMG}/bespoke/sink-granite-bespoke.webp", "Carved granite basin on a stone vanity",
         cta="Request an Australian quotation"),
    product_cards(["slabs", "counter", "vanity", "sinks", "tubs", "blocks"], "Australian"),
    table("Australian specifications", "Common Australian formats", ["Product", "Typical specification"],
          [["Granite and marble benchtops", "20 mm or 30 mm, with 40 mm+ mitred aprons on request"],
           ["Kitchen islands", "Cut to drawing, including waterfall ends"],
           ["Full slabs", "20 mm and 30 mm gangsaw slabs for local fabrication"],
           ["Vanity tops", "Cut to size with undermount or vessel basin cut-outs"],
           ["Bathroom", "Carved vessel basins and freestanding single-block bathtubs"]]),
    table("Shipping", "Shipping to Australia", ["Item", "Detail"],
          [["Destination ports", "Sydney (Port Botany), Melbourne, Brisbane, Fremantle, Adelaide"],
           ["Biosecurity", "ISPM-15 treated and marked timber packaging; fumigation certificate supplied"],
           ["Incoterms", "FOB Mundra or Kandla, CFR or CIF to your Australian port"],
           ["Documents", "Commercial invoice, packing list, certificate of origin, fumigation certificate, bill of lading"],
           ["Silica safety", "Natural stone is permitted; fabricators follow Safe Work Australia silica controls"]],
          alt_bg=True),
    steps("How it works", "Ordering from India, step by step", PROCESS),
    faq(au_faq),
    links("Guides", "Useful reading", GUIDE_LINKS),
    other_markets("/australia"),
    cta("Send your benchtop sizes or a slab list, and we will reply with an Australian quotation."),
]


# ───────────────────────── New Zealand ─────────────────────────
nz_faq = [
    ("Do you ship stone benchtops to New Zealand?",
     "Yes. We ship granite and marble benchtops, slabs, vanity tops, basins and bathtubs by container to "
     "Auckland, Tauranga, Wellington, Lyttelton and Port Chalmers."),
    ("How do you meet New Zealand MPI biosecurity requirements?",
     "Timber packaging is ISPM-15 treated and marked, and containers are packed clean. We supply the "
     "fumigation certificate with the documents. MPI can inspect any consignment on arrival."),
    ("Can I order a single marble bathtub for a house in New Zealand?",
     "Yes, through your designer, builder or freight forwarder. A carved bathtub ships in its own "
     "braced crate and can travel with other cargo in a shared container."),
    ("What thickness are your benchtops?",
     "20 mm and 30 mm are standard, with mitred aprons for a thicker edge."),
]

new_zealand = {
    "file": "new-zealand.html",
    "path": "/new-zealand",
    "title": "Stone Benchtops & Marble Supplier New Zealand | From India",
    "description": "Granite and marble benchtops, slabs, basins and single-block marble bathtubs for New Zealand builders and designers. MPI-compliant packing.",
    "h1": "Granite and marble benchtops for New Zealand",
    "crumbs": [("Export markets", "/natural-stone-exporters"), ("New Zealand", "/new-zealand")],
    "og_image": "/assets/images/og/new-zealand.jpg",
    "og_source": "/assets/images/bespoke/vanity-bespoke.webp",
    "faq": nz_faq,
}
new_zealand["sections"] = [
    hero("Exporting to New Zealand", new_zealand["h1"],
         "Benchtops, full slabs, vanity tops, basins and carved bathtubs in Indian granite and marble, packed "
         "for MPI biosecurity and shipped to New Zealand ports.",
         new_zealand["crumbs"]),
    intro("From Udaipur to Auckland",
          ["New Zealand kitchen companies and builders use the same benchtop formats as Australia: 20 mm "
           "and 30 mm stone, often with mitred aprons. We cut to your drawings or ship full slabs for "
           "local fabrication.",
           "Smaller orders can share a container with other cargo through your forwarder. That makes it "
           "practical to import a single project's benchtops, or one carved marble bath for a residence.",
           "Packing follows ISPM-15 and MPI requirements, and every shipment carries a fumigation certificate."],
         f"{IMG}/bespoke/vanity-bespoke.webp", "Marble vanity top with integrated basin",
         cta="Request a New Zealand quotation"),
    product_cards(["counter", "slabs", "vanity", "sinks", "tubs", "marble"], "New Zealand"),
    table("Shipping", "Shipping to New Zealand", ["Item", "Detail"],
          [["Destination ports", "Auckland, Tauranga, Wellington, Lyttelton, Port Chalmers"],
           ["Biosecurity", "ISPM-15 treated and marked timber packaging; clean containers; fumigation certificate supplied"],
           ["Incoterms", "FOB Mundra or Kandla, CFR or CIF to your New Zealand port"],
           ["Smaller orders", "Shared-container (LCL) shipping through your forwarder"],
           ["Documents", "Commercial invoice, packing list, certificate of origin, fumigation certificate, bill of lading"]],
          alt_bg=True),
    steps("How it works", "Ordering from India, step by step", PROCESS),
    faq(nz_faq),
    links("Guides", "Useful reading", GUIDE_LINKS),
    other_markets("/new-zealand"),
    cta("Send your drawings or a slab list, and we will reply with a New Zealand quotation."),
]


# ───────────────────────── Europe ─────────────────────────
eu_faq = [
    ("Which European countries do you export to?",
     "We ship to importers, processors and projects across the EU and wider Europe, including Germany, "
     "Italy, the Netherlands, Belgium, France and Spain."),
    ("Do your products carry CE marking?",
     "Natural stone for construction falls under European standards such as EN 1469 (cladding slabs), "
     "EN 12058 (floor and stair slabs), EN 1467 (rough blocks) and EN 1468 (rough slabs). Tell us the end "
     "use when you enquire, and we will confirm the test reports and declaration of performance available "
     "for that stone."),
    ("Do you supply blocks to European processors?",
     "Yes. We supply Indian marble and granite blocks to processing factories. Each block is priced per "
     "cubic metre and photographed on all six faces."),
    ("Which European ports do you ship to?",
     "Rotterdam, Antwerp, Hamburg, Genoa, Valencia and other main ports, or the port your forwarder names."),
]

europe = {
    "file": "europe.html",
    "path": "/europe",
    "title": "Natural Stone Supplier Europe | Indian Marble and Granite Exporter",
    "description": "Indian marble and granite for European importers and processors: slabs, blocks, worktops and solid marble bathtubs, shipped to Rotterdam, Antwerp and Genoa.",
    "h1": "Indian marble and granite for European importers",
    "crumbs": [("Export markets", "/natural-stone-exporters"), ("Europe", "/europe")],
    "og_image": "/assets/images/og/europe.jpg",
    "og_source": "/assets/images/hero/hero-photo-3.webp",
    "faq": eu_faq,
}
europe["sections"] = [
    hero("Exporting to Europe", europe["h1"],
         "Slabs, blocks, worktops, basins and carved bathtubs for importers, processors and architects across "
         "Europe, shipped to the main North Sea and Mediterranean ports.",
         europe["crumbs"]),
    intro("A steady source of Indian stone",
          ["European processors buy Indian granite and marble blocks for their own saws. Importers and "
           "stone yards buy finished slabs and cut-to-size work. We supply both.",
           "Blocks come with net measurements and six-face photographs. Slabs are photographed and numbered "
           "before loading. Every shipment is packed in ISPM-15 timber.",
           "For hospitality and residential projects we also carve single-block marble bathtubs and basins "
           "to the designer's drawings."],
         f"{IMG}/hero/hero-photo-3.webp", "Natural stone samples on display",
         cta="Request a European quotation"),
    product_cards(["blocks", "slabs", "marble", "counter", "tubs", "sinks"], "European"),
    table("Standards", "European standards for natural stone", ["Standard", "Covers"],
          [["EN 1467", "Natural stone rough blocks"],
           ["EN 1468", "Natural stone rough slabs"],
           ["EN 1469", "Slabs for cladding"],
           ["EN 12057", "Modular tiles"],
           ["EN 12058", "Slabs for floors and stairs"]],
          intro_text="CE marking and the declaration of performance depend on the product and its end use. Tell us both when you enquire.",
          note="Requirements can differ by country and project; your importer or specifier confirms what applies."),
    table("Shipping", "Shipping to Europe", ["Item", "Detail"],
          [["Destination ports", "Rotterdam, Antwerp, Hamburg, Genoa, Valencia, or the port you name"],
           ["Incoterms", "FOB Mundra or Kandla, CFR or CIF to your European port"],
           ["Customs", "EORI number and import declaration through your forwarder"],
           ["Packing", "ISPM-15 fumigated wooden crates and A-frames"],
           ["Documents", "Commercial invoice, packing list, certificate of origin, fumigation certificate, bill of lading"]],
          alt_bg=True),
    steps("How it works", "Ordering from India, step by step", PROCESS),
    faq(eu_faq),
    links("Guides", "Useful reading", GUIDE_LINKS),
    other_markets("/europe"),
    cta("Send your stone, format and port, and we will reply with photos and a quotation."),
]

MARKET_PAGES = [usa, uk, australia, new_zealand, europe]
