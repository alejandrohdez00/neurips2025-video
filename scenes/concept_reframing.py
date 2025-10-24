"""
SCENE 2: Concept Reframing
Shows art as conceptual combinations rather than visual objects
"""

from manim import *
import numpy as np


class ConceptReframing(Scene):
    def construct(self):
        # Title - simpler animation
        title = Text("Reframing: Art as Conceptual Combinations", font_size=40).to_edge(UP)
        
        # Start with a traditional art view - simpler animation
        traditional_label = Text(
            "Traditional View: Art as Visual Object",
            font_size=28,
            color=GREY
        ).to_edge(UP).shift(DOWN * 0.5)
        
        # Artwork representation - try to load image, fallback to placeholder
        try:
            import os
            image_path = os.path.join(os.path.dirname(__file__), "..", "image__gen0.png")
            artwork = ImageMobject(image_path).scale(1.2)  # Bigger initial size
            artwork.shift(UP * 0.2)
        except:
            # Placeholder if image not found - also bigger
            artwork = Rectangle(
                height=4, width=4,
                fill_color=BLUE_E,
                fill_opacity=0.5,
                stroke_color=WHITE,
                stroke_width=3
            )
            artwork.shift(UP * 0.2)
        
        # More elegant text appearance
        self.play(FadeIn(traditional_label, shift=DOWN*0.2), run_time=1)
        self.play(FadeIn(artwork, scale=0.95), run_time=1.2)
        self.wait(1.2)  # Longer wait to let viewers see the image
        
        # Transition: "But what if we think differently?"
        self.play(
            FadeOut(traditional_label, shift=UP*0.2),
            FadeIn(title, shift=DOWN*0.2),
            run_time=1.2
        )
        self.wait(0.5)
        
        # Create concept tags data
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
        
        # NEW: Split artwork into patches
        # Create a grid of patches (3x3)
        patches = VGroup()
        rows, cols = 3, 3
        artwork_height = artwork.height
        artwork_width = artwork.width
        patch_height = artwork_height / rows
        patch_width = artwork_width / cols
        
        for i in range(rows):
            for j in range(cols):
                # Create a rectangle for each patch
                patch = Rectangle(
                    height=patch_height,
                    width=patch_width,
                    fill_color=BLUE_E,
                    fill_opacity=0.5,
                    stroke_color=WHITE,
                    stroke_width=1,
                    stroke_opacity=0.5
                )
                # Position the patch in grid
                x_offset = (j - cols/2 + 0.5) * patch_width
                y_offset = (rows/2 - i - 0.5) * patch_height
                patch.move_to(artwork.get_center() + RIGHT * x_offset + UP * y_offset)
                patches.add(patch)
        
        # First, overlay patches on the artwork
        self.play(
            artwork.animate.set_opacity(0.3),
            FadeIn(patches),
            run_time=1.2
        )
        self.wait(0.3)
        
        # Select specific patches to transform into concepts
        # We'll use 5 patches spread across the grid for our 5 concepts
        selected_patch_indices = [0, 2, 4, 6, 8]  # corners and center
        
        # Transform selected patches into concept tags
        transformations = []
        for idx, patch_idx in enumerate(selected_patch_indices):
            if idx < len(concept_tags):
                # Position concept tag at patch location initially
                concept_tags[idx].move_to(patches[patch_idx].get_center())
                transformations.append(
                    Transform(patches[patch_idx], concept_tags[idx])
                )
        
        # Animate the transformation
        self.play(
            *transformations,
            FadeOut(artwork),
            *[FadeOut(patches[i]) for i in range(len(patches)) if i not in selected_patch_indices],
            run_time=1.8
        )
        
        # Remove transformed patches and add concept tags
        for idx in selected_patch_indices:
            patches[idx].become(concept_tags[selected_patch_indices.index(idx)])
        
        self.wait(0.5)
        
        # Spread concepts in a circle
        radius = 2.2
        angles = [i * 2*PI/len(concept_tags) for i in range(len(concept_tags))]
        positions = [
            radius * np.array([np.cos(angle), np.sin(angle), 0])
            for angle in angles
        ]
        
        # Move concepts to circle positions
        animations = []
        for idx, patch_idx in enumerate(selected_patch_indices):
            animations.append(patches[patch_idx].animate.move_to(positions[idx]))
        
        self.play(*animations, run_time=2)
        self.wait(0.8)
        
        # Show the combinatorial space
        subtitle = Text(
            "Art = Strategic Recombination of Concepts",
            font_size=32,
            color=YELLOW
        ).to_edge(DOWN)
        
        # Create connections showing possible combinations
        all_connections = VGroup()
        concept_positions = [patches[idx].get_center() for idx in selected_patch_indices]
        
        for i in range(len(concept_positions)):
            for j in range(i+1, len(concept_positions)):
                line = Line(
                    concept_positions[i],
                    concept_positions[j],
                    stroke_width=1,
                    color=GREY,
                    stroke_opacity=0.3
                )
                all_connections.add(line)
        
        self.play(
            Create(all_connections),
            run_time=1.5
        )
        
        # Simpler subtitle animation
        self.play(FadeIn(subtitle, shift=UP*0.2), run_time=1)
        
        # Just let viewers see the concepts as the combination
        self.wait(2)
    
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
