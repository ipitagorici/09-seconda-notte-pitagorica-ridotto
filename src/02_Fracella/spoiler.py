from manim import *

class Spoiler(Scene):
    def construct(self):
        spoiler = Tex(r"PRIMO PC", font_size=200)\
            .set_opacity(0.25)
        
        self.play(FadeIn(spoiler, run_time=5))