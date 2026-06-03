from manim import *
from math import log, sqrt, e

class Tiri(Scene):
    def construct(self):
        equations_names = [
            Tex(r"$-2\pi \ln(x+1)$", color=BLUE),
            Tex(r"$-x\sqrt{2}e^{-\frac{x}{16}}$", color=BLUE),
            Tex(r"$\sqrt{5}e^{-\frac{(x-20)^{2}}{100}}$", color=BLUE)
        ]
        math_equations = [
            # −2πln(x+1)
            {"func": lambda x: (-2) * PI * log(x+1), "x_range": [0, 40]},
            # √2 * e^(-x/16)
            {"func": lambda x: (-x) * sqrt(2) * e ** (-(x/16)), "x_range": [0, 50]},
            # √5 * e^(-(x-20)^2/100)
            {"func": lambda x: sqrt(5) * e ** (-(((x-20)**2)/100)), "x_range": [0, 50]}
        ]

        axes = Axes(
            x_range=[-10, 40, 10], 
            y_range=[-20, 10, 10],
        )
        self.play(Create(axes))

        functions = [
            axes.plot(eq["func"], x_range=eq["x_range"]) 
            for eq in math_equations
        ]

        for i in range(len(functions)):
            self.next_section(f"Tiro {i}")

            if i == 0:
                self.play(Create(functions[i]))
                self.play(Write(equations_names[i]))
            else:
                self.play(
                    Uncreate(functions[i - 1]),
                    FadeOut(equations_names[i-1]),
                )
                self.play(
                    Create(functions[i]),
                    Write(equations_names[i])
                )
            self.wait(1)


        self.wait(2)