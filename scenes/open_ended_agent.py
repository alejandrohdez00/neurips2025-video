"""
SCENE: Open-Ended System
Visualizes the pipeline of the open-ended art generation system
"""

from manim import *


class OpenEndedAgent(Scene):
    def construct(self):
        # Title - centered on screen
        title = Text("We designed an Open-Ended Painting Generation System", font_size=30, weight=BOLD)
        subtitle = Text(
            "Evolve a concept pool through strategic recombination",
            font_size=24,
            color=GREY_A
        ).next_to(title, DOWN, buff=0.3)
        
        title_group = VGroup(title, subtitle).move_to(ORIGIN)

        self.play(FadeIn(title_group), run_time=1.5)
        self.wait(2.5)
        
        # Fade out title and subtitle
        self.play(FadeOut(title_group), run_time=1)
        
        # Color scheme
        MODULE_COLOR = BLUE
        CONCEPT_COLOR = GREEN
        PROMPT_COLOR = PURPLE
        IMAGE_COLOR = ORANGE
        NOVELTY_COLOR = YELLOW
        
        # =============================================================
        # STEP 1: Initial Concept Pool
        # =============================================================
        
        # Create initial concept pool
        concept_pool_box = RoundedRectangle(
            height=2, width=4,
            stroke_color=CONCEPT_COLOR,
            stroke_width=3,
            fill_color=CONCEPT_COLOR,
            fill_opacity=0.1,
            corner_radius=0.2
        )
        
        pool_label = Text("Concept Pool", font_size=24, color=CONCEPT_COLOR)
        pool_label.next_to(concept_pool_box, UP, buff=0.2)
        
        # Description
        pool_desc = Text(
            "Stores concepts used in the simulation.\nThey are added and recombined\nthrough the generations.",
            font_size=16,
            color=GREY_B,
            slant=ITALIC
        ).next_to(concept_pool_box, LEFT, buff=0.5)
        
        # Initial concepts
        concept1 = self.create_concept_tag("mountain", CONCEPT_COLOR)
        concept2 = self.create_concept_tag("romanticism", CONCEPT_COLOR)
        
        concepts_group = VGroup(concept1, concept2).arrange(RIGHT, buff=0.3)
        concepts_group.move_to(concept_pool_box)
        
        pool_with_label = VGroup(concept_pool_box, pool_label, pool_desc, concepts_group)
        
        self.play(
            FadeIn(pool_with_label),
            run_time=0.8
        )
        self.wait(2)
        
        # =============================================================
        # STEP 2: Inspiration Module
        # =============================================================
        
        # Show INPUT arrow and label
        input_arrow = Arrow(
            concept_pool_box.get_bottom() + DOWN * 0.3,
            concept_pool_box.get_bottom() + DOWN * 1.5,
            color=WHITE,
            stroke_width=3
        )
        input_label = Text("INPUT", font_size=16, color=WHITE)
        input_label.next_to(input_arrow, LEFT, buff=0.2)
        
        self.play(
            Create(input_arrow),
            Write(input_label),
            run_time=0.5
        )
        
        # Transition: Pool slides up and out, Inspiration Module appears
        self.play(
            pool_with_label.animate.shift(UP * 6),
            FadeOut(input_arrow),
            FadeOut(input_label),
            run_time=0.6
        )
        
        # Create Inspiration Module
        inspiration_box = RoundedRectangle(
            height=3, width=5,
            stroke_color=MODULE_COLOR,
            stroke_width=3,
            fill_color=MODULE_COLOR,
            fill_opacity=0.05,
            corner_radius=0.2
        )
        
        inspiration_label = Text(
            "Inspiration Module",
            font_size=28,
            color=MODULE_COLOR,
            weight=BOLD
        )
        inspiration_label.next_to(inspiration_box, UP, buff=0.3)
        
        # Options inside (GPT, Random, Human)
        options_text = Text(
            "GPT-4o",
            font_size=18,
            color=MODULE_COLOR
        ).move_to(inspiration_box)
        
        # Description of what it does
        inspiration_desc = Text(
            "GPT4-o suggests new concepts\nfrom input concepts\nand adds to pool.",
            font_size=16,
            color=GREY_B,
            slant=ITALIC
        ).next_to(inspiration_box, LEFT, buff=0.5)
        
        inspiration_group = VGroup(inspiration_box, inspiration_label, options_text, inspiration_desc)
        
        self.play(FadeIn(inspiration_group), run_time=0.8)
        self.wait(1.5)
        
        # Show input concepts entering from top
        input_concepts = VGroup(
            self.create_concept_tag("mountain", CONCEPT_COLOR),
            self.create_concept_tag("romanticism", CONCEPT_COLOR)
        ).arrange(RIGHT, buff=0.2).scale(0.8)
        input_concepts.next_to(inspiration_box, UP, buff=2.5)
        
        self.play(FadeIn(input_concepts, shift=DOWN * 0.5), run_time=0.5)
        
        # Animate flowing in
        self.play(
            input_concepts.animate.move_to(inspiration_box),
            run_time=0.6
        )
        self.play(FadeOut(input_concepts), run_time=0.3)
        
        # Processing animation
        self.play(
            options_text.animate.scale(1.1),
            rate_func=there_and_back,
            run_time=0.5
        )
        
        # Output new concept
        new_concept = self.create_concept_tag("cyberpunk", YELLOW)
        new_concept.move_to(inspiration_box)
        
        self.play(FadeIn(new_concept, scale=0.5), run_time=0.5)
        
        # Show OUTPUT arrow and label
        output_arrow = Arrow(
            inspiration_box.get_bottom(),
            inspiration_box.get_bottom() + DOWN * 1,
            color=YELLOW,
            stroke_width=3
        )
        output_label = Text("OUTPUT: new concept", font_size=16, color=YELLOW)
        output_label.next_to(output_arrow, RIGHT, buff=0.2)
        
        self.play(
            new_concept.animate.next_to(inspiration_box, DOWN, buff=1),
            Create(output_arrow),
            Write(output_label),
            run_time=0.7
        )
        
        # Add arrow showing this concept goes to the pool (to the LEFT)
        pool_feedback_arrow = Arrow(
            new_concept.get_left(),
            new_concept.get_left() + LEFT * 2,
            color=CONCEPT_COLOR,
            stroke_width=3
        )
        pool_feedback_label = Text("to Concept Pool", font_size=14, color=CONCEPT_COLOR)
        pool_feedback_label.next_to(pool_feedback_arrow, DOWN, buff=0.1)
        
        self.play(
            Create(pool_feedback_arrow),
            Write(pool_feedback_label),
            run_time=0.5
        )
        self.wait(1.5)
        
        # Transition out
        self.play(
            FadeOut(VGroup(inspiration_group, pool_feedback_arrow, pool_feedback_label, output_arrow, output_label, new_concept)),
            run_time=0.5
        )
        
        # =============================================================
        # STEP 3: Prompt Compositor
        # =============================================================
        
        # Create Prompt Compositor
        compositor_box = RoundedRectangle(
            height=3, width=5,
            stroke_color=PROMPT_COLOR,
            stroke_width=3,
            fill_color=PROMPT_COLOR,
            fill_opacity=0.05,
            corner_radius=0.2
        )
        
        compositor_label = Text(
            "Prompt Compositor (LLM)",
            font_size=28,
            color=PROMPT_COLOR,
            weight=BOLD
        )
        compositor_label.next_to(compositor_box, UP, buff=0.3)
        
        # Description
        compositor_desc = Text(
            "LLM selects a subset of concepts\nfrom the pool\nto form a painting prompt",
            font_size=16,
            color=GREY_B,
            slant=ITALIC
        ).next_to(compositor_box, LEFT, buff=0.5)
        
        compositor_group = VGroup(compositor_box, compositor_label, compositor_desc)
        
        self.play(FadeIn(compositor_group), run_time=0.8)
        self.wait(1.5)
        
        # Input: concept pool box (not individual concepts)
        input_pool_box = RoundedRectangle(
            height=1.2, width=2.5,
            stroke_color=CONCEPT_COLOR,
            stroke_width=3,
            fill_color=CONCEPT_COLOR,
            fill_opacity=0.1,
            corner_radius=0.2
        )
        input_pool_label = Text("Concept Pool", font_size=16, color=CONCEPT_COLOR)
        input_pool_visual = VGroup(input_pool_box, input_pool_label)
        input_pool_visual.next_to(compositor_box, UP, buff=2.5)
        
        input_text = Text("INPUT: concept pool", font_size=14, color=WHITE)
        input_text.next_to(input_pool_visual, UP, buff=0.2)
        
        self.play(
            FadeIn(input_pool_visual, shift=DOWN * 0.5),
            Write(input_text),
            run_time=0.5
        )
        
        # Animate pool entering
        self.play(
            input_pool_visual.animate.move_to(compositor_box),
            FadeOut(input_text),
            run_time=0.6
        )
        
        # Show selection process
        selected_text = Text("Selecting subset of concepts from the pool...", font_size=16, color=PROMPT_COLOR)
        selected_text.move_to(compositor_box)
        
        self.play(
            FadeOut(input_pool_visual),
            FadeIn(selected_text),
            run_time=0.5
        )
        self.wait(1.2)
        
        # Transform to prompt
        prompt_text = Text(
            '"A majestic mountain range..."',
            font_size=18,
            color=PROMPT_COLOR,
            slant=ITALIC
        )
        prompt_text.move_to(compositor_box)
        
        self.play(
            FadeOut(selected_text),
            FadeIn(prompt_text),
            run_time=0.7
        )
        
        # Output arrow
        output_arrow = Arrow(
            compositor_box.get_bottom(),
            compositor_box.get_bottom() + DOWN * 1,
            color=PROMPT_COLOR,
            stroke_width=3
        )
        output_label = Text("OUTPUT: prompt", font_size=16, color=PROMPT_COLOR)
        output_label.next_to(output_arrow, RIGHT, buff=0.2)
        
        prompt_output = prompt_text.copy()
        self.play(
            prompt_output.animate.next_to(compositor_box, DOWN, buff=1).scale(0.9),
            Create(output_arrow),
            Write(output_label),
            run_time=0.7
        )
        
        self.wait(2)
        
        # Transition out
        self.play(
            FadeOut(VGroup(compositor_group, prompt_text, output_arrow, output_label, prompt_output)),
            run_time=0.5
        )
        
        # =============================================================
        # STEP 4: Image Generator
        # =============================================================
        
        # Create Image Generator
        generator_box = RoundedRectangle(
            height=3, width=5,
            stroke_color=IMAGE_COLOR,
            stroke_width=3,
            fill_color=IMAGE_COLOR,
            fill_opacity=0.05,
            corner_radius=0.2
        )
        
        generator_label = Text(
            "Image Generator",
            font_size=28,
            color=IMAGE_COLOR,
            weight=BOLD
        )
        generator_label.next_to(generator_box, UP, buff=0.3)
        
        # Description
        generator_desc = Text(
            "Generates artwork\nfrom text prompt",
            font_size=16,
            color=GREY_B,
            slant=ITALIC
        ).next_to(generator_box, LEFT, buff=0.5)
        
        generator_group = VGroup(generator_box, generator_label, generator_desc)
        
        self.play(FadeIn(generator_group), run_time=0.8)
        self.wait(1.5)
        
        # Input prompt
        input_prompt = Text(
            '"A majestic mountain range..."',
            font_size=16,
            color=PROMPT_COLOR,
            slant=ITALIC
        )
        input_prompt.next_to(generator_box, UP, buff=2.5)
        
        input_text = Text("INPUT: prompt", font_size=14, color=WHITE)
        input_text.next_to(input_prompt, UP, buff=0.2)
        
        self.play(
            FadeIn(input_prompt, shift=DOWN * 0.5),
            Write(input_text),
            run_time=0.5
        )
        
        # Animate generation
        self.play(
            input_prompt.animate.move_to(generator_box),
            FadeOut(input_text),
            run_time=0.6
        )
        
        generating_text = Text("Generating...", font_size=16, color=IMAGE_COLOR)
        generating_text.move_to(generator_box)
        
        self.play(Transform(input_prompt, generating_text), run_time=0.5)
        self.wait(0.8)
        
        # Output image - load actual PNG
        artwork_image = ImageMobject("image__gen1.png")
        artwork_image.height = 2.5
        artwork_image.move_to(generator_box)
        
        self.play(
            FadeOut(input_prompt),
            FadeIn(artwork_image),
            run_time=0.7
        )
        
        self.wait(2)
        
        # Transition out
        self.play(
            FadeOut(generator_group),
            FadeOut(artwork_image),
            run_time=0.5
        )
        
        # =============================================================
        # STEP 5: Novelty Score
        # =============================================================
        
        # Create Novelty Score module
        novelty_box = RoundedRectangle(
            height=3, width=5,
            stroke_color=NOVELTY_COLOR,
            stroke_width=3,
            fill_color=NOVELTY_COLOR,
            fill_opacity=0.05,
            corner_radius=0.2
        )
        
        novelty_label = Text(
            "Novelty Score",
            font_size=28,
            color=NOVELTY_COLOR,
            weight=BOLD
        )
        novelty_label.next_to(novelty_box, UP, buff=0.3)
        
        # Description
        novelty_desc = Text(
            "Computes novelty\nfrom prompt + image\nbased on how different the \nidea is from previously\n generated ideas by the system",
            font_size=16,
            color=GREY_B,
            slant=ITALIC
        ).next_to(novelty_box, LEFT, buff=0.5)
        
        novelty_group = VGroup(novelty_box, novelty_label, novelty_desc)
        
        self.play(FadeIn(novelty_group), run_time=0.8)
        self.wait(1.5)
        
        # Two inputs
        input_prompt_small = Text('"prompt"', font_size=14, color=PROMPT_COLOR, slant=ITALIC)
        
        # Use actual image instead of rectangle
        input_image_small = artwork_image.copy()
        input_image_small.height = 0.8
        
        inputs = VGroup(input_prompt_small, Text("+", font_size=20)).arrange(RIGHT, buff=0.3)
        # Add image to Group since it's an ImageMobject
        inputs_with_image = Group(inputs, input_image_small)
        input_image_small.next_to(inputs, RIGHT, buff=0.3)
        
        inputs_with_image.next_to(novelty_box, UP, buff=2.5)
        
        input_text = Text("INPUT: prompt + image", font_size=14, color=WHITE)
        input_text.next_to(inputs_with_image, UP, buff=0.2)
        
        self.play(
            FadeIn(inputs_with_image, shift=DOWN * 0.5),
            Write(input_text),
            run_time=0.5
        )
        
        # Animate computation
        self.play(
            inputs_with_image.animate.move_to(novelty_box),
            FadeOut(input_text),
            run_time=1.2
        )
        
        computing_text = Text("Computing novelty...", font_size=16, color=NOVELTY_COLOR)
        computing_text.move_to(novelty_box)
        
        self.play(
            FadeOut(inputs_with_image),
            FadeIn(computing_text),
            run_time=0.5
        )
        self.wait(0.8)
        
        # Output score
        score_text = Text("Score: 0.73", font_size=24, color=NOVELTY_COLOR, weight=BOLD)
        score_text.move_to(novelty_box)
        
        self.play(
            FadeOut(computing_text),
            FadeIn(score_text),
            run_time=0.6
        )
        
        # Output arrow
        output_arrow = Arrow(
            novelty_box.get_bottom(),
            novelty_box.get_bottom() + DOWN * 1,
            color=NOVELTY_COLOR,
            stroke_width=3
        )
        output_label = Text("OUTPUT: novelty score", font_size=16, color=NOVELTY_COLOR)
        output_label.next_to(output_arrow, RIGHT, buff=0.2)
        
        score_output = score_text.copy()
        self.play(
            score_output.animate.next_to(novelty_box, DOWN, buff=1),
            Create(output_arrow),
            Write(output_label),
            run_time=0.7
        )
        
        self.wait(2.5)
        
        # =============================================================
        # STEP 6: Feedback Loop
        # =============================================================
        
        # Clear screen for final visualization
        self.play(
            FadeOut(VGroup(novelty_group, output_arrow, output_label, score_output, score_text)),
            run_time=0.5
        )
        
        # Show complete loop
        loop_text = Text(
            "Feedback Loop",
            font_size=32,
            color=YELLOW,
            weight=BOLD
        )
        
        # Create mini versions of all modules with labels
        # Concept Pool
        mini_pool_box = RoundedRectangle(
            height=1.2, width=2.2, 
            stroke_color=CONCEPT_COLOR, 
            stroke_width=3, 
            fill_color=CONCEPT_COLOR,
            fill_opacity=0.1,
            corner_radius=0.15
        )
        mini_pool_label = Text("Concept\nPool", font_size=16, color=CONCEPT_COLOR).move_to(mini_pool_box)
        mini_pool = VGroup(mini_pool_box, mini_pool_label)
        
        # Inspiration Module
        mini_inspiration_box = RoundedRectangle(
            height=1.2, width=2.2, 
            stroke_color=MODULE_COLOR, 
            stroke_width=3,
            fill_color=MODULE_COLOR,
            fill_opacity=0.1,
            corner_radius=0.15
        )
        mini_inspiration_label = Text("Inspiration\nModule", font_size=16, color=MODULE_COLOR).move_to(mini_inspiration_box)
        mini_inspiration = VGroup(mini_inspiration_box, mini_inspiration_label)
        
        # Prompt Compositor
        mini_compositor_box = RoundedRectangle(
            height=1.2, width=2.2, 
            stroke_color=PROMPT_COLOR, 
            stroke_width=3,
            fill_color=PROMPT_COLOR,
            fill_opacity=0.1,
            corner_radius=0.15
        )
        mini_compositor_label = Text("Prompt\nCompositor", font_size=16, color=PROMPT_COLOR).move_to(mini_compositor_box)
        mini_compositor = VGroup(mini_compositor_box, mini_compositor_label)
        
        # Image Generator
        mini_generator_box = RoundedRectangle(
            height=1.2, width=2.2, 
            stroke_color=IMAGE_COLOR, 
            stroke_width=3,
            fill_color=IMAGE_COLOR,
            fill_opacity=0.1,
            corner_radius=0.15
        )
        mini_generator_label = Text("Image\nGenerator", font_size=16, color=IMAGE_COLOR).move_to(mini_generator_box)
        mini_generator = VGroup(mini_generator_box, mini_generator_label)
        
        # Novelty Score
        mini_novelty_box = RoundedRectangle(
            height=1.2, width=2.2, 
            stroke_color=NOVELTY_COLOR, 
            stroke_width=3,
            fill_color=NOVELTY_COLOR,
            fill_opacity=0.1,
            corner_radius=0.15
        )
        mini_novelty_label = Text("Novelty\nScore", font_size=16, color=NOVELTY_COLOR).move_to(mini_novelty_box)
        mini_novelty = VGroup(mini_novelty_box, mini_novelty_label)
        
        # Arrange in a circular pattern (pentagon-like)
        radius = 2.2
        
        # Position modules in a pentagon shape - shifted down to avoid overlap with title
        mini_pool.move_to(UP * radius * 0.7)  # Top (reduced to avoid title)
        mini_inspiration.move_to(UP * radius * 0.1 + RIGHT * radius * 0.95)  # Top-right
        mini_compositor.move_to(DOWN * radius * 0.6 + RIGHT * radius * 0.95)  # Bottom-right
        mini_generator.move_to(DOWN * radius * 0.6 + LEFT * radius * 0.95)  # Bottom-left
        mini_novelty.move_to(UP * radius * 0.1 + LEFT * radius * 0.95)  # Top-left
        
        modules = VGroup(mini_pool, mini_inspiration, mini_compositor, mini_generator, mini_novelty)
        
        # Add arrows showing flow - using curved arrows for better aesthetics
        flow_arrows = VGroup(
            CurvedArrow(
                mini_pool.get_right() + DOWN * 0.2,
                mini_inspiration.get_top() + LEFT * 0.2,
                angle=-TAU/8,
                stroke_width=3,
                color=WHITE
            ),
            CurvedArrow(
                mini_inspiration.get_bottom() + LEFT * 0.2,
                mini_compositor.get_top() + LEFT * 0.2,
                angle=-TAU/12,
                stroke_width=3,
                color=WHITE
            ),
            CurvedArrow(
                mini_compositor.get_left() + UP * 0.1,
                mini_generator.get_right() + UP * 0.1,
                angle=TAU/6,
                stroke_width=3,
                color=WHITE
            ),
            CurvedArrow(
                mini_generator.get_top() + LEFT * 0.2,
                mini_novelty.get_bottom() + LEFT * 0.2,
                angle=TAU/12,
                stroke_width=3,
                color=WHITE
            ),
            CurvedArrow(
                mini_novelty.get_right() + DOWN * 0.1,
                mini_compositor.get_left() + UP * 0.2,
                angle=-TAU/4,
                stroke_width=4,
                color=YELLOW
            )
        )
        
        full_loop = VGroup(modules, flow_arrows)
        
        self.play(
            Write(loop_text.to_edge(UP).shift(DOWN * 0.5)),
            FadeIn(full_loop),
            run_time=1.5
        )
        self.wait(1.2)
        
        # Highlight the feedback
        feedback_text = Text(
            "Novelty guides next iteration → Process repeats for N generations",
            font_size=20,
            color=YELLOW
        ).to_edge(DOWN)
        
        self.play(
            flow_arrows[-1].animate.set_stroke(width=4, color=YELLOW),
            Write(feedback_text),
            run_time=1.2
        )
        
        self.wait(2.5)
        
        # Fade out everything at the end
        self.play(
            FadeOut(loop_text),
            FadeOut(full_loop),
            FadeOut(feedback_text),
            run_time=1
        )
    
    def create_concept_tag(self, text: str, color: str) -> VGroup:
        """Helper to create a concept tag"""
        label = Text(text, font_size=18, color=color)
        box = SurroundingRectangle(
            label,
            color=color,
            buff=0.1,
            corner_radius=0.1,
            stroke_width=2
        )
        return VGroup(box, label)