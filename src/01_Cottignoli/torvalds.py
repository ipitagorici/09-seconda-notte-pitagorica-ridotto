from manim import *

class Torvalds(Scene):
    def construct(self):
        torvalds = ImageMobject("../assets/imgs/Cottignoli/Torvalds.png")
        
        self.play(FadeIn(torvalds))
        
        
        self.wait(2)