"""Check the files and section links visitors need to use the showcase."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

root = Path(__file__).resolve().parents[1] / "site"


class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if "id" in attributes:
            self.ids.add(attributes["id"])
        for key in ("href", "src"):
            if key in attributes:
                self.urls.append(attributes[key])


page = References()
page.feed((root / "index.html").read_text())
for url in page.urls:
    reference = urlsplit(url)
    if reference.scheme or reference.netloc:
        continue
    if reference.path and not (root / reference.path).exists():
        raise SystemExit(f"Missing local file: {url}")
    if reference.fragment and reference.fragment not in page.ids:
        raise SystemExit(f"Missing page section: {url}")
