from manim import *

class Calcoli(Scene):
    def construct(self):
        grid = ImageMobject("../assets/imgs/Fracella/Grid.png")\
            .shift(LEFT*2.5).set_opacity(2)
        
        step_1 = Tex(r"4 righe\\pulibili con\\10 pezzi")\
            .to_corner(UR)
            
        step_2 = Tex(r"Bag formata\\da 7 pezzi")\
            .next_to(step_1, DOWN*2)
        
        self.play(FadeIn(grid))
        
        
        
        self.next_section("step_1")
        
        full_screen = Rectangle(
            width=config.frame_width + 0.1,
            height=config.frame_height + 0.1,
        )
        fourlane_highlight = Rectangle(
            color=WHITE,
            width=2.5, height=1)\
                .shift(LEFT*2.5).shift(DOWN*1.85)
        fourlane_overlay = Cutout(
            full_screen,
            fourlane_highlight,
            fill_color=BLACK,
            fill_opacity=0.75
        )
        
        self.play(FadeIn(fourlane_overlay))
        self.play(Write(step_1))
        
        
        
        self.next_section("step 2")
        
        bag = ImageMobject("../assets/imgs/Fracella/Bag.png")\
            .shift(UP*1.5)
        more_bag = ImageMobject("../assets/imgs/Fracella/MoreBag.png")\
            .shift(DOWN*1.5)
        plus = Tex("+")\
            .shift(DOWN*0.5)
        
        bag_highlight = Rectangle(
            color=WHITE,
            width=1.25, height=5.5)\
                .shift(UP*0.5)
        bag_overlay = Cutout(
            full_screen,
            bag_highlight,
            fill_color=BLACK,
            fill_opacity=0.75
        )
        
        self.play(FadeOut(grid), FadeOut(fourlane_overlay))
        self.play(FadeIn(bag), FadeIn(more_bag), FadeIn(plus))
        
        self.play(FadeIn(bag_overlay))
        self.play(Write(step_2))
        
        
        
        self.next_section("step 3")
        
        self.play(FadeOut(bag, more_bag, plus, bag_overlay))
        
        self.play(
            step_1.animate.move_to(ORIGIN+(0, 2, 0)),
            step_2.animate.move_to(ORIGIN)
        )
        
        step_3 = Tex(r"mcm(7, 10)\\70")\
            .set_color(RED)\
            .next_to(step_2, DOWN*2)
        self.play(Write(step_3))
        self.play(Flash(step_3, flash_radius=1))
        
        
        self.wait(2)