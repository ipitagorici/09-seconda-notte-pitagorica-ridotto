from manim import *

class Lorenz(Scene):
    def construct(self):
        lorenz = ImageMobject("../assets/imgs/BattagliaDiFunzioni/Romagnoli/Lorenz.png")
        
        self.play(FadeIn(lorenz))