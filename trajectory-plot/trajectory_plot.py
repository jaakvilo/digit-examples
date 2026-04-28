import math
import matplotlib.pyplot as plt
import numpy as np

G = 9.8
T_MAX = 10.0
X_MAX = 100.0
Y_MAX = 30.0

THROWS = [
    (20, 45),
    (25, 55),
    (30, 62),
    (35, 70),
    (40, 78),
    (45, 85),
    (50, 92),
    (55, 98),
    (60, 105),
    (65, 112),
]


def kmh_to_ms(kmh):
    return kmh / 3.6


def trajectory(angle_deg, speed_kmh, steps=200):
    v = kmh_to_ms(speed_kmh)
    theta = math.radians(angle_deg)
    vx = v * math.cos(theta)
    vy = v * math.sin(theta)

    t = np.linspace(0, T_MAX, steps)
    x = vx * t
    y = vy * t - 0.5 * G * t * t

    # Keep within 0..X_MAX and y>=0
    mask = (x <= X_MAX) & (y >= 0)
    if not np.any(mask):
        return np.array([]), np.array([])

    x = x[mask]
    y = y[mask]

    # Ensure we end on the ground if it crosses below 0
    if len(y) > 0 and y[-1] > 0:
        # nothing to adjust
        pass
    return x, y


def main():
    speeds = [s for _, s in THROWS]
    s_min, s_max = min(speeds), max(speeds)

    cmap = plt.cm.get_cmap("viridis")

    fig, ax = plt.subplots(figsize=(9, 5.2))
    ax.set_facecolor("#fffaf0")
    fig.patch.set_facecolor("#f7f4ee")

    for angle, speed in THROWS:
        x, y = trajectory(angle, speed)
        if x.size == 0:
            continue
        t = (speed - s_min) / (s_max - s_min)
        color = cmap(0.15 + 0.75 * t)
        ax.plot(x, y, color=color, linewidth=2.5, label=f"{angle}° @ {speed} km/h")

    ax.set_xlim(0, X_MAX)
    ax.set_ylim(0, Y_MAX)
    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Height (m)")
    ax.set_title("10 Trajectories for Ball Throws")
    ax.grid(True, color="#e3ddcf")

    # Legend in two columns for readability
    ax.legend(ncol=2, fontsize=8, frameon=False, loc="upper right")

    plt.tight_layout()
    plt.savefig("trajectory_plot.png", dpi=160)
    plt.show()


if __name__ == "__main__":
    main()
