from manim import *

class GNU(Scene):
    def construct(self):
        GNU = ImageMobject("../../assets/imgs/Cottignoli/GNU.png")
        GNU_text = Tex("GNU is Not Unix", font_size=80)\
            .next_to(GNU, UP)\
            .set_color(RED)
        
        self.play(FadeIn(GNU))
        self.play(Write(GNU_text))
        
        
        self.wait(2)