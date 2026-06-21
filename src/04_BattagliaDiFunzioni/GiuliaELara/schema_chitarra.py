from manim import *

class SchemaChitarra(Scene):
    def construct(self):
        chitarra = ImageMobject("../assets/imgs/BattagliaDiFunzioni/GiuliaELara/Chitarra.png")\
            .scale(0.5).to_edge(LEFT)

        variabili = VGroup(
            Tex("Tensione"),
            Tex("Densità"),
            Tex("Lunghezza"),
            Tex("Modo Armonico")
        ).arrange_in_grid(rows=4, cell_alignements=RIGHT)

        unison = Tex("]", font_size=200).next_to(variabili, RIGHT)
        equals = Tex("=", font_size=50).next_to(unison, RIGHT)

        risultato = Tex("Frequenza", font_size=75).next_to(equals, RIGHT)

        self.play(FadeIn(chitarra))
        self.play(Write(variabili))
        self.play(Create(unison), Create(equals))
        self.play(SpinInFromNothing(risultato))


        self.wait(2)