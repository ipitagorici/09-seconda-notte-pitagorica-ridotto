from manim import *

class TetrisUI(Scene):
    def construct(self):
        tetris_ui = ImageMobject("assets/imgs/Fracella/TetrisUI.png")
        
        self.play(FadeIn(tetris_ui))
        
        
        self.wait(2)