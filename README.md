# OBJCLT101 — Objets Cultes

**A virtual exhibition exploring cult figurines and sacred objects across the ages.**

![Status](https://img.shields.io/badge/status-in%20development-orange)
![Language](https://img.shields.io/badge/language-French-blue)

---

## About

OBJCLT101 (Objets Cultes 101) is an immersive, web-based virtual exhibition that reimagines how we experience ancient art online. The first edition focuses on Japan's **Jomon period** (14,000 BCE – 0 CE) — one of the oldest ceramic cultures in the world — showcasing its enigmatic *dogu* figurines, flame vessels, and ritual objects.

Rather than presenting artifacts as flat images on a page, OBJCLT101 places them in a designed spatial experience: a virtual museum with gallery rooms, curated alcoves, contextual timelines, and layered visual storytelling.

## The Experience

The exhibition unfolds across four interconnected sections:

1. **Salle d'exposition** — A perspective-rendered gallery hall with arched alcoves displaying figurines at varying depths, centered around the iconic *Shakoki-dogu* (goggle-eyed figurine) on a pedestal.

2. **Bibliotheque** — A contextual library page pairing a navigable Jomon timeline (Proto-Jomon through Final Jomon) with a visual grid of cultural context — flora, fauna, dwellings, pottery, ornaments — alongside featured artifacts.

3. **Collection** — A scattered gallery of twelve figurines inviting exploration, with hover interactions and a timeline sidebar for temporal orientation.

4. **Detail / Rites** — A focused view presenting select figurines at larger scale for close examination, filtered by ritual context.

## Design Approach

- **Color palette**: Deep terracotta and burgundy evoking earth, clay, and archaeological warmth
- **Typography**: Monospaced geometric type for the OBJCLT101 identity, reinforcing a systematic, archival sensibility
- **Navigation**: Room-to-room link-based navigation (no scrolling), mimicking the physical experience of moving through gallery spaces
- **Interactivity**: Parallax mouse-tracking effects and hover-zoom interactions that bring static artifacts to life

## Technology

Built as a lightweight, static site — pure HTML, CSS, and vanilla JavaScript. No frameworks, no dependencies. Designed to load fast, work anywhere, and let the content speak.

## About the Designer

**Claude Tortorici** is a designer with a deep passion for art history and a belief that design can be a powerful tool for education. OBJCLT101 is his first project at the intersection of these interests — applying design thinking and spatial storytelling to make ancient art accessible, engaging, and alive in a digital context.

The broader vision behind this work is to explore **what figurines, sacred objects, and cult artifacts reveal about human cultures across time and geography** — from Jomon-era Japan to Cycladic Greece, from pre-Columbian Mesoamerica to ancient Mesopotamia. Each culture shaped small objects imbued with meaning, and each deserves a thoughtful, designed exhibition experience.

## For Museums and Cultural Institutions

This project serves as a proof of concept for what digital exhibition design can offer museums seeking to enrich their online presence.

**What I offer:**

- **Bespoke virtual exhibitions** — Immersive, designed web experiences tailored to your collection, your narrative, and your audience
- **Design-led digital mediation** — Not just digitizing catalogs, but creating genuine spatial and visual storytelling around artifacts
- **Lightweight, accessible technology** — Fast-loading, responsive experiences that work on any device without requiring apps or plugins
- **Art historical rigor** — Content designed with care for chronology, context, and curatorial intent

**Why it matters:**

Museums hold extraordinary collections, but online experiences often reduce them to database entries and thumbnail grids. A well-designed virtual exhibition can extend a museum's reach, engage new audiences, support educational programming, and complement physical exhibitions — all while staying true to the institution's curatorial voice.

**If you represent a museum, gallery, or cultural institution and are interested in collaborating on a digital exhibition project, I would love to hear from you.**

---

## Project Structure

```
OBJCLTPRT101.ai          # Original Illustrator design file (4 artboards)
exports/                  # Exported assets from the design
  page-{1..4}.png         # Full-page design reference mockups
  images/                 # Individual extracted image assets
site/                     # The live website
  index.html              # Single-page exhibition (4 sections)
  style.css               # All styling
  script.js               # Navigation and interaction logic
  images/
    figurines/            # 19 figurine PNGs with transparency
    context/              # 12 contextual images (flora, fauna, artifacts)
```

## License

All design work and code by Claude Tortorici. All rights reserved.

Artifact images are used for educational and portfolio purposes. Original artworks belong to their respective institutions and collections.
