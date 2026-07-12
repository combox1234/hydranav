# Project Manifest

## Project

**HydraNav**

---

# Executive Summary

HydraNav is a reusable Computer Vision-based autonomous navigation framework for Autonomous Surface Vehicle (ASV) simulation.

The project is designed around a modular robotics software architecture where perception, environment representation, path planning, visualization, and evaluation remain independent components.

The initial implementation focuses on demonstrating autonomous navigation through a **Vision-Based Trash Collection Simulation** using images and videos.

HydraNav emphasizes software engineering, modularity, research-driven development, and reproducible experimentation rather than hardware deployment.

---

# Vision

Develop a reusable vision-based navigation framework capable of supporting multiple Autonomous Surface Vehicle (ASV) applications through interchangeable software modules.

HydraNav should enable researchers and developers to evaluate perception and navigation algorithms without requiring physical hardware.

---

# Mission

Design and implement a production-quality Computer Vision pipeline that demonstrates safe autonomous navigation in simulation while maintaining clean software architecture, engineering discipline, and extensibility.

---

# Current Scope

Version 1.0 is intentionally restricted to a single application.

## Current Module

**Vision-Based Trash Collection Simulation**

The system will:

- Detect floating trash
- Detect navigable water
- Detect obstacles
- Build an environment representation
- Compute the shortest safe navigation path
- Visualize the complete navigation pipeline

Simulation only.

---

# Out of Scope

The following are intentionally excluded from Version 1.0.

- Physical robots
- ROS / ROS2
- GPS
- IMU
- LiDAR
- Sonar
- Arduino
- ESP32
- Jetson
- Autonomous control
- Motor control
- Embedded deployment
- Sensor fusion
- SLAM
- Multi-agent coordination

These topics may be explored in future versions but are not part of the current project.

---

# Engineering Principles

HydraNav follows several core engineering principles.

## Modular Design

Every subsystem should remain independent and replaceable.

---

## Research First

Engineering decisions must be supported by literature, experimentation, or benchmarking.

---

## Reproducibility

Experiments should be reproducible using documented datasets, configurations, and evaluation procedures.

---

## Maintainability

Readable architecture is preferred over unnecessary optimization.

---

## Extensibility

The architecture should allow future navigation applications without redesigning the framework.

---

# Platform Architecture

HydraNav consists of five major components.

1. Perception

2. Environment Representation

3. Path Planning

4. Visualization

5. Evaluation

Each module owns a clearly defined responsibility and communicates through documented interfaces.

---

# Development Philosophy

The project follows a staged engineering workflow.

Research

↓

Architecture

↓

Implementation

↓

Testing

↓

Evaluation

↓

Release

No implementation should begin without sufficient architectural understanding.

---

# Scope Lock

To prevent feature creep, Version 1.0 is restricted to the Vision-Based Trash Collection Simulation.

Future application domains such as:

- River Inspection
- Marina Navigation
- Environmental Monitoring
- Obstacle Avoidance

remain conceptual and will not be implemented until Version 1.0 is complete.

---

# Success Criteria

Version 1.0 will be considered successful when the system can:

- Detect floating trash from images and videos.
- Identify navigable water.
- Represent the environment for planning.
- Compute a valid collision-free path.
- Visualize the planned navigation route.
- Produce reproducible evaluation results.

No physical deployment is required.

---

# Stakeholders

Primary stakeholders include:

- Students
- Robotics Researchers
- Computer Vision Researchers
- Open Source Contributors
- Recruiters and Portfolio Reviewers

---

# Related Documentation

- ROADMAP.md
- ARCHITECTURE.md
- REQUIREMENTS.md
- TECH_STACK.md
- DATASET_STRATEGY.md
- DEVELOPER_GUIDE.md

---

# Document Status

**Status:** Approved

**Version:** v0.1.0

**Last Updated:** Repository Foundation