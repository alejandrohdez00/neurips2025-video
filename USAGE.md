# CAS (Cultural Alien Sampler) Manim Animations

Visualization of the Cultural Alien Sampler concept selection method.

## Project Structure

```
manimations/
├── main.py                  # Main entry point with scene orchestration
├── render_scenes.py        # Custom render script
├── scenes/                 # Scene modules
│   ├── __init__.py        # Package initialization
│   ├── helpers.py         # Shared helper functions and constants
│   ├── creative_paradox.py
│   ├── concept_reframing.py
│   ├── llm_problem.py
│   └── introducing_cas_solution.py
└── media/                  # Output directory for rendered videos
```

## Installation

Make sure you have Manim installed:

```bash
pip install manim
```

## Usage

### Render Individual Scenes

```bash
# Default quality (480p15)
manim main.py CreativeParadox
manim main.py ConceptReframing
manim main.py LLMProblem
manim main.py IntroducingCASSolution
```

### Render All Scenes Together

```bash
manim main.py CASVideoComposition
```

### Quality Settings

Manim provides several quality flags:

```bash
# Low quality - 480p, 15fps
manim -ql main.py CreativeParadox

# Medium quality - 720p, 30fps
manim -qm main.py CreativeParadox

# High quality - 1080p, 60fps
manim -qh main.py CreativeParadox

# Production quality - 1440p, 60fps
manim -qp main.py CreativeParadox

# 4K quality - 2160p, 60fps
manim -qk main.py CreativeParadox
```

### Additional Flags

```bash
# Preview after rendering
manim -p -qh main.py CreativeParadox

# Save last frame as image
manim -s -qh main.py CreativeParadox

# Render as GIF
manim -qm --format=gif main.py CreativeParadox

# Render specific scene with preview
manim -pqh main.py ConceptReframing
```

### Custom Configuration

Create a custom config file with specific quality and FPS settings:

```bash
# Generate a custom config file
python main.py --create-config --quality high --fps 60

# Then render using the custom config
manim --custom_config config.cfg main.py CreativeParadox
```

## Scene Descriptions

### 1. CreativeParadox
Illustrates the tension between originality and coherence in AI creativity.
- Visual: Two circles representing "Original" vs "Coherent"
- Shows the fundamental creative paradox

### 2. ConceptReframing
Shows art as conceptual combinations rather than visual objects.
- Dissolves artwork into concept tags
- Demonstrates combinatorial concept space

### 3. LLMProblem
Demonstrates how LLMs fall into cultural gravity wells.
- Visualizes "cultural anchoring"
- Shows repetition statistics for GPT models

### 4. IntroducingCASSolution
Explains the Cultural Alien Sampler approach.
- Split view of Coherence vs Typicality models
- Shows the CAS scoring formula

## Development

### Adding a New Scene

1. Create a new file in `scenes/` directory:
```python
# scenes/my_new_scene.py
from manim import *

class MyNewScene(Scene):
    def construct(self):
        # Your animation code here
        pass
```

2. Import it in `scenes/__init__.py`:
```python
from .my_new_scene import MyNewScene

__all__ = [
    # ... existing scenes
    'MyNewScene'
]
```

3. Import it in `main.py`:
```python
from scenes import (
    # ... existing scenes
    MyNewScene
)
```

4. Render it:
```bash
manim main.py MyNewScene
```

### Using Helper Functions

Helper functions and constants are available in `scenes/helpers.py`:

```python
from .helpers import (
    create_concept_node,
    create_balance_scale,
    create_gravity_well,
    distribute_in_circle,
    CAS_GREEN,
    CONTEXT_RED,
    # ... other helpers
)
```

## Quality Presets

| Preset | Resolution | FPS | Flag |
|--------|-----------|-----|------|
| Low | 854x480 | 15 | `-ql` |
| Medium | 1280x720 | 30 | `-qm` |
| High | 1920x1080 | 60 | `-qh` |
| Production | 2560x1440 | 60 | `-qp` |
| 4K | 3840x2160 | 60 | `-qk` |

## Tips

- Use `-p` flag to preview immediately after rendering
- Start with `-ql` for quick testing, then render final version with `-qh` or `-qk`
- Use `--format=gif` for easy sharing (though file size will be larger)
- Check the `media/` directory for rendered outputs

## License

[Your License Here]
