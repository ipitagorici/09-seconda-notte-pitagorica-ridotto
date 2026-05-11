from manim import *

class Tux(Scene):
    def construct(self):
        tux = ImageMobject("../../assets/imgs/Cottignoli/Tux.png")\
            .scale(2.5)
        tux_text = Tex("Tux", font_size=60).next_to(tux, UP)
        
        self.play(FadeIn(tux))
        self.play(Write(tux_text))
        
        
        self.wait(2)