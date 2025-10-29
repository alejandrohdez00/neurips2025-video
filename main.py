#!/usr/bin/env python3
"""
Cultural Alien Sampler Video - Main Entry Point
Visualization of the CAS concept selection method

This version includes all 5 scenes:
1. CreativeParadox - The tension between originality and coherence
2. ConceptReframing - Art as conceptual combinations
3. LLMProblem - How LLMs fall into cultural gravity wells
4. IntroducingCASSolution - The CAS approach
5. EvolutionaryTree - Visualizing the evolutionary search (NEW!)

Usage:
    # Render individual scenes
    manim main.py CreativeParadox
    manim main.py ConceptReframing
    manim main.py LLMProblem
    manim main.py IntroducingCASSolution
    manim main.py EvolutionaryTree
    
    # Render all scenes together
    manim main.py CASVideoComposition
    
    # Custom quality settings
    manim -qh main.py EvolutionaryTree          # High quality (1080p60)
    manim -qk main.py CASVideoComposition       # 4K quality
    manim -ql main.py EvolutionaryTree          # Low quality (480p15)
    
Quality flags:
    -ql : Low quality (480p15)
    -qm : Medium quality (720p30)
    -qh : High quality (1080p60)
    -qp : Production quality (1440p60)
    -qk : 4K quality (2160p60)
"""

from manim import *
import argparse
import sys

# Import all scenes
from scenes import (
    CreativeParadox,
    ConceptReframing,
    LLMProblem,
    IntroducingCASSolution,
    EvolutionaryTree,
    CAMShowcase,
    ExperimentalResults
)


# ============================================================================
# MAIN COMPOSITION SCENE
# ============================================================================
class CASVideoComposition(Scene):
    """Combines all five scenes into one continuous video"""
    
    def construct(self):
        # Scene 1: Creative Paradox
        # Shows the fundamental tension between originality and coherence
        scene1 = CreativeParadox()
        scene1.construct()
        self.wait(0.5)
        self.clear()
        
        # Scene 2: Concept Reframing
        # Reframes art as conceptual combinations rather than visual objects
        scene2 = ConceptReframing()
        scene2.construct()
        self.wait(0.5)
        self.clear()
        
        # Scene 3: LLM Problem
        # Demonstrates how LLMs fall into cultural gravity wells
        scene3 = LLMProblem()
        scene3.construct()
        self.wait(0.5)
        self.clear()
        
        # Scene 4: Introducing CAS Solution
        # Explains the Cultural Alien Sampler approach
        scene4 = IntroducingCASSolution()
        scene4.construct()
        self.wait(0.5)
        self.clear()
        
        # Scene 5: Evolutionary Tree (NEW!)
        # Visualizes the evolutionary exploration through embedding space
        scene5 = EvolutionaryTree()
        scene5.construct()
        self.wait(1)


# ============================================================================
# ALTERNATIVE: SHORTENED VERSION FOR PRESENTATIONS
# ============================================================================
class CASVideoShort(Scene):
    """Shortened version focusing on key points (recommended for talks)"""
    
    def construct(self):
        # Problem
        scene3 = LLMProblem()
        scene3.construct()
        self.wait(0.3)
        self.clear()
        
        # Solution
        scene4 = IntroducingCASSolution()
        scene4.construct()
        self.wait(0.3)
        self.clear()
        
        # Results
        scene5 = EvolutionaryTree()
        scene5.construct()
        self.wait(0.5)


# ============================================================================
# ALTERNATIVE: DEMO-FOCUSED VERSION
# ============================================================================
class CASVideoDemo(Scene):
    """Demo version focusing on the evolutionary process"""
    
    def construct(self):
        # Quick setup
        scene2 = ConceptReframing()
        scene2.construct()
        self.wait(0.3)
        self.clear()
        
        # The magic
        scene5 = EvolutionaryTree()
        scene5.construct()
        self.wait(1)


if __name__ == "__main__":
    """
    Command-line interface for quick access
    
    Examples:
        python main.py                    # Show help
        python main.py --list             # List available scenes
        python main.py --render-all       # Render all scenes individually
    """
    
    if len(sys.argv) > 1:
        if "--list" in sys.argv:
            print("\nAvailable scenes:")
            print("1. CreativeParadox - The creative tension")
            print("2. ConceptReframing - Art as concepts")
            print("3. LLMProblem - Cultural anchoring problem")
            print("4. IntroducingCASSolution - CAS method explanation")
            print("5. EvolutionaryTree - Evolutionary visualization (NEW!)")
            print("\nCompositions:")
            print("- CASVideoComposition - All scenes (full version)")
            print("- CASVideoShort - Key scenes (presentation version)")
            print("- CASVideoDemo - Demo version (quick overview)")
            print("\nUsage:")
            print("  manim main.py [SceneName]")
            print("  manim -qh main.py CASVideoComposition")
            print("  python render_scenes.py [scene_number] [quality]")
        
        elif "--render-all" in sys.argv:
            print("To render all scenes, use:")
            print("  python render_scenes.py all [quality]")
            print("\nExample:")
            print("  python render_scenes.py all h    # High quality")
        
        else:
            print(__doc__)
    else:
        print(__doc__)