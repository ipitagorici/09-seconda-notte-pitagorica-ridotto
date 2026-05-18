from manim import *

class PcExamples(Scene):
    def construct(self):
        i = ImageMobject("../assets/imgs/Fracella/I").to_corner(UL)
        j = ImageMobject("../assets/imgs/Fracella/J").next_to(i, RIGHT)
        o = ImageMobject("../assets/imgs/Fracella/O").next_to(j, RIGHT)
        t = ImageMobject("../assets/imgs/Fracella/T").next_to(o, RIGHT)
        pieces = VGroup(i, j, o, t)
        
        self.play(ShowIncreasingSubsets(pieces))
        
        layout_1 = ImageMobject("../assets/imgs/Fracella/Layout1")
        
        self.play(FadeIn(layout_1))
        
        
        
        self.next_section("second example")
        
        i = ImageMobject("../assets/imgs/Fracella/I").to_edge(LEFT)
        l = ImageMobject("../assets/imgs/Fracella/Z").next_to(i, RIGHT)
        s = ImageMobject("../assets/imgs/Fracella/S").next_to(l, RIGHT)
        z = ImageMobject("../assets/imgs/Fracella/Z").next_to(s, RIGHT)
        pieces = VGroup(i, l, s, z)
        
        self.play(ShowIncreasingSubsets(pieces))
        
        layout_2 = ImageMobject("../assets/imgs/Fracella/Layout2")
        
        self.play(FadeIn(layout_2))