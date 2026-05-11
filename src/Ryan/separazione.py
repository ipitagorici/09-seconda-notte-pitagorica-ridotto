from manim import *

class Separazione(Scene):
    def construct(self):
        separazione = Text("Separazione", color=PURPLE, font_size=100)
        cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = 1.1,
            width = 0.5,
        ).move_to(separazione[0])

        self.play(TypeWithCursor(separazione, cursor, run_time=1))
        self.play(Blink(cursor, blinks=2))
     