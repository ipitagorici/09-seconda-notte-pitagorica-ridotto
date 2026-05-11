from manim import *

class TorvaldsCottignoli(Scene):
    def construct(self):
        torvalds = ImageMobject("assets/imgs/Cottignoli/Torvalds.png").set_opacity(0.3)\
            .shift(LEFT*3)
        cottignoli = ImageMobject("assets/imgs/Cottignoli/Cottignoli.png").set_opacity(0.3)\
            .scale(0.3)\
            .shift(RIGHT*3)

        self.play(FadeIn(torvalds), FadeIn(cottignoli))
        
    

        self.next_section("Torvalds talking")
        
        
        
        self.play(cottignoli.animate.set_opacity(0.3))
        self.play(torvalds.animate.set_opacity(1))
        
        
        
        self.next_section("Cottignoli talking")
        
        
        
        self.play(torvalds.animate.set_opacity(0.3))
        self.play(cottignoli.animate.set_opacity(1))         