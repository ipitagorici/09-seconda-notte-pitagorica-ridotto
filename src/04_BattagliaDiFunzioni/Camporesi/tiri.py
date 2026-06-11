from manim import *
from math import log, sqrt, e

from manim.animation.growing import GrowFromCenter

class Tiri(Scene):
    def construct(self):        
        ################
        ### MOBJECTS ###
        ################
        
        axes = Axes(
            x_range=[-10, 40, 10], 
            y_range=[-20, 10, 10],
            tips = False
        )
        
        equations_names = [
            Tex(r"$-2\pi \ln(x+1)$", color=BLUE).to_corner(UR),
            Tex(r"$-x\sqrt{2}e^{-\frac{x}{16}}$", color=BLUE).to_corner(UR),
            Tex(r"$\sqrt{5}e^{-\frac{(x-20)^{2}}{100}}$", color=BLUE).to_corner(UR)
        ]

        calciatori = [
            Tex("Alex Del Piero", color=RED, font_size=30).move_to(axes.get_origin()).shift(UP*0.5).shift(RIGHT*1.2),
            Tex("Roberto Carlos", color=RED, font_size=30).move_to(axes.get_origin()).shift(UP*0.5).shift(RIGHT*1.2),
            Tex("Andrea Pirlo", color=RED, font_size=30).move_to(axes.get_origin()).shift(DOWN*0.5).shift(RIGHT)
        ]
        
        math_equations = [
            # −2πln(x+1)
            {"func": lambda x: (-2) * PI * log(x+1), "x_range": [0, 20]},
            # √2 * e^(-x/16)
            {"func": lambda x: (-x) * sqrt(2) * e ** (-(x/16)), "x_range": [0, 35]},
            # √5 * e^(-(x-20)^2/100)
            {"func": lambda x: sqrt(5) * e ** (-(((x-20)**2)/100)), "x_range": [0, 25]}
        ]

        functions = [
            axes.plot(eq["func"], x_range=eq["x_range"]) 
            for eq in math_equations
        ]
        
        porte = [
            Line(axes.c2p(20, -13), axes.c2p(20, -20), color=DARK_GREY),
            Line(axes.c2p(35, 0),   axes.c2p(35, -6), color=DARK_GREY),
            Line(axes.c2p(25, 1),   axes.c2p(25, 7), color=DARK_GREY)
        ]



        ##################
        ### ANIMATIONS ###
        ##################

        self.play(Create(axes, run_time=2))

        for i in range(len(functions)):
            self.next_section(f"Tiro {i}")

            if i == 0:
                self.play(
                    Write(calciatori[i]),
                    Create(functions[i]),
                    Write(equations_names[i]),
                    DrawBorderThenFill(porte[i]),
                    run_time=1.5
                )
            else:
                self.play(
                    FadeOut(calciatori[i-1]),
                    Uncreate(functions[i-1]),
                    FadeOut(equations_names[i-1]),
                    Uncreate(porte[i-1])
                )
                self.play(
                    Write(calciatori[i]),
                    Create(functions[i]),
                    Write(equations_names[i]),
                    DrawBorderThenFill(porte[i], run_time=0.5),
                    run_time=1.5
                )
            self.wait(1)


        self.wait(2)