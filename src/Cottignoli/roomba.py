from manim import *

class Roomba(Scene):
    def construct(self):
        roomba = ImageMobject("../assets/imgs/Cottignoli/Roomba.png")
        
        self.play(FadeIn(roomba))
        
        
        self.wait(2)