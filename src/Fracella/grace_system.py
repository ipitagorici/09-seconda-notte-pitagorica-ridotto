from manim import *

class GraceSystem(Scene):
    def construct(self):
        grace = ImageMobject("../assets/imgs/Fracella/GraceSystem.png")\
            .scale(2)
        
        self.play(FadeIn(grace))
        
        
        self.wait(2)