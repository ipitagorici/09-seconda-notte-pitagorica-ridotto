from manim import *

class Stallman(Scene):
    def construct(self):
        stallman = ImageMobject("../assets/imgs/Cottignoli/Stallman.png")
        
        richard_text = Tex("Richard", font_size=90)\
            .shift(LEFT*4).shift(UP*2)
        stallman_text = Tex("Stallman", font_size=90)\
            .shift(RIGHT*4).shift(UP*2)
        
        self.play(FadeIn(stallman))
        self.play(Write(richard_text), Write(stallman_text))
        
        
        self.wait(2)