from manim import *

class OperatingSystemComponents(Scene):
    def construct(self):
        os = Title("Minimi requisiti per un sistema operativo:")
        
        self.play(Write(os))
        
        
        
        self.next_section("Strumenti di base")
        
        
        
        section = Tex("STRUMENTI DI BASE")\
            .to_corner(UL).shift(DOWN)\
            .set_color(BLUE)
        tools = VGroup(
            Tex("Editor di testo"),
            Tex("Spostare file"),
            Tex("Eseguire file"),
            Tex("...")
        ).arrange(DOWN)\
            .next_to(section, DOWN)
        
        self.play(Write(section))
        for t in tools:
            self.play(Write(t))
        
        
        
        self.next_section("shell")
        
        
        
        section = Tex("SHELL")\
            .to_corner(UR).shift(DOWN).shift(LEFT*1.5)\
            .set_color(BLUE)
        explanation = Tex(r"Strato di interazione\\tra utente e\\sistema operativo")\
            .next_to(section, DOWN)
        
        self.play(Write(section))
        self.play(Write(explanation))
        
        
        
        self.next_section("kernel???")
        
        self.play(FadeIn(
            Tex("?", font_size=300).set_color(GREEN).shift(DOWN*2),
            run_time=3))
        
        
        self.wait(2)