from manim import *

class Tetris(Scene):
    def construct(self):
        tetris = ImageMobject("../assets/imgs/Fracella/Tetris.png")\
            .scale(0.75)
        
        self.play(FadeIn(tetris))
        
        
        self.wait(2)