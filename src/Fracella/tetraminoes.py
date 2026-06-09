from manim import *

class Tetraminoes(Scene):
    def construct(self):
        tetraminoes = ImageMobject("../assets/imgs/Fracella/Tetraminoes.png")\
            .scale(0.75)\
            .shift(UP*.5)
        t = Tex("T")\
            .shift(UP)
        o = Tex("O")\
            .shift(UR*3).shift(RIGHT*1.5)
        i = Tex("I")\
            .shift(DOWN*2)
        j = Tex("J")\
            .shift(UL*3)
        l = Tex("L")\
            .shift(UP*3)
        s = Tex("S")\
            .shift(LEFT*4.5)
        z = Tex("Z")\
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