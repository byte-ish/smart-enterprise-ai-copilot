import os

# Base project directory name
BASE_DIR = "smart-enterprise-ai-copilot"

# Folder structure to create
FOLDERS = [
    "agents",
    "tools",
    "memory",
    "state",
    "graph/nodes",
    "config",
    "tests",
    "docs",
    "llm",
    "data",
    "utils",
    "api",
]

# Standard placeholder files to add
FILES = [
    ".gitignore",
    "README.md",
    "requirements.txt",
    ".env.example",
    "pyproject.toml"  # optional: used if you later switch to Poetry
]

def create_project_structure():
    # Create base directory
    os.makedirs(BASE_DIR, exist_ok=True)

    # Create all folders
    for folder in FOLDERS:
        full_path = os.path.join(BASE_DIR, folder)
        os.makedirs(full_path, exist_ok=True)
        init_file = os.path.join(full_path, "__init__.py")
        with open(init_file, "w") as f:
            f.write("# Init for " + folder)

    # Create standard files
    for filename in FILES:
        filepath = os.path.join(BASE_DIR, filename)
        with open(filepath, "w") as f:
            f.write("")

    print(f"✅ Project structure for '{BASE_DIR}' created successfully.")

if __name__ == "__main__":
    create_project_structure()