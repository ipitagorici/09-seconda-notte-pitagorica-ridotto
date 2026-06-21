from manim import *
from custom_mobjects.BoheldText import BoheldText
from custom_mobjects.Tetraktys import Tetraktys

class DiscorsoFinale(Scene):
    def construct(self):
        frase_lat = VGroup(
            BoheldText("Homo sum."),
            BoheldText("Humani nihil"),
            BoheldText("a me alienum puto")
        ).arrange_in_grid(rows=3).to_edge(UP)
        frase_ita = Tex(r"Sono umano.\\Nulla di umano\\mi è estraneo")\
            .to_edge(DOWN)
        pytagoricum = Tetraktys().scale(0.5).shift(DOWN*0.5)



        self.next_section("latino")

        self.play(Write(frase_lat, run_time=3))



        self.next_section("italiano")

        self.play(Write(frase_ita, run_time=3))

        self.wait(2)

        self.play(FadeIn(pytagoricum))


        self.wait(2)