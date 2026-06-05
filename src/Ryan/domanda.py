from manim import *

class Domanda(Scene):
    def construct(self):
        domanda = Text("Cosa succede\nquando ogni individuo\nrinuncia ad un po' del suo io\nper diventare parte\ndi qualcosa di più grande?",
                    font_size=60)
        
        self.play(AddTextLetterByLetter(domanda, time_per_char=0.125))
        
        
        self.wait(2)