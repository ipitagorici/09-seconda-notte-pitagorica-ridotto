from manim import *

class Examples(Scene):
    def construct(self):
        examples = ImageMobject("assets/BattagliaDiFunzioni/Cottignoli/Examples.png")
        
        self.play(FadeIn(examples))
        
        
        self.wait(2)