from manim import *

class ScaryImages(Scene):
    def construct(self):
        scary_1 = ImageMobject("../assets/imgs/BattagliaDiFunzioni/Cottignoli/Scary1.png")
        scary_2 = ImageMobject("../assets/imgs/BattagliaDiFunzioni/Cottignoli/Scary2.png")
        scary_3 = ImageMobject("../assets/imgs/BattagliaDiFunzioni/Cottignoli/Scary3.png")



        self.next_section("scary1")

        self.play(FadeIn(scary_1))



        self.next_section("scary2")

        self.play(FadeOut(scary_1), FadeIn(scary_2))



        self.next_section("scary3")

        self.play(FadeOut(scary_2), FadeIn(scary_3))