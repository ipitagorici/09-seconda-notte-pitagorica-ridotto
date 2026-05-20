#
# PROVARE A METTERE BOHELD TEXT
#



from manim import *

WIDTH_OFFSET = 3

class Speaker():
    def __init__(self, name, description):
        self.name = name
        self.description = description

class SpeakerDisplay(Scene):
    def init_new_scene(self, title):
        self.next_section(title)
        self.remove(*self.mobjects)
    
    def fib(self, n):
        if n == 0 or n == 1:
            return 1
        
        return self.fib(n - 1) + self.fib(n - 2)

    def construct(self):
        speakers = [
            Speaker("Cottignoli Marco", "La Nascita dell'Open Source"),
            Speaker("Fracella Pietro", "Tetris"),
            Speaker("Ryan Zullo", "Boids: Una Poesia nel Cielo"),
            Speaker("Zarri Nicolò", "La Chiave"),
            Speaker("Zarri Nicolò", "Il suono della chiave"),
            Speaker("Battaglia di funzioni", r"con la partecipazione di:\\Marco, Giacomo, Nicolas, Lorenzo, Giulia\&Lara"),
        ]

        # Creazione oggetti - Serie di Fibonacci e Golden Ratio
        squares = VGroup(Square(1 * 0.3))
        next_dir = [RIGHT, UP, LEFT, DOWN]
        FSeq = [ ]
        for n in range(1, 12):
            FSeq.append(self.fib(n))

        for j, i in enumerate(FSeq):
            d = next_dir[j % 4]
            squares.add(Square(i * 0.3).next_to(squares, d, buff=0))

        squares.center().scale_to_fit_width(self.camera.frame_width)
        squares.set_stroke(color=GRAY, width=.25).set_z_index(-1)

        direction = [1, -1, -1, 1]
        corner = [[UL, -UL], [UR, -UR]]
        spiral = VGroup()

        for j, i in enumerate(squares):
            c = corner[j % 2]
            d = direction[j % 4]
            arc = ArcBetweenPoints(
                i.get_corner(c[0]),
                i.get_corner(c[1]),
                angle=PI / 2 * d,
                stroke_width=1
            )
            if direction[j % 4] != 1:
                arc = arc.reverse_direction()
            spiral.add(arc)

        spiral.set_color(ManimColor("#82001eab"))\
            .set_z_index(-1)\

        fibonacci = VGroup(squares, spiral).add_updater(lambda m, dt: m.scale(1 + 0.1 * dt))
        
        for speaker in speakers:
            self.init_new_scene(speaker.name)

            name = Text(speaker.name).scale_to_fit_width(self.camera.frame_width - WIDTH_OFFSET)
            description = Tex(rf"\textsc{{{speaker.description}}}").scale(1.1)
            both = VGroup(name, description)\
                .arrange_in_grid(rows=2)\
                .center()
            
            self.play(Write(name), run_time=2)
            self.play(FadeIn(description, shift=UP * .3))
            for square in fibonacci[0]:
                self.play(Create(square, run_time=0.2))
            
            self.play(Create(fibonacci[1]), run_time=2)
            self.wait()