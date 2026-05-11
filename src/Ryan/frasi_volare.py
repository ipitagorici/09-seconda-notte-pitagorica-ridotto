from manim import *

class FrasiVolare(Scene):
    def construct(self):
        frase1 = Tex("Come sarebbe bello volare con loro")\
            .shift(UP*2)
        
        self.play(Write(frase1))
        
        
        
        self.next_section("frase1+2")
        
        
        
        frase2 = Tex("Come sarebbe bello volare con loro")\
            .next_to(frase1, DOWN)
        
        self.play(Write(frase2))
        
        
        
        self.next_section("frase1+2+3")
        
        
        
        frase3 = Tex(r"e\\vedere quello che vedono loro\\e\\capire quello che capiscono loro")\
            .next_to(frase2, DOWN)
            
        self.play(Write(frase3))