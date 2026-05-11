from manim import *

class FSF(Scene):
    def construct(self):
        logo = ImageMobject("../../assets/imgs/Cottignoli/FSF.png")\
            .scale(1.5)
        
        self.play(FadeIn(logo))
        
        
        self.wait(2)