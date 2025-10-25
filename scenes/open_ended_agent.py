"""
SCENE: Open-Ended Art Agent with Flow
Dynamic visualization showing outputs traveling through space to become inputs,
with individual focus on components and final zoom-out to reveal full pipeline
"""

from manim import *
import numpy as np


class OpenEndedAgent(MovingCameraScene):
    def construct(self):
        # Title
        title = Text("Open-Ended Art Agent", font_size=48, weight=BOLD)
        subtitle = Text(
            "An Iterative Creative System",
            font_size=28,
            color=GREY_B,
            slant=ITALIC
        ).next_to(title, DOWN, buff=0.3)
        
        self.play(
            Write(title, run_time=0.8),
            FadeIn(subtitle, shift=UP*0.3),
        )
        self.wait(0.8)
        self.play(
            FadeOut(title, shift=UP),
            FadeOut(subtitle, shift=UP),
            run_time=0.6
        )
        
        # ========================================================================
        # PART 1: STEP-BY-STEP FLOW WITH TRAVELING OUTPUTS
        # ========================================================================
        
        # Camera frame for zooming
        self.camera.frame.save_state()
        
        # ------ STEP 1: Initial Concept Pool ------
        step1_label = Text("Initial Concept Pool", font_size=36, color=WHITE, weight=BOLD)
        step1_label.to_edge(UP)
        
        # Create initial concepts
        initial_concepts = VGroup(
            self.create_concept_node("Woman", TEAL),
            self.create_concept_node("Ukiyo-e", TEAL)
        ).arrange(RIGHT, buff=1.5).move_to(LEFT * 8)
        
        self.play(
            Write(step1_label),
            LaggedStart(*[
                FadeIn(concept, shift=UP*0.5, scale=0.5) 
                for concept in initial_concepts
            ], lag_ratio=0.3),
            run_time=1.2
        )
        self.wait(0.5)
        
        # Prepare to travel - create a "data packet" that will travel
        data_packet = VGroup(
            initial_concepts.copy()
        ).scale(0.6)
        
        self.play(
            FadeOut(step1_label, shift=UP*0.3),
            initial_concepts.animate.scale(0.8).set_opacity(0.3),
            FadeIn(data_packet),
            run_time=0.5
        )
        
        # ------ TRAVELING TO INSPIRATION MODULE ------
        # Create a path for the data to travel
        travel_path1 = CubicBezier(
            initial_concepts.get_center(),
            initial_concepts.get_center() + RIGHT * 4 + UP * 2,
            RIGHT * 0 + UP * 2,
            RIGHT * 0
        )
        
        # Travel animation with trail effect
        trail1 = TracedPath(
            data_packet.get_center,
            stroke_color=TEAL,
            stroke_width=3,
            stroke_opacity=[0.8, 0]
        )
        self.add(trail1)
        
        self.play(
            MoveAlongPath(data_packet, travel_path1),
            run_time=1.5,
            rate_func=smooth
        )
        self.remove(trail1)
        
        # ------ STEP 2: Inspiration Module (CAS) ------
        # Focus camera on new location
        self.play(
            self.camera.frame.animate.move_to(ORIGIN).scale(0.9),
            run_time=0.8
        )
        
        inspiration_label = Text("Inspiration Module (CAS)", font_size=34, color=GREEN, weight=BOLD)
        inspiration_label.move_to(UP * 3.2)
        
        inspiration_box = RoundedRectangle(
            height=3.5, width=5,
            corner_radius=0.3,
            stroke_color=GREEN,
            stroke_width=4,
            fill_opacity=0.1,
            fill_color=GREEN_E
        ).move_to(ORIGIN)
        
        # CAS internals (simplified)
        cas_text = Text("Cultural\nAlien\nSampler", font_size=20, color=GREEN_A, line_spacing=0.8)
        cas_text.move_to(inspiration_box.get_center())
        
        self.play(
            Write(inspiration_label),
            Create(inspiration_box),
            FadeIn(cas_text),
            run_time=0.8
        )
        
        # Data packet enters the module
        self.play(
            data_packet.animate.move_to(inspiration_box.get_top() + DOWN * 0.8).scale(0.8),
            run_time=0.6
        )
        
        # Processing animation - module "thinks"
        processing_dots = VGroup(*[
            Dot(radius=0.08, color=GREEN).move_to(
                inspiration_box.get_center() + 
                0.8 * np.array([np.cos(i * TAU/5), np.sin(i * TAU/5), 0])
            )
            for i in range(5)
        ])
        
        self.play(
            LaggedStart(*[
                Flash(dot, color=YELLOW, line_length=0.2, num_lines=8)
                for dot in processing_dots
            ], lag_ratio=0.1),
            inspiration_box.animate.set_stroke(color=YELLOW, width=6),
            rate_func=there_and_back,
            run_time=1.5
        )
        
        # Output: New concept added
        new_concept = self.create_concept_node("Knife", GREEN)
        new_concept.move_to(inspiration_box.get_bottom() + DOWN * 0.8)
        
        self.play(
            FadeIn(new_concept, shift=DOWN*0.5, scale=0.5),
            run_time=0.6
        )
        
        # Combine with existing concepts for next stage
        updated_packet = VGroup(
            self.create_concept_node("Woman", TEAL),
            self.create_concept_node("Ukiyo-e", TEAL),
            self.create_concept_node("Knife", GREEN)
        ).arrange(RIGHT, buff=0.3).scale(0.6)
        updated_packet.move_to(inspiration_box.get_center())
        
        self.play(
            FadeOut(data_packet),
            FadeOut(new_concept),
            FadeIn(updated_packet),
            run_time=0.5
        )
        
        # ------ TRAVELING TO PROMPT COMPOSITOR ------
        travel_path2 = CubicBezier(
            updated_packet.get_center(),
            updated_packet.get_center() + RIGHT * 4 + DOWN * 2,
            RIGHT * 8 + DOWN * 2,
            RIGHT * 8
        )
        
        # Travel with trail
        trail2 = TracedPath(
            updated_packet.get_center,
            stroke_color=GREEN,
            stroke_width=3,
            stroke_opacity=[0.8, 0]
        )
        self.add(trail2)
        
        self.play(
            MoveAlongPath(updated_packet, travel_path2),
            self.camera.frame.animate.move_to(RIGHT * 8),
            run_time=2.2,
            rate_func=smooth
        )
        self.remove(trail2)
        
        # ------ STEP 3: Prompt Compositor ------
        compositor_label = Text("Prompt Compositor (GPT-4o)", font_size=34, color=BLUE, weight=BOLD)
        compositor_label.move_to(RIGHT * 8 + UP * 3.2)
        
        compositor_box = RoundedRectangle(
            height=3.5, width=5.5,
            corner_radius=0.3,
            stroke_color=BLUE,
            stroke_width=4,
            fill_opacity=0.1,
            fill_color=BLUE_E
        ).move_to(RIGHT * 8)
        
        gpt_text = Text("GPT-4o", font_size=24, color=BLUE_A, weight=BOLD)
        gpt_text.move_to(compositor_box.get_center())
        
        self.play(
            Write(compositor_label),
            Create(compositor_box),
            FadeIn(gpt_text),
            run_time=0.8
        )
        
        # Concepts enter and arrange
        self.play(
            updated_packet.animate.move_to(compositor_box.get_top() + DOWN * 0.8),
            run_time=0.6
        )
        
        # Processing - text generation effect
        prompt_lines = VGroup(*[
            Line(LEFT * 1.5, RIGHT * 1.5, stroke_width=2, color=BLUE_B).shift(DOWN * 0.3 * i)
            for i in range(3)
        ]).move_to(compositor_box.get_center() + DOWN * 0.5)
        
        self.play(
            LaggedStart(*[Create(line) for line in prompt_lines], lag_ratio=0.2),
            compositor_box.animate.set_stroke(color=BLUE_B, width=6),
            rate_func=there_and_back,
            run_time=1.5
        )
        
        # Output: Text prompt
        prompt_box = Rectangle(
            height=0.8, width=4,
            stroke_color=BLUE,
            stroke_width=3,
            fill_opacity=0.2,
            fill_color=BLUE_E
        )
        prompt_text = Text(
            "ukiyo-e woman with knife...",
            font_size=16,
            color=BLUE_B
        ).move_to(prompt_box)
        prompt_output = VGroup(prompt_box, prompt_text)
        prompt_output.move_to(compositor_box.get_bottom() + DOWN * 0.8)
        
        self.play(
            FadeOut(prompt_lines),
            FadeIn(prompt_output, shift=DOWN*0.3),
            run_time=0.6
        )
        
        # Prepare prompt packet for travel
        prompt_packet = prompt_output.copy().scale(0.8)
        
        self.play(
            FadeOut(updated_packet),
            prompt_output.animate.set_opacity(0.3),
            FadeIn(prompt_packet),
            run_time=0.4
        )
        
        # ------ TRAVELING TO IMAGE GENERATOR ------
        travel_path3 = CubicBezier(
            prompt_packet.get_center(),
            prompt_packet.get_center() + DOWN * 3 + RIGHT * 2,
            RIGHT * 8 + DOWN * 7 + LEFT * 2,
            RIGHT * 8 + DOWN * 7
        )
        
        trail3 = TracedPath(
            prompt_packet.get_center,
            stroke_color=BLUE,
            stroke_width=3,
            stroke_opacity=[0.8, 0]
        )
        self.add(trail3)
        
        self.play(
            MoveAlongPath(prompt_packet, travel_path3),
            self.camera.frame.animate.move_to(RIGHT * 8 + DOWN * 4.5),
            run_time=2.2,
            rate_func=smooth
        )
        self.remove(trail3)
        
        # ------ STEP 4: Image Generator ------
        generator_label = Text("Image Generator", font_size=34, color=PURPLE, weight=BOLD)
        generator_label.move_to(RIGHT * 8 + DOWN * 3)
        
        generator_box = RoundedRectangle(
            height=3, width=4,
            corner_radius=0.3,
            stroke_color=PURPLE,
            stroke_width=4,
            fill_opacity=0.1,
            fill_color=PURPLE_E
        ).move_to(RIGHT * 8 + DOWN * 7)
        
        gen_icon = Square(side_length=1.2, color=PURPLE_A, fill_opacity=0.3)
        gen_icon.move_to(generator_box.get_center())
        
        self.play(
            Write(generator_label),
            Create(generator_box),
            FadeIn(gen_icon),
            run_time=0.8
        )
        
        # Prompt enters
        self.play(
            prompt_packet.animate.move_to(generator_box.get_top() + DOWN * 0.8).scale(0.8),
            run_time=0.6
        )
        
        # Generation effect - artistic creation
        creation_effect = VGroup(*[
            Arc(
                start_angle=i * TAU/6, 
                angle=TAU/8,
                radius=0.8,
                color=interpolate_color(PURPLE, PINK, i/6),
                stroke_width=3
            ).move_to(generator_box.get_center())
            for i in range(6)
        ])
        
        self.play(
            LaggedStart(*[Create(arc) for arc in creation_effect], lag_ratio=0.1),
            generator_box.animate.set_stroke(color=PINK, width=6),
            gen_icon.animate.rotate(TAU/4),
            rate_func=there_and_back,
            run_time=2
        )
        
        self.play(FadeOut(creation_effect), run_time=0.3)
        
        # Output: Generated image
        artwork = Rectangle(
            height=2, width=2,
            stroke_color=PURPLE,
            stroke_width=4,
            fill_opacity=0.3,
            fill_color=PURPLE_E
        )
        art_star = Star(n=8, outer_radius=0.6, color=PURPLE_B, fill_opacity=0.7)
        art_star.move_to(artwork)
        image_output = VGroup(artwork, art_star)
        image_output.move_to(generator_box.get_bottom() + DOWN * 1.5)
        
        self.play(
            FadeOut(prompt_packet),
            FadeIn(image_output, scale=0.5),
            run_time=0.8
        )
        
        # Prepare image packet for travel
        image_packet = image_output.copy().scale(0.7)
        
        self.play(
            image_output.animate.set_opacity(0.3),
            FadeIn(image_packet),
            run_time=0.4
        )
        
        # ------ TRAVELING TO NOVELTY SCORE ------
        travel_path4 = CubicBezier(
            image_packet.get_center(),
            image_packet.get_center() + LEFT * 5 + DOWN * 1,
            LEFT * 8 + DOWN * 7 + DOWN * 1,
            LEFT * 8 + DOWN * 7
        )
        
        trail4 = TracedPath(
            image_packet.get_center,
            stroke_color=PURPLE,
            stroke_width=3,
            stroke_opacity=[0.8, 0]
        )
        self.add(trail4)
        
        self.play(
            MoveAlongPath(image_packet, travel_path4),
            self.camera.frame.animate.move_to(LEFT * 0 + DOWN * 4.5),
            run_time=2.5,
            rate_func=smooth
        )
        self.remove(trail4)
        
        # ------ STEP 5: Novelty Score ------
        novelty_label = Text("Novelty Score", font_size=34, color=YELLOW, weight=BOLD)
        novelty_label.move_to(LEFT * 8 + DOWN * 3)
        
        novelty_box = RoundedRectangle(
            height=3, width=4,
            corner_radius=0.3,
            stroke_color=YELLOW,
            stroke_width=4,
            fill_opacity=0.1,
            fill_color=YELLOW_E
        ).move_to(LEFT * 8 + DOWN * 7)
        
        score_formula = MathTex(
            r"N = \frac{1}{2}(N_{\text{text}} + N_{\text{img}})",
            font_size=20,
            color=YELLOW_A
        ).move_to(novelty_box.get_center())
        
        self.play(
            Write(novelty_label),
            Create(novelty_box),
            Write(score_formula),
            run_time=0.8
        )
        
        # Image enters for evaluation
        self.play(
            image_packet.animate.move_to(novelty_box.get_top() + DOWN * 0.8).scale(0.8),
            run_time=0.6
        )
        
        # Scoring animation
        score_display = VGroup(
            Text("Score:", font_size=24, color=YELLOW),
            Text("0.67", font_size=32, color=GREEN, weight=BOLD)
        ).arrange(RIGHT, buff=0.3).move_to(novelty_box.get_bottom() + DOWN * 0.8)
        
        self.play(
            novelty_box.animate.set_stroke(color=GREEN, width=6),
            rate_func=there_and_back,
            run_time=1.2
        )
        
        self.play(
            FadeOut(image_packet),
            Write(score_display),
            run_time=0.6
        )
        
        # Feedback arrow going back to start
        feedback_path = CurvedArrow(
            novelty_box.get_top(),
            initial_concepts.get_center() + DOWN * 1,
            angle=-TAU/4,
            color=YELLOW,
            stroke_width=3
        )
        
        feedback_label = Text("Update Pool", font_size=16, color=YELLOW)
        feedback_label.move_to(feedback_path.get_center() + UP * 0.5)
        
        self.play(
            Create(feedback_path),
            Write(feedback_label),
            run_time=1
        )
        
        # ========================================================================
        # PART 2: ZOOM OUT TO REVEAL FULL PIPELINE
        # ========================================================================
        
        self.wait(0.5)
        
        # Prepare for zoom out - fade feedback elements
        self.play(
            FadeOut(feedback_label),
            feedback_path.animate.set_stroke_opacity(0.4),
            score_display.animate.set_opacity(0.5),
            run_time=0.5
        )
        
        # Create connecting flows between all components
        flow_connections = VGroup(
            # Pool to Inspiration
            CurvedArrow(
                initial_concepts.get_right(),
                inspiration_box.get_left(),
                angle=-TAU/12,
                color=TEAL,
                stroke_width=2,
                stroke_opacity=0.6
            ),
            # Inspiration to Compositor
            CurvedArrow(
                inspiration_box.get_right(),
                compositor_box.get_left(),
                angle=TAU/12,
                color=GREEN,
                stroke_width=2,
                stroke_opacity=0.6
            ),
            # Compositor to Generator
            CurvedArrow(
                compositor_box.get_bottom(),
                generator_box.get_top(),
                angle=-TAU/6,
                color=BLUE,
                stroke_width=2,
                stroke_opacity=0.6
            ),
            # Generator to Novelty
            CurvedArrow(
                generator_box.get_left(),
                novelty_box.get_right(),
                angle=-TAU/8,
                color=PURPLE,
                stroke_width=2,
                stroke_opacity=0.6
            )
        )
        
        # Smooth zoom out revealing the entire pipeline
        self.play(
            self.camera.frame.animate.move_to(ORIGIN + DOWN * 2).scale(3.5),
            Create(flow_connections),
            # Restore full opacity to key elements
            initial_concepts.animate.set_opacity(1),
            prompt_output.animate.set_opacity(1),
            image_output.animate.set_opacity(1),
            # Enhance component labels
            inspiration_label.animate.scale(0.8),
            compositor_label.animate.scale(0.8),
            generator_label.animate.scale(0.8),
            novelty_label.animate.scale(0.8),
            run_time=3.5,
            rate_func=smooth
        )
        
        # Add overall system label
        system_label = Text(
            "Iterative Open-Ended Art Generation Pipeline",
            font_size=42,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(
            Write(system_label),
            run_time=1
        )
        
        # Final pulsing animation to show the cyclic nature
        self.play(
            LaggedStart(*[
                Indicate(comp, color=YELLOW, scale_factor=1.05)
                for comp in [
                    inspiration_box,
                    compositor_box,
                    generator_box,
                    novelty_box
                ]
            ], lag_ratio=0.3),
            run_time=2
        )
        
        # Generation counter appears
        gen_counter = Text(
            "Generation: 1 → 2 → 3 → ...",
            font_size=28,
            color=YELLOW
        ).move_to(DOWN * 9)
        
        self.play(
            Write(gen_counter),
            run_time=1
        )
        
        self.wait(2)
    
    def create_concept_node(self, text: str, color: str, scale: float = 1) -> VGroup:
        """Create a styled concept node"""
        box = RoundedRectangle(
            height=0.6 * scale, 
            width=len(text) * 0.15 * scale + 0.5 * scale,
            corner_radius=0.15 * scale,
            stroke_color=color,
            stroke_width=2,
            fill_opacity=0.2,
            fill_color=color
        )
        label = Text(text, font_size=18 * scale, color=color)
        node = VGroup(box, label)
        label.move_to(box.get_center())
        return node