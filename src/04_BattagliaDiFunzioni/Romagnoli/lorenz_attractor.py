from manim import *
import numpy as np


class LorenzAttractor(ThreeDScene):
    def construct(self):
        # Lorenz params
        sigma, rho, beta = 10, 28, 8/3
        dt = 0.005
        steps = 8000

        # Compute trajectory
        def lorenz_step(x, y, z):
            dx = sigma * (y - x)
            dy = x * (rho - z) - y
            dz = x * y - beta * z
            return dx, dy, dz

        xs, ys, zs = [0.1], [0.0], [0.0]
        for _ in range(steps):
            dx, dy, dz = lorenz_step(xs[-1], ys[-1], zs[-1])
            xs.append(xs[-1] + dx * dt)
            ys.append(ys[-1] + dy * dt)
            zs.append(zs[-1] + dz * dt)

        # Normalize to scene
        pts = np.array([xs, ys, zs]).T
        center = pts.mean(axis=0)
        pts -= center
        scale = 5.5 / np.abs(pts).max()
        pts *= scale

        # Camera setup
        self.set_camera_orientation(phi=70 * DEGREES, theta=-60 * DEGREES)
        self.camera.set_zoom(0.85)

        # Axes
        axes = ThreeDAxes(
            x_range=[-7, 7], y_range=[-7, 7], z_range=[-7, 7],
            x_length=10, y_length=10, z_length=10,
            axis_config={"stroke_width": 1, "color": GREY},
            tips=False,
        )
        self.add(axes)

        # Title
        title = Text("Lorenz Attractor", font_size=36, color=WHITE)
        title.to_corner(UL)
        self.add_fixed_in_frame_mobjects(title)
        self.play(FadeIn(title), run_time=0.5)

        # Build segments with gradient color
        n_segs = 80
        seg_size = len(pts) // n_segs
        colors = color_gradient([BLUE, PURPLE, RED, ORANGE, YELLOW], n_segs)

        curves = VGroup()
        for i in range(n_segs):
            chunk = pts[i * seg_size:(i + 1) * seg_size + 1]
            verts = [axes.c2p(*p) for p in chunk]
            curve = VMobject()
            curve.set_points_smoothly(verts)
            curve.set_stroke(color=colors[i], width=1.2, opacity=0.85)
            curves.add(curve)

        # Dot tracer
        dot = Sphere(radius=0.06, color=WHITE)
        dot.move_to(axes.c2p(*pts[0]))
        self.add(dot)

        # Animate drawing
        self.begin_ambient_camera_rotation(rate=0.18)

        for i, curve in enumerate(curves):
            frac = (i + 1) / n_segs
            end_idx = min(int(frac * len(pts)), len(pts) - 1)
            dot.move_to(axes.c2p(*pts[end_idx]))
            self.play(Create(curve), run_time=0.18, rate_func=linear)

        self.wait(0.5)

        # Final slow spin
        self.play(FadeOut(dot), run_time=0.4)
        self.wait(3)
        self.stop_ambient_camera_rotation()
