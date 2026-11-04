# ZooGlass website

The project showcase for [zooglass.io](https://zooglass.io). Static HTML, CSS and JavaScript live in `site/`. The interactive example illustrates the ordering rules locally. The fleet screenshot comes from the [vehicle demo](https://github.com/sproates/zooglass/tree/main/demos/vehicle-tracker), including its map attribution.

Run `python3 -m http.server 8000 --directory site` and open http://localhost:8000. Check changes with `python3 scripts/check-site.py` and `node --check site/example.js`.

Pull requests run the site checks. Merging to main deploys the contents of `site/` through GitHub Pages.
