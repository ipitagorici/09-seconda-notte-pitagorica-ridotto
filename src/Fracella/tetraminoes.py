from manim import *

class Tetraminoes(Scene):
    def construct(self):
        tetraminoes = ImageMobject("assets/imgs/Fracella/Tetraminoes.png")\
            .scale(0.75)
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
            Write(t),
            Write(o),
            Write(i),
            Write(j),
            Write(l),
            Write(s),
            Write(z),
        ))
        
        
        
        self.wait(2)