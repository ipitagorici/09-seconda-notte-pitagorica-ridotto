from manim import *

class Mask(Scene):
    def construct(self):
        mask = ImageMobject("../assets/imgs/BattagliaDiFunzioni/Cottignoli/Mask.png")
        
        self.play(FadeIn(mask))
        
        
        self.wait(2)