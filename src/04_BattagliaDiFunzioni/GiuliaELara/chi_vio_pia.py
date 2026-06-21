from manim import *

class ChiVioPia(Scene):
    def construct(self):
        chitarra = ImageMobject("../assets/imgs/BattagliaDiFunzioni/GiuliaELara/Chitarra.png")\
            .scale(0.5)\
            .to_edge(LEFT)
        violino = ImageMobject("../assets/imgs/BattagliaDiFunzioni/GiuliaELara/Violino.png")\
            .scale(0.75)
        pianoforte = ImageMobject("../assets/imgs/BattagliaDiFunzioni/GiuliaELara/Pianoforte.png")\
            .scale(0.3)\
            .to_edge(RIGHT)

        self.play(FadeIn(chitarra))
        self.play(FadeIn(violino))
        self.play(FadeIn(pianoforte))