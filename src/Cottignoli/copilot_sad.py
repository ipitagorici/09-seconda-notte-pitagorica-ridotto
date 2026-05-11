from manim import *

class CopilotSad(Scene):
    def construct(self):
        copilot = ImageMobject("assets/imgs/Cottignoli/Copilot.png")\
            .scale(0.25)\
            .shift(LEFT)
        sad = Tex(":(", font_size=100)\
            .next_to(copilot, RIGHT)
        
        self.play(FadeIn(copilot), Write(sad))
        
        
        self.wait(2)