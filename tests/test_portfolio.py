"""Lightweight portfolio integrity checks; uses only the Python standard library."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PortfolioParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.fragment_links = []
        self.local_assets = []
        self.unsafe_external_links = []
        self.h1_count = 0
        self.images_without_alt = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "h1":
            self.h1_count += 1
        if tag == "a":
            href = attrs.get("href", "")
            if href.startswith("#"):
                self.fragment_links.append(href[1:])
            if attrs.get("target") == "_blank":
                rel = set(attrs.get("rel", "").split())
                if not {"noopener", "noreferrer"}.issubset(rel):
                    self.unsafe_external_links.append(href)
        if tag == "img" and not attrs.get("alt"):
            self.images_without_alt.append(attrs.get("src"))
        for attr in ("src", "href"):
            value = attrs.get(attr, "")
            if value.startswith("assets/"):
                self.local_assets.append(value)


class PortfolioChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.css = (ROOT / "style.css").read_text(encoding="utf-8")
        cls.page = PortfolioParser()
        cls.page.feed(cls.html)

    def test_one_main_heading(self):
        self.assertEqual(self.page.h1_count, 1)

    def test_no_duplicate_ids(self):
        self.assertEqual(len(self.page.ids), len(set(self.page.ids)))

    def test_navigation_targets_exist(self):
        self.assertFalse(set(self.page.fragment_links) - set(self.page.ids))

    def test_local_project_images_exist(self):
        self.assertTrue(self.page.local_assets)
        for path in self.page.local_assets:
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).is_file(), path)

    def test_images_have_alt_text(self):
        self.assertFalse(self.page.images_without_alt)

    def test_external_links_are_safe(self):
        self.assertFalse(self.page.unsafe_external_links)

    def test_page_metadata(self):
        self.assertRegex(self.html, r'<meta name="description"')
        self.assertRegex(self.html, r'<meta name="viewport"')

    def test_mobile_anchor_offset_accounts_for_sticky_navigation(self):
        # The mobile navigation wraps to two rows; anchor targets must not hide behind it.
        self.assertRegex(self.css, r"@media\s*\(max-width:\s*620px\)\s*\{[\s\S]*?scroll-padding-top:\s*135px")
        for section_id in ("home", "about", "skills", "projects", "contact"):
            self.assertIn("#" + section_id, self.css)
        self.assertIn("scroll-margin-top: 135px", self.css)

    def test_responsive_and_reduced_motion_styles(self):
        self.assertIn("@media(max-width:620px)", self.css)
        self.assertIn("prefers-reduced-motion:reduce", self.css)


if __name__ == "__main__":
    unittest.main()
