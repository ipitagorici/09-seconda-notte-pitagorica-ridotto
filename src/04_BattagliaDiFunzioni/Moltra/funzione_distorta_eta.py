from manim import *
from math import cos, sin

class FunzioneDistortaEta(Scene):
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


        curve = axes.plot(lambda x: (1/x)*(cos(2*x*sin(x))+0.7), x_range=[3.84, 85], color=ORANGE, stroke_width=4)

        self.play(Create(axes), Write(x_label))
        self.play(Create(curve), run_time=2)
        
        self.wait(2)