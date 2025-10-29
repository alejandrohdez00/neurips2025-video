"""
SCENE 4: Introducing CAS Solution
Explains the Cultural Alien Sampler approach
"""

from manim import *


class IntroducingCASSolution(Scene):
    def construct(self):
        # First: The question slide
        title = Text("Cultural Alien Sampler (CAS)", font_size=38, weight=BOLD).to_edge(UP, buff=0.3)
        
        question = Text(
            "What if we explicitly navigate away from\ncultural patterns?",
            font_size=32,
            color=YELLOW,
            line_spacing=1.3
        ).move_to(ORIGIN)
        
        self.play(
            FadeIn(title),
            Write(question),
            run_time=1.5
        )
        self.wait(0.8)
        self.play(FadeOut(question), run_time=0.8)
        
        # Second: WikiArt processing slide (simplified)
        dataset_title = Text(
            "We decomposed each WikiArt artwork into 10 concepts using CLIP",
            font_size=26
        ).to_edge(UP, buff=1.3)
        
        self.play(
            title.animate.to_edge(UP, buff=0.3),
            Write(dataset_title),
            run_time=1
        )
        
        # Left side: Three artworks stacked
        artworks = VGroup()
        for i in range(3):
            box = Rectangle(
                height=0.6, width=1.2,
                fill_color=BLUE_E,
                fill_opacity=0.4,
                stroke_color=WHITE,
                stroke_width=2
            )
            label = Text(f"artwork{i+1}", font_size=14, color=WHITE)
            item = VGroup(box, label).arrange(ORIGIN)
            artworks.add(item)
        
        artworks.arrange(DOWN, buff=0.4).shift(LEFT * 3)
        
        self.play(
            LaggedStart(*[FadeIn(art) for art in artworks], lag_ratio=0.2),
            run_time=1
        )
        
        # CLIP label at bottom
        clip_label = Text("CLIP", font_size=28, weight=BOLD, color=PURPLE).to_edge(DOWN, buff=1.5)
        
        self.play(Write(clip_label), run_time=0.6)
        
        # Right side: Three concept lists stacked
        concept_lists = VGroup()
        for i in range(3):
            box = Rectangle(
                height=0.6, width=2.5,
                fill_color=TEAL_E,
                fill_opacity=0.2,
                stroke_color=TEAL,
                stroke_width=2
            )
            label = Text(f"concept list {i+1}", font_size=14, color=TEAL)
            item = VGroup(box, label).arrange(ORIGIN)
            concept_lists.add(item)
        
        concept_lists.arrange(DOWN, buff=0.4).shift(RIGHT * 3)
        
        # Arrows connecting artwork to concept list (one-to-one)
        arrows = VGroup()
        for i in range(3):
            arrow = Arrow(
                artworks[i].get_right(),
                concept_lists[i].get_left(),
                color=PURPLE,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.15
            )
            arrows.add(arrow)
        
        self.play(
            LaggedStart(*[GrowArrow(arrow) for arrow in arrows], lag_ratio=0.2),
            run_time=1
        )
        
        self.play(
            LaggedStart(*[FadeIn(cl) for cl in concept_lists], lag_ratio=0.2),
            run_time=1
        )
        
        self.wait(1)
        
        # Clear everything
        self.play(
            FadeOut(dataset_title),
            FadeOut(artworks),
            FadeOut(clip_label),
            FadeOut(arrows),
            FadeOut(concept_lists),
            run_time=0.8
        )
        
        # Create split view with divider
        divider = DashedLine(UP * 2.7, DOWN * 3.5, color=GREY, dash_length=0.15)
        self.play(Create(divider), run_time=0.5)
        
        # LEFT SIDE: Concept Coherence Model
        coherence_title = Text(
            "Concept Coherence Model",
            font_size=24,
            color=GREEN
        ).move_to(LEFT * 3.5 + UP * 2.5)
        
        coherence_question = Text(
            '"Do these concepts fit together in an artwork?"',
            font_size=18,
            color=GREEN_A,
            slant=ITALIC
        ).next_to(coherence_title, DOWN, buff=0.25)
        
        # Show artwork-based training
        artwork_icon = Rectangle(
            height=0.5, width=0.5,
            fill_color=GREEN_E,
            fill_opacity=0.4,
            stroke_color=GREEN
        ).move_to(LEFT * 3.5 + UP * 1.3)
        
        artwork_label = Text(
            "GPT2 trained on concepts\nused together in artworks",
            font_size=15,
            color=GREEN_A,
            line_spacing=0.9
        ).next_to(artwork_icon, DOWN, buff=0.18)
        
        # Example concepts with high coherence
        coherent_concepts = VGroup(
            Text("Anime", font_size=17, color=GREEN),
            Text("Rabbit", font_size=17, color=GREEN),
            Text("Renaissance", font_size=17, color=GREEN),
        ).arrange(DOWN, buff=0.25).move_to(LEFT * 3.5 + DOWN * 0.6)
        
        coherence_arrows = VGroup(*[
            Arrow(
                coherent_concepts[i].get_bottom(),
                coherent_concepts[i+1].get_top(),
                color=GREEN,
                buff=0.12,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.15
            )
            for i in range(len(coherent_concepts)-1)
        ])
        
        high_score = Text(
            "High Score ✓",
            font_size=20,
            color=GREEN,
            weight=BOLD
        ).next_to(coherent_concepts, DOWN, buff=0.45)
        
        # RIGHT SIDE: Cultural Context Model
        context_title = Text(
            "Cultural Context Model",
            font_size=24,
            color=RED
        ).move_to(RIGHT * 3.5 + UP * 2.5)
        
        context_question = Text(
            '"Is this combination typical?"',
            font_size=18,
            color=RED_A,
            slant=ITALIC
        ).next_to(context_title, DOWN, buff=0.25)
        
        # Show artist-based training
        artist_icon = VGroup(
            *[Rectangle(height=0.28, width=0.28, fill_opacity=0.4,
                       stroke_color=RED, fill_color=RED_E).shift(RIGHT * 0.22 * i)
              for i in range(-1, 2)]
        ).move_to(RIGHT * 3.5 + UP * 1.3)
        
        artist_label = Text(
            "GPT-2 trained on concepts extracted from\nartists' complete body of work",
            font_size=15,
            color=RED_A,
            line_spacing=0.9
        ).next_to(artist_icon, DOWN, buff=0.18)
        
        # Same concepts but checking cultural typicality
        typical_concepts = VGroup(
            Text("Anime", font_size=17, color=RED),
            Text("Rabbit", font_size=17, color=RED),
            Text("Renaissance", font_size=17, color=RED),
        ).arrange(DOWN, buff=0.25).move_to(RIGHT * 3.5 + DOWN * 0.6)
        
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
            font_size=20,
            color=RED,
            weight=BOLD
        ).next_to(typical_concepts, DOWN, buff=0.45)
        
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
            height=1.2, width=12,
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
            font_size=32
        ).move_to(formula_bg).shift(UP * 0.25)
        formula[1].set_color(GREEN)
        formula[3].set_color(RED)
        
        target = Text(
            "Target: Coherent but Culturally Untypical Combinations",
            font_size=23,
            color=YELLOW,
            weight=BOLD
        ).next_to(formula, DOWN, buff=0.25)
        
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