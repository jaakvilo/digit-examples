from PIL import Image, ImageDraw
import argparse
import random

# Defaults
DEFAULT_WIDTH = 2048
DEFAULT_HEIGHT = 1600
DEFAULT_COLS = 20
DEFAULT_ROWS = 16
DEFAULT_MARGIN = 64
DEFAULT_BG = "#f9f6f0"

# Line style range
LIGHT = (210, 210, 210)  # light gray
DARK = (60, 60, 60)      # dark gray
THIN = 1
THICK = 6


def lerp(a, b, t):
    return a + (b - a) * t


def color_at(t):
    return tuple(int(lerp(LIGHT[i], DARK[i], t)) for i in range(3))


def main():
    parser = argparse.ArgumentParser(description="Draw a grid of lighter->darker, thinner->thicker lines.")
    parser.add_argument("--width", type=int, default=DEFAULT_WIDTH, help="Image width in pixels")
    parser.add_argument("--height", type=int, default=DEFAULT_HEIGHT, help="Image height in pixels")
    parser.add_argument("--cols", type=int, default=DEFAULT_COLS, help="Number of vertical grid cells")
    parser.add_argument("--rows", type=int, default=DEFAULT_ROWS, help="Number of horizontal grid cells")
    parser.add_argument("--margin", type=int, default=DEFAULT_MARGIN, help="Outer margin in pixels")
    parser.add_argument("--bg", default=DEFAULT_BG, help="Background color")
    parser.add_argument("--out", default="grid_lines.png", help="Output filename")
    parser.add_argument("--seed", type=int, default=None, help="Random seed for pastel colors")
    args = parser.parse_args()

    width = args.width
    height = args.height
    cols = args.cols
    rows = args.rows
    margin = args.margin

    cell_w = (width - margin * 2) / max(1, cols)
    cell_h = (height - margin * 2) / max(1, rows)

    if args.seed is not None:
        random.seed(args.seed)

    img = Image.new("RGB", (width, height), args.bg)
    draw = ImageDraw.Draw(img)

    # Fill cells with random pastel colors
    for r in range(rows):
        for c in range(cols):
            # Pastel color: high base + small random variation
            color = tuple(random.randint(180, 245) for _ in range(3))
            x0 = margin + c * cell_w
            y0 = margin + r * cell_h
            x1 = margin + (c + 1) * cell_w
            y1 = margin + (r + 1) * cell_h
            draw.rectangle([x0, y0, x1, y1], fill=color)

    # Vertical lines
    for i in range(cols + 1):
        t = i / max(1, cols)
        color = color_at(t)
        w = int(round(lerp(THIN, THICK, t)))
        x = margin + i * cell_w
        draw.line([(x, margin), (x, height - margin)], fill=color, width=w)

    # Horizontal lines
    for j in range(rows + 1):
        t = j / max(1, rows)
        color = color_at(t)
        w = int(round(lerp(THIN, THICK, t)))
        y = margin + j * cell_h
        draw.line([(margin, y), (width - margin, y)], fill=color, width=w)

    img.save(args.out)
    print(f"Saved {args.out}")


if __name__ == "__main__":
    main()
