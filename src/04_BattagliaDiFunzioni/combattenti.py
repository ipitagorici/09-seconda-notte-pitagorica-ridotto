from manim import *
import random

class Combattenti(Scene):
    def construct(self):
        cttmlt_1 = ImageMobject("../assets/imgs/BattagliaDiFunzioni/Intro/CottMoltra1.png")\
                .scale_to_fit_height(config.frame_height)\
                .scale_to_fit_width(config.frame_width)
        cttmlt_2 = ImageMobject("../assets/imgs/BattagliaDiFunzioni/Intro/CottMoltra2.png")\
                .scale_to_fit_height(config.frame_height)\
                .scale_to_fit_width(config.frame_width)

        rmgcmpzrr_1 = ImageMobject("../assets/imgs/BattagliaDiFunzioni/Intro/RomaCampoZar1.png")\
                .scale_to_fit_height(config.frame_height)\
                .scale_to_fit_width(config.frame_width)
        rmgcmpzrr_2 = ImageMobject("../assets/imgs/BattagliaDiFunzioni/Intro/RomaCampoZar2.png")\
                .scale_to_fit_height(config.frame_height)\
                .scale_to_fit_width(config.frame_width)

        glalra_1 = ImageMobject("../assets/imgs/BattagliaDiFunzioni/Intro/GiuliLara1.png")\
                .scale_to_fit_height(config.frame_height)\
                .scale_to_fit_width(config.frame_width)
        glalra_2 = ImageMobject("../assets/imgs/BattagliaDiFunzioni/Intro/GiuliLara2.png")\
                .scale_to_fit_height(config.frame_height)\
                .scale_to_fit_width(config.frame_width)

        pairs = [
            (cttmlt_1, cttmlt_2),
            (rmgcmpzrr_1, rmgcmpzrr_2),
            (glalra_1, glalra_2)
        ]

        

        for i in range(18):
            pair = pairs[i%3]
            img_a, img_b = pair
            
            self.add(img_a)
            self.wait(0.5)
            self.remove(img_a)
            
            self.add(img_b)
            self.wait(0.5)
            self.remove(img_b)