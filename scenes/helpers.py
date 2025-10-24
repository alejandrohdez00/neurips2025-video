"""
Helper functions and constants shared across all scenes
"""

from manim import *
import numpy as np
from typing import List


# ============================================================================
# COLOR PALETTE (define once, use throughout)
# ============================================================================
CAS_GREEN = "#2ECC71"
CAS_TEAL = "#1ABC9C"
CONTEXT_RED = "#E74C3C"
CONTEXT_RED_LIGHT = "#EC7063"
GPT_PURPLE = "#9B59B6"
GPT_PURPLE_LIGHT = "#BB8FCE"
HIGHLIGHT_YELLOW = "#F1C40F"
CONCEPT_ORANGE = "#E67E22"
BACKGROUND_DARK = "#1C1C1C"


# ============================================================================
# HELPER FUNCTIONS (shared across scenes)
# ============================================================================
def create_concept_node(text: str, color: str, position: np.ndarray, 
                        radius: float = 0.4) -> VGroup:
    """Create a circular node with concept label
    
    Args:
        text: Concept text
        color: Node color
        position: 3D position array [x, y, z]
        radius: Circle radius
        
    Returns:
        VGroup containing circle and label
    """
    circle = Circle(
        radius=radius, 
        color=color, 
        fill_opacity=0.2, 
        stroke_width=2
    )
    label = Text(text, font_size=16, color=color)
    node = VGroup(circle, label).move_to(position)
    return node


def create_balance_scale() -> VGroup:
    """Create a simple balance scale visualization
    
    Returns:
        VGroup with (left_side, center, right_side) sub-groups
    """
    # Base
    base = Line(LEFT * 0.5, RIGHT * 0.5, stroke_width=6, color=GREY)
    
    # Fulcrum (triangle)
    fulcrum = Triangle(color=GREY, fill_opacity=1).scale(0.2).next_to(base, DOWN, buff=0)
    
    # Left arm (coherence - green)
    left_arm = Line(ORIGIN, LEFT * 1.2 + UP * 0.2, stroke_width=4, color=CAS_GREEN)
    left_plate = Circle(
        radius=0.25, 
        color=CAS_GREEN, 
        fill_opacity=0.3, 
        stroke_width=2
    ).move_to(left_arm.get_end())
    
    # Right arm (typicality - red)
    right_arm = Line(ORIGIN, RIGHT * 1.2 + UP * 0.2, stroke_width=4, color=CONTEXT_RED)
    right_plate = Circle(
        radius=0.25, 
        color=CONTEXT_RED, 
        fill_opacity=0.3, 
        stroke_width=2
    ).move_to(right_arm.get_end())
    
    left_side = VGroup(left_arm, left_plate)
    right_side = VGroup(right_arm, right_plate)
    center = VGroup(base, fulcrum)
    
    scale = VGroup(left_side, center, right_side)
    return scale


def create_gravity_well(position: np.ndarray, num_circles: int = 4, 
                       max_radius: float = 0.8, color: str = RED) -> VGroup:
    """Create concentric circles representing a 'gravity well'
    
    Args:
        position: Center position
        num_circles: Number of concentric circles
        max_radius: Radius of outermost circle
        color: Well color
        
    Returns:
        VGroup of concentric circles
    """
    well = VGroup()
    for i in range(num_circles):
        circle = Circle(
            radius=max_radius - i * (max_radius / (num_circles + 1)),
            color=color,
            stroke_width=2,
            stroke_opacity=0.6 - i * (0.6 / num_circles)
        ).move_to(position)
        well.add(circle)
    return well


def distribute_in_circle(num_items: int, radius: float = 2.0, 
                        center: np.ndarray = ORIGIN) -> List[np.ndarray]:
    """Distribute points evenly around a circle
    
    Args:
        num_items: Number of points
        radius: Circle radius
        center: Circle center position
        
    Returns:
        List of position arrays
    """
    angles = [i * 2 * PI / num_items for i in range(num_items)]
    positions = [
        center + radius * np.array([np.cos(angle), np.sin(angle), 0])
        for angle in angles
    ]
    return positions
