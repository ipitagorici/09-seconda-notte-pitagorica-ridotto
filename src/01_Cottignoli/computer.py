from manim import *

class Computer(Scene):
	def construct(self):
		computer = ImageMobject("../assets/imgs/Cottignoli/Computer.png")
  
		self.play(FadeIn(computer))
  
  
		self.wait(2)