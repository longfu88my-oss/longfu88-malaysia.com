#!/usr/bin/env python3
"""One-shot: strip `.html` from internal links + canonical/og/hreflang/sitemap
so metadata points at the 200 URL Cloudflare Pages actually serves (it
308-redirects /x.html -> /x). Idempotent. Does NOT touch asset paths or
non-.html files."""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://longfu88-malaysia.com"

def clean_html(text: str) -> str:
    # 1) internal page links: href="index.html" -> href="/"
    text = re.sub(r'href="index\.html"', 'href="/"', text)
    # 2) internal page links: href="bonus.html" -> href="bonus"
    text = re.sub(r'href="([a-z0-9][a-z0-9-]*)\.html"', r'href="\1"', text)
    # 3) absolute URLs (canonical/og:url/hreflang): .../bonus.html -> .../bonus
    text = re.sub(rf'({re.escape(SITE)}/)index\.html', r'\1', text)
    text = re.sub(rf'({re.escape(SITE)}/)([a-z0-9][a-z0-9-]*)\.html', r'\1\2', text)
    return text

def main():
    pages = [p for p in ROOT.glob("*.html")]
    for p in pages:
        p.write_text(clean_html(p.read_text(encoding="utf-8")), encoding="utf-8")
        print(f"cleaned {p.name}")
    # sitemap.xml: same absolute-URL rule inside <loc>
    sx = ROOT / "sitemap.xml"
    t = sx.read_text(encoding="utf-8")
    t = re.sub(rf'({re.escape(SITE)}/)index\.html', r'\1', t)
    t = re.sub(rf'({re.escape(SITE)}/)([a-z0-9][a-z0-9-]*)\.html', r'\1\2', t)
    sx.write_text(t, encoding="utf-8")
    print("cleaned sitemap.xml")

if __name__ == "__main__":
    main()
