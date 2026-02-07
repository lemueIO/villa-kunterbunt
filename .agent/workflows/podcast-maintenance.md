---
description: podcast maintenance and branding guidelines
---

# Podcast Maintenance and Branding

This workflow outlines the standardization for podcast layout, metadata, and branding across the Villa Kunterbunt project.

## Branding Guidelines

### titles and Labels
- **Main Module**: "Villa Kunterbunt | Das Korrespondenz Epos"
- **Cowork Module**: "Villa Kunterbunt | Die Anthologie & Apokryphen"
- **Meta Module**: "Villa Kunterbunt | Das Kompendium"

### Episode Tags
- Use the format `[Module Name] (Hörbuch)` for audiobook pages (e.g., `Das Korrespondenz Epos (Hörbuch)`).

## MediaSession & MP3 Metadata (iPhone Widget Support)

To ensure the iPhone widget and media players display correctly:

- **Artist (Künstler)**: `Villa Kunterbunt`
- **Album**: The Module Title (e.g., `Das Korrespondenz Epos`)
- **Title (Titel)**: The Episode Name (e.g., `Das Hörbuch`)

### Example Implementation (JavaScript)
```javascript
navigator.mediaSession.metadata = new MediaMetadata({
    title: "Das Hörbuch",
    artist: "Villa Kunterbunt",
    album: "Das Korrespondenz Epos",
    artwork: [ ... ]
});
```

## Repository Maintenance
- **Author**: Commit as `Cipher-Pup <code@lemue.org>`.
- **Large Files**: Avoid committing large raw project files (e.g., `.aup3`). Ensure they are in `.gitignore`.
- **Favicons**: Use section-specific favicons generated from the `/images/favicon_source.png` of each module.
