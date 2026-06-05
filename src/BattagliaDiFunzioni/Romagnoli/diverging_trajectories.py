from manim import *
import numpy as np


def compute_lorenz(x0=0.1, y0=0.0, z0=0.0, steps=9000, dt=0.005):
    sigma, rho, beta = 10, 28, 8/3
    xs, ys, zs = [x0], [y0], [z0]
    for _ in range(steps):
        x, y, z = xs[-1], ys[-1], zs[-1]
        xs.append(x + sigma*(y-x)*dt)
        ys.append(y + (x*(rho-z)-y)*dt)
        zs.append(z + (x*y-beta*z)*dt)
    return np.array([xs, ys, zs]).T


def normalize_shared(pts1, pts2, scale=5.0):
    combined = np.vstack([pts1, pts2])
    center = combined.mean(axis=0)
    s = scale / np.abs(combined - center).max()
    return (pts1 - center)*s, (pts2 - center)*s


class DivergingTrajectories(ThreeDScene):
    def construct(self):
        self.camera.background_color = BLACK
        self.set_camera_orientation(phi=65*DEGREES, theta=-55*DEGREES)
        self.camera.set_zoom(0.88)

        axes = ThreeDAxes(
            x_range=[-7,7], y_range=[-7,7], z_range=[-7,7],
            x_length=10, y_length=10, z_length=10,
            axis_config={"stroke_width":0.8, "color":DARK_GREY},
            tips=False,
        )
        self.add(axes)

        epsilon = 1e-5
        raw1 = compute_lorenz(x0=0.1)
        raw2 = compute_lorenz(x0=0.1+epsilon)
        pts1, pts2 = normalize_shared(raw1, raw2)

        lbl = Text("Sensibilità alle condizioni iniziali", font_size=26, color=GREY_A)
        lbl.to_corner(UL)
        self.add_fixed_in_frame_mobjects(lbl)

        # Legend
        leg_r = Text("● Traiettoria A", font_size=20, color=RED)
        leg_b = Text("● Traiettoria B", font_size=20, color=BLUE)
        leg_r.to_corner(DR).shift(UP*0.5)
        leg_b.next_to(leg_r, UP, buff=0.15)
        self.add_fixed_in_frame_mobjects(leg_r, leg_b)

        phase_lbl = Text("Stesse condizioni iniziali", font_size=22, color=YELLOW)
        phase_lbl.to_corner(UR)
        self.add_fixed_in_frame_mobjects(phase_lbl)

        dot1 = Dot3D(point=axes.c2p(*pts1[0]), radius=0.12, color=RED)
        dot2 = Dot3D(point=axes.c2p(*pts2[0]), radius=0.12, color=BLUE)
        self.play(FadeIn(dot1), FadeIn(dot2), run_time=0.8)
        self.wait(1.5)

        n_segs = 90
        seg_size = len(pts1) // n_segs
        overlap_end = int(n_segs * 0.32)
        separate_start = int(n_segs * 0.48)

        self.begin_ambient_camera_rotation(rate=0.10)

        for i in range(n_segs):
            chunk1 = pts1[i*seg_size:(i+1)*seg_size+1]
            chunk2 = pts2[i*seg_size:(i+1)*seg_size+1]

            v1 = [axes.c2p(*p) for p in chunk1]
            v2 = [axes.c2p(*p) for p in chunk2]

            c1 = VMobject()
            c1.set_points_smoothly(v1)
            c2 = VMobject()
            c2.set_points_smoothly(v2)

            if i < overlap_end:
                # Red thick underneath, blue thinner on top — both visible
                c1.set_stroke(color=RED, width=3.2, opacity=0.9)
                c2.set_stroke(color=BLUE, width=1.5, opacity=0.85)
            elif i < separate_start:
                frac = (i - overlap_end) / (separate_start - overlap_end)
                c1.set_stroke(color=RED, width=2.5 + frac*0.5, opacity=0.9)
                c2.set_stroke(color=BLUE, width=2.5 + frac*0.5, opacity=0.9)
            else:
                c1.set_stroke(color=RED, width=2.2, opacity=0.92)
                c2.set_stroke(color=BLUE, width=2.2, opacity=0.92)

            end_idx = min((i+1)*seg_size, len(pts1)-1)
            dot1.move_to(axes.c2p(*pts1[end_idx]))
            dot2.move_to(axes.c2p(*pts2[end_idx]))

            if i == overlap_end:
                new_lbl = Text("Leggera divergenza...", font_size=22, color=ORANGE)
                new_lbl.to_corner(UR)
                self.remove(phase_lbl)
                self.add_fixed_in_frame_mobjects(new_lbl)
                phase_lbl = new_lbl
                self.wait(1.5)

            if i == separate_start:
                new_lbl = Text("Traiettorie opposte!", font_size=22, color=RED)
                new_lbl.to_corner(UR)
                self.remove(phase_lbl)
                self.add_fixed_in_frame_mobjects(new_lbl)
                phase_lbl = new_lbl
                self.wait(1.5)

            self.add(c1, c2)
            self.wait(4/15)

        self.play(FadeOut(dot1), FadeOut(dot2), run_time=0.6)
        self.wait(4)
        self.stop_ambient_camera_rotation()
