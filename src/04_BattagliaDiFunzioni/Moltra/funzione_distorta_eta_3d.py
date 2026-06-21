from manim import *
import numpy as np

class SurfacePlotPositiveRotate(ThreeDScene):
    def construct(self):
        # 1. Restrict axes to the positive quadrant
        axes = ThreeDAxes(
            x_range=[0, 4, 1],
            y_range=[0, 4, 1],
            z_range=[-5, 5, 1],
            x_length=6,
            y_length=6,
            z_length=6
        )

        # 2. Define the parameterized surface
        def param_surface(u, v):
            x = u
            y = v
            
            denominator = x**3 * y + 0.1
            
            if abs(denominator) < 1e-4:
                denominator = 1e-4 if denominator > 0 else -1e-4
                
            z = (np.sin(x * y) + np.cos(x**3)) / denominator
            
            # Clip the z-axis
            z = np.clip(z, -5, 5)
            
            return axes.c2p(x, y, z)

        # 3. Restrict the surface mesh to positive u and v values
        surface = Surface(
            param_surface,
            u_range=[0, 4], 
            v_range=[0, 4], 
            resolution=(40, 40) 
        )
        
        surface.set_style(fill_opacity=0.8, fill_color=ORANGE, stroke_color=WHITE, stroke_width=0.5)

        # 4. Animate the scene
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        
        self.play(Create(axes))
        self.play(Create(surface), run_time=3)
        self.wait()
        
        # First pan to the side
        self.move_camera(phi=60 * DEGREES, theta=135 * DEGREES, run_time=3)
        self.wait(0.5)
        
        # Rotate 90 degrees more at the end (135 + 90 = 225 degrees)
        self.move_camera(theta=225 * DEGREES, run_time=3)
        self.wait(2)