#!/usr/bin/env python3
"""Import a WordPress WXR export into Astro Markdown posts + public uploads."""

from __future__ import annotations

import html
import re
import urllib.parse
import urllib.request
from pathlib import Path
from xml.etree import ElementTree as ET

from bs4 import BeautifulSoup
from markdownify import markdownify as html_to_md

ROOT = Path(__file__).resolve().parents[1]
EXPORT = Path("/Users/joan/Downloads/joan039stechstuff.WordPress.2026-07-27.xml")
BLOG_DIR = ROOT / "src" / "content" / "blog"
PUBLIC_DIR = ROOT / "public"
UPLOADS_DIR = PUBLIC_DIR / "uploads"
ABOUT_OUT = ROOT / "src" / "pages" / "about.md"

NS = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "excerpt": "http://wordpress.org/export/1.2/excerpt/",
    "wp": "http://wordpress.org/export/1.2/",
    "dc": "http://purl.org/dc/elements/1.1/",
}

NON_ASCII_SLUG_RE = re.compile(r"[^a-z0-9-]+")


def clean_slug(raw: str, title: str) -> str:
    # Prefer decoded post_name with leading emoji/symbols stripped.
    decoded = urllib.parse.unquote(raw or "").strip().lower()
    decoded = re.sub(r"^[^a-z0-9]+", "", decoded)
    decoded = NON_ASCII_SLUG_RE.sub("-", decoded)
    decoded = re.sub(r"-+", "-", decoded).strip("-")
    if decoded:
        return decoded
    fallback = NON_ASCII_SLUG_RE.sub("-", title.lower())
    return re.sub(r"-+", "-", fallback).strip("-") or "post"


def yaml_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def strip_wp_comments(html_body: str) -> str:
    return re.sub(r"<!--\s*/?wp:.*?-->", "", html_body, flags=re.DOTALL)


def rewrite_image_urls(html_body: str, url_map: dict[str, str]) -> str:
    soup = BeautifulSoup(html_body, "html.parser")
    for img in soup.find_all("img"):
        src = img.get("src")
        if not src:
            continue
        # Drop size suffixes WordPress inserts: foo-1024x768.png -> foo.png
        candidates = [src]
        bare = re.sub(r"-\d+x\d+(?=\.(?:png|jpe?g|webp|gif)$)", "", src, flags=re.I)
        if bare != src:
            candidates.append(bare)
        for candidate in candidates:
            if candidate in url_map:
                img["src"] = url_map[candidate]
                break
            # Also match without querystring
            base = candidate.split("?")[0]
            if base in url_map:
                img["src"] = url_map[base]
                break
        for attr in ("srcset", "sizes", "data-src", "data-srcset"):
            if attr in img.attrs:
                del img.attrs[attr]
    # Unwrap WordPress figure blocks that are just images
    return str(soup)


def description_from(excerpt: str, html_body: str, title: str) -> str:
    text = BeautifulSoup(excerpt or html_body or "", "html.parser").get_text(" ", strip=True)
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return title
    return text[:180] + ("…" if len(text) > 180 else "")


def download(url: str, dest: Path) -> bool:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 0:
        return True
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "joanfihu-migration/1.0"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            dest.write_bytes(resp.read())
        print(f"  downloaded {dest.relative_to(ROOT)}")
        return True
    except Exception as exc:  # noqa: BLE001
        print(f"  FAILED {url}: {exc}")
        return False


def local_upload_path(attachment_url: str) -> Path:
    parsed = urllib.parse.urlparse(attachment_url)
    # Keep /wp-content/uploads/YYYY/MM/file under public/uploads/YYYY/MM/file
    parts = Path(parsed.path).parts
    if "uploads" in parts:
        idx = parts.index("uploads")
        rel = Path(*parts[idx + 1 :])
    else:
        rel = Path(Path(parsed.path).name)
    return UPLOADS_DIR / rel


def main() -> None:
    tree = ET.parse(EXPORT)
    channel = tree.getroot().find("channel")
    assert channel is not None

    # Remove starter posts
    if BLOG_DIR.exists():
        for path in BLOG_DIR.glob("*"):
            if path.is_file():
                path.unlink()
    BLOG_DIR.mkdir(parents=True, exist_ok=True)
    UPLOADS_DIR.mkdir(parents=True, exist_ok=True)

    url_map: dict[str, str] = {}
    for item in channel.findall("item"):
        if item.findtext("wp:post_type", default="", namespaces=NS) != "attachment":
            continue
        url = item.findtext("wp:attachment_url", default="", namespaces=NS)
        if not url:
            continue
        dest = local_upload_path(url)
        if download(url, dest):
            public_url = "/" + str(dest.relative_to(PUBLIC_DIR)).replace("\\", "/")
            url_map[url] = public_url
            url_map[url.split("?")[0]] = public_url

    posts_written = 0
    for item in channel.findall("item"):
        post_type = item.findtext("wp:post_type", default="", namespaces=NS)
        status = item.findtext("wp:status", default="", namespaces=NS)
        title = html.unescape(item.findtext("title") or "").strip()
        raw_slug = item.findtext("wp:post_name", default="", namespaces=NS) or ""
        date = (item.findtext("wp:post_date", default="", namespaces=NS) or "")[:10]
        content = item.findtext("content:encoded", default="", namespaces=NS) or ""
        excerpt = item.findtext("excerpt:encoded", default="", namespaces=NS) or ""

        if post_type == "page" and status == "publish" and clean_slug(raw_slug, title) == "about":
            html_body = rewrite_image_urls(strip_wp_comments(content), url_map)
            md = html_to_md(html_body, heading_style="ATX", bullets="-").strip() + "\n"
            about_astro = ROOT / "src" / "pages" / "about-content.md"
            about_astro.write_text(md, encoding="utf-8")
            # Keep a simple marker file for the importer; about.astro will embed content.
            (ROOT / "src" / "content" / "about.md").parent.mkdir(parents=True, exist_ok=True)
            (ROOT / "src" / "content" / "about.md").write_text(
                f'---\ntitle: "About"\ndescription: "About Joan"\n---\n\n{md}',
                encoding="utf-8",
            )
            print(f"wrote about page ({len(md)} chars)")
            continue

        if post_type != "post" or status != "publish":
            continue

        slug = clean_slug(raw_slug, title)
        html_body = rewrite_image_urls(strip_wp_comments(content), url_map)
        md_body = html_to_md(html_body, heading_style="ATX", bullets="-").strip()
        # Collapse excessive blank lines from WP markup
        md_body = re.sub(r"\n{3,}", "\n\n", md_body)
        desc = description_from(excerpt, content, title)
        # Parse date for Astro frontmatter format
        try:
            y, m, d = date.split("-")
            months = [
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun",
                "Jul",
                "Aug",
                "Sep",
                "Oct",
                "Nov",
                "Dec",
            ]
            pub = f"{months[int(m) - 1]} {int(d)} {y}"
        except Exception:  # noqa: BLE001
            pub = date

        frontmatter = (
            "---\n"
            f'title: "{yaml_escape(title)}"\n'
            f'description: "{yaml_escape(desc)}"\n'
            f"pubDate: '{pub}'\n"
            "---\n\n"
        )
        out = BLOG_DIR / f"{slug}.md"
        out.write_text(frontmatter + md_body + "\n", encoding="utf-8")
        posts_written += 1
        print(f"wrote {out.name}")

    print(f"\nDone: {posts_written} posts, {len(url_map) // 2} images mapped")


if __name__ == "__main__":
    main()
