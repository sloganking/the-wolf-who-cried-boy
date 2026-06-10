"""Build Gumroad cover/thumbnail assets from the full-res AI cover art.

Source: side-by-side variants; we use the RIGHT one (with subtitle).
Re-run anytime: python product/make_assets.py
"""
from PIL import Image

SRC = r"C:\Users\Brioche Elm\Documents\GitHub\the-wolf-who-cried-boy\product\cover-original.png"
OUT = r"C:\Users\Brioche Elm\Documents\GitHub\the-wolf-who-cried-boy\product"

im = Image.open(SRC).convert("RGB")
w, h = im.size
print("source:", im.size)

# Right half = variant with subtitle; skip the white gutter at the seam.
right = im.crop((w // 2 + 6, 0, w, h))

# Auto-trim any near-white margins (gutter remnants / edges).
def trim_white(img, white=170, inset=4):
    """Bounding box of all DARK pixels (the navy cover), excluding any
    white border/gutter on any side, then a small safety inset."""
    gray = img.convert("L")
    mask = gray.point(lambda v: 255 if v < white else 0)
    bbox = mask.getbbox()
    l, t, r, b = bbox
    return img.crop((l + inset, t + inset, r - inset, b - inset))

right = trim_white(right)

# Verify: brightest pixel within 5px of each edge (want dark navy, < ~100)
px = right.load()
W, H = right.size
edges = {
    "left":   max(sum(px[x, y]) / 3 for x in range(5) for y in range(H)),
    "right":  max(sum(px[x, y]) / 3 for x in range(W - 5, W) for y in range(H)),
    "top":    max(sum(px[x, y]) / 3 for y in range(5) for x in range(W)),
    "bottom": max(sum(px[x, y]) / 3 for y in range(H - 5, H) for x in range(W)),
}
print("edge max brightness (want < ~100):", {k: round(v) for k, v in edges.items()})
right.save(rf"{OUT}\book-cover.png")
print("book-cover:", right.size)

# Sample navy background from inside the cover, away from edges/content
bg = right.getpixel((10, right.height - 10))
print("bg color:", bg)

def canvas(size, cover, margin=0.94):
    cw, ch = size
    c = Image.new("RGB", size, bg)
    scale = min((ch * margin) / cover.height, (cw * margin) / cover.width)
    nw, nh = round(cover.width * scale), round(cover.height * scale)
    r = cover.resize((nw, nh), Image.LANCZOS)
    c.paste(r, ((cw - nw) // 2, (ch - nh) // 2))
    return c

canvas((1280, 720), right).save(rf"{OUT}\cover.png")
canvas((600, 600), right).save(rf"{OUT}\thumbnail.png")
print("wrote cover.png (1280x720) and thumbnail.png (600x600)")
