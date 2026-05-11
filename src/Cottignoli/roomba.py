from manim import *

class Roomba(Scene):
    def construct(self):
        roomba = ImageMobject("assets/imgs/Cottignoli/Roomba.png")\
            .scale(0.5)
        
        self.play(FadeIn(roomba))
        
        
        self.wait(2)