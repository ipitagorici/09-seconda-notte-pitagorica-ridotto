from manim import *

class Linux(Scene):
    def construct(self):
        linux = ImageMobject("../assets/imgs/Cottignoli/Linux.png")\
            .scale(0.75)
        
        self.play(FadeIn(linux))
        
        
        self.wait(2)