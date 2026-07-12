<!-- # System Architecture

## Why it exists
To explain the high-level data flow and modular boundaries of the system.

## Who uses it
Software engineers implementing new modules.

## When it is used
Before writing implementation code in `src/` to ensure modular compliance.

## High-Level Flow
1. **Inputs:** Videos/Images
2. **Perception:** Generic perception module to detect targets (e.g., Trash Detection) and segment navigable water.
3. **Mapping:** Converts perception masks into a 2D costmap.
4. **Planning:** Computes the shortest safe navigation path.
5. **Visualization:** Renders bounding boxes, masks, and path overlays.
6. **Evaluation:** Framework for analyzing metrics and accuracy.

*(Refer to `docs/PROJECT_MANIFEST.md` for scope constraints).*

## Current Status
High-level design frozen. The architecture remains reusable. 

## Future Responsibility
Will be updated as new generic navigation modules are officially integrated. -->


# HydraNav Architecture

## Overview

HydraNav is designed as a modular Computer Vision-based navigation framework for Autonomous Surface Vehicle (ASV) simulation.

The architecture separates perception, environment representation, planning, visualization, and evaluation into independent modules. Each module has a clearly defined responsibility and communicates through well-defined interfaces.

This separation allows components to evolve independently without requiring changes throughout the system.

---

# Architectural Principles

The architecture is guided by the following principles:

- Modular design
- Single responsibility
- Loose coupling
- Reproducible experimentation
- Replaceable components
- Research-first engineering

---

# System Overview

The Version 1.0 pipeline consists of five primary modules.

```text
              Images / Videos
                     │
                     ▼
              Input Interface
                     │
                     ▼
               Perception
                     │
                     ▼
       Environment Representation
                     │
                     ▼
             Path Planning
                     │
                     ▼
             Visualization
                     │
                     ▼
                Evaluation
```

Each module consumes structured outputs from the previous stage and produces standardized outputs for the next.

---

# Module Responsibilities

## 1. Input

Responsible for reading and validating input media.

Inputs include:

- Images
- Video files

Responsibilities:

- Frame extraction
- Image preprocessing
- Input validation

Output:

Standardized image frames.

---

## 2. Perception

Responsible for understanding the visual scene.

Responsibilities:

- Trash detection
- Water segmentation
- Obstacle detection

Output:

- Bounding boxes
- Segmentation masks
- Detection metadata

This module does not perform navigation.

---

## 3. Environment Representation

Responsible for converting perception results into a navigation-friendly representation.

Responsibilities:

- Bird's Eye View transformation
- Occupancy grid generation
- Costmap construction

Output:

Structured planning map.

This module bridges Computer Vision and Navigation.

---

## 4. Path Planning

Responsible for computing a safe navigation route.

Responsibilities:

- Goal selection
- Shortest path computation
- Collision avoidance
- Path validation

Output:

Navigation path.

Planning is deterministic and independent of perception.

---

## 5. Visualization

Responsible for presenting the complete navigation pipeline.

Responsibilities:

- Detection overlays
- Segmentation overlays
- Planned route rendering
- Debug visualization

Output:

Annotated images and videos.

---

## 6. Evaluation

Responsible for measuring system quality.

Responsibilities:

- Detection metrics
- Segmentation metrics
- Planning metrics
- Performance metrics

Output:

Evaluation reports.

---

# Repository Mapping

HydraNav mirrors the architecture inside the source tree.

```text
src/

config/

core/

perception/

mapping/

planning/

visualization/

evaluation/

interfaces/

utils/
```

Each package corresponds to one logical subsystem.

---

# Data Flow

The complete pipeline follows a linear flow.

```text
Input

↓

Perception

↓

Environment Representation

↓

Planning

↓

Visualization

↓

Evaluation
```

Intermediate outputs are explicitly defined to simplify debugging and experimentation.

---

# Interface Philosophy

Modules communicate through structured data rather than direct dependencies.

Examples include:

- Detection results
- Segmentation masks
- Occupancy grids
- Navigation paths

This minimizes coupling and improves maintainability.

---

# Architectural Decisions

Major engineering decisions are documented separately as Architecture Decision Records (ADRs).

Examples include:

- Model selection
- Mapping strategy
- Planner selection
- Data representation

The architecture document intentionally avoids implementation-specific decisions.

---

# Version 1.0 Constraints

The architecture intentionally excludes:

- ROS / ROS2
- Hardware integration
- Sensor fusion
- GPS
- IMU
- LiDAR
- Sonar
- Embedded deployment
- Multi-agent coordination

These constraints simplify the system while allowing future expansion.

---

# Future Extensibility

The modular design allows future additions such as:

- Multiple planners
- Additional perception models
- Alternative mapping techniques
- Dynamic obstacle tracking
- Hardware interfaces

These extensions should integrate without changing the overall architecture.

---

# Related Documentation

- PROJECT_MANIFEST.md
- ROADMAP.md
- REQUIREMENTS.md
- TECH_STACK.md
- DATASET_STRATEGY.md
- ADR/

---

# Document Status

Status: Approved

Version: v0.1.0

Last Updated: Repository Foundation