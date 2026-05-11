from manim import *

class ComportamentoEmergente(Scene):
    def construct(self):
        comportamento = Text("Comportamento\nEmergente", font_size=80)
        cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = 1.1,
            width = 0.5,
        ).move_to(comportamento[0])
        
        self.play(TypeWithCursor(comportamento, cursor))
        self.play(Blink(cursor, blinks=2))
        
        
        self.wait(2)