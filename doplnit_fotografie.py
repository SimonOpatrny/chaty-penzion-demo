#!/usr/bin/env python3
"""Doplni opravdove fotografie Pexels do assets/images (bez externich balicku)."""
from pathlib import Path
from urllib.request import urlopen, Request
from zipfile import ZipFile
from io import BytesIO

LINK = "https://d2ol7oe51mr4n9.cloudfront.net/user_3J45Owuse1C9720cvhhjpt14vdZ/3263a7fe-d2d7-4d4a-b057-57c46791b454.zip"
ROOT = Path(__file__).resolve().parent
DEST = ROOT / "assets" / "images"
DEST.mkdir(parents=True, exist_ok=True)
print("Stahuji 28 fotografii WebP...")
with urlopen(Request(LINK,headers={"User-Agent":"Mozilla/5.0"}),timeout=60) as response:
    payload=response.read()
with ZipFile(BytesIO(payload)) as z:
    for name in z.namelist():
        if name.endswith(".webp"):
            (DEST / Path(name).name).write_bytes(z.read(name))
        elif name == "FOTO-ZDROJE.txt":
            (ROOT / name).write_bytes(z.read(name))
print("Hotovo:",len(list(DEST.glob("*.webp"))),"fotografii. Nyni lze otevrit index.html nebo nahrat projekt na GitHub Pages.")
