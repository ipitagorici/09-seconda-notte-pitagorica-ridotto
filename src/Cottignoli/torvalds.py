from manim import *

class Torvalds(Scene):
    def construct(self):
        torvalds = ImageMobject("../../assets/imgs/Cottignoli/Torvalds.png")\
            .scale(2)
        
        self.play(FadeIn(torvalds))
        
        
        self.wait(2)