# ZooGlass website

Static source for [zooglass.io](https://zooglass.io), introducing the
[ZooGlass project](https://github.com/sproates/zooglass) and its creator, Ian Sproates.

## Edit and check

Edit the HTML under `site/` and the shared stylesheet in `site/assets/`.
There is no build step, JavaScript application, external font or package dependency.
Keep the header, footer and structured data consistent across the three pages.

```sh
python3 scripts/check_site.py
python3 -m http.server 8080 --directory site
```

Open `http://localhost:8080` to preview. Check the three pages on desktop and a
narrow mobile viewport before publishing. The worked example is explanatory;
it does not connect to a running ZooGlass service.

## Publishing

GitHub Actions validates pull requests. Changes to `main` publish **only `site/`**
to GitHub Pages after validation. Configure Settings → Pages → Source → GitHub
Actions before the first deployment. Hosting a public site from a private
repository requires a GitHub plan that supports it; a public repository works
with GitHub Free.

See [domain setup](DOMAIN_SETUP.md) for the custom domain and GoDaddy records.
The `CNAME` file documents the intended hostname; Actions publishing also requires
setting the custom domain in GitHub Pages settings.

## Content and search

The homepage, worked example and About page are plain HTML, readable without
JavaScript. Each has its own title, description and canonical URL. JSON-LD connects
ZooGlass to Ian Sproates and the public source repository. The sitemap includes
all three pages; the 404 page is excluded from indexing.

Keep capability claims aligned with the public project's delivered behavior.
Distinguish the versioned snapshot API from the existing demo subscription API.
Do not describe roadmap items as implemented or claim production readiness.

After publishing and verifying the domain, submit `https://zooglass.io/sitemap.xml`
in Google Search Console and inspect the three URLs. Indexing and AI-search
mentions are not guaranteed by metadata or sitemap submission.

The site includes no analytics, forms, trackers or third-party embeds.
