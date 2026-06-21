from manim import *

class PitagoraCorde(Scene):
    def construct(self):
        pitagora = ImageMobject("../assets/imgs/BattagliaDiFunzioni/GiuliaELara/PitagoraCorde.png")\
            .scale(2)

        self.play(FadeIn(pitagora))


        self.wait(2)