import matplotlib.pyplot as plt
import numpy as np


def build_chart() -> None:
    # Determine the number of elements and corresponding steps for linear and binary search
    n = np.arange(1, 21)
    linear_search_steps = n
    binary_search_steps = np.log2(n)

    # Chart construction
    plt.figure(figsize=(10, 6))
    plt.plot(n, linear_search_steps, label="Linear Search", color="blue")
    plt.plot(n, binary_search_steps, label="Binary Search", color="green")
    plt.xlabel("Number of elements (n)")
    plt.ylabel("Number of steps")
    plt.title("Comparison of Linear and Binary Search")
    plt.legend()
    plt.grid(visible=True)  # pyright: ignore[reportUnknownMemberType]
    plt.tight_layout()

    # Show the chart
    plt.show()


def main() -> None:
    build_chart()


if __name__ == "__main__":
    main()
