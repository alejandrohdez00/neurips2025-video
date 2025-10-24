"""
SCENE 2: Concept Reframing
Shows art as conceptual combinations rather than visual objects
"""

from manim import *
import numpy as np


class ConceptReframing(Scene):
    def construct(self):
        # Title
        title = Text("Reframing: Art as Conceptual Combinations", font_size=40).to_edge(UP)
        
        # Start with a traditional art view
        traditional_label = Text(
            "Traditional View: Art as Visual Object",
            font_size=28,
            color=GREY
        ).to_edge(UP).shift(DOWN * 0.5)
        
        # Artwork representation - try to load image, fallback to placeholder
        try:
            import os
            image_path = os.path.join(os.path.dirname(__file__), "..", "image__gen0.png")
            artwork = ImageMobject(image_path).scale(0.8)
            artwork.shift(UP * 0.2)
        except:
            # Placeholder if image not found
            artwork = Rectangle(
                height=3, width=3,
                fill_color=BLUE_E,
                fill_opacity=0.5,
                stroke_color=WHITE,
                stroke_width=3
            )
            artwork.shift(UP * 0.2)
        
        self.play(Write(traditional_label), run_time=0.8)
        self.play(FadeIn(artwork), run_time=1)
        self.wait(0.5)
        
        # Transition: "But what if we think differently?"
        self.play(
            FadeOut(traditional_label),
            Write(title),
            run_time=1
        )
        
        # Dissolve artwork into concepts
        concepts_data = [
            ("Woman", ORANGE),
            ("Ukiyo-e", TEAL),
            ("Landscape", GREEN),
            ("Winter", BLUE),
            ("Mountain", PURPLE),
        ]
        
        concept_tags = VGroup(*[
            self.create_concept_tag(text, color)
            for text, color in concepts_data
        ])
        
        # Initially all at artwork center
        for tag in concept_tags:
            tag.move_to(artwork.get_center())
        
        # Dissolve animation
        self.play(
            artwork.animate.set_fill_opacity(0.05).set_stroke_opacity(0.3),
            LaggedStart(*[FadeIn(tag, scale=0.5) for tag in concept_tags], lag_ratio=0.15),
            run_time=1.5
        )
        self.play(FadeOut(artwork))
        
        # Spread concepts in a circle
        radius = 2
        angles = [i * 2*PI/len(concept_tags) for i in range(len(concept_tags))]
        positions = [
            radius * np.array([np.cos(angle), np.sin(angle), 0])
            for angle in angles
        ]
        
        self.play(
            *[tag.animate.move_to(pos) for tag, pos in zip(concept_tags, positions)],
            run_time=1.5
        )
        
        # Show the combinatorial space
        subtitle = Text(
            "Art = Strategic Recombination of Concepts",
            font_size=32,
            color=YELLOW
        ).to_edge(DOWN)
        
        # Create connections showing possible combinations
        all_connections = VGroup()
        for i in range(len(concept_tags)):
            for j in range(i+1, len(concept_tags)):
                line = Line(
                    concept_tags[i].get_center(),
                    concept_tags[j].get_center(),
                    stroke_width=1,
                    color=GREY,
                    stroke_opacity=0.3
                )
                all_connections.add(line)
        
        self.play(
            Create(all_connections),
            run_time=1.2
        )
        
        # Highlight a few example combinations with pulsing
        combo1 = VGroup(concept_tags[0], concept_tags[1], concept_tags[2])  # Woman + Ukiyo-e + Landscape
        combo2 = VGroup(concept_tags[1], concept_tags[3], concept_tags[4])  # Ukiyo-e + Winter + Mountain
        
        self.play(Write(subtitle), run_time=0.8)
        
        # Pulse first combination
        self.play(
            *[tag.animate.scale(1.2).set_stroke_width(4) for tag in combo1],
            run_time=0.4
        )
        self.play(
            *[tag.animate.scale(1/1.2).set_stroke_width(2) for tag in combo1],
            run_time=0.4
        )
        
        # Pulse second combination
        self.play(
            *[tag.animate.scale(1.2).set_stroke_width(4) for tag in combo2],
            run_time=0.4
        )
        self.play(
            *[tag.animate.scale(1/1.2).set_stroke_width(2) for tag in combo2],
            run_time=0.4
        )
        
        self.wait(1)
    
    def create_concept_tag(self, text: str, color: str) -> VGroup:
        """Helper to create a rounded rectangle concept tag"""
        label = Text(text, font_size=22, color=color, weight=BOLD)
        box = SurroundingRectangle(
            label,
            color=color,
            buff=0.15,
            corner_radius=0.15,
            stroke_width=2,
            fill_opacity=0.1
        )
        return VGroup(box, label)
