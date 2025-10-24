#!/usr/bin/env python3
"""
Cultural Alien Sampler Video - Main Entry Point
Visualization of the CAS concept selection method

Usage:
    # Render individual scenes with default quality (480p15)
    manim main.py CreativeParadox
    manim main.py ConceptReframing
    manim main.py LLMProblem
    manim main.py IntroducingCASSolution
    
    # Render all scenes together
    manim main.py CASVideoComposition
    
    # Custom quality settings
    manim -qh main.py CreativeParadox          # High quality (1080p60)
    manim -qk main.py CASVideoComposition      # 4K quality
    manim -ql main.py CreativeParadox          # Low quality (480p15)
    
    # Custom FPS (requires config)
    manim --custom_config config.cfg main.py CreativeParadox
    
Quality flags:
    -ql : Low quality (480p15)
    -qm : Medium quality (720p30)
    -qh : High quality (1080p60)
    -qp : Production quality (1440p60)
    -qk : 4K quality (2160p60)
    
Other useful flags:
    -p  : Preview after rendering
    -s  : Save last frame as image
    --format=gif : Render as GIF
"""

from manim import *
import argparse
import sys

# Import all scenes
from scenes import (
    CreativeParadox,
    ConceptReframing,
    LLMProblem,
    IntroducingCASSolution
)


# ============================================================================
# CONFIGURATION
# ============================================================================
# You can customize default quality and FPS here
DEFAULT_QUALITY = "medium_quality"  # low_quality, medium_quality, high_quality, production_quality, fourk_quality
DEFAULT_FPS = 30

# Quality presets
QUALITY_PRESETS = {
    "low": {"pixel_height": 480, "pixel_width": 854, "frame_rate": 15},
    "medium": {"pixel_height": 720, "pixel_width": 1280, "frame_rate": 30},
    "high": {"pixel_height": 1080, "pixel_width": 1920, "frame_rate": 60},
    "production": {"pixel_height": 1440, "pixel_width": 2560, "frame_rate": 60},
    "fourk": {"pixel_height": 2160, "pixel_width": 3840, "frame_rate": 60},
}


# ============================================================================
# MAIN COMPOSITION SCENE
# ============================================================================
class CASVideoComposition(Scene):
    """Combines all four scenes into one continuous video"""
    
    def construct(self):
        # Scene 1: Creative Paradox
        scene1 = CreativeParadox()
        scene1.construct()
        self.wait(0.5)
        self.clear()
        
        # Scene 2: Concept Reframing
        scene2 = ConceptReframing()
        scene2.construct()
        self.wait(0.5)
        self.clear()
        
        # Scene 3: LLM Problem
        scene3 = LLMProblem()
        scene3.construct()
        self.wait(0.5)
        self.clear()
        
        # Scene 4: Introducing CAS Solution
        scene4 = IntroducingCASSolution()
        scene4.construct()
        self.wait(1)


# ============================================================================
# HELPER FUNCTION FOR CUSTOM CONFIGURATION
# ============================================================================
def create_config_file(quality="medium", fps=30, output_file="config.cfg"):
    """
    Create a custom Manim config file with specified quality and FPS
    
    Args:
        quality: Quality preset name (low, medium, high, production, fourk)
        fps: Frame rate
        output_file: Path to save the config file
    """
    preset = QUALITY_PRESETS.get(quality, QUALITY_PRESETS["medium"])
    
    config_content = f"""[CLI]
quality = {quality}_quality
preview = True
save_last_frame = False

[{quality}_quality]
pixel_height = {preset['pixel_height']}
pixel_width = {preset['pixel_width']}
frame_rate = {fps}
"""
    
    with open(output_file, 'w') as f:
        f.write(config_content)
    
    print(f"Config file created: {output_file}")
    print(f"Quality: {quality} ({preset['pixel_width']}x{preset['pixel_height']})")
    print(f"FPS: {fps}")
    print(f"\nUse with: manim --custom_config {output_file} main.py SceneName")


# ============================================================================
# CLI ENTRY POINT
# ============================================================================
if __name__ == "__main__":
    """
    This allows for custom configuration when running the script directly.
    
    Examples:
        # Generate a custom config file
        python main.py --create-config --quality high --fps 60
        
        # Then render with it
        manim --custom_config config.cfg main.py CreativeParadox
    """
    
    # Check if user wants to create a custom config
    if len(sys.argv) > 1 and "--create-config" in sys.argv:
        parser = argparse.ArgumentParser(description="Create custom Manim configuration")
        parser.add_argument("--create-config", action="store_true", help="Create a custom config file")
        parser.add_argument("--quality", choices=["low", "medium", "high", "production", "fourk"], 
                          default="medium", help="Quality preset")
        parser.add_argument("--fps", type=int, default=30, help="Frame rate")
        parser.add_argument("--output", default="config.cfg", help="Output config file name")
        
        args = parser.parse_args()
        create_config_file(args.quality, args.fps, args.output)
    else:
        print(__doc__)
