# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**OBJCLT101** (Objets Cultes 101) is a French-language virtual museum/exhibition website showcasing ancient cult figurines, primarily from Japan's Jomon period (14,000 BCE – 0 CE). The site is designed as an immersive gallery experience with multiple "rooms" (salles) and library/context pages.

## Repository Structure

- `OBJCLTPRT101.ai` — Adobe Illustrator source file containing the full design (4 pages/artboards)
- `exports/` — Assets exported from the Illustrator file
  - `page-{1..4}.png` — Full-page design mockups (the reference designs to implement)
  - `images/` — ~206 individual image assets extracted via `pdfimages`
- `site/` — The website being built (currently scaffolded with empty image directories)
  - `images/context/` — Contextual images (flora, fauna, artifacts, architecture)
  - `images/figurines/` — Individual figurine photos

## Design Reference (from page exports)

- **Page 1**: Main exhibition hall — 3D perspective gallery with arched alcoves, figurines displayed in virtual museum space. Navigation: "Fouiller à la bibliothèque" (library) and "Découvrir la salle suivante" (next room)
- **Page 2**: Library/context page (S03) — Left panel: timeline (Période Jomon, 14000 BCE to 0 CE with sub-periods: Proto-Jomon, Archaïque, Ancien, Moyen, Récent, Final). Center: contextual image grid. Right: featured figurines (A, B). Navigation between pages
- **Page 3**: Collection gallery — Full grid of ~15 figurines with timeline sidebar. Filter by "motifs"
- **Page 4**: Detail/rites view — Larger figurine display with timeline sidebar. Filter by "rites"

## Visual Identity

- **Primary color palette**: Deep terracotta/burgundy red (background), with lighter rose tones for content panels
- **Typography**: Monospaced/geometric typeface for "OBJCLT101" header branding
- **Language**: French throughout — all UI labels, navigation, and content

## Key Extracted Image Assets

The `exports/images/` directory contains PNGs numbered `img-000.png` through `img-205.png`. These need to be sorted into `site/images/context/` and `site/images/figurines/` based on content type.
