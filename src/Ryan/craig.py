from manim import *

class CraigReynolds(Scene):
    def construct(self):
        craig = ImageMobject("Craig_Facebook_300x300.jpg")\
            .scale(4)
            
        self.play(FadeIn(craig))
        
        
        self.wait(2)