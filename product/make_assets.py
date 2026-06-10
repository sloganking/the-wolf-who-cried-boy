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
def trim_white(img, thresh=235):
    px = img.load()
    W, H = img.size
    def col_dark(x):
        return any(sum(px[x, y]) / 3 < thresh for y in range(0, H, 8))
    def row_dark(y):
        return any(sum(px[x, y]) / 3 < thresh for x in range(0, W, 8))
    l = next(x for x in range(W) if col_dark(x))
    r = next(x for x in range(W - 1, -1, -1) if col_dark(x))
    t = next(y for y in range(H) if row_dark(y))
    b = next(y for y in range(H - 1, -1, -1) if row_dark(y))
    return img.crop((l, t, r + 1, b + 1))

right = trim_white(right)
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
