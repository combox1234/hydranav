# Dataset Strategy

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
Maintained as the source of truth for data lineage.
