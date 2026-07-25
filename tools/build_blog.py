#!/usr/bin/env python3
"""Static blog generator for longfu88-malaysia.com."""
from __future__ import annotations
import json, pathlib, sys
import yaml, markdown
from jinja2 import Environment, FileSystemLoader, StrictUndefined

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "tools" / "blog-content"
BLOG_DIR = ROOT / "blog"
TEMPLATE_DIR = ROOT / "tools"
SITE = "https://longfu88-malaysia.com"
ORG_NAME = "Longfu88 Malaysia"
AUTHOR = "Lucas Chong"
ABOUT_URL = f"{SITE}/about-us"
CTA = "https://ln88--longfu88.com/ms/fast-registration"
OG_DEFAULT = f"{SITE}/assets/img/og-default.jpg"
REQUIRED = ["slug", "title", "meta_description", "category",
            "primary_keyword", "date_published", "date_modified", "faq"]

def load_post(path: pathlib.Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---"):
        raise ValueError(f"{path.name}: missing YAML front-matter")
    _, fm, body = raw.split("---", 2)
    meta = yaml.safe_load(fm) or {}
    missing = [k for k in REQUIRED if k not in meta or meta[k] in (None, "")]
    if missing:
        raise ValueError(f"{path.name}: missing front-matter fields: {missing}")
    meta.setdefault("tier1_links", [])
    meta.setdefault("related", [])
    meta["body_html"] = markdown.markdown(
        body.strip(), extensions=["extra", "sane_lists", "toc"])
    meta["url"] = f"{SITE}/blog/{meta['slug']}"
    meta["hero_abs"] = meta.get("hero_image") and (
        meta["hero_image"] if meta["hero_image"].startswith("http")
        else SITE + meta["hero_image"]) or OG_DEFAULT
    return meta

def _iso(d) -> str:
    return d.isoformat() if hasattr(d, "isoformat") else str(d)

def build_jsonld(post: dict) -> str:
    url = post["url"]
    blocks = [
        {"@context": "https://schema.org", "@type": "BlogPosting",
         "@id": f"{url}#article", "headline": post["title"],
         "description": post["meta_description"],
         "datePublished": _iso(post["date_published"]),
         "dateModified": _iso(post["date_modified"]),
         "inLanguage": "en-MY", "image": post["hero_abs"],
         "mainEntityOfPage": {"@type": "WebPage", "@id": url},
         "author": {"@type": "Person", "name": AUTHOR, "url": ABOUT_URL},
         "publisher": {"@type": "Organization", "name": ORG_NAME,
                       "logo": {"@type": "ImageObject",
                                "url": f"{SITE}/assets/img/logo.png"}}},
        {"@context": "https://schema.org", "@type": "BreadcrumbList",
         "itemListElement": [
             {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
             {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{SITE}/blog/"},
             {"@type": "ListItem", "position": 3, "name": post["title"], "item": url}]},
        {"@context": "https://schema.org", "@type": "FAQPage",
         "mainEntity": [
             {"@type": "Question", "name": q["q"],
              "acceptedAnswer": {"@type": "Answer", "text": q["a"]}}
             for q in post["faq"]]},
    ]
    def _dump(b):
        # Escape "</" so a field value containing "</script>" (or any "</")
        # cannot prematurely close the enclosing <script> block. "\/" is a
        # valid JSON escape for "/", so json.loads still parses this fine.
        return json.dumps(b, ensure_ascii=False, indent=2).replace("</", "<\\/")

    return "\n".join(
        f'<script type="application/ld+json">\n{_dump(b)}\n</script>'
        for b in blocks)

def _env() -> Environment:
    return Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)),
                       undefined=StrictUndefined, autoescape=False)

def render_post(post: dict, env: Environment) -> str:
    tpl = env.get_template("blog-template.html.j2")
    return tpl.render(post=post, jsonld=build_jsonld(post),
                      author=AUTHOR, about_url=ABOUT_URL, cta=CTA, site=SITE)

def render_index(posts: list[dict], env: Environment) -> str:
    tpl = env.get_template("blog-index-template.html.j2")
    ordered = sorted(posts, key=lambda p: _iso(p["date_published"]), reverse=True)
    return tpl.render(posts=ordered, site=SITE, cta=CTA,
                      canonical=f"{SITE}/blog/")

def main() -> int:
    env = _env()
    BLOG_DIR.mkdir(exist_ok=True)
    posts = [load_post(p) for p in sorted(CONTENT_DIR.glob("*.md"))]
    for post in posts:
        (BLOG_DIR / f"{post['slug']}.html").write_text(
            render_post(post, env), encoding="utf-8")
        print(f"built blog/{post['slug']}.html")
    (BLOG_DIR / "index.html").write_text(render_index(posts, env), encoding="utf-8")
    print(f"built blog/index.html ({len(posts)} posts)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
