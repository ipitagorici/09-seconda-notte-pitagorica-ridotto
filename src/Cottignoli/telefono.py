from manim import *

class Telefono(Scene):
    def construct(self):
        telefono = ImageMobject("assets/imgs/Cottignoli/telefono.png")\
            .scale(1.3)
        
        self.play(FadeIn(telefono))
        
        
        self.wait(2)