from manim import *

class Ambiguita(Scene):
    def construct(self):
        ambguita = Tex("Ambiguità", color=RED, font_size=250)
        
        self.play(FadeIn(ambguita, run_time=3))
        
        
        self.wait(2)