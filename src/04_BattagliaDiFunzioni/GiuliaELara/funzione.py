from manim import *
from math import sqrt

class Funzione(Scene):
    def construct(self) -> None:
        ################
        ### MOBJECTS ###
        ################
        
        t_track = ValueTracker(1.0)
        d_track = ValueTracker(1.0)
        l_track = ValueTracker(1.0)

        axes = Axes(
            x_range=[-2, 6, 2], x_length=7,
            y_range=[-2, 6, 2], y_length=7,
            tips=False
        ).to_edge(LEFT)

        axes_values = VGroup(
            Tex("y = frequenza"),
            Tex("x = modo armonico")
        ).to_corner(UR).arrange_in_grid(rows=3, cell_alignment=RIGHT)

        variables = always_redraw(lambda: 
            VGroup(
                Tex(f"tensione = {t_track.get_value():.2f}", color=RED),
                Tex(f"densità = {d_track.get_value():.2f}", color=GREEN),
                Tex(f"lunghezza = {l_track.get_value():.2f}", color=BLUE)
            ).to_edge(RIGHT).arrange_in_grid(rows=3, cell_alignment=RIGHT).shift(DOWN)
        )

        def get_plot():
            t = t_track.get_value()
            d = d_track.get_value()
            l = l_track.get_value()
            
            coeff = (d / 2) * l
            
            if coeff <= 0 or t <= 0:
                start_x = 0.0001
            else:
                start_x = t * (coeff ** 2) / 36
            
            start_x = min(start_x, 5.9)

            func = lambda x: (d / 2 * l) * sqrt(t / x)
            
            plot = axes.plot(
                func, 
                x_range=[start_x, 6, 0.01],
                use_smoothing=True
            )

            # Wrap the plot in CurvesAsSubmobjects before applying the gradient
            return CurvesAsSubmobjects(plot).set_color_by_gradient(RED, GREEN, BLUE)

        dynamic_graph = always_redraw(get_plot)



        ##################
        ### ANIMATIONS ###
        ##################

        self.play(
            Create(axes),
            FadeIn(axes_values[0]), FadeIn(axes_values[1])
        )



        self.next_section("function_appears")

        self.play(Write(variables))
        self.play(Create(dynamic_graph))



        self.next_section("changing_parameters")
        
        self.play(
            t_track.animate.set_value(5),
            d_track.animate.set_value(1),
            l_track.animate.set_value(1),
            run_time=2
        )

        self.play(
            t_track.animate.set_value(1),
            d_track.animate.set_value(5),
            l_track.animate.set_value(1),
            run_time=2
        )

        self.play(
            t_track.animate.set_value(1),
            d_track.animate.set_value(1),
            l_track.animate.set_value(5),
            run_time=2
        )

        self.play(
            t_track.animate.set_value(4),
            d_track.animate.set_value(3),
            l_track.animate.set_value(2),
            run_time=2
        )

        self.play(
            t_track.animate.set_value(2),
            d_track.animate.set_value(5),
            l_track.animate.set_value(1),
            run_time=2
        )

        self.play(
            t_track.animate.set_value(2),
            d_track.animate.set_value(4),
            l_track.animate.set_value(1),
            run_time=2
        )

        self.play(
            t_track.animate.set_value(1),
            d_track.animate.set_value(1),
            l_track.animate.set_value(1)
        )


        self.wait(2)