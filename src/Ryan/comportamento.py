from manim import *

class ComportamentoEmergente(Scene):
    def construct(self):
        comportamento = Tex(r"Comportamento\\Emergente", font_size=150)
        
        self.play(FadeIn(comportamento, run_time=3))
        
        
        self.wait(2)