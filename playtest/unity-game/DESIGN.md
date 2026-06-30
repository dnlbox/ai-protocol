---
# Art direction tokens for Lumen (a game, not a web UI). Reshaped from docs/concept/
# by /sync-protocol, and hand-editable.
name: Lumen
palette:
  night: "#0B0F14"    # the cold dark world (backgrounds)
  ink: "#11161D"      # deepest shadow and HUD text
  slate: "#3A4A5A"    # cool mid-tones, structures
  mist: "#8FA3B0"     # desaturated cool highlight, fog and depth
  lantern: "#E8A14B"  # the single warm accent: the lantern glow
mood: "muted nordic, cool and melancholic, one warm light"
typography:
  ui: "Hanken Grotesk"   # menus and HUD only; the world is hand-painted
  baseSize: "16px"
---

# DESIGN.md

The art direction contract for Lumen. This is a game art bible, not web UI tokens:
the palette and mood govern hand-painted assets, lighting, and HUD. Use these
values; do not introduce new ones without updating this file.

<!-- BEGIN PROJECT SPECIFICS: reconciled from docs/concept/ by /sync-protocol,
and hand-editable. -->

## Overview

A calm, melancholic, warm-at-the-edges world. The player is a lantern relighting
the stars, so the whole frame reads cold and quiet except where the lantern
touches it. Restraint over spectacle: negative space, parallax depth, soft glows,
no UI clutter.

## Palette

- night / ink: the cold world and its shadows; almost everything sits here.
- slate / mist: cool structure and atmospheric depth (fog, far parallax layers).
- lantern: the only warm hue in the game; reserve it for light the player casts or
  seeks. Warmth equals meaning, so spend it sparingly.

## Look and feel

- Hand-painted backgrounds, 2D skeletal animation, parallax for depth.
- The lantern is the key light: soft additive glow, gentle falloff, never neon.
- HUD is minimal and diegetic where possible; menus use the UI type at low
  contrast against `night`.

<!-- END PROJECT SPECIFICS -->
