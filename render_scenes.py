"""
Script to render each scene from main.py individually.
This allows you to generate separate video files for each scene.

Usage:
    python render_scenes.py [scene_number] [quality]
    
    If no scene_number is provided, all scenes will be rendered.
    Scene numbers: 1 = CreativeParadox, 2 = ConceptReframing, 
                   3 = LLMProblem, 4 = IntroducingCASSolution
    
    Quality options: l=low (480p15), m=medium (720p30), h=high (1080p60), k=4K (2160p60)

Examples:
    python render_scenes.py              # Render all scenes (low quality)
    python render_scenes.py 1            # Render only CreativeParadox (low quality)
    python render_scenes.py 3 h          # Render only LLMProblem (high quality)
    python render_scenes.py all m        # Render all scenes (medium quality)
"""

import sys
import subprocess

# Define all scene classes
SCENES = [
    "CreativeParadox",
    "ConceptReframing", 
    "LLMProblem",
    "IntroducingCASSolution"
]


def render_scene(scene_name, quality="l"):
    """
    Render a specific scene from main.py
    
    Args:
        scene_name: Name of the scene class to render
        quality: Render quality (l=low, m=medium, h=high, k=4k)
    """
    print(f"\n{'='*60}")
    print(f"Rendering scene: {scene_name}")
    print(f"{'='*60}\n")
    
    # Build the manim command - use virtual environment python if available
    import os
    import sys
    
    # Check if we're in a virtual environment
    venv_python = os.path.join(os.path.dirname(__file__), ".venv", "Scripts", "python.exe")
    
    if os.path.exists(venv_python):
        # Use virtual environment Python with manim module
        cmd = [
            venv_python,
            "-m", "manim",
            "-q" + quality,  # Quality flag (e.g., -ql, -qh)
            "main.py",
            scene_name
        ]
    else:
        # Fall back to system manim command
        cmd = [
            "manim",
            "-q" + quality,
            "main.py",
            scene_name
        ]
    
    try:
        # Run the command
        result = subprocess.run(cmd, check=True)
        print(f"\n✓ Successfully rendered {scene_name}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Error rendering {scene_name}: {e}")
        return False
    except FileNotFoundError:
        print("\n✗ Error: manim command not found. Make sure Manim is installed.")
        print("   Install with: pip install manim")
        print(f"   Or activate your virtual environment first")
        return False


def render_all_scenes(quality="l"):
    """Render all scenes"""
    print(f"\nRendering all {len(SCENES)} scenes...")
    
    success_count = 0
    failed_scenes = []
    
    for i, scene in enumerate(SCENES, 1):
        print(f"\n[{i}/{len(SCENES)}]")
        if render_scene(scene, quality):
            success_count += 1
        else:
            failed_scenes.append(scene)
    
    # Summary
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Successfully rendered: {success_count}/{len(SCENES)} scenes")
    
    if failed_scenes:
        print(f"\nFailed scenes:")
        for scene in failed_scenes:
            print(f"  - {scene}")
    else:
        print("\n✓ All scenes rendered successfully!")
    
    return success_count == len(SCENES)


def main():
    """Main entry point"""
    # Default quality (can be modified)
    quality = "l"  # l=low (480p), m=medium (720p), h=high (1080p), k=4k
    
    # Check if a specific scene number was provided
    if len(sys.argv) > 1:
        try:
            scene_num = int(sys.argv[1])
            if 1 <= scene_num <= len(SCENES):
                scene_name = SCENES[scene_num - 1]
                print(f"\nRendering scene #{scene_num}: {scene_name}")
                render_scene(scene_name, quality)
            else:
                print(f"Error: Scene number must be between 1 and {len(SCENES)}")
                print(f"\nAvailable scenes:")
                for i, scene in enumerate(SCENES, 1):
                    print(f"  {i}. {scene}")
        except ValueError:
            print("Error: Please provide a valid scene number")
            print(f"\nAvailable scenes:")
            for i, scene in enumerate(SCENES, 1):
                print(f"  {i}. {scene}")
    else:
        # Render all scenes
        render_all_scenes(quality)


if __name__ == "__main__":
    main()
