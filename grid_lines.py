from PIL import Image, ImageDraw

# Simple parameters
COLS = 10  # vertical grid cells
ROWS = 6   # horizontal grid cells
CELL_SIZE = 80
MARGIN = 40
BG = "#f9f6f0"

# Line style range
LIGHT = (210, 210, 210)  # light gray
DARK = (60, 60, 60)      # dark gray
THIN = 1
THICK = 5


def lerp(a, b, t):
    return a + (b - a) * t


def color_at(t):
    return tuple(int(lerp(LIGHT[i], DARK[i], t)) for i in range(3))


def main():
    width = MARGIN * 2 + COLS * CELL_SIZE
    height = MARGIN * 2 + ROWS * CELL_SIZE

    img = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(img)

    # Vertical lines
    for i in range(COLS + 1):
        t = i / max(1, COLS)
        color = color_at(t)
        w = int(round(lerp(THIN, THICK, t)))
        x = MARGIN + i * CELL_SIZE
        draw.line([(x, MARGIN), (x, height - MARGIN)], fill=color, width=w)

    # Horizontal lines
    for j in range(ROWS + 1):
        t = j / max(1, ROWS)
        color = color_at(t)
        w = int(round(lerp(THIN, THICK, t)))
        y = MARGIN + j * CELL_SIZE
        draw.line([(MARGIN, y), (width - MARGIN, y)], fill=color, width=w)

    img.save("grid_lines.png")
    print("Saved grid_lines.png")


if __name__ == "__main__":
    main()
