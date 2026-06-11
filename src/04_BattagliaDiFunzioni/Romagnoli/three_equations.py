from manim import *

class ThreeEquations(Scene):
    def construct(self):
        first = Text(r"dx/dt = σ(y − x)")\
            .shift(UP*2)
        second = Text(r"dy/dt = x(ρ − z) − y")
        third = Text(r"dz/dt = xy − βz")\
            .shift(DOWN*2)
            
            
        self.play(Write(first),
                  Write(second),
                  Write(third),
                  run_time=2
        )
        
        
        self.wait(2)