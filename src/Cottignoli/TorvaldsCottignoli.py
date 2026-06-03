from manim import *

class TorvaldsCottignoli(Scene):
    def construct(self):
        inactive_opcaity = 0.2
        active_opcaity = 1

        torvalds = ImageMobject("../assets/imgs/Cottignoli/Torvalds.png").set_opacity(inactive_opcaity)\
            .scale(0.25)\
            .shift(LEFT*3)
        cottignoli = ImageMobject("../assets/imgs/Relatori/Cottignoli.png").set_opacity(active_opcaity)\
            .scale(0.3)\
            .shift(RIGHT*3)

        self.play(FadeIn(torvalds), FadeIn(cottignoli))
        
    

        self.next_section("Torvalds talking 1")
        
        self.play(torvalds.animate.set_opacity(1), cottignoli.animate.set_opacity(inactive_opcaity))
        
    

        self.next_section("Cottignoli talking 2")
        
        self.play(torvalds.animate.set_opacity(inactive_opcaity), cottignoli.animate.set_opacity(1))



        self.next_section("Torvalds talking 2")
        
        self.play(torvalds.animate.set_opacity(1), cottignoli.animate.set_opacity(inactive_opcaity))
        
    

        self.next_section("Cottignoli talking 3")
        
        self.play(torvalds.animate.set_opacity(inactive_opcaity), cottignoli.animate.set_opacity(1))



        self.next_section("Torvalds talking 3")
        
        self.play(torvalds.animate.set_opacity(1), cottignoli.animate.set_opacity(inactive_opcaity))
        
    

        self.next_section("Cottignoli talking 4")
        
        self.play(torvalds.animate.set_opacity(inactive_opcaity), cottignoli.animate.set_opacity(1))



        self.next_section("Torvalds talking 4")
        
        self.play(torvalds.animate.set_opacity(1), cottignoli.animate.set_opacity(inactive_opcaity))
        
    

        self.next_section("Cottignoli talking Final")
        
        self.play(torvalds.animate.set_opacity(inactive_opcaity), cottignoli.animate.set_opacity(1))


        self.wait(2)