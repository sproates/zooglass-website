"""Build Folio with canonical URLs for its intended host."""
import argparse
from hashlib import sha256
from pathlib import Path
from shutil import copyfile
from xml.etree import ElementTree as XML

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
PAGES = {
    "index.html": "Overview",
    "behaviours.html": "Behaviours",
    "architecture.html": "Architecture",
    "demonstrations.html": "Demonstrations",
    "verification.html": "Verification",
    "demonstrations-orders.html": "Orders",
    "demonstrations-sports.html": "Sports",
}


DESCRIPTIONS = {
    "demonstrations-orders.html": "Watch independent order, payment, stock and courier reports become configured ZooGlass views.",
    "demonstrations-sports.html": "Watch goal corrections and withdrawals produce different Sports views from one match feed.",
    "behaviours.html": "Configure how ZooGlass handles late events, gaps, retries, source priority, freshness, corrections and totals.",
    "verification.html": "Explore ZooGlass verification: combined reconciliation, crash recovery, returning clients and access revocation, with reproducible evidence.",
    "index.html": "ZooGlass maintains live views from independent event sources. Configure how each field handles late and duplicate events, and subscribe to the resulting view.",
    "architecture.html": "See where ZooGlass fits between event sources and applications, how events contribute to fields, and how subscribers receive snapshots and updates.",
    "demonstrations.html": "Explore Fleet, Orders and Sports screen recordings: late reports, independent sources and corrected facts through ZooGlass.",
}


def asset(source, output):
    digest = sha256(source.read_bytes()).hexdigest()[:16]
    relative = Path("assets") / f"{source.stem}.{digest}{source.suffix}"
    copyfile(source, output / relative)
    return relative.as_posix()


def render(template, values):
    for key, value in values.items():
        template = template.replace("{{" + key + "}}", value)
    return template


def build(output, base):
    (output / "assets").mkdir(parents=True, exist_ok=True)
    media = SRC / "media"
    common = {
        "share_image": base + asset(SRC / "share.png", output),
        "css": asset(SRC / "folio.css", output),
        "video": asset(media / "continuous-driving.mp4", output),
        "poster": asset(media / "continuous-driving-desktop.webp", output),
        "footer": (SRC / "footer.html").read_text(),
    }
    for demo in ("orders", "sports"):
        common[demo + "_video"] = asset(media / (demo + ".mp4"), output)
        common[demo + "_poster"] = asset(media / (demo + ".webp"), output)
    layout = (SRC / "layout.html").read_text()
    sitemap = XML.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for filename, name in PAGES.items():
        links = []
        for target, label in PAGES.items():
            if target in ("demonstrations-orders.html", "demonstrations-sports.html"):
                continue
            current = ' aria-current="page"' if target == filename or (target == "demonstrations.html" and filename.startswith("demonstrations-")) else ""
            href = "./" if target == "index.html" else target
            links.append(f'<a href="{href}"{current}>{label}</a>')
        canonical = base if filename == "index.html" else base + filename
        XML.SubElement(XML.SubElement(sitemap, "url"), "loc").text = canonical
        content = render((SRC / "pages" / filename).read_text(), common)
        page = render(layout, dict(common, content=content, navigation="\n".join(links),
                                  description=DESCRIPTIONS[filename],
                                  title="ZooGlass · Event-driven live views" if filename == "index.html" else f"{name} · ZooGlass",
                                  canonical=canonical))
        (output / filename).write_text(page)
    XML.indent(sitemap)
    XML.ElementTree(sitemap).write(output / "sitemap.xml", encoding="utf-8", xml_declaration=True)
    rule = "Allow: /" if base == "https://zooglass.io/" else "Disallow: /"
    (output / "robots.txt").write_text(f"User-agent: *\n{rule}\nSitemap: {base}sitemap.xml\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    parser.add_argument("--base", default="https://zooglass.io/")
    args = parser.parse_args()
    build(args.output, args.base.rstrip("/") + "/")
