from manim import *
import numpy as np


def compute_lorenz(steps=12000, dt=0.005):
    sigma, rho, beta = 10, 28, 8/3
    xs, ys, zs = [0.1], [0.0], [0.0]
    for _ in range(steps):
        x, y, z = xs[-1], ys[-1], zs[-1]
        xs.append(x + sigma*(y-x)*dt)
        ys.append(y + (x*(rho-z)-y)*dt)
        zs.append(z + (x*y-beta*z)*dt)
    pts = np.array([xs, ys, zs]).T
    center = pts.mean(axis=0)
    pts -= center
    pts *= 5.8 / np.abs(pts).max()
    return pts


class BeautifulLorenz(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#08000a"
        self.set_camera_orientation(phi=68*DEGREES, theta=-48*DEGREES)
        self.camera.set_zoom(0.92)

        axes = ThreeDAxes(
            x_range=[-7,7], y_range=[-7,7], z_range=[-7,7],
            x_length=10, y_length=10, z_length=10,
            axis_config={"stroke_width":0, "color":BLACK},
            tips=False,
        )
        self.add(axes)

        pts = compute_lorenz()
        warm = ["#8B0000","#B22222","#CC3300","#E84000",
                "#FF5500","#FF7000","#FF8C00","#FFA500",
                "#FFB700","#FFD700","#FFB700","#FFA500",
                "#FF8C00","#FF5500","#E84000","#CC3300","#B22222"]

        n_segs = 120
        seg_size = len(pts) // n_segs
        colors = color_gradient(warm, n_segs)

        for i in range(n_segs):
            chunk = pts[i*seg_size:(i+1)*seg_size+1]
            verts = [axes.c2p(*p) for p in chunk]
            if len(verts) < 2:
                continue
            curve = VMobject()
            curve.set_points_smoothly(verts)
            w = 1.5 + 0.7*abs(np.sin(i*PI/n_segs))
            curve.set_stroke(color=colors[i], width=w, opacity=0.93)
            self.add(curve)

        # Subtle white glow overlay
        for i in range(0, n_segs, 4):
            chunk = pts[i*seg_size:(i+1)*seg_size+1]
            verts = [axes.c2p(*p) for p in chunk]
            if len(verts) < 2:
                continue
            gc = VMobject()
            gc.set_points_smoothly(verts)
            gc.set_stroke(color=WHITE, width=0.4, opacity=0.12)
            self.add(gc)

        # Slow cinematic rotation
        self.begin_ambient_camera_rotation(rate=0.05)
        self.wait(15)
        self.stop_ambient_camera_rotation()
