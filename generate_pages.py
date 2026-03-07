#!/usr/bin/env python3
"""Generate HTML pages for the objetscultes site from SVG exports."""

import os

SITE_DIR = "site"
PAGES_DIR = os.path.join(SITE_DIR, "pages")

# Page template
def make_page(img_path, page_id, nav_links, title="OBJCLT101"):
    """Generate an HTML page with WebP image and nav overlay."""
    nav_html = ""
    for link in nav_links:
        cls = f'nav-link {link["class"]}'
        if link.get("disabled"):
            nav_html += f'      <span class="{cls} nav-disabled">{link["label"]}</span>\n'
        else:
            nav_html += f'      <a href="{link["href"]}" class="{cls}">{link["label"]}</a>\n'

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <section id="{page_id}" class="page">
    <img src="../{img_path}" class="page-img" alt="Page">
    <div class="nav-overlay">
{nav_html}    </div>
  </section>
  <script src="../script.js"></script>
</body>
</html>
"""

# Navigation definitions
# obj pages 1-16
obj_pages = {
    1: {
        "id": "landing",
        "title": "OBJCLT101 — Figurines",
        "nav": [
            {"label": "ABOUT", "href": "obj-2.html", "class": "nav-btn-about"},
            {"label": "VISIT", "href": "obj-3.html", "class": "nav-btn-visit"},
        ]
    },
    2: {
        "id": "about",
        "title": "OBJCLT101 — Craquer le code",
        "nav": [
            {"label": "VISIT", "href": "obj-3.html", "class": "nav-btn-visit-solo"},
        ]
    },
    3: {
        "id": "map",
        "title": "OBJCLT101 — Map",
        "nav": [
            {"label": "Image objet", "href": "obj-4.html", "class": "nav-image-objet"},
            {"label": "Accéder aux salles", "href": "obj-4.html", "class": "nav-acceder-salles"},
        ]
    },
    4: {
        "id": "lobby",
        "title": "OBJCLT101 — Accueil",
        "nav": [
            {"label": "Accéder aux salles", "href": "obj-5.html", "class": "nav-acceder-salles-lobby"},
        ]
    },
    5: {
        "id": "prehistoire-far",
        "title": "OBJCLT101 — Préhistoire",
        "nav": [
            {"label": "Retour", "href": "obj-4.html", "class": "nav-back-square"},
            {"label": "S'approcher", "href": "obj-6.html", "class": "nav-sapprocher"},
            {"label": "Salle suivante", "href": "obj-9.html", "class": "nav-door-right"},
        ]
    },
    6: {
        "id": "prehistoire-close",
        "title": "OBJCLT101 — Venus",
        "nav": [
            {"label": "Retour", "href": "obj-5.html", "class": "nav-back-square"},
            {"label": "Accéder aux salles", "href": "obj-8.html", "class": "nav-acceder-salles-center"},
        ]
    },
    7: {
        "id": "prehistoire-nav",
        "title": "OBJCLT101 — Préhistoire",
        "nav": [
            {"label": "Retour", "href": "obj-4.html", "class": "nav-back-square"},
            {"label": "S'approcher", "href": "obj-6.html", "class": "nav-sapprocher"},
            {"label": "Accéder aux salles", "href": "obj-9.html", "class": "nav-acceder-salles-right"},
        ]
    },
    8: {
        "id": "prehistoire-collection",
        "title": "OBJCLT101 — Collection Préhistoire",
        "nav": [
            {"label": "Fouiller à la bibliothèque", "href": "tmln-6.html", "class": "nav-fouiller"},
            {"label": "Découvrir la salle suivante", "href": "obj-9.html", "class": "nav-decouvrir"},
        ]
    },
    9: {
        "id": "jomon-exhibition",
        "title": "OBJCLT101 — Jōmon",
        "nav": [
            {"label": "Fouiller à la bibliothèque", "href": "tmln-10.html", "class": "nav-fouiller"},
            {"label": "Découvrir la salle suivante", "href": "obj-10.html", "class": "nav-decouvrir"},
        ]
    },
    10: {
        "id": "egypt-exhibition",
        "title": "OBJCLT101 — Égypte",
        "nav": [
            {"label": "Fouiller à la bibliothèque", "href": "tmln-2.html", "class": "nav-fouiller"},
            {"label": "Découvrir la salle suivante", "href": "obj-11.html", "class": "nav-decouvrir"},
        ]
    },
    11: {
        "id": "medieval-exhibition",
        "title": "OBJCLT101 — Moyen Âge",
        "nav": [
            {"label": "Fouiller à la bibliothèque", "href": "tmln-14.html", "class": "nav-fouiller"},
            {"label": "Découvrir la salle suivante", "href": "obj-12.html", "class": "nav-decouvrir"},
        ]
    },
    12: {
        "id": "porcelain-exhibition",
        "title": "OBJCLT101 — Porcelaine",
        "nav": [
            {"label": "Fouiller à la bibliothèque", "href": "tmln-18.html", "class": "nav-fouiller"},
            {"label": "Découvrir la salle suivante", "href": "obj-13.html", "class": "nav-decouvrir"},
        ]
    },
    13: {
        "id": "boutique",
        "title": "OBJCLT101 — Boutique",
        "nav": [
            {"label": "Accéder à la bibliothèque", "href": "obj-14.html", "class": "nav-acceder-biblio"},
        ]
    },
    14: {
        "id": "bookshop",
        "title": "OBJCLT101 — Librairie",
        "nav": [
            {"label": "Retourner à la salle d'exposition", "href": "obj-4.html", "class": "nav-retourner-center"},
        ]
    },
    15: {
        "id": "overview",
        "title": "OBJCLT101 — Vue d'ensemble",
        "nav": [
            {"label": "VISIT", "href": "obj-4.html", "class": "nav-btn-visit-map"},
        ]
    },
    16: {
        "id": "craquer-detail",
        "title": "OBJCLT101 — Craquer le code",
        "nav": [
            {"label": "QUIZZ", "href": "obj-1.html", "class": "nav-btn-quizz"},
        ]
    },
}

# tmln pages - room sub-pages
# Egypt: exhibition=tmln-1, library=tmln-2, collection=tmln-3, detail=tmln-4
# Préhistoire: library=tmln-6, collection=tmln-7, detail=tmln-8
# Jōmon: exhibition=tmln-9, library=tmln-10, collection=tmln-11, detail=tmln-12
# Medieval: exhibition=tmln-13, library=tmln-14, collection=tmln-15, detail=tmln-16
# Porcelain: exhibition=tmln-17, library=tmln-18, collection=tmln-19, detail=tmln-20
# Boutique: tmln-21

# Room definitions: (exhibition_page, library_page, collection_pages..., back_to_obj)
rooms = {
    "egypt": {
        "exhibition": 1, "sub_pages": [2, 3, 4],
        "obj_exhibition": "obj-10.html",
        "next_room_exhibition": "obj-11.html",
    },
    "prehistoire": {
        "exhibition": None,  # uses obj pages
        "sub_pages": [6, 7, 8],
        "obj_exhibition": "obj-8.html",
        "next_room_exhibition": "obj-9.html",
    },
    "jomon": {
        "exhibition": 9, "sub_pages": [10, 11, 12],
        "obj_exhibition": "obj-9.html",
        "next_room_exhibition": "obj-10.html",
    },
    "medieval": {
        "exhibition": 13, "sub_pages": [14, 15, 16],
        "obj_exhibition": "obj-11.html",
        "next_room_exhibition": "obj-12.html",
    },
    "porcelain": {
        "exhibition": 17, "sub_pages": [18, 19, 20],
        "obj_exhibition": "obj-12.html",
        "next_room_exhibition": "obj-13.html",
    },
}

tmln_pages = {}

# Exhibition halls from tmln (have "Fouiller" + "Découvrir")
for room_name, room in rooms.items():
    if room["exhibition"]:
        p = room["exhibition"]
        sub = room["sub_pages"]
        tmln_pages[p] = {
            "id": f"{room_name}-exhibition-tmln",
            "title": f"OBJCLT101 — {room_name.title()}",
            "nav": [
                {"label": "Fouiller à la bibliothèque", "href": f"tmln-{sub[0]}.html", "class": "nav-fouiller"},
                {"label": "Découvrir la salle suivante", "href": room["next_room_exhibition"], "class": "nav-decouvrir"},
            ]
        }

    # Sub-pages (library, collection, detail) have "Retourner" + "Précédente" + "Suivante"
    sub = room["sub_pages"]
    for i, p in enumerate(sub):
        prev_page = sub[i - 1] if i > 0 else None
        next_page = sub[i + 1] if i < len(sub) - 1 else None

        nav = [
            {"label": "Retourner à la salle d'exposition", "href": room["obj_exhibition"], "class": "nav-retourner"},
        ]

        if prev_page:
            nav.append({"label": "Page précédente", "href": f"tmln-{prev_page}.html", "class": "nav-precedente"})
        else:
            nav.append({"label": "Page précédente", "href": "#", "class": "nav-precedente", "disabled": True})

        if next_page:
            nav.append({"label": "Page suivante", "href": f"tmln-{next_page}.html", "class": "nav-suivante"})
        else:
            nav.append({"label": "Page suivante", "href": room["obj_exhibition"], "class": "nav-suivante"})

        tmln_pages[p] = {
            "id": f"{room_name}-sub-{i+1}",
            "title": f"OBJCLT101 — {room_name.title()}",
            "nav": nav,
        }

# Boutique tmln-21
tmln_pages[21] = {
    "id": "boutique-tmln",
    "title": "OBJCLT101 — Boutique",
    "nav": [
        {"label": "Accéder à la bibliothèque", "href": "obj-14.html", "class": "nav-acceder-biblio"},
    ]
}

# Generate all pages
os.makedirs(PAGES_DIR, exist_ok=True)

for num, page in obj_pages.items():
    html = make_page(f"webp/obj/page-{num}.webp", page["id"], page["nav"], page["title"])
    filepath = os.path.join(PAGES_DIR, f"obj-{num}.html")
    with open(filepath, "w") as f:
        f.write(html)
    print(f"Generated {filepath}")

for num, page in tmln_pages.items():
    html = make_page(f"webp/tmln/page-{num}.webp", page["id"], page["nav"], page["title"])
    filepath = os.path.join(PAGES_DIR, f"tmln-{num}.html")
    with open(filepath, "w") as f:
        f.write(html)
    print(f"Generated {filepath}")

print(f"\nTotal: {len(obj_pages)} obj pages + {len(tmln_pages)} tmln pages = {len(obj_pages) + len(tmln_pages)} pages")
