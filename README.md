# ZooGlass website

The [ZooGlass](https://zooglass.io) project site lives in `site/`. The order example illustrates view-local mappings and publication retries in the browser.

Use `panack-http-server` for previews. Serve a copy of `site/` with its canonical URL set to the preview address. Bind the server to the Mac’s LAN address with `--no-cache --noindex` and share that address with reviewers.

Run `python3 scripts/check-site.py` and `node --check site/example.js` to check local references and JavaScript syntax. Merging to main deploys the static site through GitHub Pages.
