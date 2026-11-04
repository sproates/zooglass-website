"""Check publishable pages, metadata and local navigation using the standard library."""
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1] / 'site'
errors = []

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.ids = set()
        self.links = []
        self.h1_count = 0
        self.canonical = None
        self.description = None
        self.has_language = False
        self.has_title = False
        self.json_parts = []
        self.in_json = False
        self.json_buffer = ''

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html':
            self.has_language = attrs.get('lang') == 'en'
        if tag == 'title':
            self.has_title = True
        if tag == 'h1':
            self.h1_count += 1
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                errors.append(f'{self.path}: duplicate id {attrs["id"]}')
            self.ids.add(attrs['id'])
        if tag == 'meta' and attrs.get('name') == 'description':
            self.description = attrs.get('content')
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = attrs.get('href')
        for attribute in ('href', 'src'):
            if attribute in attrs:
                self.links.append(attrs[attribute])
        if tag == 'img' and 'alt' not in attrs:
            errors.append(f'{self.path}: image without alt')
        if tag == 'script':
            if attrs.get('type') != 'application/ld+json':
                errors.append(f'{self.path}: unexpected executable script')
            self.in_json = attrs.get('type') == 'application/ld+json'
            self.json_buffer = ''

    def handle_data(self, text):
        if self.in_json:
            self.json_buffer += text

    def handle_endtag(self, tag):
        if tag == 'script' and self.in_json:
            self.json_parts.append(json.loads(self.json_buffer))
            self.in_json = False

pages = {}
for file in ROOT.rglob('*.html'):
    page = Page(file.relative_to(ROOT))
    page.feed(file.read_text())
    pages[file.resolve()] = page
    if not page.has_language or not page.has_title or page.h1_count != 1:
        errors.append(f'{page.path}: expected language, title and exactly one h1')
    if file.name == 'index.html':
        suffix = file.parent.relative_to(ROOT).as_posix()
        expected = 'https://zooglass.io/' + (suffix + '/' if suffix != '.' else '')
        if page.canonical != expected or not page.description:
            errors.append(f'{page.path}: invalid canonical or missing description')
        graphs = [item for data in page.json_parts for item in data.get('@graph', [])]
        if not any(item.get('@type') == 'Person' and item.get('name') == 'Ian Sproates' for item in graphs):
            errors.append(f'{page.path}: missing creator identity')
        if not any(item.get('@type') == 'SoftwareSourceCode' and item.get('codeRepository') == 'https://github.com/sproates/zooglass' for item in graphs):
            errors.append(f'{page.path}: missing software identity')

for file, page in pages.items():
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            if url.scheme and url.scheme != 'https':
                errors.append(f'{page.path}: non-HTTPS external link {link}')
            continue
        target = (ROOT / unquote(url.path).lstrip('/')) if url.path.startswith('/') else file.parent / unquote(url.path)
        if not url.path:
            target = file
        if target.is_dir():
            target /= 'index.html'
        target = target.resolve()
        if not target.is_relative_to(ROOT.resolve()) or not target.is_file():
            errors.append(f'{page.path}: missing local target {link}')
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            errors.append(f'{page.path}: missing fragment {link}')

sitemap = ET.parse(ROOT / 'sitemap.xml')
urls = {node.text for node in sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
expected_urls = {page.canonical for page in pages.values() if page.canonical}
if urls != expected_urls:
    errors.append('Sitemap does not match canonical pages')
if (ROOT / 'CNAME').read_text().strip() != 'zooglass.io':
    errors.append('Incorrect custom domain')
if 'Sitemap: https://zooglass.io/sitemap.xml' not in (ROOT / 'robots.txt').read_text():
    errors.append('Missing sitemap in robots.txt')

if errors:
    raise SystemExit('\n'.join(errors))
print(f'Passed: {len(pages)} HTML pages, local links and anchors, metadata, structured data, sitemap and domain.')
print('Browser layout and external destinations require separate verification.')
