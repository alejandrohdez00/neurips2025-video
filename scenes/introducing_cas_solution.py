"""
SCENE 4: Introducing CAS Solution
Explains the Cultural Alien Sampler approach
"""

from manim import *


class IntroducingCASSolution(Scene):
    def construct(self):
        # Transition from problem
        question = Text(
            "What if we explicitly navigate away from\ncultural patterns?",
            font_size=36,
            color=YELLOW,
            line_spacing=1.2
        )
        self.play(Write(question), run_time=1.5)
        self.wait(0.8)
        self.play(FadeOut(question))
        
        # Title
        title = Text("Cultural Alien Sampler (CAS)", font_size=42, weight=BOLD).to_edge(UP)
        self.play(Write(title), run_time=0.8)
        
        # Create split view with divider
        divider = DashedLine(UP * 3, DOWN * 3.5, color=GREY, dash_length=0.15)
        self.play(Create(divider), run_time=0.5)
        
        # LEFT SIDE: Concept Coherence Model
        coherence_title = Text(
            "Concept Coherence Model",
            font_size=28,
            color=GREEN
        ).move_to(LEFT * 3.5 + UP * 2.8)
        
        coherence_question = Text(
            '"Do these concepts fit together?"',
            font_size=20,
            color=GREEN_A,
            slant=ITALIC
        ).next_to(coherence_title, DOWN, buff=0.2)
        
        # Show artwork-based training
        artwork_icon = Rectangle(
            height=0.6, width=0.6,
            fill_color=GREEN_E,
            fill_opacity=0.4,
            stroke_color=GREEN
        ).move_to(LEFT * 3.5 + UP * 1.2)
        
        artwork_label = Text(
            "Trained on:\nartwork combinations",
            font_size=16,
            color=GREEN_A,
            line_spacing=0.9
        ).next_to(artwork_icon, DOWN, buff=0.15)
        
        # Example concepts with high coherence
        coherent_concepts = VGroup(
            Text("Hunter", font_size=18, color=GREEN),
            Text("Knife", font_size=18, color=GREEN),
            Text("Machinery", font_size=18, color=GREEN),
        ).arrange(DOWN, buff=0.2).move_to(LEFT * 3.5 + DOWN * 0.3)
        
        coherence_arrows = VGroup(*[
            Arrow(
                coherent_concepts[i].get_bottom(),
                coherent_concepts[i+1].get_top(),
                color=GREEN,
                buff=0.1,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.15
            )
            for i in range(len(coherent_concepts)-1)
        ])
        
        high_score = Text(
            "High Score ✓",
            font_size=22,
            color=GREEN,
            weight=BOLD
        ).next_to(coherent_concepts, DOWN, buff=0.4)
        
        # RIGHT SIDE: Cultural Context Model
        context_title = Text(
            "Cultural Context Model",
            font_size=28,
            color=RED
        ).move_to(RIGHT * 3.5 + UP * 2.8)
        
        context_question = Text(
            '"Are these combinations typical?"',
            font_size=20,
            color=RED_A,
            slant=ITALIC
        ).next_to(context_title, DOWN, buff=0.2)
        
        # Show artist-based training
        artist_icon = VGroup(
            *[Rectangle(height=0.3, width=0.3, fill_opacity=0.4, 
                       stroke_color=RED, fill_color=RED_E).shift(RIGHT * 0.25 * i)
              for i in range(-1, 2)]
        ).move_to(RIGHT * 3.5 + UP * 1.2)
        
        artist_label = Text(
            "Trained on:\nartist vocabularies",
            font_size=16,
            color=RED_A,
            line_spacing=0.9
        ).next_to(artist_icon, DOWN, buff=0.15)
        
        # Same concepts but checking cultural typicality
        typical_concepts = VGroup(
            Text("Hunter", font_size=18, color=RED),
            Text("Knife", font_size=18, color=RED),
            Text("Machinery", font_size=18, color=RED),
        ).arrange(DOWN, buff=0.2).move_to(RIGHT * 3.5 + DOWN * 0.3)
        
        # Show weak/broken connections (culturally rare)
        weak_arrows = VGroup(
            DashedLine(
                typical_concepts[0].get_bottom(),
                typical_concepts[1].get_top(),
                color=RED,
                dash_length=0.1,
                stroke_width=2,
                stroke_opacity=0.5
            ),
            DashedLine(
                typical_concepts[1].get_bottom(),
                typical_concepts[2].get_top(),
                color=RED,
                dash_length=0.1,
                stroke_width=1,
                stroke_opacity=0.3
            )
        )
        
        low_score = Text(
            "Low Score ✓",
            font_size=22,
            color=RED,
            weight=BOLD
        ).next_to(typical_concepts, DOWN, buff=0.4)
        
        # Animate left side
        self.play(
            Write(coherence_title),
            Write(coherence_question),
            run_time=1
        )
        self.play(
            FadeIn(artwork_icon),
            Write(artwork_label),
            run_time=0.8
        )
        self.play(
            LaggedStart(*[FadeIn(concept) for concept in coherent_concepts], lag_ratio=0.2),
            run_time=1
        )
        self.play(
            LaggedStart(*[GrowArrow(arrow) for arrow in coherence_arrows], lag_ratio=0.3),
            run_time=1
        )
        self.play(Write(high_score), run_time=0.5)
        
        # Animate right side
        self.play(
            Write(context_title),
            Write(context_question),
            run_time=1
        )
        self.play(
            FadeIn(artist_icon),
            Write(artist_label),
            run_time=0.8
        )
        self.play(
            LaggedStart(*[FadeIn(concept) for concept in typical_concepts], lag_ratio=0.2),
            run_time=1
        )
        self.play(
            LaggedStart(*[Create(arrow) for arrow in weak_arrows], lag_ratio=0.3),
            run_time=1
        )
        self.play(Write(low_score), run_time=0.5)
        
        # Show the scoring formula at the bottom
        formula_bg = Rectangle(
            height=1.3, width=12,
            fill_color=BLACK,
            fill_opacity=0.85,
            stroke_color=YELLOW,
            stroke_width=2
        ).to_edge(DOWN, buff=0)
        
        formula = MathTex(
            r"S_{\text{CAS}} = (1-\beta) \cdot ",
            r"\text{Coherence}",
            r" \; - \; \beta \cdot ",
            r"\text{Typicality}",
            font_size=36
        ).move_to(formula_bg).shift(UP * 0.3)
        formula[1].set_color(GREEN)
        formula[3].set_color(RED)
        
        target = Text(
            "Target: Coherent but Culturally Alien",
            font_size=26,
            color=YELLOW,
            weight=BOLD
        ).next_to(formula, DOWN, buff=0.2)
        
        self.play(FadeIn(formula_bg), run_time=0.5)
        self.play(Write(formula), run_time=1.2)
        self.play(Write(target), run_time=0.8)
        
        # Visual indication of the combination being selected
        selection_box = SurroundingRectangle(
            VGroup(coherent_concepts, typical_concepts),
            color=YELLOW,
            stroke_width=4,
            buff=0.3,
            corner_radius=0.2
        )
        
        self.play(Create(selection_box), run_time=0.8)
        self.play(
            selection_box.animate.set_stroke(width=6),
            rate_func=there_and_back,
            run_time=0.6
        )
        
        self.wait(1.5)
