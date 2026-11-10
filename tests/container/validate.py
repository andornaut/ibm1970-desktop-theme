"""Validate iTerm colour schemes and reject duplicate dictionary keys."""

import plistlib
import xml.etree.ElementTree as ElementTree
from pathlib import Path

files = sorted(Path(".").rglob("*.itermcolors"))
if not files:
    raise SystemExit("no .itermcolors files matched: the gate checked nothing")
for path in files:
    print(path)
    with path.open("rb") as source:
        plistlib.load(source)
    for mapping in ElementTree.parse(path).iter("dict"):
        seen = set()
        for key in mapping.findall("key"):
            if key.text in seen:
                raise SystemExit(f"{path}: duplicate key {key.text!r}")
            seen.add(key.text)
