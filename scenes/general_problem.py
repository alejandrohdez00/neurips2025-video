"""
SCENE 0: General Problem
Illustrates the gap between LLM success in verifiable domains vs culturally-situated domains
"""

from manim import *

ORANGE_A = "#FF8C00"


class GeneralProblem(Scene):
    def construct(self):
        # ============================================================
        # PART 1: Current Trend - Success in Verifiable Domains
        # ============================================================
        
        # Main message
        trend_message = VGroup(
            Text(
                "Open-ended LLM systems are gaining traction",
                font_size=36,
                weight=BOLD
            ),
            Text(
                "for discovery in verifiable domains",
                font_size=36,
                weight=BOLD
            )
        ).arrange(DOWN, buff=0.2).to_edge(UP, buff=1)
        
        self.play(
            FadeIn(trend_message),
            run_time=1.2
        )
        self.wait(0.5)
        
        # Examples with clean boxes
        examples_title = Text(
            "Examples:",
            font_size=28,
            color=GREY_A
        ).next_to(trend_message, DOWN, buff=0.8)
        
        # Create three clean domain boxes
        box_width = 2.8
        box_height = 1.2
        spacing = 0.5
        
        math_box = VGroup(
            Rectangle(
                width=box_width,
                height=box_height,
                fill_color=GREEN_E,
                fill_opacity=0.2,
                stroke_color=GREEN,
                stroke_width=3
            ),
            Text("Math", font_size=28, color=GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0)
        math_box[1].move_to(math_box[0])
        
        science_box = VGroup(
            Rectangle(
                width=box_width,
                height=box_height,
                fill_color=BLUE_E,
                fill_opacity=0.2,
                stroke_color=BLUE,
                stroke_width=3
            ),
            Text("Science", font_size=28, color=BLUE, weight=BOLD)
        ).arrange(DOWN, buff=0)
        science_box[1].move_to(science_box[0])
        
        code_box = VGroup(
            Rectangle(
                width=box_width,
                height=box_height,
                fill_color=PURPLE_E,
                fill_opacity=0.2,
                stroke_color=PURPLE,
                stroke_width=3
            ),
            Text("Coding", font_size=28, color=PURPLE, weight=BOLD)
        ).arrange(DOWN, buff=0)
        code_box[1].move_to(code_box[0])
        
        # Arrange boxes horizontally
        boxes = VGroup(math_box, science_box, code_box).arrange(
            RIGHT, buff=spacing
        ).next_to(examples_title, DOWN, buff=0.6)
        
        self.play(FadeIn(examples_title), run_time=0.6)
        self.play(
            LaggedStart(
                FadeIn(math_box, shift=UP * 0.3),
                FadeIn(science_box, shift=UP * 0.3),
                FadeIn(code_box, shift=UP * 0.3),
                lag_ratio=0.2
            ),
            run_time=1.5
        )
        self.wait(0.5)
        
        # Key characteristic
        characteristic = VGroup(
            Text(
                "Goals are explicit",
                font_size=26,
                color=WHITE
            ),
            Text(
                "Correctness is measurable",
                font_size=26,
                color=WHITE
            )
        ).arrange(DOWN, buff=0.3).next_to(boxes, DOWN, buff=0.8)
        
        self.play(
            Write(characteristic[0]),
            run_time=1
        )
        self.play(
            Write(characteristic[1]),
            run_time=1
        )
        self.wait(1)
        
        # ============================================================
        # TRANSITION: Fade out and introduce "However"
        # ============================================================
        
        # Fade everything out
        first_screen = VGroup(
            trend_message,
            examples_title,
            boxes,
            characteristic
        )
        
        self.play(
            FadeOut(first_screen),
            run_time=0.8
        )
        self.wait(0.3)
        
        # ============================================================
        # PART 2: The Gap - Culturally-Situated Domains
        # ============================================================
        
        # "However" message
        however_message = VGroup(
            Text(
                "However, ambiguous and culturally-situated tasks",
                font_size=30,
                weight=BOLD,
                color=ORANGE
            ),
            Text(
                "remain largely unexplored",
                font_size=30,
                weight=BOLD,
                color=ORANGE
            ),
            Text(
                "despite their centrality to human cognition",
                font_size=30,
                weight=BOLD,
                color=ORANGE
            )
        ).arrange(DOWN, buff=0.2).to_edge(UP, buff=1)
        
        self.play(
            FadeIn(however_message),
            run_time=1.2
        )
        self.wait(0.5)
        
        # Examples of unexplored domains
        unexplored_title = Text(
            "Examples:",
            font_size=28,
            color=GREY_A
        ).next_to(however_message, DOWN, buff=0.8)
        
        # Create three clean domain boxes for cultural domains
        art_box = VGroup(
            Rectangle(
                width=box_width,
                height=box_height,
                fill_color=RED_E,
                fill_opacity=0.2,
                stroke_color=RED,
                stroke_width=3
            ),
            Text("Art", font_size=28, color=RED, weight=BOLD)
        ).arrange(DOWN, buff=0)
        art_box[1].move_to(art_box[0])
        
        writing_box = VGroup(
            Rectangle(
                width=box_width,
                height=box_height,
                fill_color=YELLOW_E,
                fill_opacity=0.2,
                stroke_color=YELLOW,
                stroke_width=3
            ),
            Text("Creative Writing", font_size=22, color=YELLOW, weight=BOLD)
        ).arrange(DOWN, buff=0)
        writing_box[1].move_to(writing_box[0])
        
        music_box = VGroup(
            Rectangle(
                width=box_width,
                height=box_height,
                fill_color=TEAL_E,
                fill_opacity=0.2,
                stroke_color=TEAL,
                stroke_width=3
            ),
            Text("Music", font_size=28, color=TEAL, weight=BOLD)
        ).arrange(DOWN, buff=0)
        music_box[1].move_to(music_box[0])
        
        # Arrange boxes horizontally
        cultural_boxes = VGroup(art_box, writing_box, music_box).arrange(
            RIGHT, buff=spacing
        ).next_to(unexplored_title, DOWN, buff=0.6)
        
        self.play(FadeIn(unexplored_title), run_time=0.6)
        self.play(
            LaggedStart(
                FadeIn(art_box, shift=UP * 0.3),
                FadeIn(writing_box, shift=UP * 0.3),
                FadeIn(music_box, shift=UP * 0.3),
                lag_ratio=0.2
            ),
            run_time=1.5
        )
        self.wait(0.5)
        
        # Key characteristic of these domains
        cultural_characteristic = VGroup(
            Text(
                "No fixed endpoints",
                font_size=26,
                color=WHITE
            ),
            Text(
                "No universal criteria for success",
                font_size=26,
                color=WHITE
            ),
            Text(
                "Require contextual sensitivity and iterative exploration",
                font_size=26,
                color=WHITE
            )
        ).arrange(DOWN, buff=0.3).next_to(cultural_boxes, DOWN, buff=0.7)
        
        self.play(
            Write(cultural_characteristic[0]),
            run_time=1
        )
        self.play(
            Write(cultural_characteristic[1]),
            run_time=1
        )
        self.play(
            Write(cultural_characteristic[2]),
            run_time=1
        )        
        self.wait(2)