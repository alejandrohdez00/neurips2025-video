"""
SCENE 1: Creative Paradox
Illustrates the tension between originality and coherence in AI creativity
"""

from manim import *


class CreativeParadox(Scene):
    def construct(self):
        # Create two concept circles
        original = Circle(radius=1.5, color=ORANGE).shift(LEFT * 3.5)
        coherent = Circle(radius=1.5, color=TEAL).shift(RIGHT * 3.5)
        
        # Labels
        orig_label = Text("Original", font_size=40).next_to(original, UP)
        coh_label = Text("Coherent", font_size=40).next_to(coherent, UP)
        
        # Visual representations inside circles
        # Original: scattered, diverging arrows
        orig_arrows = VGroup(*[
            Arrow(ORIGIN, direction, color=ORANGE, buff=0)
            for direction in [
                UP + LEFT, UP + RIGHT, DOWN + LEFT, DOWN + RIGHT,
                LEFT, RIGHT, UP, DOWN
            ]
        ]).scale(0.5).move_to(original)
        
        # Coherent: organized grid pattern
        dots = VGroup(*[
            Dot(point, color=TEAL, radius=0.05)
            for point in [
                UP + LEFT, UP, UP + RIGHT,
                LEFT, ORIGIN, RIGHT,
                DOWN + LEFT, DOWN, DOWN + RIGHT
            ]
        ]).scale(0.5).move_to(coherent)
        
        lines = VGroup(*[
            Line(dots[i], dots[j], color=TEAL, stroke_width=2)
            for i, j in [(0,1),(1,2),(3,4),(4,5),(6,7),(7,8),
                         (0,3),(3,6),(1,4),(4,7),(2,5),(5,8)]
        ])
        
        # Tension band
        tension = DashedLine(
            original.get_right(), coherent.get_left(),
            color=YELLOW, stroke_width=3, dash_length=0.2
        )
        
        # Question
        question = Text(
            "Can AI be both?",
            font_size=48,
            color=WHITE
        ).to_edge(DOWN)
        
        # Animations
        self.play(
            Create(original),
            Create(coherent),
            run_time=1
        )
        self.play(
            FadeIn(orig_label),
            FadeIn(coh_label),
            run_time=0.8
        )
        self.play(
            Create(orig_arrows),
            Create(dots),
            Create(lines),
            run_time=1.5
        )
        self.play(
            Create(tension),
            tension.animate.set_stroke(width=5),
            rate_func=there_and_back,
            run_time=1.5
        )
        self.play(FadeIn(question), run_time=0.8)
        self.wait(1.5)
