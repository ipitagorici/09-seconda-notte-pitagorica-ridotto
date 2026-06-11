from manim import *

class SepAllCoe(Scene):
    def construct(self):
        allineamento = Text("Allineamento", font_size=80, color=PURPLE)
        separazione = Text("Separazione", font_size=80, color=PURPLE).next_to(allineamento, UP)
        coesione = Text("Coesione", font_size=80, color=PURPLE).next_to(allineamento, DOWN)
        
        cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = 1.1,
            width = 0.5,
        ).move_to(separazione[0])
        
        self.play(TypeWithCursor(separazione, cursor))
        self.play(Blink(cursor, blinks=2))
        
        
        
        self.next_section("SepAll")
        
        
        
        cursor.move_to(allineamento[0])
        
        self.play(TypeWithCursor(allineamento, cursor))
        self.play(Blink(cursor, blinks=2))
        
        
        
        self.next_section("SepAllCoe")
        
        

        cursor.move_to(coesione[0])
        
        self.play(TypeWithCursor(coesione, cursor))
        self.play(Blink(cursor, blinks=2, hide_at_end=True))