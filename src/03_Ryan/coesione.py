from manim import *

class Coesione(Scene):
    def construct(self):
        coesione = Text("Coesione", color=PURPLE, font_size=100)
        cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = 1.1,
            width = 0.5,
        ).move_to(coesione[0])

        self.play(TypeWithCursor(coesione, cursor, run_time=1))
        self.play(Blink(cursor, blinks=2))