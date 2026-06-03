from manim import *

class HelsinkiUni(Scene):
    def construct(self):
        uni = ImageMobject("../assets/imgs/Cottignoli/Helsinki.png")
        
        self.play(FadeIn(uni))
        
        
        self.wait(2)