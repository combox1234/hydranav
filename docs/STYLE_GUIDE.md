# Engineering Style Guide

## Why it exists
Prevents formatting debates and ensures a uniform codebase.

## Who uses it
All contributors.

## When it is used
During local development and PR reviews.

## Official Engineering Workflow

### Branch Naming
- `main`
- `feature/<feature-name>`

### Commit Convention
- `feat:` (New features)
- `fix:` (Bug fixes)
- `docs:` (Documentation changes)
- `refactor:` (Code refactoring)
- `test:` (Testing)
- `chore:` (Maintenance, dependencies)

### Release Tags
- `v0.x.x`

### Issue Naming
- `Stage XX — Title`

### Pull Requests
- Conventional title
- Short summary
- Testing checklist

## General Conventions
- **Markdown:** 100 char limit, Title Case headers.
- **Python Style:** PEP8, enforced by Ruff.
- **Folder Naming:** `kebab-case`.
- **File Naming:** `snake_case.py`.
- **Diagram Convention:** Mermaid.js.
- **Logging:** Use Python `logging` module (INFO for standard, DEBUG for files).
- **Configuration:** `.yaml` files in `configs/`.

## Current Status
Active.

## Future Responsibility
Enforced strictly by CI pipelines.
