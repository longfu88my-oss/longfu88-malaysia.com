import sys, pathlib, json, importlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import pytest
from jinja2 import Environment, FileSystemLoader, StrictUndefined, UndefinedError

bb = importlib.import_module("build_blog")
FIX = pathlib.Path(__file__).parent / "fixtures" / "sample-post.md"

def _env():
    return Environment(loader=FileSystemLoader(str(bb.TEMPLATE_DIR)),
                       undefined=StrictUndefined, autoescape=False)

def test_load_post_parses_frontmatter_and_body():
    post = bb.load_post(FIX)
    assert post["slug"] == "sample-post"
    assert post["primary_keyword"] == "sample keyword Malaysia"
    assert "<h2" in post["body_html"] and "First heading" in post["body_html"]

def test_load_post_missing_field_raises(tmp_path):
    bad = tmp_path / "bad.md"
    bad.write_text("---\nslug: x\n---\nbody\n", encoding="utf-8")
    with pytest.raises(ValueError):
        bb.load_post(bad)

def test_build_jsonld_valid_and_typed():
    post = bb.load_post(FIX)
    html = bb.build_jsonld(post)
    import re
    blocks = re.findall(r'<script type="application/ld\+json">\n(.*?)\n</script>', html, re.S)
    types = {json.loads(b)["@type"] for b in blocks}
    assert {"BlogPosting", "BreadcrumbList", "FAQPage"} <= types
    faq = [json.loads(b) for b in blocks if json.loads(b)["@type"] == "FAQPage"][0]
    assert len(faq["mainEntity"]) == 1
    assert faq["mainEntity"][0]["acceptedAnswer"]["text"] == "Yes, this is a sample answer."

def test_jsonld_uses_clean_url():
    post = bb.load_post(FIX)
    html = bb.build_jsonld(post)
    assert "longfu88-malaysia.com/blog/sample-post" in html
    assert "sample-post.html" not in html

def test_render_post_no_unfilled_placeholders():
    post = bb.load_post(FIX)
    out = bb.render_post(post, _env())
    assert "{{" not in out and "{%" not in out
    assert "Lucas Chong" in out
    assert 'href="https://ln88--longfu88.com/ms/fast-registration"' in out
    assert 'rel="canonical" href="https://longfu88-malaysia.com/blog/sample-post"' in out

def test_strictundefined_raises_on_missing_var():
    # guarantees the anti-placeholder-leak property: a missing var fails the build
    env = Environment(undefined=StrictUndefined, autoescape=False)
    tpl = env.from_string("Hello {{ missing_var }}")
    with pytest.raises(UndefinedError):
        tpl.render()

def test_html_escaping_onpage_vs_jsonld(tmp_path):
    md = tmp_path / "amp.md"
    md.write_text(
        '---\n'
        'slug: amp-post\n'
        'title: "Odds & Ends at Longfu88 Malaysia"\n'
        'meta_description: "Odds & Ends explained for Malaysia."\n'
        'category: Games\n'
        'primary_keyword: "odds and ends Malaysia"\n'
        'date_published: 2026-07-25\n'
        'date_modified: 2026-07-25\n'
        'faq:\n'
        '  - q: "What are odds & ends?"\n'
        '    a: "Bits & pieces."\n'
        '---\n\n'
        '## Body\n\nText.\n',
        encoding="utf-8")
    out = bb.render_post(bb.load_post(md), _env())
    # on-page: ampersand escaped in the <title> element
    assert "Odds &amp; Ends at Longfu88 Malaysia" in out
    # JSON-LD: raw ampersand preserved inside the BlogPosting headline
    assert '"headline": "Odds & Ends at Longfu88 Malaysia"' in out
