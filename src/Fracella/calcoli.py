from manim import *

class Calcoli(Scene):
    def construct(self):
        grid = ImageMobject("../assets/imgs/Fracella/Grid.png")\
            .shift(LEFT*2.5)
        
        self.play(FadeIn(grid))
        
        step_1 = Tex(r"4 righe\\pulibili con\\10 pezzi")\
            .to_corner(UR)
            
        step_2 = Tex(r"Bag formata\\da 7 pezzi")\
            .next_to(step_1, DOWN)
        
        step_3 = Tex(r"mcm(7, 10) = 70")\
            .next_to(step_2, DOWN)
            
        self.play(Write(step_1))
        
        
        
        self.next_section("step 2")
        
        self.play(Write(step_2))
        
        
        
        self.next_section("step 3")
        
        self.play(Write(step_3))