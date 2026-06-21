from manim import *

class PoincarePitagorine(Scene):
    def construct(self):
        phrases = {
            "ricci": (
                Tex(r"L'uomo di scienza non studia la natura perché ciò è utile;\\"
                r"la studia perché ci prova gusto,\\" +
                r"e ci prova gusto perché la natura è bella.\\"
                r"Se la natura non fosse bella, non varrebbe la pena conoscerla,\\"
                r"né varrebbe la pena vivere la nostra vita",
                font_size=50)
            ),
            "baldini": (
                Tex(r"Non intendo parlare, naturalmente,\\" +
                r"di quella bellezza che colpisce i sensi,\\"
                r"della bellezza delle apparenze qualitative;\\"
                r"non che la disdegni, tutt'altro,\\"
                r"ma essa non ha niente a che vedere con la scienza\\",
                font_size=50)
            ),
            "pavirani": (
                Tex(r"Essa dà un corpo, uno scheletro per così dire,\\"
                r"alle cangianti apparenze che deliziano i nostri sensi,\\"
                r"e senza questo sostegno la bellezza di quei sogni fugaci\\" +
                r"non sarebbe che imperfetta\\"
                r"perché confusa e sempre fuggitiva\\",
                font_size=50)
            )
        }



        self.next_section("ricci")
        
        self.play(Write(phrases["ricci"]))



        self.next_section("baldini")

        self.play(FadeOut(phrases["ricci"]))
        self.play(Write(phrases["baldini"]))



        self.next_section("pavirani")

        self.play(FadeOut(phrases["baldini"]))
        self.play(Write(phrases["pavirani"]))


        self.wait(2)