# ZooGlass website

Run `python3 build.py` to generate the five-page Folio site in `dist/` for zooglass.io. The editable pages, layout, footer and stylesheet live in `src/`. The demo recording and poster are in `src/media/`.

For a LAN preview, supply its URL with `--base` and its serving directory with `--output`. Serve the generated files using `panack-http-server --no-cache --noindex`.

The build fingerprints the stylesheet, recording and poster. A production host with configurable cache headers can serve `assets/` with `Cache-Control: public, max-age=31536000, immutable` and revalidate HTML, robots.txt and sitemap.xml on each visit.
