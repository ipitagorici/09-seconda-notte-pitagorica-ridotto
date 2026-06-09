from manim import *

class Frase4(Scene):
    def construct(self):
        frase4_1 = Tex(r"Cosa ci diremmo?").shift(UP*2)
        frase4_2 = Tex(r"Come faremmo ad organizzarci\\in questo movimento simile alle onde?")
        frase4_3 = Tex(r"Come faremmo a non colpirci l'uno con l'altro\\o stamparci contro gli ostacoli?").shift(DOWN*2)

        self.play(DrawBorderThenFill(frase4_1, run_time=2.5, rate_func=rush_from))
        self.play(DrawBorderThenFill(frase4_2, run_time=3.5, rate_func=rush_from))
        self.play(DrawBorderThenFill(frase4_3, run_time=5, rate_func=rush_from))


        self.wait(2)