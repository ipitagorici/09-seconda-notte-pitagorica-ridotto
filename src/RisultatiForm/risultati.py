from manim.animation.creation import Create, Write
from manim.animation.fading import FadeIn, FadeOut
from manim.animation.growing import SpinInFromNothing
from manim.constants import DOWN, UP
from manim.mobject.text.tex_mobject import Tex, Title
from manim.mobject.types.vectorized_mobject import VGroup
from manim.scene.scene import Scene
from manim.utils.color.manim_colors import BLUE, RED, YELLOW 

class Risultati(Scene):
    def construct(self) -> None:
        title = Title("Classifica Battaglia di Funzioni")

        ranking_types = VGroup(
            Tex(r"Voto più comune\\per ogni domanda"),
            Tex(r"Numero totale di 5\\ricevuti in tutte le domande"),
            Tex(r"Numero totale di 1\\ricevuti in tutte le domande"),
            Tex(r"Voto medio\\per ogni domanda"),
        )
            
        ranking_grids = VGroup(
            VGroup(
                Tex("Relatore", font_size=30, color=BLUE), Tex("Interessante", font_size=30, color=BLUE), Tex("Originalità", font_size=30, color=BLUE), Tex("Esposizione", font_size=30, color=BLUE), Tex("Pitagorismo", font_size=30, color=BLUE), Tex("Totale", font_size=30, color=BLUE), 
                Tex("Cottignoli", font_size=40, color=RED), Tex("4"), Tex("5"), Tex("5"), Tex("5"), Tex("19", color=YELLOW), 
                Tex("Zarri", font_size=40, color=RED), Tex("5"), Tex("5"), Tex("4"), Tex("5"), Tex("19", color=YELLOW), 
                Tex("Moltrasio", font_size=40, color=RED), Tex("5"), Tex("3"), Tex("4"), Tex("5"), Tex("17", color=YELLOW), 
                Tex("Camporesi", font_size=40, color=RED), Tex("5"), Tex("5"), Tex("5"), Tex("5"), Tex("20", color=YELLOW), 
                Tex(r"Giulia\&Lara", font_size=40, color=RED), Tex("5"), Tex("5"), Tex("4"), Tex("5"), Tex("19", color=YELLOW), 
                Tex("Romagnoli", font_size=40, color=RED), Tex("5"), Tex("5"), Tex("5"), Tex("5"), Tex("20", color=YELLOW), 
            ).arrange_in_grid(rows=7, columns=6).scale(0.80),
            VGroup (
                Tex("Relatore", font_size=30, color=BLUE), Tex("Cottignoli", font_size=40, color=RED), Tex("Zarri", font_size=40, color=RED), Tex("Moltrasio", font_size=40, color=RED), Tex("Camporesi", font_size=40, color=RED), Tex(r"Giulia\&Lara", font_size=40, color=RED), Tex("Romagnoli", font_size=40, color=RED), 
                Tex("5 ricevuti", font_size=30, color=BLUE), Tex("89"), Tex("88"), Tex("79"), Tex("86"), Tex("81"), Tex("107"), 
            ).arrange_in_grid(rows=2, columns=7).scale(0.8),
            VGroup(
                Tex("Relatore", font_size=30, color=BLUE), Tex("Cottignoli", font_size=40, color=RED), Tex("Zarri", font_size=40, color=RED), Tex("Moltrasio", font_size=40, color=RED), Tex("Camporesi", font_size=40, color=RED), Tex(r"Giulia\&Lara", font_size=40, color=RED), Tex("Romagnoli", font_size=40, color=RED), 
                Tex("1 ricevuti", font_size=30, color=BLUE), Tex("2"), Tex("0"), Tex("0"), Tex("17"), Tex("7"), Tex("0"), 
            ).arrange_in_grid(rows=2, columns=7).scale(0.8),
            VGroup(
                Tex("Relatore", font_size=30, color=BLUE), Tex("Interessante", font_size=30, color=BLUE), Tex("Originalità", font_size=30, color=BLUE), Tex("Esposizione", font_size=30, color=BLUE), Tex("Pitagorismo", font_size=30, color=BLUE), Tex("Media", font_size=30, color=BLUE), 
                Tex("Cottignoli", font_size=40, color=RED), Tex("3.9"), Tex("4.1"), Tex("3.9"), Tex("4.0"), Tex("3.975", color=YELLOW), 
                Tex("Zarri", font_size=40, color=RED), Tex("4.1"), Tex("4.1"), Tex("3.8"), Tex("4.0"), Tex("4.0", color=YELLOW), 
                Tex("Moltrasio", font_size=40, color=RED), Tex("4.0"), Tex("3.8"), Tex("3.8"), Tex("4.1"), Tex("3.925", color=YELLOW), 
                Tex("Camporesi", font_size=40, color=RED), Tex("3.6"), Tex("3.9"), Tex("3.6"), Tex("3.9"), Tex("3.75", color=YELLOW), 
                Tex(r"Giulia\&Lara", font_size=40, color=RED), Tex("3.8"), Tex("3.8"), Tex("3.7"), Tex("4.0"), Tex("3.825", color=YELLOW), 
                Tex("Romagnoli", font_size=40, color=RED), Tex("4.7"), Tex("4.1"), Tex("4.1"), Tex("4.3"), Tex("4.3", color=YELLOW), 
            ).arrange_in_grid(rows=7, columns=6).scale(0.80),
        )
        
        winners = VGroup(
            Tex("ROMAGNOLI E CAMPORESI", font_size=60, color=YELLOW),
            Tex("ROMAGNOLI", font_size=75, color=YELLOW),
            Tex("CAMPORESI", font_size=75, color=YELLOW),
            Tex("ROMAGNOLI", font_size=75, color=YELLOW),
        ).to_edge(DOWN).shift(DOWN*0.25)
        winner_texts = VGroup(
            Tex("Vincitore:"),
            Tex("Vincitore:"),
            Tex("Perdente:"),
            Tex("Vincitore definitivo:"),
        )



        ##################
        ##  ANIMATIONS  ##
        ##################
        
        self.next_section("title")
        self.play(Create(title))
        self.wait(0.5)

        for i, (ranking_type, ranking_grid, winner_text, winner) in enumerate(zip(ranking_types, ranking_grids, winner_texts, winners)):
            self.next_section(f"{ranking_type}")
            
            ranking_type.next_to(title, DOWN, buff=0.5)
            ranking_grid.next_to(ranking_type, DOWN, buff=0.5)
            winner_text.next_to(winner, UP)
    
            self.play(Write(ranking_type))
            self.wait(1)
            self.play(Create(ranking_grid))
    
            self.wait(1)
    
            self.play(FadeIn(winner_text))
            self.play(SpinInFromNothing(winner))
            self.wait(2)

            self.play(FadeOut(ranking_type, ranking_grid, winner_text, winner, shift=UP))

        self.play(FadeIn(Tex(r"GRAZIE\\DELLA PARTECIPAZIONE", font_size=100, color=YELLOW)))
        
        
        self.wait(2)