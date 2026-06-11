from manim import *

class Fototcamera(Scene):
    def construct(self):
        fotocamera = ImageMobject("../assets/imgs/Cottignoli/Camera.png")\
            .scale(2)
        
        self.play(FadeIn(fotocamera))
        
        
        self.wait(2)