# HydraNav

## Overview
HydraNav is a reusable Computer Vision-based autonomous navigation framework for Autonomous Surface Vehicle (ASV) simulation. The framework is designed for generic navigation tasks, with the initial demonstration module focusing on a Vision-Based Trash Collection Simulation.

## Architecture Overview
The system relies on a modular architecture encompassing:
1. **Perception:** Detects objects and segments navigable water.
2. **Mapping:** Converts perception masks into a 2D costmap.
3. **Planning:** Computes safe navigation paths avoiding obstacles.
4. **Visualization:** Renders the pipeline outputs (bounding boxes, paths, masks).
5. **Evaluation:** Verifies system performance and metrics.

## Features
- Modular Perception Pipeline (Object Detection & Segmentation)
- Configurable Environment Mapping
- Autonomous Path Planning
- High-fidelity Visualization

## Documentation
Start reading the documentation at `docs/NAVIGATION.md`.

## Roadmap
HydraNav is developed in progressive stages. See `docs/ROADMAP.md` for the official Semantic Versioning roadmap.

## Current Development Phase
Currently in Stage 1: Development Environment.

## Current Status
Repository Foundation is Complete. Scope is locked for Version 1.0.

## Contributing
See `CONTRIBUTING.md` for guidelines on how to contribute.

## License
Apache 2.0. See `LICENSE`.

## Simulation Scope
**Note: This project is Simulation Only.**
Out of scope: ROS, Hardware, GPS, Motors, Arduino, ESP32, Jetson, Sensor Fusion, SLAM.
