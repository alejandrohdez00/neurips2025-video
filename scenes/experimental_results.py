"""
SCENE 5: Experimental Results
Shows key findings from human evaluation and quantitative analysis
"""

from manim import *


class ExperimentalResults(Scene):
    def construct(self):
        # Title
        title = Text("Experimental Results", font_size=48, weight=BOLD).to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.3)
        
        # ============================================================
        # FINDING 1: Human Evaluation - Originality
        # ============================================================
        finding1_title = Text(
            "Human Evaluation of Paintings: Originality",
            font_size=36,
            color=BLUE_B,
            weight=BOLD
        ).shift(UP * 1.5)
        
        # Create ranking display
        ranking1 = VGroup(
            Text("Human", font_size=32, color=ORANGE, weight=BOLD),
            Text("≈", font_size=32, color=WHITE),
            Text("CAS", font_size=32, color=GREEN, weight=BOLD),
            Text(">", font_size=32, color=WHITE),
            Text("GPT", font_size=32, color=PURPLE),
            Text(">", font_size=32, color=WHITE),
            Text("Random", font_size=32, color=GREY)
        ).arrange(RIGHT, buff=0.3).shift(UP * 0.3)
        
        # Key insight
        insight1 = Text(
            "Human + CAS lead in originality",
            font_size=28,
            color=YELLOW,
            weight=BOLD
        ).shift(DOWN * 0.8)
        
        self.play(FadeIn(finding1_title), run_time=0.8)
        self.play(
            LaggedStart(*[Write(item) for item in ranking1], lag_ratio=0.1),
            run_time=1.2
        )
        self.play(FadeIn(insight1), run_time=0.7)
        self.wait(1.5)
        
        # Clear for next finding
        self.play(
            FadeOut(finding1_title),
            FadeOut(ranking1),
            FadeOut(insight1),
            run_time=0.6
        )
        
        # ============================================================
        # FINDING 2: Human Evaluation - Harmony
        # ============================================================
        finding2_title = Text(
            "Human Evaluation of Paintings: Harmony",
            font_size=36,
            color=GREEN_B,
            weight=BOLD
        ).shift(UP * 1.5)
        
        # Create ranking display
        ranking2 = VGroup(
            Text("CAS", font_size=32, color=GREEN, weight=BOLD),
            Text("≈", font_size=32, color=WHITE),
            Text("Human", font_size=32, color=ORANGE, weight=BOLD),
            Text(">", font_size=32, color=WHITE),
            Text("GPT", font_size=32, color=PURPLE),
            Text(">", font_size=32, color=WHITE),
            Text("Random", font_size=32, color=GREY)
        ).arrange(RIGHT, buff=0.3).shift(UP * 0.3)
        
        insight2 = Text(
            "CAS best in harmony (tied with Human)",
            font_size=28,
            color=YELLOW,
            weight=BOLD
        ).shift(DOWN * 0.8)
        
        self.play(FadeIn(finding2_title), run_time=0.8)
        self.play(
            LaggedStart(*[Write(item) for item in ranking2], lag_ratio=0.1),
            run_time=1.2
        )
        self.play(FadeIn(insight2), run_time=0.7)
        self.wait(1.5)
        
        self.play(
            FadeOut(finding2_title),
            FadeOut(ranking2),
            FadeOut(insight2),
            run_time=0.6
        )
        
        # ============================================================
        # FINDING 3: Concept Repetition
        # ============================================================
        finding3_title = Text(
            "Concept Repetition Across Runs",
            font_size=36,
            color=RED_B,
            weight=BOLD
        ).next_to(title, DOWN, buff=1.0)
        
        # Repetition: Human: ~21.7%, CAS: ~23.3%, GPT (Free): 74.3%
        methods3 = ["Human", "CAS", "GPT"]
        repetition = [21.7, 23.3, 74.3]
        colors3 = [ORANGE, GREEN, RED]
        
        # Create bars (0-100% scale)
        bars3 = VGroup()
        bar_width = 0.6
        max_height3 = 3.0
        
        for i, (method, rep, color) in enumerate(zip(methods3, repetition, colors3)):
            x_pos = -3 + i * 3
            bar_height = (rep / 100) * max_height3
            
            bar = Rectangle(
                width=bar_width,
                height=bar_height,
                fill_color=color,
                fill_opacity=0.7,
                stroke_color=color,
                stroke_width=2
            ).move_to([x_pos, bar_height/2 - 1, 0])
            
            label = Text(method, font_size=24, color=WHITE, weight=BOLD).next_to(bar, DOWN, buff=0.2)
            score_text = Text(f"{rep:.1f}%", font_size=26, color=color, weight=BOLD).next_to(bar, UP, buff=0.1)
            
            bars3.add(VGroup(bar, label, score_text))
        
        bars3.move_to([0, -0.3, 0])
        
        self.play(FadeIn(finding3_title), run_time=0.8)
        self.play(
            LaggedStart(*[GrowFromEdge(bar_group, DOWN) for bar_group in bars3], lag_ratio=0.2),
            run_time=1.5
        )
        
        insight3 = Text(
            "GPT repeats ideas the most (~74%)",
            font_size=28,
            color=YELLOW,
            weight=BOLD
        ).next_to(bars3, DOWN, buff=1.5)
        
        self.play(FadeIn(insight3), run_time=0.7)
        self.wait(1.5)
        
        # Final summary - line 1
        summary1 = MarkupText(
            f"CAS achieves human-level <span fgcolor='{BLUE}' weight='bold'>originality</span> and <span fgcolor='{RED}' weight='bold'>harmony</span>",
            font_size=28,
            color=GREEN,
            weight=BOLD
        ).move_to(ORIGIN).shift(UP * 0.3)
        
        # Final summary - line 2
        summary2 = MarkupText(
            f"with greater <span fgcolor='{YELLOW}' weight='bold'>conceptual diversity</span> than GPT.",
            font_size=28,
            color=GREEN,
            weight=BOLD
        ).move_to(ORIGIN).shift(DOWN * 0.3)
        
        self.play(
            FadeOut(finding3_title),
            FadeOut(bars3),
            FadeOut(insight3),
            run_time=0.5
        )
        self.play(
            FadeIn(summary1),
            Write(summary2),
            run_time=1.0
        )
        self.wait(2)
        
        # ============================================================
        # FINAL MESSAGE: Bigger is not always better
        # ============================================================
        self.play(
            FadeOut(title),
            FadeOut(summary1),
            FadeOut(summary2),
            run_time=0.6
        )
        
        # Main headline - highlighted
        headline = Text(
            "Bigger is not always better",
            font_size=48,
            color=YELLOW,
            weight=BOLD
        ).move_to(ORIGIN).shift(UP * 0.5)
        
        # Supporting text - line 1
        supporting_text1 = Text(
            "Lightweight task-specific models can outperform",
            font_size=36,
            color=WHITE,
            weight=BOLD
        ).move_to(ORIGIN).shift(DOWN * 0.5)
        
        # Supporting text - line 2
        supporting_text2 = Text(
            "frontier LLMs in creative tasks.",
            font_size=36,
            color=WHITE,
            weight=BOLD
        ).move_to(ORIGIN).shift(DOWN * 1.2)
        
        self.play(Write(headline), run_time=1.2)
        self.play(
            FadeIn(supporting_text1),
            FadeIn(supporting_text2),
            run_time=1.0
        )
        self.wait(3)