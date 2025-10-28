"""
SCENE 3: LLM Problem
Demonstrates the lack of originality in LLMs due to cultural bias
"""

from manim import *


class LLMProblem(Scene):
    def construct(self):
        # Title
        title = Text("The Problem: LLMs Lack Originality", font_size=44, weight=BOLD).to_edge(UP)
        
        self.play(
            FadeIn(title),
            run_time=1
        )
        self.wait(0.5)
        
        # SLIDE 1: Main Problem Statement
        # Create a box for the main statement
        problem_box = Rectangle(
            height=2.5, width=12,
            fill_color="#1a1a2e",
            fill_opacity=0.9,
            stroke_color=RED,
            stroke_width=3
        ).shift(UP * 0.8)
        
        problem_text = VGroup(
            Text(
                "LLMs are not original when you run the system",
                font_size=32,
                color=WHITE
            ),
            Text(
                "for different inputs",
                font_size=32,
                color=WHITE
            )
        ).arrange(DOWN, buff=0.2).move_to(problem_box)
        
        self.play(
            FadeIn(problem_box),
            FadeIn(problem_text),
            run_time=1.5
        )
        self.wait(1)
        
        # SLIDE 2: Explanation of Why
        explanation_box = Rectangle(
            height=3.5, width=12,
            fill_color="#16213e",
            fill_opacity=0.9,
            stroke_color=ORANGE,
            stroke_width=2
        ).shift(DOWN * 2.25)
        
        explanation_title = Text(
            "Why?",
            font_size=30,
            color=ORANGE,
            weight=BOLD
        ).next_to(explanation_box.get_top(), DOWN, buff=0.3)
        
        bullet_points = VGroup(
            Text("• Training data reflects dominant cultural norms", font_size=24, color=WHITE),
            Text("• Inherently biased toward familiar patterns", font_size=24, color=WHITE),
            Text("• Cultural anchoring limits originality and diversity", font_size=24, color=WHITE),
            Text("• Cannot challenge assumptions or subvert norms", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(explanation_title, DOWN, buff=0.3)
        
        self.play(
            FadeIn(explanation_box),
            FadeIn(explanation_title),
            run_time=1
        )
        
        self.play(
            LaggedStart(*[FadeIn(bullet, shift=RIGHT*0.3) for bullet in bullet_points], lag_ratio=0.4),
            run_time=2.5
        )
        self.wait(2)
        
        # Transition: fade out first slide
        self.play(
            FadeOut(problem_box),
            FadeOut(problem_text),
            FadeOut(explanation_box),
            FadeOut(explanation_title),
            FadeOut(bullet_points),
            run_time=1
        )
        
        # SLIDE 3: Statistics
        stats_title = Text(
            "Evidence from GPT-4o",
            font_size=36,
            weight=BOLD,
            color=YELLOW
        ).shift(UP * 2.5)
        
        self.play(FadeIn(stats_title), run_time=1)
        
        # Main statistic box
        main_stat_box = Rectangle(
            height=2.5, width=11,
            fill_color="#0f3460",
            fill_opacity=0.95,
            stroke_color=RED,
            stroke_width=4
        ).shift(UP * 0.3)
        
        main_stat = VGroup(
            Text("74.3%", font_size=72, color=RED, weight=BOLD),
            Text("of concepts were repeated", font_size=28, color=WHITE),
            Text("across different runs", font_size=28, color=WHITE)
        ).arrange(DOWN, buff=0.3).move_to(main_stat_box)
        
        self.play(
            FadeIn(main_stat_box),
            run_time=0.8
        )
        self.play(
            FadeIn(main_stat[0]),
            run_time=1.2
        )
        self.play(
            FadeIn(main_stat[1]),
            FadeIn(main_stat[2]),
            run_time=1
        )
        self.wait(1.5)
        
        # Transition: fade out statistics to show concepts
        self.play(
            FadeOut(main_stat_box),
            FadeOut(main_stat),
            run_time=1
        )
        
        # SLIDE 4: Common Concepts
        concepts_subtitle = Text(
            "Most Common Concepts",
            font_size=32,
            weight=BOLD,
            color=PURPLE_A
        ).shift(UP * 2.5)
        
        self.play(
            FadeOut(stats_title),
            FadeIn(concepts_subtitle),
            run_time=1
        )

        # Common concepts box
        concepts_box = Rectangle(
            height=5, width=10,
            fill_color="#16213e",
            fill_opacity=0.95,
            stroke_color=PURPLE,
            stroke_width=3
        ).shift(DOWN * 0.5)
        
        concepts_list = VGroup(
            Text("• Quantum Physics", font_size=30, color=WHITE),
            Text("• Bioluminescence", font_size=30, color=WHITE),
            Text("• Cyberpunk", font_size=30, color=WHITE),
            Text("• Mythology", font_size=30, color=WHITE),
            Text("• Dreams", font_size=30, color=WHITE),
            Text("• Algorithms", font_size=30, color=WHITE),
            Text("• Technology", font_size=30, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(concepts_box)
        
        self.play(
            FadeIn(concepts_box),
            run_time=1
        )
        self.play(
            LaggedStart(*[FadeIn(concept, shift=RIGHT*0.3) for concept in concepts_list], lag_ratio=0.2),
            run_time=2.5
        )
        
        self.wait(2)
        
        # Transition: fade out concepts slide
        self.play(
            FadeOut(concepts_subtitle),
            FadeOut(concepts_box),
            FadeOut(concepts_list),
            run_time=1
        )
        
        # SLIDE 5: Transition to Solution
        solution_title = Text(
            "Our Solution",
            font_size=48,
            weight=BOLD,
            color=GREEN
        ).shift(UP * 1.5)
        
        self.play(
            FadeIn(solution_title),
            run_time=1.2
        )
        self.wait(0.5)
        
        # Create arrow and text showing the replacement
        replacement_box = Rectangle(
            height=3.5, width=11,
            fill_color="#0a2e1a",
            fill_opacity=0.9,
            stroke_color=GREEN,
            stroke_width=3
        ).shift(DOWN * 1)
        
        replacement_text = VGroup(
            Text("Cultural Alien Sampler", font_size=40, color=GREEN, weight=BOLD),
            Text("will replace GPT-4o", font_size=28, color=WHITE),
            Text("in the Inspiration Module", font_size=28, color=WHITE)
        ).arrange(DOWN, buff=0.4).move_to(replacement_box)
        
        self.play(
            FadeIn(replacement_box),
            run_time=1
        )
        self.play(
            FadeIn(replacement_text[0]),
            run_time=1.5
        )
        self.play(
            FadeIn(replacement_text[1]),
            FadeIn(replacement_text[2]),
            run_time=1.2
        )
        
        self.wait(3)
