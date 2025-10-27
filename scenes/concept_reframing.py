"""
SCENE 2: Concept Reframing
Shows art as conceptual combinations rather than visual objects
"""

from manim import *
import numpy as np


class ConceptReframing(Scene):
    def construct(self):
        # Title - simpler animation
        title = Text("Reframing: Painting as Conceptual Combinations", font_size=32).to_edge(UP)
        
        # Start with a traditional art view - simpler animation
        traditional_label = Text(
            "Traditional View: Painting as Visual Object",
            font_size=32,
            color=GREY
        ).to_edge(UP)
        
        # Artwork representation - try to load image, fallback to placeholder
        try:
            import os
            image_path = os.path.join(os.path.dirname(__file__), "..", "river-st-urbain-1930.jpg!Large.jpg")
            artwork = ImageMobject(image_path).scale(1.2)  # Bigger initial size
            artwork.shift(DOWN * 0.5)
        except:
            # Placeholder if image not found - also bigger
            artwork = Rectangle(
                height=4, width=4,
                fill_color=BLUE_E,
                fill_opacity=0.5,
                stroke_color=WHITE,
                stroke_width=3
            )
            artwork.shift(DOWN * 0.5)
        
        # More elegant text appearance
        self.play(FadeIn(traditional_label, shift=DOWN*0.2), run_time=1)
        self.play(FadeIn(artwork, scale=0.95), run_time=1.2)
        self.wait(1.5)  # Longer wait to let viewers see the image
        
        # Transition: "But what if we think differently?"
        # First fade out the traditional label
        self.play(
            FadeOut(traditional_label, shift=UP*0.2),
            run_time=1
        )
        self.wait(0.3)
        
        # Then bring in the new reframing title
        self.play(
            FadeIn(title, shift=DOWN*0.2),
            run_time=1.2
        )
        self.wait(0.8)
        
        # Create concept tags data
        concepts_data = [
            ("Winter", ORANGE),
            ("Cottage", TEAL),
            ("Landscape", GREEN),
            ("Mountain", BLUE),
            ("Post-Impressionism", PURPLE),
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
        
        self.wait(0.8)
        
        # Show the combinatorial space
        subtitle = Text(
            "Painting generation -> Strategic Recombination of Concepts",
            font_size=32,
            color=YELLOW
        ).to_edge(DOWN)
        
        # Bring concept boxes to the front so lines stay behind
        for idx in selected_patch_indices:
            patches[idx].set_z_index(1)
        
        # Create connections showing possible combinations
        # Layout: 4 corners (indices 0,1,2,3) + 1 center (index 4)
        all_connections = VGroup()
        concept_positions = [patches[idx].get_center() for idx in selected_patch_indices]
        
        # Create a line with glow effect
        def create_glowing_line(start, end, color=BLUE):
            # Main line
            main_line = Line(start, end, stroke_width=2.5, color=color, stroke_opacity=0.8)
            # Glow layers
            glow1 = Line(start, end, stroke_width=6, color=color, stroke_opacity=0.3)
            glow2 = Line(start, end, stroke_width=10, color=color, stroke_opacity=0.15)
            return VGroup(glow2, glow1, main_line)
        
        # Connect center (index 4) to all corners (indices 0,1,2,3)
        center_idx = 4
        for corner_idx in range(4):
            connection = create_glowing_line(
                concept_positions[center_idx],
                concept_positions[corner_idx],
                color=TEAL
            )
            all_connections.add(connection)
        
        # Connect corners to form square perimeter (0->1->2->3->0)
        corner_pairs = [(0,1), (1,2), (2,3), (3,0)]
        for i, j in corner_pairs:
            connection = create_glowing_line(
                concept_positions[i],
                concept_positions[j],
                color=BLUE
            )
            all_connections.add(connection)
        
        self.play(
            Create(all_connections),
            run_time=1.8
        )
        
        # Simpler subtitle animation
        self.play(FadeIn(subtitle, shift=UP*0.2), run_time=1)
        
        # Just let viewers see the concepts as the combination
        self.wait(2)
        
        # NEW SECTION: Why this reframing is better
        # Fade out current elements
        self.play(
            FadeOut(all_connections),
            *[FadeOut(patches[idx]) for idx in selected_patch_indices],
            FadeOut(subtitle),
            run_time=1
        )
        
        # New title for this section
        why_better_title = Text(
            "Why is this reframing better?",
            font_size=32
        ).to_edge(UP)
        
        self.play(
            Transform(title, why_better_title),
            run_time=1
        )
        self.wait(0.5)
        
        # Show the explanation text
        explanation_text = Text(
            "We transform an intractable problem into a discrete\n"
            "navigation task that aligns naturally\n"
            "with the associative and combinatorial strengths of LLMs.",
            font_size=28,
            line_spacing=1.2
        ).shift(DOWN * 0.3)
        
        self.play(FadeIn(explanation_text, shift=UP*0.3), run_time=1.5)
        self.wait(2.5)
        
        # Fade out text to make room for visual
        self.play(FadeOut(explanation_text), run_time=0.8)
        
        # VISUAL PART 1: Show opaque box - Space of paintings
        paintings_label = Text(
            "Space of paintings (difficult to navigate strategically for LLMs)",
            font_size=28,
            color=RED
        ).shift(UP*2.5)
        
        # Create an opaque, solid box in the center
        opaque_box = Cube(
            side_length=2.5,
            fill_color=RED,
            fill_opacity=0.9,
            stroke_color=WHITE,
            stroke_width=2
        )
        
        self.play(
            FadeIn(paintings_label, shift=DOWN*0.2),
            run_time=1
        )
        self.play(
            FadeIn(opaque_box, scale=0.8),
            run_time=1.2
        )
        self.wait(1)
        
        # Try to show the box cannot move/is stuck
        # Small shake animation to show it's stuck
        self.play(
            opaque_box.animate.shift(RIGHT*0.1),
            run_time=0.15
        )
        self.play(
            opaque_box.animate.shift(LEFT*0.1),
            run_time=0.15
        )
        self.play(
            opaque_box.animate.shift(RIGHT*0.05),
            run_time=0.1
        )
        self.play(
            opaque_box.animate.shift(LEFT*0.05),
            run_time=0.1
        )
        self.wait(0.5)
        
        # TRANSITION: Box dissolves into millions of points
        # First, fade out the label
        self.play(FadeOut(paintings_label), run_time=0.5)
        
        # Generate positions for the concept cloud (centered)
        np.random.seed(123)
        num_concepts = 1000  # "Millions" represented by many dots
        positions = []
        cloud_center = ORIGIN
        
        for i in range(num_concepts):
            # Spread out in a much larger area
            angle = np.random.uniform(0, 2*PI)
            radius_val = np.random.uniform(0.3, 3.2)
            x = radius_val * np.cos(angle)
            y = radius_val * np.sin(angle)
            
            position = cloud_center + RIGHT * x + UP * y
            positions.append(position)
        
        # Create the concept cloud with dots starting from inside/on the box
        concept_cloud = VGroup()
        color_choices = [BLUE, GREEN, TEAL, YELLOW, ORANGE, PURPLE, PINK, MAROON]
        
        # Generate initial positions for dots inside the cube volume
        box_size = 2.5
        initial_positions = []
        for i in range(num_concepts):
            # Random position inside the cube
            x = np.random.uniform(-box_size/2, box_size/2)
            y = np.random.uniform(-box_size/2, box_size/2)
            z = 0  # Keep in 2D for simplicity
            initial_positions.append(np.array([x, y, z]))
        
        for i in range(num_concepts):
            color = color_choices[i % len(color_choices)]
            dot = Dot(
                point=initial_positions[i],
                radius=0.015,
                color=color,
                fill_opacity=0.7
            )
            concept_cloud.add(dot)
        
        # Box dissolves: it becomes the colorful points
        # First make box semi-transparent and show the dots inside
        self.play(
            opaque_box.animate.set_opacity(0.2),
            FadeIn(concept_cloud),
            run_time=1
        )
        
        # Now the box completely disappears as dots spread out
        animations = []
        for i, dot in enumerate(concept_cloud):
            animations.append(dot.animate.move_to(positions[i]))
        
        self.play(
            FadeOut(opaque_box),
            *animations,
            run_time=2.5,
            rate_func=rush_from
        )
        self.wait(0.5)
        
        # VISUAL PART 2: Show new label for concept space
        concepts_label = Text(
            "Space of concepts",
            font_size=28,
            color=GREEN
        ).shift(UP*2.5)
        
        self.play(
            FadeIn(concepts_label, shift=DOWN*0.2),
            run_time=1
        )
        self.wait(0.5)
        
        # Show millions of thin glowing trajectories connecting sets of 5 concepts each
        trajectory_colors = [YELLOW, ORANGE, PINK, TEAL, PURPLE, GREEN, RED]
        all_trajectories = VGroup()
        
        # Create many trajectories (representing millions)
        num_trajectories = 25 # Represents "millions" of possible paths
        
        for traj_idx in range(num_trajectories):
            # Pick 5 random concepts for this trajectory
            np.random.seed(42 + traj_idx)
            selected_indices = np.random.choice(num_concepts, size=5, replace=False)
            selected_positions = [positions[idx] for idx in selected_indices]
            
            # Pick a color for this trajectory
            color = trajectory_colors[traj_idx % len(trajectory_colors)]
            
            # Create thin glowing lines connecting these 5 concepts
            trajectory = VGroup()
            for i in range(len(selected_positions) - 1):
                # Glow layer: subtle
                glow = Line(
                    selected_positions[i],
                    selected_positions[i + 1],
                    stroke_width=3,
                    color=color,
                    stroke_opacity=0.15
                )
                trajectory.add(glow)
                
                # Main line: Very thin
                line = Line(
                    selected_positions[i],
                    selected_positions[i + 1],
                    stroke_width=0.8,
                    color=color,
                    stroke_opacity=0.6
                )
                trajectory.add(line)
            
            all_trajectories.add(trajectory)
        
        # Animate trajectories: first 5 in a staggered way, then the rest all at once
        # First 5 trajectories - staggered start with overlap
        if len(all_trajectories) >= 3:
            for i in range(3):
                if i == 0:
                    # First trajectory plays fully
                    self.play(
                        Create(all_trajectories[i]),
                        run_time=1.2,
                        rate_func=linear
                    )
                else:
                    # Each subsequent trajectory starts when the previous is halfway
                    # We need to start the next animation before the previous finishes
                    # Use a shorter duration and no wait
                    self.play(
                        Create(all_trajectories[i]),
                        run_time=1.2,
                        rate_func=linear
                    )

            # Now animate the rest all at once (if there are more than 3)
            if len(all_trajectories) > 3:
                remaining_trajectories = VGroup(*[all_trajectories[i] for i in range(3, len(all_trajectories))])
                self.play(
                    Create(remaining_trajectories, lag_ratio=0.002),
                    run_time=2.5,
                    rate_func=linear
                )
        else:
            # Fallback if less than 5 trajectories
            self.play(
                Create(all_trajectories, lag_ratio=0.002),
                run_time=4,
                rate_func=linear
            )
        
        self.wait(1)
        
        # Add "Easier to explore strategically" in the middle of the screen with opaque background
        explore_label = Text(
            "Easier to explore strategically",
            font_size=32,
            color=GREEN,
            slant=ITALIC
        ).move_to(ORIGIN)
        
        # Create opaque background box
        explore_bg = SurroundingRectangle(
            explore_label,
            color=BLACK,
            buff=0.3,
            corner_radius=0.1,
            stroke_width=2,
            stroke_color=GREEN,
            fill_color=BLACK,
            fill_opacity=0.95
        )
        explore_bg.set_z_index(10)
        explore_label.set_z_index(11)
        
        explore_group = VGroup(explore_bg, explore_label)
        
        self.play(
            FadeIn(explore_group, scale=0.95),
            run_time=1
        )
        
        self.wait(1.5)
    
    def create_concept_tag(self, text: str, color: str) -> VGroup:
        """Helper to create a rounded rectangle concept tag"""
        label = Text(text, font_size=22, color=WHITE, weight=BOLD)
        box = SurroundingRectangle(
            label,
            color=color,
            buff=0.15,
            corner_radius=0.15,
            stroke_width=2,
            fill_color=color,
            fill_opacity=0.95
        )
        return VGroup(box, label)
