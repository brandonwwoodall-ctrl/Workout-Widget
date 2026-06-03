#!/usr/bin/env python3
"""
Run this locally to generate an AI Atlas badge image and embed it.
Requires: pip install pillow requests

Uses Pollinations.ai (free, no API key needed).
"""

import base64, io, re, sys, time
from pathlib import Path

try:
    import requests
    from PIL import Image
except ImportError:
    sys.exit("Install deps first:  pip install pillow requests")

HTML_FILE = Path(__file__).parent / "workout_widget.html"

PROMPT = (
    "Boris Vallejo fantasy art style, massively muscular Atlas kneeling on a jagged rocky cliff, "
    "straining upward with both arms raised overhead, pushing a colossal glowing Earth planet "
    "that fills the sky, dramatic top-down blue-cyan light from the planet illuminating his "
    "ripped glistening bronze body, deep shadow in cool purple-blue, long flowing golden hair, "
    "chiseled jaw clenched in heroic effort, dark cosmic space background with swirling nebula "
    "clouds, tiny distant stars, hyperrealistic oil painting, epic fantasy illustration, "
    "cinematic lighting, dynamic composition, 4k detail"
)

WIDTH, HEIGHT = 420, 520


def generate(prompt: str, w: int, h: int, retries: int = 4) -> bytes:
    import urllib.parse
    encoded = urllib.parse.quote(prompt)
    url = (
        f"https://image.pollinations.ai/prompt/{encoded}"
        f"?width={w}&height={h}&nologo=true&model=flux&seed=42"
    )
    print(f"Requesting image from Pollinations.ai (Flux model)…")
    print(f"  prompt: {prompt[:80]}…")
    for attempt in range(1, retries + 1):
        try:
            r = requests.get(url, timeout=90, headers={"User-Agent": "Mozilla/5.0"})
            if r.status_code == 200 and r.content[:3] in (b'\xff\xd8\xff', b'\x89PN', b'GIF'):
                print(f"  ✓ Downloaded {len(r.content):,} bytes")
                return r.content
            print(f"  attempt {attempt} → HTTP {r.status_code}, retrying…")
        except Exception as e:
            print(f"  attempt {attempt} error: {e}")
        time.sleep(3 * attempt)
    sys.exit("Failed to download image after retries.")


def process(raw: bytes, w: int, h: int) -> str:
    img = Image.open(io.BytesIO(raw)).convert("RGB")
    img = img.resize((w, h), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=72, optimize=True)
    b64 = base64.b64encode(buf.getvalue()).decode()
    return f"data:image/jpeg;base64,{b64}"


def embed(html: str, data_url: str, w: int, h: int) -> str:
    svg = (
        f'<svg viewBox="0 0 {w} {h}" style="width:100%;height:auto;display:block" '
        f'xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">'
        f'<image href="{data_url}" x="0" y="0" width="{w}" height="{h}" '
        f'preserveAspectRatio="xMidYMid slice"/>'
        # gradient overlay so the text at bottom reads clearly
        f'<defs><linearGradient id="ato_g" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="55%" stop-color="#000" stop-opacity="0"/>'
        f'<stop offset="100%" stop-color="#000" stop-opacity="0.88"/>'
        f'</linearGradient></defs>'
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="url(#ato_g)"/>'
        f'</svg>'
    )
    pattern = r'var ATLAS_SVG=`[^`]*`'
    if not re.search(pattern, html):
        sys.exit("Could not find ATLAS_SVG in HTML — has the file been patched?")
    return re.sub(pattern, f'var ATLAS_SVG=`{svg}`', html)


if __name__ == "__main__":
    raw = generate(PROMPT, WIDTH, HEIGHT)
    print("Processing image…")
    data_url = process(raw, WIDTH, HEIGHT)
    print(f"  ✓ Base64 length: {len(data_url):,} chars")

    html = HTML_FILE.read_text(encoding="utf-8")
    html = embed(html, data_url, WIDTH, HEIGHT)
    HTML_FILE.write_text(html, encoding="utf-8")
    print(f"  ✓ Embedded into {HTML_FILE.name}")
    print("\nDone! Open workout_widget.html to see the Atlas badge.")
