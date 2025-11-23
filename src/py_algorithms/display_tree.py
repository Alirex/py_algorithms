from pathlib import Path

# TODO: (?) Use colorama or rich for better colored output

# ANSI escape codes for colored output
COLOR_BLUE = "\033[94m"
COLOR_RESET = "\033[0m"


def display_tree(path: Path, indent: str = "", prefix: str = "") -> None:
    if path.is_dir():
        # Use blue color for directories
        print(f"{indent}{prefix}{COLOR_BLUE}{path.name}{COLOR_RESET}")
        indent += "    " if prefix else ""

        # Get a sorted list of children, with directories last
        children = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))

        for index, child in enumerate(children):
            # Check if the current child is the last one in the directory
            is_last = index == len(children) - 1
            display_tree(child, indent, "└── " if is_last else "├── ")
    else:
        print(indent + prefix + str(path.name))


def main() -> None:
    root = Path(__file__).parent  # Change to any directory you want to display
    display_tree(root)


if __name__ == "__main__":
    main()
