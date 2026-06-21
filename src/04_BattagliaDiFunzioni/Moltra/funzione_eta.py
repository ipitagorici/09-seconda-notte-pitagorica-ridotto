from manim import *

class FunzioneEta(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 85, 10],
            y_range=[0, 0.26, 0.05],
            x_length=9,
            y_length=5.5,
            tips=False,
            axis_config={"include_numbers": True, "font_size": 20}
        )

        x_label = Text("Anni", font_size=18).next_to(axes.x_axis, DOWN)
        y_label = Text(
            "Valore relativo di un anno sull'intera vita", 
            font_size=18
        ).rotate(PI/2).next_to(axes.y_axis, LEFT)

        curve = axes.plot(lambda x: 1/x, x_range=[3.84, 85], color=ORANGE, stroke_width=4)

        points_info = [
            (5, RED, "5 anni (20.0%)"),
            (20, BLUE, "20 anni (5.0%)"),
            (50, PURPLE, "50 anni (2.0%)"),
            (80, GREEN, "80 anni (1.2%)")
        ]

        dots = VGroup()
        point_labels = VGroup()

        for x_val, color, text in points_info:
            y_val = 1 / x_val
            dot = Dot(axes.c2p(x_val, y_val), color=color)
            label = Text(text, font_size=14).next_to(dot, UR, buff=0.1)
            
            dots.add(dot)
            point_labels.add(label)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(curve), run_time=2)
        self.play(FadeIn(dots), Write(point_labels))
        
        self.wait(2)