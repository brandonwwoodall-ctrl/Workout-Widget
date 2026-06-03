#!/usr/bin/env python3
"""
Embed an Atlas badge image into workout_widget.html.

  # Option A — use an image you already have (only needs Pillow):
  pip install pillow
  python generate_atlas.py --file atlas_badge.png

  # Option B — generate a new one via DALL-E 3:
  pip install pillow openai
  export OPENAI_API_KEY=sk-...
  python generate_atlas.py
"""

import argparse, base64, io, os, re, sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    sys.exit("Install Pillow first:  pip install pillow")

HTML_FILE = Path(__file__).parent / "workout_widget.html"

PROMPT = (
    "Boris Vallejo fantasy art style. Massively muscular Atlas kneeling on a jagged rocky cliff, "
    "straining upward with both arms raised overhead, pushing a colossal glowing Earth planet "
    "that fills the entire sky above him. Dramatic top-down blue-cyan light from the planet "
    "illuminates his ripped glistening bronze body. Deep cool purple-blue shadows. Long flowing "
    "golden hair. Chiseled jaw clenched in heroic effort. Dark cosmic space background with "
    "swirling nebula clouds and tiny distant stars. Hyperrealistic oil painting, epic fantasy "
    "illustration, cinematic lighting, dynamic vertical composition."
)

# DALL-E 3 supports: 1024x1024, 1792x1024, 1024x1792
DALLE_SIZE = "1024x1792"   # tall portrait — best for the kneeling pose
OUTPUT_W, OUTPUT_H = 420, 520  # resized for the badge card


def generate(prompt: str) -> bytes:
    try:
        from openai import OpenAI
    except ImportError:
        sys.exit("Install the OpenAI package first:  pip install openai")
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        sys.exit(
            "No OPENAI_API_KEY found.\n"
            "Set it with:  export OPENAI_API_KEY=sk-..."
        )
    client = OpenAI(api_key=api_key)
    print("Requesting image from OpenAI DALL-E 3…")
    print(f"  prompt: {prompt[:90]}…")
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size=DALLE_SIZE,
        quality="hd",
        response_format="b64_json",
        n=1,
    )
    raw = base64.b64decode(response.data[0].b64_json)
    print(f"  ✓ Received {len(raw):,} bytes")
    return raw


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
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="Path to an existing image file to embed")
    args = parser.parse_args()

    if args.file:
        raw = Path(args.file).read_bytes()
        print(f"Using local file: {args.file} ({len(raw):,} bytes)")
    else:
        raw = generate(PROMPT)
    print("Processing image…")
    data_url = process(raw, OUTPUT_W, OUTPUT_H)
    print(f"  ✓ Base64 length: {len(data_url):,} chars")

    html = HTML_FILE.read_text(encoding="utf-8")
    html = embed(html, data_url, OUTPUT_W, OUTPUT_H)
    HTML_FILE.write_text(html, encoding="utf-8")
    print(f"  ✓ Embedded into {HTML_FILE.name}")
    print("\nDone! Open workout_widget.html to see the Atlas badge.")
