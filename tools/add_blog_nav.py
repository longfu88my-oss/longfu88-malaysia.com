#!/usr/bin/env python3
"""Insert a sitewide "Blog" nav item into every root *.html page.

Positioned after the last game-vertical nav item ("Fast Games"), before
"Bonus" — matches the surrounding markup/classes exactly, in both the
desktop (`hover:text-[#C70028]`) and mobile (`py-2`) nav blocks.

Root pages use relative hrefs (e.g. `href="fast-games"`), so the Blog
link uses the site-root-absolute form `href="/blog/"` per the task spec
(verified by `grep -l 'href="/blog/"' *.html | wc -l` -> 17).
"""
from __future__ import annotations
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

DESKTOP_ANCHOR = '        <a href="fast-games" class="hover:text-[#C70028]" style="color:var(--text)">Fast Games</a>\n'
DESKTOP_INSERT = '        <a href="/blog/" class="hover:text-[#C70028]" style="color:var(--text)">Blog</a>\n'

MOBILE_ANCHOR = '        <a href="fast-games" class="py-2" style="color:var(--text)">Fast Games</a>\n'
MOBILE_INSERT = '        <a href="/blog/" class="py-2" style="color:var(--text)">Blog</a>\n'


def process(path: pathlib.Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if 'href="/blog/"' in text:
        return False  # already has it
    if DESKTOP_ANCHOR not in text or MOBILE_ANCHOR not in text:
        raise ValueError(f"{path.name}: nav anchor markup not found — unexpected nav structure")
    text = text.replace(DESKTOP_ANCHOR, DESKTOP_ANCHOR + DESKTOP_INSERT, 1)
    text = text.replace(MOBILE_ANCHOR, MOBILE_ANCHOR + MOBILE_INSERT, 1)
    path.write_text(text, encoding="utf-8")
    return True


def main() -> int:
    changed = 0
    for path in sorted(ROOT.glob("*.html")):
        if process(path):
            changed += 1
            print(f"updated {path.name}")
        else:
            print(f"skipped {path.name} (already has Blog nav)")
    print(f"done: {changed} files updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
