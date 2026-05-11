from manim import *

class Cabinato(Scene):
    def construct(self):
        cabinato = ImageMobject("assets/imgs/Fracella/Cabinato.png")
        
        self.play(FadeIn(cabinato))
        
        
        self.wait(2)