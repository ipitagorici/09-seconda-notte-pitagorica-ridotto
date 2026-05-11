from manim import *

class UncannyValley(Scene):
    def construct(self):
        uncanny_valley = ImageMobject("assets/BattagliaDiFunzioni/Cottignoli/UncannyValley.png")
        
        self.play(FadeIn(uncanny_valley))
        
        
        self.wait(2)