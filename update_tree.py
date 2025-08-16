# update_tree.py
# This script generates a directory tree structure and updates the README file with it.
import os

def generate_tree(path=".", prefix=""):
    tree = []
    files = sorted(os.listdir(path))
    for index, name in enumerate(files):
        if name.startswith(".") or name in ["__pycache__", "build", "dist", ".git"]:
            continue  # skip hidden and unwanted folders
        full_path = os.path.join(path, name)
        connector = "└── " if index == len(files) - 1 else "├── "
        tree.append(f"{prefix}{connector}{name}")
        if os.path.isdir(full_path):
            extension = "    " if index == len(files) - 1 else "│   "
            tree.extend(generate_tree(full_path, prefix + extension))
    return tree


def update_readme(readme="README.md"):
    tree = "\n".join(generate_tree())

    start = "<!-- TREE_START -->"
    end = "<!-- TREE_END -->"
    new_section = f"{start}\n```\n{tree}\n```\n{end}"

    if os.path.exists(readme):
        # Update existing README
        with open(readme, "r", encoding="utf-8") as f:
            content = f.read()
        if start in content and end in content:
            content = content.split(start)[0] + new_section + content.split(end)[1]
        else:
            # inject into Folder Structure section if it exists
            if "## Folder Structure" in content:
                content = content.replace("## Folder Structure", f"## Folder Structure\n\n{new_section}")
            else:
                content += f"\n\n{new_section}"
    else:
        # Create a new README with default structure
        content = f"""# Project 

## Project Overview


### ✨ Key Features


## Folder Structure

{new_section}


## 🚀 Installation

### For Linux / macOS

1. Clone the repository:
   ```bash
   git clone <repo>
"""