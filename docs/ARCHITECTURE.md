# System Architecture

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
Will be updated as new generic navigation modules are officially integrated.
