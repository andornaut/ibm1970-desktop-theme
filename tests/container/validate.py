"""Validate iTerm colour schemes and reject duplicate dictionary keys."""

import plistlib
from pathlib import Path


class UniqueDictionary(dict):
    def __setitem__(self, key, value):
        if key in self:
            raise SystemExit(f"{path}: duplicate key {key!r}")
        super().__setitem__(key, value)


files = sorted(Path().rglob("*.itermcolors"))
if not files:
    raise SystemExit("no .itermcolors files matched: the gate checked nothing")
for path in files:
    print(path)
    with path.open("rb") as source:
        plistlib.load(source, fmt=plistlib.FMT_XML, dict_type=UniqueDictionary)
