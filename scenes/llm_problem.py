"""
SCENE 3: LLM Problem
Demonstrates how LLMs fall into cultural gravity wells
"""

from manim import *


class LLMProblem(Scene):
    def construct(self):
        # Title
        title = Text("The Problem: Cultural Anchoring", font_size=40).to_edge(UP)
        
        # Subtitle explaining the reframed problem
        subtitle = Text(
            "LLMs trained on human culture repeat familiar combinations",
            font_size=26,
            color=GREY
        ).next_to(title, DOWN, buff=0.3)
        
        self.play(
            Write(title),
            Write(subtitle),
            run_time=1.2
        )
        
        # Create the concept space
        space = Rectangle(
            height=5, width=11,
            stroke_color=PURPLE_A,
            stroke_width=2,
            fill_opacity=0
        ).shift(DOWN * 0.5)
        
        space_label = Text(
            "Concept Space",
            font_size=24,
            color=PURPLE_A
        ).next_to(space, UP, buff=0.1).shift(LEFT * 4)
        
        self.play(
            Create(space),
            Write(space_label),
            run_time=1
        )
        
        # Create "cultural gravity wells" - regions of high density
        gravity_wells = []
        well_positions = [
            LEFT * 3 + UP * 0.5,
            RIGHT * 1 + DOWN * 0.8,
            LEFT * 1 + DOWN * 1.5
        ]
        
        well_labels = [
            "mythology\ndreamscape\nphoenix",
            "cyberpunk\nquantum\nrobot",
            "bioluminescence\nsynesthesia"
        ]
        
        for pos, label_text in zip(well_positions, well_labels):
            # Create a gravity well visualization (concentric circles)
            well = VGroup()
            for i in range(4):
                circle = Circle(
                    radius=0.8 - i*0.15,
                    color=RED,
                    stroke_width=2,
                    stroke_opacity=0.6 - i*0.15
                ).move_to(pos)
                well.add(circle)
            
            # Add label
            label = Text(
                label_text,
                font_size=16,
                color=RED_A,
                line_spacing=0.8
            ).move_to(pos)
            
            well.add(label)
            gravity_wells.append(well)
        
        # Animate gravity wells appearing
        self.play(
            LaggedStart(*[FadeIn(well) for well in gravity_wells], lag_ratio=0.3),
            run_time=2
        )
        
        # Show GPT icon/label
        gpt_icon = Text("GPT-4o", font_size=32, color=PURPLE, weight=BOLD)
        gpt_icon.to_corner(UL).shift(DOWN * 1.5 + RIGHT * 0.5)
        
        self.play(FadeIn(gpt_icon), run_time=0.5)
        
        # Simulate GPT generating concepts - they keep falling into gravity wells
        # Create a tracer dot
        tracer = Dot(color=YELLOW, radius=0.08).move_to(space.get_top())
        
        self.play(FadeIn(tracer), run_time=0.3)
        
        # Path that keeps getting pulled into wells
        paths = [
            # Start from top, wander, get pulled into first well
            [space.get_top(), 
             LEFT * 2 + UP * 1.5, 
             LEFT * 2.5 + UP * 0.8,
             well_positions[0]],
            # Jump to new position, get pulled into second well
            [RIGHT * 0.5 + UP * 0.2,
             RIGHT * 0.8 + DOWN * 0.3,
             well_positions[1]],
            # Try again, pulled into third well
            [LEFT * 0.5 + DOWN * 0.5,
             LEFT * 0.8 + DOWN * 1.2,
             well_positions[2]]
        ]
        
        # Animate the paths
        for path in paths:
            self.play(
                MoveAlongPath(tracer, VMobject().set_points_as_corners(path)),
                run_time=1.2,
                rate_func=rush_into
            )
            # Pulse the tracer when it reaches a well
            self.play(
                tracer.animate.scale(1.5).set_color(RED),
                run_time=0.3
            )
            self.play(
                tracer.animate.scale(1/1.5).set_color(YELLOW),
                run_time=0.3
            )
            # Leave a mark
            mark = Dot(color=RED_A, radius=0.05).move_to(tracer.get_center())
            self.add(mark)
            self.wait(0.2)
        
        # Show statistics
        stat_box = Rectangle(
            height=1.2, width=4,
            fill_color=BLACK,
            fill_opacity=0.8,
            stroke_color=RED,
            stroke_width=2
        ).to_corner(DR)
        
        stat_text = VGroup(
            Text("Concept Repetition:", font_size=22, color=WHITE),
            Text("GPT: 59%", font_size=26, color=RED, weight=BOLD),
            Text("Free GPT: 74%", font_size=26, color=RED, weight=BOLD)
        ).arrange(DOWN, buff=0.15).move_to(stat_box)
        
        self.play(
            FadeIn(stat_box),
            Write(stat_text),
            run_time=1.2
        )
        
        self.wait(1.5)
