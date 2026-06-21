from manim import *

class RelatoriEntrata(Scene):
    def construct(self):
        relatori = ["Cottignoli", "Fracella", "Ryan", "Zarri"]


        for r in relatori: 
            self.next_section(r)

            bg = ImageMobject(f"../assets/imgs/Relatori/{r}/bg.png")\
                .scale_to_fit_height(config.frame_height)\
                .scale_to_fit_width(config.frame_width)
            first = ImageMobject(f"../assets/imgs/Relatori/{r}/{r}_destra.png").scale(0.2)\
                .to_corner(DR).shift(DOWN*0.5)
            second = ImageMobject(f"../assets/imgs/Relatori/{r}/{r}2_destra.png").scale(0.2)\
                .next_to(first, LEFT)

            self.add(bg)

            for i in range(0, 5):
                if i == 0:
                    self.play(FadeIn(first))
                else:
                    self.play(FadeOut(second), FadeIn(first))
                second.next_to(first, LEFT)
                self.play(FadeOut(first), FadeIn(second))
                first.next_to(second, LEFT)