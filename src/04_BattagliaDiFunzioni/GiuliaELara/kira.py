from manim import *

class Kira(Scene):
    def construct(self):
        kira = ImageMobject("../assets/imgs/BattagliaDiFunzioni/GiuliaELara/Kira.png")\
            .scale(2.5)

        self.play(FadeIn(kira))


        self.wait(2)