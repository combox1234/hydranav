<!-- # Technology Stack

## Why it exists
To mandate the tools, libraries, and languages used in the repository.

## Who uses it
All developers.

## When it is used
During environment setup and before adding new dependencies.

## Stack
- Python 3.9+
- OpenCV (Image processing)
- PyTorch (Perception)
- NumPy (Matrix operations)
- Pytest (Testing)
- Ruff (Linting)

## Current Status
Frozen for Stage 1.

## Future Responsibility
Updated only when a new major dependency is approved via ADR. -->

# HydraNav Technology Stack

## Overview

This document defines the technology stack selected for HydraNav Version 1.0.

The selected technologies prioritize modularity, maintainability, reproducibility, and compatibility with modern Computer Vision workflows.

This document will evolve only when significant engineering decisions introduce or replace core technologies.

---

# Programming Language

## Python

Python is the primary implementation language for HydraNav.

Reasons:

- Mature Computer Vision ecosystem
- Strong AI/ML libraries
- Rapid experimentation
- Excellent scientific computing support
- Large robotics community

---

# Computer Vision

## OpenCV

Purpose

- Image processing
- Video processing
- Camera geometry
- Perspective transformation
- Visualization
- Image utilities

---

# Deep Learning

## PyTorch

Purpose

- Model execution
- Tensor operations
- Deep learning workflows

PyTorch serves as the primary machine learning framework for Version 1.0.

---

## Ultralytics YOLO

Purpose

- Object detection
- Segmentation
- Model training
- Inference

The exact model variant will be finalized during the Perception stage.

---

# Scientific Computing

## NumPy

Purpose

- Matrix operations
- Numerical computation
- Coordinate transformations
- Geometry utilities

---

# Visualization

## Matplotlib

Purpose

- Graph generation
- Experiment visualization
- Evaluation plots

---

# Development Environment

Development is performed using

- Python Virtual Environment (venv)
- Git
- GitHub

---

# Development Tools

Current tools include

- Cursor
- AntiGravity
- GitHub

Each tool has a clearly defined responsibility.

Cursor

- Software development
- Refactoring
- Debugging

AntiGravity

- Documentation
- Research
- Architecture

GitHub

- Version control
- Collaboration
- Release management

---

# Planned Project Structure

```
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

---

# Coding Standards

HydraNav follows

- PEP 8
- Type hints where appropriate
- Modular architecture
- Conventional Commits

Detailed guidelines are documented separately in `STYLE_GUIDE.md`.

---

# Dependency Philosophy

Only dependencies required for implementation should be introduced.

Unnecessary packages should not be added.

Each dependency should have a documented purpose.

---

# Technologies Not Included

The following technologies are intentionally excluded from Version 1.0.

- ROS / ROS2
- Gazebo
- Docker
- Kubernetes
- TensorFlow
- Embedded SDKs

Future versions may introduce these technologies if required.

---

# Related Documentation

- PROJECT_MANIFEST.md
- REQUIREMENTS.md
- ARCHITECTURE.md
- STYLE_GUIDE.md

---

# Document Status

Status: Approved

Version: v0.1.0

Last Updated: Repository Foundation