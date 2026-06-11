from manim import *

class GPLLink(Scene):
    def construct(self):
        gpl_link = Tex("https://www.gnu.org/licenses/old-licenses/gpl-1.0", font_size=60)\
            .set_color(BLUE)
        gpl_link_u = Underline(gpl_link)\
            .set_color(BLUE)
            
        self.play(Write(gpl_link), Create(gpl_link_u, run_time=2))
        
        
        self.wait(2)