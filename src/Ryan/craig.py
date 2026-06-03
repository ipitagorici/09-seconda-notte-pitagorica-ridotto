from manim import *

class CraigReynolds(Scene):
    def construct(self):
        craig = ImageMobject("../assets/Ryan/CraigReynolds.png")\
            .scale(4)
            
        self.play(FadeIn(craig))
        
        
        self.wait(2)