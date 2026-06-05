from manim import *

class PcExamples(Scene):
    def construct(self):
        i = ImageMobject("../assets/imgs/Fracella/I").to_edge(LEFT).shift(UP*1.5).shift(RIGHT*0.5).scale(0.5)
        j = ImageMobject("../assets/imgs/Fracella/J").next_to(i, RIGHT).scale(0.5)
        o = ImageMobject("../assets/imgs/Fracella/O").next_to(j, RIGHT).scale(0.5)
        t = ImageMobject("../assets/imgs/Fracella/T").next_to(o, RIGHT).scale(0.5)
        pieces = Group(i, j, o, t)
        
        self.play(ShowIncreasingSubsets(pieces, run_time=2))
        
        self.wait()
        
        layout_1 = ImageMobject("../assets/imgs/Fracella/Layout1").scale(3).next_to(t, RIGHT*5)
        
        self.play(SpinInFromNothing(layout_1, angle=PI))
        self.play(Flash(layout_1, flash_radius=1.5, num_lines=30))
        
        
        
        self.next_section("second example")
        
        i = ImageMobject("../assets/imgs/Fracella/I").to_edge(LEFT).shift(DOWN*1.5).shift(RIGHT*0.5).scale(0.5)
        l = ImageMobject("../assets/imgs/Fracella/l").next_to(i, RIGHT).scale(0.5)
        s = ImageMobject("../assets/imgs/Fracella/S").next_to(l, RIGHT).scale(0.5)
        z = ImageMobject("../assets/imgs/Fracella/Z").next_to(s, RIGHT).scale(0.5)
        pieces = Group(i, l, s, z)
        
        self.play(ShowIncreasingSubsets(pieces, run_time=2))
        
        self.wait()
        
        layout_2 = ImageMobject("../assets/imgs/Fracella/Layout2").scale(3).next_to(z, RIGHT*5) 
        
        self.play(SpinInFromNothing(layout_2, angle=PI))
        self.play(Flash(layout_2, flash_radius=1.5, num_lines=30))