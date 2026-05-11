from manim import *

class KernelCreation(Scene):
    def construct(self):
        timeline = Line((-7,3,0), (7,3,0))
        
        self.play(Create(timeline))
        
        
        
        self.next_section("Name")
        
        
        
        name_line = Line((-6, 3.2, 0), (-6, 2.8, 0))
        name_date = Tex("1991").set_color(RED)\
            .next_to(name_line, UP)
        name = Tex("Linux").next_to(name_line, DOWN)
        name_origin = Tex(r"Linus\\+\\Unix").set_color(GREEN)\
            .next_to(name, DOWN*3)
        
        self.play(Succession(
            Create(name_date),
            Wait(0.1),
            Create(name_line),
            Wait(0.1),
            Write(name),
            Write(name_origin)
        ))
 
        
        
        
        self.next_section("post")
        
        
        
        
        post_line = Line((-3.8, 3.2, 0), (-3.8, 2.8, 0))
        post_date = Tex("Agosto").set_color(RED)\
            .next_to(post_line, UP)
        site = Tex(r"comp.os\\.minix").next_to(post_line, DOWN)
        post = Tex(r"Sistema\\operativo\\gratis").set_color(GREEN)\
            .next_to(site, DOWN*3)
        
        self.play(Succession(
            Create(post_date),
            Wait(0.1),
            Write(post_line),
            Wait(0.1),
            Write(site),
            Wait(0.3),
            Write(post)
        ))
        
        
        
        self.next_section("first release")
        
        
        
        first_release_line = Line((-1.6, 3.2, 0), (-1.6, 2.8, 0))
        first_release_date = Tex("Settembre").set_color(RED)\
            .next_to(first_release_line, UP)
        first_release = Tex("0.0.1").set_color(BLUE)\
            .next_to(first_release_line, DOWN)
        
        self.play(Succession(
            Create(first_release_date),
            Wait(0.1),
            Write(first_release_line),
            Wait(0.1),
            Write(first_release),
        ))
        
        
        
        self.next_section("first official release")
        
        
        
        first_or_line = Line((0.6, 3.2, 0), (0.6, 2.8, 0))
        first_or_date = Tex("Ottobre").set_color(RED)\
            .next_to(first_or_line, UP)
        first_or = Tex("0.02").set_color(BLUE)\
            .next_to(first_or_line, DOWN)
            
        self.play(Succession(
            Create(first_or_date),
            Wait(0.1),
            Write(first_or_line),
            Wait(0.1),
            Write(first_or),
        ))
        
        
        
        self.next_section("gpl")
        
        
        
        gpl_line = Line((2.8, 3.2, 0), (2.8, 2.8, 0))
        gpl_date = Tex("Gennaio").set_color(RED)\
            .next_to(gpl_line, UP)
        gpl_version = Tex("0.12").set_color(BLUE)\
            .next_to(gpl_line, DOWN)
        gpl = Tex(r"Adotta\\la GPL").set_color(GREEN)\
            .next_to(gpl_version, DOWN*3)
            
        self.play(Succession(
            Create(gpl_date),
            Wait(0.1),
            Write(gpl_line),
            Wait(0.1),
            Write(gpl_version),
            Wait(0.3),
            Write(gpl)
        ))
        
        
        
        self.next_section("1.0")
        
        
        
        one_line = Line((5.9, 3.2, 0), (5.9, 2.8, 0))
        one_date = Tex("Marzo 94").set_color(RED)\
            .next_to(one_line, UP)
        one = Tex("1.0", font_size=100).set_color(BLUE)\
            .next_to(one_line, DOWN) 
            
        self.play(Succession(
            Create(one_date),
            Wait(0.1),
            Write(one_line),
            Wait(0.1),
            Write(one),
        )) 
        
        
        self.play(Flash(one, flash_radius=0.5), one.animate.set_color(GOLD)) 
        
        
        self.wait(2)