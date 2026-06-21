from manim import *
from custom_mobjects.BoheldText import BoheldText
from custom_mobjects.Tetraktys import Tetraktys

class PoincareCompleto(Scene):
    def construct(self):
        poincare = VGroup(
            BoheldText("L'uomo di scienza non studia la natura perché ciò è utile;\n"
                "la studia perché ci prova gusto,\n" +
                "e ci prova gusto perché la natura è bella.\n"
                "Se la natura non fosse bella, non varrebbe la pena conoscerla,\n"
                "né varrebbe la pena vivere la nostra vita",
                font_size=20).to_corner(UL),
            BoheldText("Non intendo parlare, naturalmente,\n" +
                "di quella bellezza che colpisce i sensi,\n"
                "della bellezza delle apparenze qualitative;\n"
                "non che la disdegni, tutt'altro,\n"
                "ma essa non ha niente a che vedere con la scienza",
                font_size=20).move_to(ORIGIN),
            BoheldText("Essa dà un corpo, uno scheletro per così dire,\n"
                "alle cangianti apparenze che deliziano i nostri sensi,\n"
                "e senza questo sostegno la bellezza di quei sogni fugaci\n" +
                "non sarebbe che imperfetta\n"
                "perché confusa e sempre fuggitiva\n",
                font_size=20).to_corner(DR)
        )

        decorations = Group(
            Tetraktys().scale(0.35).to_corner(UR),
            Tetraktys().scale(0.35).to_corner(DL)
        )

        self.play(FadeIn(decorations))
        self.play(Write(poincare))


        self.wait(2)