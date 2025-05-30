import os

# List of folders to skip
EXCLUDE_DIRS = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    ".idea",
    ".vscode",
    "tests",  # remove this if you want tests included
    "build",
    "dist",
    ".eggs",
    ".mypy_cache",
    ".pytest_cache",
}

# List of files to skip (if any)
EXCLUDE_FILES = {
    # Example: 'consolidate_project_files.py',
}


def should_skip_dir(dir_name):
    return dir_name in EXCLUDE_DIRS


def should_skip_file(file_name):
    return file_name in EXCLUDE_FILES


def consolidate_files(root_dir, output_file):
    with open(output_file, "w", encoding="utf-8") as outfile:
        # Include pyproject.toml and poetry.lock first if exist
        for special_file in ["pyproject.toml", "poetry.lock"]:
            path = os.path.join(root_dir, special_file)
            if os.path.isfile(path):
                outfile.write(f"\n{'='*80}\nFile: {special_file}\n{'='*80}\n\n")
                with open(path, "r", encoding="utf-8") as f:
                    outfile.write(f.read())
                    outfile.write("\n\n")

        # Walk through directory to find .py files
        for dirpath, dirnames, filenames in os.walk(root_dir):
            # Modify dirnames in-place to skip excluded directories
            dirnames[:] = [d for d in dirnames if not should_skip_dir(d)]

            for filename in filenames:
                if filename.endswith(".py") and not should_skip_file(filename):
                    filepath = os.path.join(dirpath, filename)
                    # Avoid writing this consolidation script itself
                    if os.path.abspath(filepath) == os.path.abspath(__file__):
                        continue

                    rel_path = os.path.relpath(filepath, root_dir)
                    outfile.write(f"\n{'='*80}\nFile: {rel_path}\n{'='*80}\n\n")
                    with open(filepath, "r", encoding="utf-8") as f:
                        outfile.write(f.read())
                        outfile.write("\n\n")


if __name__ == "__main__":
    root_directory = os.getcwd()
    output_filename = "consolidated_project.txt"
    consolidate_files(root_directory, output_filename)
    print(f"All .py files and poetry files consolidated into {output_filename}")
