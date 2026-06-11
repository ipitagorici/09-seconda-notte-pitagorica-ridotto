from manim import *

class TetrisUI(Scene):
    def construct(self):
        tetris_ui = ImageMobject("../assets/imgs/Fracella/TetrisUI.png")
        
        full_screen = Rectangle(
            width=config.frame_width + 0.1,
            height=config.frame_height + 0.1,
        )
        
        self.play(FadeIn(tetris_ui))
        
        
        
        self.next_section("Griglia")
        
        grid_highlight = Rectangle(
            color=WHITE,
            width=2.5, height=4.6)\
                .shift(LEFT*0.05)
        grid_overlay = Cutout(
            full_screen,
            grid_highlight,
            fill_color=BLACK,
            fill_opacity=0.75
        )
        self.play(FadeIn(grid_overlay))
        self.wait(2)
        
        
        
        self.next_section("Hold")
        
        hold_highlight = Rectangle(color=WHITE, width=1.2, height=0.9).move_to((-1.9, 1.85, 0))
        hold_overlay = Cutout(
            full_screen,
            hold_highlight,
            fill_color=BLACK,
            fill_opacity=0.75
        )
        self.play(
            FadeOut(grid_overlay),
            Transform(
                grid_highlight,
                hold_highlight,
                replace_mobject_with_target_in_scene=True
            ),
            FadeIn(hold_overlay)
        )
        
        self.wait(2)
        
        
        
        self.next_section("Bag")
        
        bag_highlight = Rectangle(color=WHITE, width=1.15, height=3.65).move_to((1.8, 0.5, 0))
        bag_overlay = Cutout(
            full_screen,
            bag_highlight,
            fill_color=BLACK,
            fill_opacity=0.75
        )
        self.play(
            FadeOut(hold_overlay),
            Transform(
                hold_highlight,
                bag_highlight,
                replace_mobject_with_target_in_scene=True
            ),
            FadeIn(bag_overlay)
        )

        self.wait(2)