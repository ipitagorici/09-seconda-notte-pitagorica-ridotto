from manim import *
import numpy as np


def compute_lorenz(x0=0.1, y0=0.0, z0=0.0, steps=8000, dt=0.005):
    sigma, rho, beta = 10, 28, 8/3
    xs, ys, zs = [x0], [y0], [z0]
    for _ in range(steps):
        x, y, z = xs[-1], ys[-1], zs[-1]
        xs.append(x + sigma * (y - x) * dt)
        ys.append(y + (x * (rho - z) - y) * dt)
        zs.append(z + (x * y - beta * z) * dt)
    pts = np.array([xs, ys, zs]).T
    center = pts.mean(axis=0)
    pts -= center
    pts *= 5.0 / np.abs(pts).max()
    return pts


class ThreeClicks(ThreeDScene):
    def construct(self):
        self.camera.background_color = BLACK
        self.set_camera_orientation(phi=70 * DEGREES, theta=-50 * DEGREES)
        self.camera.set_zoom(0.9)

        axes = ThreeDAxes(
            x_range=[-7,7], y_range=[-7,7], z_range=[-7,7],
            x_length=10, y_length=10, z_length=10,
            axis_config={"stroke_width": 0.8, "color": DARK_GREY},
            tips=False,
        )
        self.add(axes)

        def show_label(txt, color=GREY_A):
            l = Text(txt, font_size=30, color=color)
            l.to_corner(UL)
            self.add_fixed_in_frame_mobjects(l)
            return l

        # ── CLICK 1: fixed point ──────────────────────────────────────────
        lbl1 = show_label("① Punto fisso")
        dot_fixed = Sphere(radius=0.18, color=WHITE)
        dot_fixed.move_to(axes.c2p(0, 0, 0))
        self.play(FadeIn(dot_fixed), run_time=0.6)
        self.play(Flash(dot_fixed, color=YELLOW, line_length=0.4, num_lines=10), run_time=1.0)
        self.wait(2)

        # ── CLICK 2: regular orbit ────────────────────────────────────────
        lbl2 = show_label("② Orbita regolare")
        self.play(FadeOut(lbl1), FadeOut(dot_fixed), run_time=0.3)

        r = 2.5
        orbit_pts = [
            axes.c2p(r * np.cos(t), r * np.sin(t), 0.5)
            for t in np.linspace(0, TAU, 150)
        ]
        orbit_curve = VMobject()
        orbit_curve.set_points_smoothly(orbit_pts + [orbit_pts[0]])
        orbit_curve.set_stroke(color=BLUE, width=2.5)

        orbit_dot = Sphere(radius=0.12, color=BLUE_A)
        orbit_dot.move_to(orbit_pts[0])

        self.play(Create(orbit_curve), run_time=1.5)
        self.add(orbit_dot)
        # Animate dot with MoveAlongPath — much faster than frame loop
        self.play(
            MoveAlongPath(orbit_dot, orbit_curve),
            run_time=3, rate_func=linear
        )
        self.wait(1)

        # ── CLICK 3: full Lorenz attractor ───────────────────────────────
        lbl3 = show_label("③ Attrattore caotico")
        self.play(FadeOut(lbl2), FadeOut(orbit_curve), FadeOut(orbit_dot), run_time=0.3)

        pts = compute_lorenz()
        n_segs = 80
        seg_size = len(pts) // n_segs
        colors = color_gradient([BLUE_D, TEAL, GREEN_C, YELLOW, RED], n_segs)

        tracer = Sphere(radius=0.07, color=WHITE)
        tracer.move_to(axes.c2p(*pts[0]))
        self.add(tracer)

        self.begin_ambient_camera_rotation(rate=0.12)

        for i in range(n_segs):
            chunk = pts[i * seg_size:(i+1)*seg_size+1]
            verts = [axes.c2p(*p) for p in chunk]
            curve = VMobject()
            curve.set_points_smoothly(verts)
            curve.set_stroke(color=colors[i], width=1.4, opacity=0.9)
            end_idx = min((i+1)*seg_size, len(pts)-1)
            tracer.move_to(axes.c2p(*pts[end_idx]))
            self.play(Create(curve), run_time=0.20, rate_func=linear)

        self.play(FadeOut(tracer), run_time=0.3)
        self.wait(2)
        self.stop_ambient_camera_rotation()
