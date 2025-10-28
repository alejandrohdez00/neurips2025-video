"""
SCENE 5: Evolutionary Tree
Visual aesthetic scene showing a gif in center with a glowing tree growing in the background
Synchronized to show one image per second
"""

from manim import *
import numpy as np
from PIL import Image
import os


class EvolutionaryTree(Scene):
    def construct(self):
        # Set background to dark for better glow effect
        self.camera.background_color = "#0a0a0a"
        
        # Parameters
        num_generations = 30
        seconds_per_image = 1.0  # Each gif frame shows for 1 second
        
        # Create the glowing tree in background (large scale)
        # Generate tree structure first
        tree_data = self._generate_background_tree(num_generations)
        
        # Create all tree elements but keep them invisible initially
        tree_lines = VGroup()
        tree_glows = VGroup()
        tree_nodes = VGroup()
        
        for i, node in enumerate(tree_data):
            if i == 0:
                continue  # Skip root
            
            # Create glowing line
            line = Line(
                node['parent_pos'],
                node['pos'],
                stroke_width=2,  # Slightly thicker main line
                stroke_opacity=0
            ).set_color(node['color'])
            
            # Create glow effect (thick, very transparent line behind)
            glow_line = Line(
                node['parent_pos'],
                node['pos'],
                stroke_width=15,  # Much thicker glow for visibility
                stroke_opacity=0
            ).set_color(node['color'])
            
            # Create small node
            dot = Dot(
                node['pos'],
                radius=0.04,  # Slightly larger for visibility at edges
                color=node['color'],
                fill_opacity=0
            )
            
            tree_lines.add(line)
            tree_glows.add(glow_line)
            tree_nodes.add(dot)
        
        # Add tree to scene (in background)
        self.add(tree_glows, tree_lines, tree_nodes)
        
        # Create centered GIF frame
        gif_size = 6.5
        gif_frames = []
        gif_mobject = None
        
        try:
            # Try to load and extract gif frames
            gif_path = "romanticism-landscape.gif"
            
            # Load GIF using PIL to extract frames
            pil_gif = Image.open(gif_path)
            
            # Extract all frames
            frame_count = 0
            try:
                while True:
                    # Convert current frame to ImageMobject
                    frame_path = f"/tmp/gif_frame_{frame_count}.png"
                    pil_gif.save(frame_path)
                    frame_mob = ImageMobject(frame_path).scale_to_fit_height(gif_size)
                    frame_mob.move_to(ORIGIN)
                    gif_frames.append(frame_mob)
                    
                    frame_count += 1
                    pil_gif.seek(frame_count)
            except EOFError:
                pass  # End of frames
            
            # If we have frames, start with the first one
            if gif_frames:
                gif_mobject = gif_frames[0]
            else:
                # Fallback to static image
                gif_mobject = ImageMobject(gif_path).scale_to_fit_height(gif_size)
                gif_mobject.move_to(ORIGIN)
            
            # Add subtle frame around gif
            gif_frame = Rectangle(
                height=gif_size + 0.2,
                width=gif_size + 0.2,
                stroke_color=WHITE,
                stroke_width=2,
                stroke_opacity=0.3,
                fill_opacity=0
            ).move_to(ORIGIN)
            
            self.add(gif_frame)
            self.add(gif_mobject)
            
        except Exception as e:
            # Fallback placeholder
            print(f"Could not load GIF: {e}")
            placeholder = Rectangle(
                height=gif_size,
                width=gif_size,
                fill_color=GREY_E,
                fill_opacity=0.1,
                stroke_color=WHITE,
                stroke_width=2,
                stroke_opacity=0.3
            ).move_to(ORIGIN)
            
            placeholder_text = Text(
                "evolution.gif",
                font_size=24,
                color=GREY,
                weight=LIGHT
            ).move_to(ORIGIN)
            
            self.add(placeholder, placeholder_text)
        
        # Animate tree growth synchronized with gif (1 second per image)
        nodes_per_second = num_generations / (num_generations * seconds_per_image)
        
        frame_index = 0
        for i in range(len(tree_data) - 1):
            # Update GIF frame if we have multiple frames
            if gif_frames and len(gif_frames) > 1 and gif_mobject is not None:
                next_frame_index = (frame_index + 1) % len(gif_frames)
                self.play(
                    Transform(gif_mobject, gif_frames[next_frame_index]),
                    tree_glows[i].animate.set_stroke(opacity=0.3),
                    run_time=seconds_per_image * 0.3
                )
                frame_index = next_frame_index
            else:
                # Fade in the glow
                self.play(
                    tree_glows[i].animate.set_stroke(opacity=0.3),
                    run_time=seconds_per_image * 0.3
                )
            
            # Fade in the line and node (no need to update frame here)
            self.play(
                tree_lines[i].animate.set_stroke(opacity=0.6),
                tree_nodes[i].animate.set_fill(opacity=0.8),
                run_time=seconds_per_image * 0.4
            )
            
            # Pulse the glow (no need to update frame here)
            self.play(
                tree_glows[i].animate.set_stroke(opacity=0.5, width=20),  # Larger pulse
                rate_func=there_and_back,
                run_time=seconds_per_image * 0.3
            )
        
        # Final hold
        self.wait(2)
    
    def _generate_background_tree(self, num_nodes):
        """Generate a tree structure that fills the background"""
        
        # Start from center
        root_pos = ORIGIN
        
        # Store tree data
        tree_data = [{
            'pos': root_pos,
            'parent_pos': root_pos,
            'color': BLUE_E
        }]
        
        # Active branches for growth
        active_branches = [0]
        
        # Color palette (glowing colors)
        colors = [
            BLUE_C,
            TEAL_C, 
            GREEN_C,
            PURPLE_C,
            PINK,
            ORANGE,
            YELLOW_C,
            RED_C
        ]
        current_color_idx = 0
        
        # Branch probability
        branch_prob = 0.12
        
        for gen in range(1, num_nodes):
            # Pick random active branch to extend
            if active_branches:
                parent_idx = np.random.choice(active_branches)
                parent_pos = tree_data[parent_idx]['pos']
                parent_color = tree_data[parent_idx]['color']
            else:
                parent_idx = 0
                parent_pos = root_pos
                parent_color = colors[0]
                active_branches = [0]
            
            # Generate new position with LARGE distances
            angle = np.random.uniform(0, 2 * PI)
            distance = np.random.uniform(0.8, 1.5)  # Much larger distances - edges more visible
            
            dx = distance * np.cos(angle)
            dy = distance * np.sin(angle)
            
            new_pos = parent_pos + np.array([dx, dy, 0])
            
            # Keep within frame bounds (with margin for gif in center)
            # Allow tree to spread very wide across background
            new_pos[0] = np.clip(new_pos[0], -7.0, 7.0)
            new_pos[1] = np.clip(new_pos[1], -4.0, 4.0)
            
            # Skip if too close to center (where gif is)
            if np.linalg.norm(new_pos) < 3.5:
                # Push it away from center - further out
                direction = new_pos / np.linalg.norm(new_pos)
                new_pos = direction * 3.5
            
            # Branching
            should_branch = np.random.random() < branch_prob
            
            if should_branch and len(active_branches) < 10:
                current_color_idx = (current_color_idx + 1) % len(colors)
                new_color = colors[current_color_idx]
                active_branches.append(gen)
            else:
                new_color = parent_color
            
            tree_data.append({
                'pos': new_pos,
                'parent_pos': parent_pos,
                'color': new_color
            })
            
            # Prune old branches occasionally
            if len(active_branches) > 6 and np.random.random() < 0.15:
                active_branches.pop(np.random.randint(len(active_branches)))
        
        return tree_data