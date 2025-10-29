"""
SCENE: CAM Showcase
Elegant display of Cultural Alien Sampler image sequences
"""

from manim import *
import os
import glob


class CAMShowcase(Scene):
    def construct(self):
        # Title with elegant typography
        title = Text(
            "CAM Examples",
            font_size=52,
            weight=BOLD,
            color=WHITE
        )
        
        self.play(
            FadeIn(title),
            run_time=1.0
        )
        self.wait(0.5)
        
        # Get all image folders
        images_path = "images"
        
        # Check if directory exists
        if not os.path.exists(images_path):
            error_text = Text(
                "Images folder not found",
                font_size=32,
                color=RED
            )
            self.play(Write(error_text))
            self.wait(2)
            return
        
        # Get folders (each represents a concept combination)
        folders = [f for f in os.listdir(images_path) 
                  if os.path.isdir(os.path.join(images_path, f))]
        
        if not folders:
            error_text = Text(
                "No image sequences found",
                font_size=32,
                color=RED
            )
            self.play(Write(error_text))
            self.wait(2)
            return
        
        # PART 1: Show abstract expressionism earth sequence alone
        target_folder = None
        for folder in folders:
            if "abstract" in folder.lower() and "earth" in folder.lower():
                target_folder = folder
                break
        
        if target_folder:
            folder_path = os.path.join(images_path, target_folder)
            image_files = sorted(glob.glob(os.path.join(folder_path, "*.png")))
            concepts = self.parse_concepts(target_folder)
            
            # Fade out title before showing images
            self.play(
                FadeOut(title),
                run_time=0.8
            )
            
            self.show_sequence_fullscreen(concepts, image_files)
            self.wait(0.3)
            self.clear()
        
        # PART 2: Show three sequences evolving simultaneously
        other_folders = [f for f in folders if f != target_folder]
        
        # Arrange folders with water_sky in the center
        water_sky_folder = None
        remaining_folders = []
        
        for folder in other_folders:
            if "water" in folder.lower() and "sky" in folder.lower():
                water_sky_folder = folder
            else:
                remaining_folders.append(folder)
        
        # Arrange: [remaining[0], water_sky, remaining[1]]
        if water_sky_folder and len(remaining_folders) >= 2:
            ordered_folders = [remaining_folders[0], water_sky_folder, remaining_folders[1]]
        else:
            ordered_folders = other_folders[:3]
        
        if len(ordered_folders) >= 3:
            self.show_three_sequences_parallel(ordered_folders, images_path)
    
    def parse_concepts(self, folder_name):
        """Extract concepts from folder name"""
        # Replace underscores and hyphens with spaces, split by common separators
        concepts = folder_name.replace('_', ' ').replace('-', ' ')
        # Capitalize each word
        concepts = concepts.title()
        
        # Handle special multi-word concepts
        if "Abstract Expressionism" in concepts:
            # Keep "Abstract Expressionism" as one concept
            other_parts = concepts.replace("Abstract Expressionism", "").strip()
            words = ["Abstract Expressionism"]
            if other_parts:
                words.extend(other_parts.split())
        else:
            # Split into individual concepts
            words = concepts.split()
        
        return words
    
    def show_sequence_fullscreen(self, concepts, image_files):
        """Display a single sequence in fullscreen with concepts"""
        
        # Create concept tags
        concept_tags = self.create_concept_tags(concepts)
        concept_tags.arrange(RIGHT, buff=0.25)
        concept_tags.scale(0.9)
        concept_tags.to_edge(UP, buff=0.5)
        
        # Animate concepts appearing
        self.play(
            LaggedStart(
                *[FadeIn(tag, shift=DOWN*0.3) for tag in concept_tags],
                lag_ratio=0.15
            ),
            run_time=1.2
        )
        self.wait(0.5)
        
        # Display images in sequence
        num_images = min(len(image_files), 8)
        
        for img_idx in range(num_images):
            try:
                # Load image
                img = ImageMobject(image_files[img_idx])
                img.height = 5
                img.move_to(ORIGIN)
                
                # Add generation label
                gen_label = Text(
                    f"Generation {img_idx + 1}",
                    font_size=28,
                    color=YELLOW,
                    weight=BOLD
                ).to_edge(DOWN, buff=0.5)
                
                # Add elegant frame
                frame = SurroundingRectangle(
                    img,
                    color=WHITE,
                    stroke_width=3,
                    buff=0.15,
                    corner_radius=0.1
                )
                
                if img_idx == 0:
                    # First image: fade in
                    self.play(
                        FadeIn(img, scale=0.95),
                        Create(frame),
                        Write(gen_label),
                        run_time=1
                    )
                else:
                    # Subsequent images: crossfade
                    old_img = self.mobjects[-3]
                    old_frame = self.mobjects[-2]
                    old_label = self.mobjects[-1]
                    
                    self.play(
                        FadeOut(old_img),
                        FadeOut(old_frame),
                        FadeOut(old_label),
                        FadeIn(img, scale=0.95),
                        Create(frame),
                        Write(gen_label),
                        run_time=0.8
                    )
                
                self.wait(0.6)
                
            except Exception as e:
                print(f"Error loading image {image_files[img_idx]}: {e}")
                continue
        
        self.wait(0.3)
    
    def show_three_sequences_parallel(self, folders, images_path):
        """Show three sequences evolving side by side"""
        
        # Load all three sequences
        sequences_data = []
        for folder in folders:
            folder_path = os.path.join(images_path, folder)
            image_files = sorted(glob.glob(os.path.join(folder_path, "*.png")))
            concepts = self.parse_concepts(folder)
            sequences_data.append({
                'concepts': concepts,
                'images': image_files
            })
        
        if len(sequences_data) < 3:
            return
        
        # Create concept tags for each sequence
        positions = [LEFT * 4, ORIGIN, RIGHT * 4]
        concept_groups = []
        
        for seq_data, pos in zip(sequences_data, positions):
            concept_tags = self.create_concept_tags(seq_data['concepts'])
            concept_tags.arrange(DOWN, buff=0.15, center=True)
            concept_tags.scale(0.5)
            concept_tags.move_to(pos + UP * 3.2)
            concept_groups.append(concept_tags)
        
        # Show all concept tags
        self.play(
            LaggedStart(
                *[FadeIn(group, shift=DOWN*0.2) for group in concept_groups],
                lag_ratio=0.3
            ),
            run_time=1.5
        )
        self.wait(0.5)
        
        # Determine maximum number of generations
        max_gens = max(min(len(seq['images']), 8) for seq in sequences_data)
        
        # Show images evolving in parallel
        current_mobjects = [None, None, None]  # Track current image groups
        
        for gen_idx in range(max_gens):
            new_mobjects = []
            animations = []
            
            for seq_idx, (seq_data, pos) in enumerate(zip(sequences_data, positions)):
                if gen_idx < len(seq_data['images']):
                    try:
                        # Load image
                        img = ImageMobject(seq_data['images'][gen_idx])
                        img.height = 3.6
                        img.move_to(pos + DOWN * 0.3)
                        
                        # Frame
                        frame = SurroundingRectangle(
                            img,
                            color=WHITE,
                            stroke_width=2,
                            buff=0.1,
                            corner_radius=0.08
                        )
                        
                        # Generation label
                        label = Text(
                            f"Gen {gen_idx + 1}",
                            font_size=18,
                            color=YELLOW
                        ).next_to(img, DOWN, buff=0.15)
                        
                        img_group = Group(img, frame, label)
                        new_mobjects.append(img_group)
                        
                        # Create animations
                        if current_mobjects[seq_idx] is None:
                            # First image: fade in
                            animations.extend([
                                FadeIn(img, scale=0.9),
                                Create(frame),
                                Write(label)
                            ])
                        else:
                            # Crossfade
                            animations.extend([
                                FadeOut(current_mobjects[seq_idx]),
                                FadeIn(img, scale=0.9),
                                Create(frame),
                                Write(label)
                            ])
                        
                    except Exception as e:
                        print(f"Error loading image: {e}")
                        new_mobjects.append(None)
                else:
                    new_mobjects.append(None)
            
            # Play all animations simultaneously
            if animations:
                self.play(*animations, run_time=0.9)
                self.wait(1)
            
            current_mobjects = new_mobjects
        
        self.wait(2)
    
    def create_concept_tags(self, concepts):
        """Create elegant concept tag labels"""
        tags = VGroup()
        
        colors = [BLUE, GREEN, ORANGE, PURPLE, TEAL, PINK, YELLOW, RED]
        
        for i, concept in enumerate(concepts):
            color = colors[i % len(colors)]
            
            # Create text
            text = Text(
                concept,
                font_size=22,
                color=color,
                weight=BOLD
            )
            
            # Create pill-shaped background
            bg = RoundedRectangle(
                width=text.width + 0.4,
                height=text.height + 0.3,
                corner_radius=0.2,
                fill_color=color,
                fill_opacity=0.2,
                stroke_color=color,
                stroke_width=2
            )
            
            tag = VGroup(bg, text)
            tags.add(tag)
        
        return tags


class CAMShowcaseGrid(Scene):
    """Alternative: Show multiple generations in a grid layout"""
    
    def construct(self):
        # Title
        title = Text(
            "Cultural Alien Sampler: Evolution Grid",
            font_size=48,
            weight=BOLD
        ).to_edge(UP, buff=0.3)
        
        self.play(Write(title), run_time=1)
        self.wait(0.5)
        
        # Get images
        images_path = "/mnt/user-data/uploads/images"
        
        if not os.path.exists(images_path):
            return
        
        folders = [f for f in os.listdir(images_path) 
                  if os.path.isdir(os.path.join(images_path, f))]
        
        if not folders:
            return
        
        # Take first folder as example
        folder_path = os.path.join(images_path, folders[0])
        image_files = sorted(glob.glob(os.path.join(folder_path, "*.png")))[:6]
        
        if not image_files:
            return
        
        # Parse concepts
        concepts = folders[0].replace('_', ' ').replace('-', ' ').title().split()
        
        # Display concepts
        concept_display = Text(
            "Input: " + " + ".join(concepts),
            font_size=28,
            color=YELLOW
        ).next_to(title, DOWN, buff=0.3)
        
        self.play(FadeIn(concept_display), run_time=0.8)
        self.wait(0.5)
        
        # Create grid of images
        grid_group = VGroup()
        
        for i, img_path in enumerate(image_files):
            try:
                img = ImageMobject(img_path)
                img.height = 1.8
                
                # Frame
                frame = SurroundingRectangle(
                    img,
                    color=WHITE,
                    stroke_width=2,
                    buff=0.05,
                    corner_radius=0.05
                )
                
                # Label
                label = Text(
                    f"Gen {i+1}",
                    font_size=16,
                    color=GREY
                ).next_to(img, UP, buff=0.1)
                
                img_group = Group(img, frame, label)
                grid_group.add(img_group)
                
            except Exception as e:
                print(f"Error loading {img_path}: {e}")
                continue
        
        # Arrange in grid
        grid_group.arrange_in_grid(
            rows=2,
            cols=3,
            buff=0.4
        )
        grid_group.move_to(DOWN * 0.5)
        
        # Animate grid appearance
        self.play(
            LaggedStart(
                *[FadeIn(item, scale=0.9) for item in grid_group],
                lag_ratio=0.2
            ),
            run_time=2.5
        )
        
        self.wait(2)