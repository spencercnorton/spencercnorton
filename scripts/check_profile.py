#!/usr/bin/env python3
"""Check profile links locally; CI separately scans the full secret history."""
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent


def validate_links(text: str, root: Path) -> int:
    links = re.findall(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)", text)
    links += re.findall(r'(?:href|src)=["\x27]([^"\x27]+)["\x27]', text)
    if not links:
        raise ValueError("profile has no links")
    for link in links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            if url.scheme != "https" or not url.hostname or url.username or url.password:
                raise ValueError("external links must use HTTPS without credentials")
        elif url.path:
            path = (root / unquote(url.path)).resolve()
            if not path.is_relative_to(root.resolve()) or not path.is_file():
                raise ValueError("relative link does not name a repository file")
    return len(links)


if __name__ == "__main__":
    count = validate_links((ROOT / "README.md").read_text(encoding="utf-8"), ROOT)
    print(f"Profile checks passed: {count} links have valid targets and syntax.")
