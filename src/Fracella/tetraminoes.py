from manim import *

class Tetraminoes(Scene):
    def construct(self):
        tetraminoes = ImageMobject("../assets/imgs/Fracella/Tetraminoes.png")\
            .scale(0.75)\
            .shift(UP*.5)
        t = Tex("T").set_color(BLACK)\
            .shift(UP)
        o = Tex("O").set_color(BLACK)\
            .shift(UR*3).shift(RIGHT*1.5)
        i = Tex("I").set_color(BLACK)\
            .shift(DOWN*2)
        j = Tex("J").set_color(BLACK)\
            .shift(UL*3)
        l = Tex("L").set_color(BLACK)\
            .shift(UP*3)
        s = Tex("S").set_color(BLACK)\
            .shift(LEFT*4.5)
        z = Tex("Z").set_color(BLACK)\
            .shift(RIGHT*4.5)
        
        self.play(FadeIn(tetraminoes))
        
        self.play(Succession(
            Write(t, run_time=0.5),
            Write(o, run_time=0.5),
            Write(i, run_time=0.5),
            Write(j, run_time=0.5),
            Write(l, run_time=0.5),
            Write(s, run_time=0.5),
            Write(z, run_time=0.5),
        ))
        
        
        
        self.wait(2)