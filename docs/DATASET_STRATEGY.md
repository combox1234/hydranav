<!-- # Dataset Strategy

## Why it exists
To govern how data is acquired, annotated, and consumed.

## Who uses it
Data engineers and ML researchers.

## When it is used
During `STAGE_03_DATASET_STRATEGY` and `STAGE_04_PERCEPTION`.

## Strategy
- Use open-source datasets (e.g., TACO) if available.
- Supplement with synthetic or simulated data.
- Store annotations in YOLO/COCO format.
- Do NOT commit raw data to git.

## Current Status
Pending execution in Stage 3.

## Future Responsibility
Maintained as the source of truth for data lineage. -->


# HydraNav Dataset Strategy

## Overview

This document defines the dataset strategy for HydraNav Version 1.0.

The objective is to establish a reproducible and scalable data pipeline for training, validating, and evaluating the perception subsystem.

HydraNav follows a research-driven approach where dataset selection is justified through engineering requirements rather than convenience.

---

# Objectives

The perception pipeline requires datasets capable of supporting:

- Floating trash detection
- Water segmentation
- Obstacle detection
- General scene understanding

The selected datasets should allow experimentation while remaining practical for a simulation-only project.

---

# Dataset Categories

HydraNav organizes datasets into four categories.

## 1. Object Detection

Purpose

Detect floating trash and relevant objects.

Expected outputs

- Bounding boxes
- Object classes

Potential datasets

- TACO (Trash Annotations in Context)
- TrashCan Dataset
- Custom annotated images

---

## 2. Water Segmentation

Purpose

Identify navigable water regions.

Expected outputs

- Pixel-wise segmentation masks

Potential datasets

- MaSTr1325
- MODS Maritime Dataset
- Custom segmentation masks

---

## 3. Obstacle Detection

Purpose

Identify visible navigation hazards.

Examples

- Boats
- Buoys
- Shorelines
- Floating obstacles

These datasets may overlap with maritime perception datasets.

---

## 4. Evaluation Dataset

Purpose

Benchmark the complete perception pipeline.

Evaluation data should remain independent from training data whenever possible.

---

# Dataset Selection Criteria

Datasets should satisfy the following requirements.

- Publicly available
- Well documented
- Research validated
- Appropriate licensing
- Representative maritime environments
- High-quality annotations

---

# Data Organization

The repository separates datasets into three stages.

```
datasets/

raw/

processed/

annotations/
```

Each stage has a distinct purpose.

Raw

Original downloaded data.

Processed

Prepared data ready for experimentation.

Annotations

Ground truth labels used for training and evaluation.

---

# Annotation Philosophy

HydraNav prefers standardized annotation formats whenever possible.

Future annotation formats may include

- YOLO
- COCO

The exact format will be selected during implementation.

---

# Data Processing Pipeline

The planned workflow is

Dataset Acquisition

↓

Validation

↓

Preprocessing

↓

Annotation Verification

↓

Training

↓

Evaluation

↓

Documentation

Each transformation should be reproducible.

---

# Version 1.0 Scope

HydraNav will prioritize publicly available datasets.

If existing datasets prove insufficient, limited custom annotation may be introduced for demonstration purposes.

Large-scale dataset creation is outside the scope of Version 1.0.

---

# Risks

Potential challenges include

- Limited maritime trash datasets
- Class imbalance
- Lighting variability
- Water reflections
- Camera perspective differences

These risks will be evaluated during Stage 3.

---

# Future Work

Future versions may introduce

- Synthetic dataset generation
- Domain adaptation
- Semi-supervised learning
- Active learning

These topics are intentionally postponed beyond Version 1.0.

---

# Related Documentation

- REQUIREMENTS.md
- ARCHITECTURE.md
- ROADMAP.md
- RESEARCH/

---

# Document Status

Status: Approved

Version: v0.1.0

Last Updated: Repository Foundation