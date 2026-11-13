# ZooGlass website

Run `python3 build.py` to generate the seven-page Folio site in `dist/` for
zooglass.io. Editable pages, layout, footer and styles live in `src/`.

The Demonstrations section uses ordinary page links to switch between Fleet,
Orders and Sports. Each page has a native video player with a poster and
`preload="none"`; playback is user-controlled. Text beside the silent recordings
explains the behaviour to watch.

Recordings and posters live in `src/media/`. Fleet retains its existing continuous
recording. Orders and Sports were captured from real interactive demos at public
commit `bf09373`, stepping through the first nine checkpoints at normal speed on
13 November 2026. They use simulated source data and a prepared ZooGlass JAR.
Their guides currently link to the shared delivery branch because combined main
delivery is pending; update those links and availability notes after that merge.

For a LAN preview, supply its URL with `--base` and its serving directory with
`--output`. Serve generated files using `panack-http-server --no-cache --noindex`.

The build fingerprints styles, recordings and posters. Hosts with configurable
cache headers can serve `assets/` with
`Cache-Control: public, max-age=31536000, immutable` and revalidate HTML,
robots.txt and sitemap.xml on each visit.
