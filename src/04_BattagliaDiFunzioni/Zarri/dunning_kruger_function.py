from manim import *
import numpy as np

class DunningKrugerFunction(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 8, 1],
            y_range=[0, 4, 1],
            x_length=9,
            y_length=5,
            axis_config={"include_numbers": False},
            tips=True
        )
        
        x_label = Tex("Competenze effettive")\
            .next_to(axes.x_axis, DOWN, buff=0.3)\
            .scale(0.8)
        y_label = Tex("Competenze pensate")\
            .shift(LEFT*5)\
            .rotate(90 * DEGREES)\
            .scale(0.8)
        
        dk_equation = lambda x: (11 * x * np.exp(-1.5 * x)) + (3 * (x**2) / (x**2 + 35))

        curve_up = axes.plot(dk_equation, color=ORANGE, x_range=[0, 0.65])
        curve_down = axes.plot(dk_equation, color=BLUE, x_range=[0.65, 2.0])
        curve_bottom = axes.plot(dk_equation, color=GREEN, x_range=[2.0, 3.5])
        curve_recovery = axes.plot(dk_equation, color=YELLOW, x_range=[3.5, 7.5])

        dot_up = Dot(point=curve_up.get_end(), color=ORANGE, radius=0.08)
        dot_down = Dot(point=curve_down.get_end(), color=BLUE, radius=0.08)
        dot_bottom = Dot(point=curve_bottom.get_end(), color=GREEN, radius=0.08)



        self.next_section("Rise")

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)

        self.play(Create(curve_up), run_time=2)
        self.play(GrowFromCenter(dot_up), run_time=0.2)
        self.wait(0.3)



        self.next_section("Down")

        self.play(Create(curve_down), run_time=2)
        self.play(GrowFromCenter(dot_down), run_time=0.2)
        self.wait(0.3)
        


        self.next_section("Bottom")

        self.play(Create(curve_bottom), run_time=2)
        self.play(GrowFromCenter(dot_bottom), run_time=0.2)
        self.wait(0.3)



        self.next_section("End")

        self.play(Create(curve_recovery), run_time=2)

        self.wait(2)