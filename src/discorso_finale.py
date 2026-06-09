from manim import *

class DiscorsoFinale(Scene):
    def construct(self):
        frase_lat = Tex(r"Homo sum\\Humani nihil\\a me alienum puto")\
            .to_edge(UP).shift(DOWN)
        frase_ita = Tex(r"Sono umano\\Nulla di umano\\mi è estraneo")\
            .to_edge(DOWN).shift(UP)



        self.next_section("latino")

        self.play(Write(frase_lat, run_time=3))



        self.next_section("italiano")

        self.play(Write(frase_ita, run_time=3))