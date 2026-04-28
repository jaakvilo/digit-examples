# digit-examples

Small, beginner-friendly Python examples using PIL and Matplotlib.

Each mini-project lives in its own folder. This keeps the repository easy to
copy as a static website and easy to clone as a collection of runnable examples.

## Examples

| Example | Folder | What it shows |
| --- | --- | --- |
| Ball throw trajectories | `trajectory-plot/` | Matplotlib projectile trajectories with varying angle and speed |
| Polygon row patterns | `shapes-first-program/` | PIL regular polygons, gradients, rows, and generated image output |
| Grid lines | `grid-lines/` | PIL grid drawing with pastel cells and line thickness/color gradients |

Open `index.html` in a browser to browse the examples locally. The same file can
also be used as the website entry point when publishing the repository.

## Running Examples

Install the Python dependencies:

```bash
python3 -m pip install matplotlib numpy pillow
```

Run an example from its folder:

```bash
cd trajectory-plot
python3 ./trajectory_plot.py
```

```bash
cd shapes-first-program
python3 ./shapes_first_program.py
```

```bash
cd grid-lines
python3 ./grid_lines.py
```

## Adding A New Example

1. Create a new folder with a short URL-friendly name, such as
   `my-new-example/`.
2. Put the script, generated output, and a small `index.html` inside that folder.
3. Add the new folder to the examples list in the top-level `index.html`.
4. Add a row to the examples table in this README.
