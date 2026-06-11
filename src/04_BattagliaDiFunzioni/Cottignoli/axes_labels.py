from manim import *

class AxesLabels(Scene):
    def construct(self):
        axes_labels = ImageMobject("../assets/imgs/BattagliaDiFunzioni/Cottignoli/AxesLabels.png")
        
        self.play(FadeIn(axes_labels))
        
        
        self.wait(2)