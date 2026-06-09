from manim import *

class Git(Scene):
    def construct(self):
        git = ImageMobject("../assets/imgs/Cottignoli/Git.png")\
            .scale(1.5)

        self.play(FadeIn(git))


        self.wait(2)