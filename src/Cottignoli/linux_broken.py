from manim import *

class LinuxBroken(Scene):
    def construct(self):
        broken_linux = ImageMobject("../assets/imgs/Cottignoli/LinuxBroken.png")

        self.play(FadeIn(broken_linux))


        self.wait(2)