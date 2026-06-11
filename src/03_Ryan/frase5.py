from manim import *

class Frase5(Scene):
    def construct(self):
        frase5 = Text("Lo stormo non esiste!", font_size=80)
        cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = 1.1,
            width = 0.5,
        ).move_to(frase5[0])
        
        self.play(TypeWithCursor(frase5, cursor))
        self.play(Blink(cursor, blinks=2))