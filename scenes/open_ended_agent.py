"""
SCENE: Open-ended Agent Architecture
Shows the autonomous agent comprised of main components
"""

from manim import *


class OpenEndedAgent(Scene):
    def construct(self):
        # Title
        title = Text("We built a Open-Ended System for Art", font_size=40, weight=BOLD).to_edge(UP)
        
        self.play(Write(title), run_time=1)
        self.wait(0.5)
        
        # Main agent architecture - simplified version
        # Components: Concept Pool → Inspiration Module → Prompt Compositor → Image Generator → Novelty Score
        
        component_width = 2.2
        component_height = 1.2
        
        # Concept Pool
        concept_pool = VGroup(
            RoundedRectangle(
                width=component_width,
                height=component_height,
                corner_radius=0.15,
                fill_color=BLUE_E,
                fill_opacity=0.3,
                stroke_color=BLUE,
                stroke_width=3
            ),
            Text("Concept\nPool", font_size=22, color=BLUE, weight=BOLD)
        ).move_to(LEFT * 4.5 + UP * 0.5)
        
        # Inspiration Module
        inspiration = VGroup(
            RoundedRectangle(
                width=component_width,
                height=component_height,
                corner_radius=0.15,
                fill_color=PURPLE_E,
                fill_opacity=0.3,
                stroke_color=PURPLE,
                stroke_width=3
            ),
            Text("Inspiration\nModule\n(GPT-4o)", font_size=22, color=PURPLE, weight=BOLD)
        ).move_to(LEFT * 1.8 + UP * 0.5)
        
        # Prompt Compositor
        compositor = VGroup(
            RoundedRectangle(
                width=component_width,
                height=component_height,
                corner_radius=0.15,
                fill_color=GREEN_E,
                fill_opacity=0.3,
                stroke_color=GREEN,
                stroke_width=3
            ),
            Text("Prompt\nCompositor\n(LLM)", font_size=22, color=GREEN, weight=BOLD)
        ).move_to(RIGHT * 1 + UP * 0.5)
        
        # Image Generator
        image_gen = VGroup(
            RoundedRectangle(
                width=component_width,
                height=component_height,
                corner_radius=0.15,
                fill_color=ORANGE,
                fill_opacity=0.3,
                stroke_color=ORANGE,
                stroke_width=3
            ),
            Text("Image\nGenerator", font_size=22, color=ORANGE, weight=BOLD)
        ).move_to(RIGHT * 3.8 + UP * 0.5)
        
        # Novelty Score (feedback component)
        novelty = VGroup(
            RoundedRectangle(
                width=component_width * 1.3,
                height=component_height * 0.8,
                corner_radius=0.15,
                fill_color=YELLOW_E,
                fill_opacity=0.3,
                stroke_color=YELLOW,
                stroke_width=3
            ),
            Text("Novelty Score", font_size=22, color=YELLOW, weight=BOLD)
        ).move_to(DOWN * 1.8)
        
        # Animate components appearing in sequence
        self.play(FadeIn(concept_pool, shift=RIGHT * 0.3), run_time=0.7)
        
        # Forward flow arrows
        arrow1 = Arrow(
            concept_pool.get_right(),
            inspiration.get_left(),
            color=WHITE,
            stroke_width=3,
            buff=0.1,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(GrowArrow(arrow1), run_time=0.5)
        self.play(FadeIn(inspiration, shift=RIGHT * 0.3), run_time=0.7)
        
        # Arrow from inspiration back to concept pool
        inspiration_feedback = CurvedArrow(
            inspiration.get_bottom() + DOWN * 0.1,
            concept_pool.get_bottom() + DOWN * 0.1 + RIGHT * 0.5,
            color=PURPLE,
            stroke_width=3,
            angle=-TAU/6
        )
        
        self.play(Create(inspiration_feedback), run_time=0.8)
        
        arrow2 = Arrow(
            inspiration.get_right(),
            compositor.get_left(),
            color=WHITE,
            stroke_width=3,
            buff=0.1,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(GrowArrow(arrow2), run_time=0.5)
        self.play(FadeIn(compositor, shift=RIGHT * 0.3), run_time=0.7)
        
        arrow3 = Arrow(
            compositor.get_right(),
            image_gen.get_left(),
            color=WHITE,
            stroke_width=3,
            buff=0.1,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(GrowArrow(arrow3), run_time=0.5)
        self.play(FadeIn(image_gen, shift=RIGHT * 0.3), run_time=0.7)
        
        # Arrow down to novelty score
        arrow4 = Arrow(
            image_gen.get_bottom(),
            novelty.get_top() + RIGHT * 1.5,
            color=WHITE,
            stroke_width=3,
            buff=0.1,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(GrowArrow(arrow4), run_time=0.5)
        self.play(FadeIn(novelty, shift=UP * 0.2), run_time=0.7)
        
        # Feedback loop arrow (curved back to concept pool)
        feedback_path = CurvedArrow(
            novelty.get_left() + LEFT * 0.5,
            concept_pool.get_bottom() + DOWN * 0.1,
            color=YELLOW,
            stroke_width=4,
            angle=-TAU/4
        )
        
        feedback_label = Text(
            "iterative\nfeedback",
            font_size=16,
            color=YELLOW,
            line_spacing=0.9
        ).next_to(feedback_path, LEFT, buff=0.2).shift(UP * 0.3)
        
        self.play(Create(feedback_path), run_time=1.2)
        self.play(FadeIn(feedback_label), run_time=0.5)
        
        # Summary description
        description = Text(
            "Novelty drives the exploration of conceptual combinations",
            font_size=26,
            color=WHITE
        ).to_edge(DOWN, buff=0.5)
        
        self.play(FadeIn(description), run_time=1)
        
        self.wait(2)