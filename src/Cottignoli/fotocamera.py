from manim import *

class Fototcamera(Scene):
    def construct(self):
        fotocamera = ImageMobject("../assets/imgs/Cottignoli/SonyCamera.png")\
            .scale(0.5)
        
        self.play(FadeIn(fotocamera))
        
        
        self.wait(2)