# ZooGlass website

Run `python3 build.py` to generate the seven-page Folio site in `dist/` for
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
Publish this handoff only after the combined Order/Sports delivery reaches main.

For a LAN preview, supply its URL with `--base` and its serving directory with
`--output`. Serve generated files using `panack-http-server --no-cache --noindex`.

The build fingerprints styles, recordings and posters. Hosts with configurable
cache headers can serve `assets/` with
`Cache-Control: public, max-age=31536000, immutable` and revalidate HTML,
robots.txt and sitemap.xml on each visit.
