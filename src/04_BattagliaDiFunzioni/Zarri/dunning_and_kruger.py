from manim import *

class DunningAndKruger(Scene):
    def construct(self):
        d_and_k = ImageMobject("../assets/imgs/BattagliaDiFunzioni/Zarri/DunningAndKruger.png")\
            .shift(DOWN)
        dunning = Tex("David Dunning", font_size=60)\
            .next_to(d_and_k, UP)\
            .shift(RIGHT*3)
        kruger = Tex("Justin Kruger", font_size=60)\
            .next_to(d_and_k, UP)\
            .shift(LEFT*3)

        self.play(FadeIn(d_and_k))
        self.play(Write(dunning), Write(kruger))


        self.wait(2)