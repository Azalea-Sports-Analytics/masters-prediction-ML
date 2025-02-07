# Git Workflow Guidelines

This document defines our branch naming conventions and commit practices to maintain a clean, understandable, and traceable project history.

---

## Branch Naming Conventions

Since our project uses only a single primary branch (`main`), please follow the guidelines below when creating additional branches.

### Main Branch
- **`main`**
  - **Purpose:** Contains production-ready code.
  - **Guidelines:** Always maintain a deployable state in this branch. All finalized features, bug fixes, and improvements should be merged back into `main`.

### Feature Branches
- **Naming Format:** `feature/<descriptive-name>`
  - **Examples:** `feature/add-user-auth`, `feature/update-dashboard`
- **Usage:**  
  - Branch off from `main`.
  - Use for developing new features or enhancements.
  - Once the feature is complete and tested, open a pull request (or merge request) to merge it back into `main`.

### Bugfix Branches
- **Naming Format:** `bugfix/<descriptive-name>`
  - **Examples:** `bugfix/fix-api-timeout`, `bugfix/correct-chart-scaling`
- **Usage:**  
  - Branch off from `main`.
  - After fixing the bug, open a pull request to merge the changes back into `main`.

---

## Commit Practices

### When to Commit
- **Logical, Self-Contained Changes:**  
  - Commit changes that are focused and relate to a single task or feature rather than bundling multiple unrelated modifications.
- **After Testing:**  
  - Ensure your changes pass local tests or continuous integration (CI) checks before committing.
- **Before Creating a Pull Request:**  
  - Commit all changes once your branch is in a stable, review-ready state.

### Commit Message Guidelines
- **Structure:**  
  - **Header:** A short, descriptive summary (50 characters or less).
  - **Body (Optional):** A more detailed explanation, wrapped at 72 characters per line.
- **Examples:**
