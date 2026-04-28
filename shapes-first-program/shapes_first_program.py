from PIL import Image, ImageDraw
import math

# Simple parameters students can tweak
MIN_SIDES = 3
MAX_SIDES = 24      # try 24 for 24-corner polygons
PER_ROW = 6        # shapes per row (fixed at 6)

# Canvas/layout
CELL_W = 130
CELL_H = 180
MARGIN_X = 40
MARGIN_Y = 30
RADIUS = 48
BG = "#fff7ea"

# Base colors (used to generate lists)
FILL_LIGHT = "#f7c9c2"
FILL_DARK = "#e16044"
OUTLINE_DARK = "#2f2a2a"
OUTLINE_LIGHT = "#665c5c"


def regular_polygon(center, radius, sides, rotation_deg=-90):
    cx, cy = center
    points = []
    for i in range(sides):
        angle = math.radians(rotation_deg + (360 / sides) * i)
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        points.append((x, y))
    return points


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)


def lerp(a, b, t):
    return a + (b - a) * t


def color_gradient(start_hex, end_hex, n):
    if n <= 1:
        return [start_hex]
    s = hex_to_rgb(start_hex)
    e = hex_to_rgb(end_hex)
    colors = []
    for i in range(n):
        t = i / (n - 1)
        rgb = tuple(round(lerp(s[c], e[c], t)) for c in range(3))
        colors.append(rgb_to_hex(rgb))
    return colors


def draw_row(draw, y_center, sides_list, fills, outlines):
    for idx, sides in enumerate(sides_list):
        cx = MARGIN_X + idx * CELL_W + CELL_W / 2
        cy = y_center
        pts = regular_polygon((cx, cy), RADIUS, sides)
        draw.polygon(pts, fill=fills[idx], outline=outlines[idx], width=4)


def main():
    sides_all = list(range(MIN_SIDES, MAX_SIDES + 1))
    total = len(sides_all)
    rows = math.ceil(total / PER_ROW)

    width = MARGIN_X * 2 + CELL_W * PER_ROW
    height = MARGIN_Y * 2 + CELL_H * rows

    img = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(img)

    # Print the color lists used for each row (first program style output)
    print("Base colors:")
    print("  FILL_LIGHT:", FILL_LIGHT)
    print("  FILL_DARK:", FILL_DARK)
    print("  OUTLINE_DARK:", OUTLINE_DARK)
    print("  OUTLINE_LIGHT:", OUTLINE_LIGHT)

    for r in range(rows):
        start = r * PER_ROW
        end = min(start + PER_ROW, total)
        row_sides = sides_all[start:end]
        n = len(row_sides)

        # Row color direction
        if r % 2 == 0:
            # Row 1 pattern: light->dark fill, dark->light outline
            fills = color_gradient(FILL_LIGHT, FILL_DARK, n)
            outlines = color_gradient(OUTLINE_DARK, OUTLINE_LIGHT, n)
        else:
            # Row 2 pattern: dark->light fill, light->dark outline
            fills = color_gradient(FILL_DARK, FILL_LIGHT, n)
            outlines = color_gradient(OUTLINE_LIGHT, OUTLINE_DARK, n)

        print(f"Row {r + 1} fill colors:", fills)
        print(f"Row {r + 1} outline colors:", outlines)

        y_center = MARGIN_Y + CELL_H / 2 + r * CELL_H
        draw_row(draw, y_center, row_sides, fills, outlines)

    img.save("shapes_first_program.png")
    print("Saved shapes_first_program.png")


if __name__ == "__main__":
    main()
