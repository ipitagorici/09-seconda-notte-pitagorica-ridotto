from manim.animation.creation import Create
from manim.mobject.text.tex_mobject import Tex, Title
from manim.mobject.types.vectorized_mobject import VGroup
from manim.scene.scene import Scene
from manim.utils.color.manim_colors import BLUE, WHITE

def from_dict_to_vgroup_grid(dict: dict, rows, columns, key_color=BLUE, value_color=WHITE) -> VGroup:
    vgroup = VGroup()
    for key, value in dict.items():
        key_tex = Tex(f"{key}:", color=key_color)
        value_tex = Tex(value, color=value_color)
        
        vgroup.add(key_tex, value_tex)

    vgroup.arrange_in_grid(rows=rows, columns=columns)

    return vgroup

class Combattenti(Scene):
    def construct(self) -> None:
        title = Title("Combattenti della Battaglia di Funzioni")

        names = {
            "Cottignoli Marco": "Uncanny Valley",
            "Zarri Giacomo": "Effetto Dunning-Kruger",
            "Moltrasio Nicolas": "Percezione dle tempo",
            "Camporesi Lorenzo": "Funzioni nel calcio",
            r"Giulia\&Lara": "Corde di uno strumento",
            "Romagnoli Samuele": "Attrattore di Lorenz"
        }

        names_grid = from_dict_to_vgroup_grid(names, 6, 2)



        self.next_section("title")

        self.play(Create(title))



        self.next_section("combattenti")

        self.play(Create(names_grid))


        self.wait(2)