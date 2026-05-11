from manim import *

class Xerox9700(Scene):
    def construct(self):
        xerox = ImageMobject("../../assets/imgs/Cottignoli/xerox9700.png")\
            .scale(1.5)
        
        self.play(FadeIn(xerox))
        
        
        self.wait(2)