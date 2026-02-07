# digit-examples

Small, beginner-friendly Python examples using PIL and Matplotlib.

## 1) Ball throw trajectories (Matplotlib)

- File: `trajectory_plot.py`
- Draws 10 projectile trajectories with varying angle and speed (km/h)
- Uses `g = 9.8 m/s²`, `t = 0–10 s`, horizontal range `0–100 m`

Run:
```bash
python3 ./trajectory_plot.py
```

Output:
- `trajectory_plot.png`

## 2) Polygon row patterns (PIL)

- File: `shapes_first_program.py`
- Draws regular polygons from `MIN_SIDES` to `MAX_SIDES`
- 6 shapes per row, auto-adds rows
- Alternates row color direction

Run:
```bash
python3 ./shapes_first_program.py
```

Output:
- `shapes_first_program.png`

## Requirements

```bash
python3 -m pip install matplotlib numpy pillow
```
