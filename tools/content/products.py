from build_pages import hero, intro, cards, table, steps, faq, links, cta

IMG = "/assets/images"

MARBLES = [
    (f"{IMG}/marble/marble-nirzerna.webp", "Nirzerna White Marble",
     "Pale ivory ground with soft, restrained veining. Our most requested white for floors, walls and vanity tops.",
     "Nirzerna Marble"),
    (f"{IMG}/marble/marble-aagaria.webp", "Aagaria Marble",
     "Warm cream with grey-gold movement. Suits classical interiors, hotel lobbies and bathrooms.",
     "Aagaria Marble"),
    (f"{IMG}/marble/marble-onyx.webp", "Indian Onyx",
     "Layered and translucent. Supplied resin-backed for backlit walls, bar fronts and feature panels.",
     "Indian Onyx Marble"),
    (f"{IMG}/marble/marble-green.webp", "Indian Green Marble (Verde Guatemala)",
     "Deep forest green with white crystalline veining. Dense and hard-wearing for a marble.",
     "Green Marble"),
    (f"{IMG}/marble/marble-pandawhite.webp", "Panda White Marble",
     "Snow-white ground with bold black streaks. Book-matched for statement walls and islands.",
     "Panda White Marble"),
]

GRANITES = [
    (f"{IMG}/granite/granite-black.webp", "Devgarh Black Granite",
     "Dense, uniform black. The standard choice for kitchen countertops and commercial flooring.",
     "Black Granite"),
    (f"{IMG}/granite/granite-pwhite.webp", "Sirohi P White Granite",
     "Grey-white granular pattern. Hard-wearing for high-traffic floors, steps and paving.",
     "P White Granite"),
    (f"{IMG}/granite/granite-alaska-white.webp", "Alaska White Granite",
     "White and grey with burgundy flecks. A popular countertop colour in the US and Australia.",
     "Alaska White Granite"),
    (f"{IMG}/granite/granite-alaska-gold.webp", "Alaska Gold Granite",
     "Gold, cream and grey movement. Warm tone for kitchens and vanity tops.",
     "Alaska Gold Granite"),
    (f"{IMG}/granite/granite-alaska-azul.webp", "Alaska Azul Granite",
     "Cool grey-blue with dark veining. Works in contemporary kitchens and bathrooms.",
     "Alaska Azul Granite"),
    (f"{IMG}/granite/granite-blue-dunes.webp", "Blue Dunes Granite",
     "Flowing blue-grey waves. A statement slab for islands and feature walls.",
     "Blue Dunes Granite"),
]

SHIPPING_ROWS = [
    ["Export ports", "Mundra and Kandla, Gujarat"],
    ["Incoterms", "FOB, CFR or CIF to your named port"],
    ["Packing", "ISPM-15 fumigated wooden crates and A-frame bundles, steel-banded"],
    ["Shipping documents", "Commercial invoice, packing list, certificate of origin, fumigation certificate, bill of lading"],
    ["Mixed loads", "Different stones and formats can usually share one container"],
]

RELATED_PRODUCTS = [
    ("Marble slabs", "/marble-slabs"),
    ("Granite slabs", "/granite-slabs"),
    ("Marble blocks", "/marble-blocks"),
    ("Granite blocks", "/granite-blocks"),
    ("Granite countertops", "/granite-countertops"),
    ("Solid marble bathtubs", "/stone-bathtubs"),
    ("Marble sinks and basins", "/luxury-stone-sinks"),
]

MARKET_LINKS = [
    ("USA", "/usa"),
    ("United Kingdom", "/uk"),
    ("Europe", "/europe"),
    ("Australia", "/australia"),
    ("New Zealand", "/new-zealand"),
]


def related_except(path):
    return [(l, h) for l, h in RELATED_PRODUCTS if h != path]


# ───────────────────────── Marble slabs ─────────────────────────
marble_slabs_faq = [
    ("Which thicknesses do you supply marble slabs in?",
     "18 mm and 20 mm are standard for flooring and wall cladding, and 30 mm for countertops, "
     "vanity tops and stair treads. Other thicknesses can be cut to order."),
    ("Can I see the actual slabs before they are shipped?",
     "Yes. Before loading we send photographs of the slabs from your block, numbered in sequence, "
     "so you approve the material you will receive rather than a sample."),
    ("Do you supply book-matched marble slabs?",
     "Yes. Slabs from one block are kept in cutting order, so consecutive slabs can be "
     "book-matched or vein-matched on a wall or island."),
    ("What is the minimum order?",
     "We ship by the container. Different stones and thicknesses can usually be combined in one "
     "container, which suits importers building a range."),
    ("Which countries do you ship marble slabs to?",
     "We export to importers, fabricators and project buyers in the USA, the UK, Europe, Australia, "
     "New Zealand and the Middle East."),
]

marble_slabs = {
    "file": "marble-slabs.html",
    "path": "/marble-slabs",
    "title": "Marble Slabs Exporter from India | Wholesale Indian Marble Slabs",
    "description": "Wholesale Indian marble slabs from Udaipur: Nirzerna white, Aagaria, onyx, green and Panda White in 18-30 mm. Exported to the USA, UK, Europe, Australia and NZ.",
    "h1": "Indian marble slabs, wholesale from Udaipur",
    "crumbs": [("Marble slabs", "/marble-slabs")],
    "og_image": "/assets/images/og/marble-slabs.jpg",
    "og_source": "/assets/images/capabilities/cap-slab.webp",
    "faq": marble_slabs_faq,
}
marble_slabs["sections"] = [
    hero("Marble slabs", marble_slabs["h1"],
         "Gangsaw and cutter slabs cut from Rajasthan's marble quarries. Polished, honed or leathered, "
         "packed in fumigated bundles and shipped by container to importers, fabricators and projects worldwide.",
         marble_slabs["crumbs"],
         "Udaipur, Rajasthan. Exporting natural stone for more than 25 years."),
    intro("Slabs selected block by block",
          ["Udaipur sits in the middle of Rajasthan's marble belt, the region that produces most of India's marble. "
           "We buy blocks at the quarry and have them sawn into slabs under our supervision.",
           "Each block is checked for cracks and colour consistency before sawing. Slabs from one block stay "
           "together and in cutting order. That lets you book-match a feature wall and keeps one floor in a "
           "single shade.",
           "We supply importers and stone yards that stock slabs, fabricators cutting countertops and vanity "
           "tops, and contractors buying for a single project."],
         f"{IMG}/capabilities/cap-slab.webp", "Polished marble slabs stacked on A-frames ready for export",
         cta="Request slab photos and prices"),
    cards("Our marbles", "Indian marble varieties we export as slabs", MARBLES,
          "These are the marbles we ship most. If you need a variety that isn't listed, tell us and we will source it."),
    table("Specifications", "Marble slab specifications",
          ["Item", "Standard supply"],
          [["Thickness", "18 mm, 20 mm, 30 mm. Others cut to order"],
           ["Slab sizes", "Gangsaw slabs at full block size, which varies by quarry. Cutter slabs in narrower widths for tiles, steps and skirting"],
           ["Finishes", "Polished, honed, leathered, brushed"],
           ["Reinforcement", "Epoxy resin and fibreglass mesh backing where the stone needs it (onyx always)"],
           ["Edges (cut-to-size)", "Eased, bevelled, half bullnose, full bullnose, mitred"],
           ["Inspection", "Thickness, flatness, polish and surface defects are checked slab by slab, with photos before loading"]],
          note="Exact slab dimensions depend on the block. We send a measured slab list with photographs before you confirm."),
    table("Export", "Packing and shipping", ["Item", "Detail"], SHIPPING_ROWS, alt_bg=True),
    faq(marble_slabs_faq, alt_bg=False),
    links("Related", "More from our range", related_except("/marble-slabs"), alt_bg=True),
    links("Export markets", "Buying from abroad?", MARKET_LINKS),
    cta("Send us your stone, thickness and quantity and we will reply with slab photos and a quote."),
]


# ───────────────────────── Granite slabs ─────────────────────────
granite_slabs_faq = [
    ("What thickness are your granite slabs?",
     "20 mm (2 cm) and 30 mm (3 cm) are standard. The US market mostly buys 3 cm for countertops, "
     "while the UK and Australia commonly use 20 mm and 30 mm worktops and benchtops."),
    ("Which granite finishes can you supply?",
     "Polished, honed, leathered and flamed. Flamed and leathered finishes add slip resistance for "
     "exterior paving and steps."),
    ("Is Indian granite suitable for kitchen countertops?",
     "Yes. Granite is hard, heat-resistant and much less porous than marble, which is why it is the most "
     "common natural stone for kitchen countertops. We recommend sealing light-coloured granites."),
    ("Can you cut granite slabs to size?",
     "Yes. Besides full slabs we cut countertops, vanity tops, tiles, steps and risers to your drawing, "
     "with finished edges and sink cut-outs."),
    ("How are granite slabs packed for export?",
     "In ISPM-15 fumigated wooden bundles or A-frames, strapped and braced so the slabs cannot shift in "
     "the container. Bundles are numbered against the packing list."),
]

granite_slabs = {
    "file": "granite-slabs.html",
    "path": "/granite-slabs",
    "title": "Granite Slabs Wholesale from India | Indian Granite Slab Exporter",
    "description": "Wholesale Indian granite slabs in 2 cm and 3 cm: Devgarh black, Alaska white, Alaska gold and more. Polished, honed or leathered, shipped worldwide from India.",
    "h1": "Granite slabs, wholesale from India",
    "crumbs": [("Granite slabs", "/granite-slabs")],
    "og_image": "/assets/images/og/granite-slabs.jpg",
    "og_source": "/assets/images/granite/granite-alaska-white.webp",
    "faq": granite_slabs_faq,
}
granite_slabs["sections"] = [
    hero("Granite slabs", granite_slabs["h1"],
         "Gangsaw granite slabs in 2 cm and 3 cm from Rajasthan's quarries, for importers, slab yards and "
         "countertop fabricators. We quote FOB, CFR or CIF to your port.",
         granite_slabs["crumbs"],
         "Udaipur, Rajasthan. Exporting natural stone for more than 25 years."),
    intro("Granite for countertops, floors and facades",
          ["India is one of the world's largest granite producers, and Rajasthan supplies many of the "
           "black, white and gold granites sold in the US, UK and Australian markets.",
           "We supply full gangsaw slabs for yards and fabricators, and cut-to-size work for projects. "
           "Slabs are polished on modern lines, and each one is checked for thickness, polish and "
           "fissures before it is bundled.",
           "Not sure which colour suits your market? Tell us where you sell and we will recommend the "
           "granites that move fastest there."],
         f"{IMG}/granite/granite-alaska-white.webp", "Alaska White granite slab surface",
         cta="Request granite slab prices"),
    cards("Our granites", "Indian granite colours we export", GRANITES),
    table("Specifications", "Granite slab specifications",
          ["Item", "Standard supply"],
          [["Thickness", "20 mm (2 cm) and 30 mm (3 cm). 40 mm and above to order"],
           ["Slab sizes", "Full gangsaw slabs, sized by the block. Measured slab lists supplied before loading"],
           ["Finishes", "Polished, honed, leathered, flamed"],
           ["Treatment", "Resin treatment on granites that benefit from it"],
           ["Cut-to-size", "Countertops, vanity tops, island tops, tiles, steps and risers to your drawing"],
           ["Inspection", "Thickness, polish, flatness and fissures checked slab by slab, with photos before loading"]]),
    table("Export", "Packing and shipping", ["Item", "Detail"], SHIPPING_ROWS, alt_bg=True),
    faq(granite_slabs_faq, alt_bg=False),
    links("Related", "More from our range", related_except("/granite-slabs"), alt_bg=True),
    links("Export markets", "Buying from abroad?", MARKET_LINKS),
    cta("Tell us the colours, thickness and finish you need and we will send slab photos with a quote."),
]


# ───────────────────────── Marble blocks ─────────────────────────
marble_blocks_faq = [
    ("How are marble blocks measured and priced?",
     "Blocks are priced per cubic metre on their net measured dimensions (length, height, width). "
     "We send the measurements and photographs of every face before you commit."),
    ("How many marble blocks fit in a container?",
     "Marble weighs roughly 2.7 tonnes per cubic metre, so a 20 ft container usually carries about "
     "9 to 10 m&sup3;, often one or two blocks. We size and pair blocks to make good use of the payload."),
    ("Can I inspect the blocks before shipment?",
     "Yes. You or your agent are welcome at the quarry or our yard. Otherwise we send wet-surface photos "
     "and videos of all six faces so veining and any defects are visible."),
    ("Do you supply gangsaw-size blocks?",
     "Yes, subject to what the quarry is producing. Tell us your gangsaw or block-cutter dimensions and "
     "we will only offer blocks that fit."),
]

marble_blocks = {
    "file": "marble-blocks.html",
    "path": "/marble-blocks",
    "title": "Marble Blocks Supplier India | Raw Indian Marble Blocks for Export",
    "description": "Raw Indian marble blocks from Rajasthan quarries for processors. Priced per cubic metre with six-face photos, shipped in 20 ft containers worldwide.",
    "h1": "Raw marble blocks for processors and factories",
    "crumbs": [("Marble blocks", "/marble-blocks")],
    "og_image": "/assets/images/og/marble-blocks.jpg",
    "og_source": "/assets/images/capabilities/cap-block.webp",
    "faq": marble_blocks_faq,
}
marble_blocks["sections"] = [
    hero("Marble blocks", marble_blocks["h1"],
         "Quarry blocks of Indian marble for gangsaw and block-cutter processing. Selected at the quarry, "
         "measured in cubic metres and photographed on every face before you buy.",
         marble_blocks["crumbs"],
         "Sourced from Rajasthan's marble quarries, shipped from Mundra and Kandla."),
    intro("Selected at the quarry, not from a list",
          ["Buying blocks from abroad is mostly about trust in the selection. A block that looks clean on "
           "one face can carry a crack or a colour change through the middle.",
           "We inspect blocks at the quarry face. We look for sound material, consistent colour, and a "
           "size that suits your saws. Each block is numbered, measured and photographed wet on all six "
           "faces, so you see the veining as it will appear once polished.",
           "Our block customers are processing factories and slab producers who need a steady supply of "
           "Indian varieties."],
         f"{IMG}/capabilities/cap-block.webp", "Raw marble block at a quarry ready for export",
         cta="Ask for available blocks"),
    cards("Varieties", "Marble varieties available as blocks", MARBLES,
          "Availability depends on what each quarry is producing. We send a current block list on request."),
    steps("How it works", "From quarry to your factory", [
        ("Tell us your specification", "Variety, colour range, block dimensions and monthly volume."),
        ("Block list and photos", "Numbered blocks with net measurements and six-face wet photos."),
        ("Inspection", "Visit the quarry yourself or send an agent, or approve from the photos and video."),
        ("Loading", "Blocks are lashed and loaded at the quarry or our yard and trucked to Mundra or Kandla."),
        ("Documents", "Invoice, packing list, certificate of origin and bill of lading sent for clearance."),
    ]),
    table("Specifications", "Block supply details", ["Item", "Detail"],
          [["Pricing unit", "Per cubic metre (net measured)"],
           ["Sizes", "Gangsaw and block-cutter sizes, matched to your machine"],
           ["Container load", "Typically 9 to 10 m&sup3; per 20 ft container (around 25 tonnes)"],
           ["Inspection", "Six-face wet photographs and video; on-site inspection welcome"],
           ["Ports", "Mundra and Kandla, Gujarat"],
           ["Incoterms", "FOB, CFR or CIF"]], alt_bg=True),
    faq(marble_blocks_faq, alt_bg=False),
    links("Related", "More from our range", related_except("/marble-blocks"), alt_bg=True),
    cta("Send your block size and the varieties you process, and we will share the current block list."),
]


# ───────────────────────── Granite blocks ─────────────────────────
granite_blocks_faq = [
    ("How are granite blocks priced?",
     "Per cubic metre on net measured dimensions. Each block is numbered, measured and photographed "
     "before you confirm."),
    ("How much granite fits in a 20 ft container?",
     "Granite weighs about 2.6 to 2.8 tonnes per cubic metre, so a 20 ft container carries roughly "
     "9 to 10 m&sup3;. Blocks are chosen and paired to use the payload well."),
    ("Do you supply rough or dressed blocks?",
     "Both. Dressed (squared) blocks waste less on the saw; rough blocks cost less per cubic metre. "
     "We quote either."),
    ("Which granite colours are available as blocks?",
     "Black, P white and the Alaska series are the most regular. Supply of each colour follows quarry "
     "production, so ask for the current list."),
]

granite_blocks = {
    "file": "granite-blocks.html",
    "path": "/granite-blocks",
    "title": "Granite Blocks Exporter India | Rough and Dressed Granite Blocks",
    "description": "Rough and dressed Indian granite blocks for gangsaw processing: black, P white and Alaska granites, priced per cubic metre and exported from Mundra.",
    "h1": "Granite blocks from Rajasthan's quarries",
    "crumbs": [("Granite blocks", "/granite-blocks")],
    "og_image": "/assets/images/og/granite-blocks.jpg",
    "og_source": "/assets/images/granite/granite-black.webp",
    "faq": granite_blocks_faq,
}
granite_blocks["sections"] = [
    hero("Granite blocks", granite_blocks["h1"],
         "Rough and dressed granite blocks for processors abroad. Measured in cubic metres, photographed on "
         "every face, and loaded to make full use of each container.",
         granite_blocks["crumbs"],
         "Sourced from Rajasthan's granite quarries, shipped from Mundra and Kandla."),
    intro("Blocks sized for your saws",
          ["We work with quarries across Rajasthan producing black, white and multicolour granites. Blocks "
           "are selected for sound material and consistent colour, then dressed or left rough as you prefer.",
           "Every block is numbered and measured, and photographed wet on all six faces. If a block shows a "
           "fissure or colour change, we tell you before it is offered.",
           "We supply processing factories that need a regular, predictable supply of Indian granite."],
         f"{IMG}/granite/granite-black.webp", "Close-up of black granite surface",
         cta="Ask for available granite blocks"),
    cards("Colours", "Granite colours available as blocks", GRANITES[:4]),
    table("Specifications", "Block supply details", ["Item", "Detail"],
          [["Pricing unit", "Per cubic metre (net measured)"],
           ["Condition", "Rough or dressed (squared)"],
           ["Sizes", "Gangsaw and block-cutter sizes, matched to your machine"],
           ["Container load", "Roughly 9 to 10 m&sup3; per 20 ft container"],
           ["Inspection", "Six-face wet photographs and video; on-site inspection welcome"],
           ["Incoterms", "FOB, CFR or CIF from Mundra or Kandla"]]),
    faq(granite_blocks_faq),
    links("Related", "More from our range", related_except("/granite-blocks")),
    cta("Tell us your block dimensions and colours, and we will send the current list with photos."),
]

PRODUCT_PAGES = [marble_slabs, granite_slabs, marble_blocks, granite_blocks]
