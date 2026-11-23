# ZooGlass website

Run `python3 build.py` to generate the nine-page Folio site in `dist/` for
zooglass.io. Editable pages, layout, footer and styles live in `src/`.

The Demonstrations section uses ordinary page links to switch between Fleet,
Orders and Sports. Each page has a native video player with a poster and
`preload="none"`; playback is user-controlled. Text beside the silent recordings
explains the behaviour to watch. Each demo also has a genuine 390×844 phone
recording and poster, selected at screen widths up to 740px. Resizing before
playback selects the matching version; rotation after playback starts does not
replace or restart the clip. JavaScript-free playback retains the desktop version.

Recordings and posters live in `src/media/`. Fleet retains its existing continuous
recording. Orders and Sports were captured from real interactive demos at public
commit `bf09373`, stepping through the first nine checkpoints at normal speed on
13 November 2026. They use simulated source data and a prepared ZooGlass JAR.
Phone recordings were captured at public commit `71242f5` (the same runtime with
documentation updates). Orders opens the selected order detail; Sports follows
the corrected result and then opens the first-reported comparison; Fleet shows
the map and selected car at phone width. These are real responsive layouts, not
cropped or scaled desktop recordings.

Demo guides and acceptance records link to the core repository’s main branch.
The site describes delivered runtime capabilities, deterministic timeline
simulation and offline configuration authoring. Keep these claims aligned with
the current capability matrix and qualification records when core features ship.
Live demo recordings illustrate real-service runs, not deterministic playback.

For a LAN preview, supply its URL with `--base` and its serving directory with
`--output`. Serve generated files using `panack-http-server --no-cache --noindex`.

The favicon uses the existing elephant-and-magnifying-glass mark in `src/favicon.svg`,
with 16, 32 and 48-pixel ICO sizes and a 180-pixel Apple touch icon. The shared
layout includes these on every page. Keep the raster icons aligned with the SVG
when changing the mark.

The build fingerprints styles, icons, recordings and posters. Hosts with configurable
cache headers can serve `assets/` with
`Cache-Control: public, max-age=31536000, immutable` and revalidate HTML,
robots.txt and sitemap.xml on each visit.

Search and sharing metadata come from the shared layout and page descriptions in
`build.py`: page titles, descriptions, canonical URLs, Open Graph previews and
Twitter cards. The homepage also declares the ZooGlass site name using WebSite
JSON-LD. The 1200×630 `src/share.png` supplies the shared preview image. The build
emits a sitemap and robots.txt. These are hints: search engines and messaging
apps choose what to display and may cache earlier previews.
