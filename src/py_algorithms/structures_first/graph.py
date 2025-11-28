# ruff: noqa: N806
import matplotlib.pyplot as plt
import networkx as nx


def example() -> None:
    # Create an empty graph
    G: nx.Graph[str] = nx.Graph()

    # Adding nodes
    G.add_node("A")
    G.add_node("B")
    G.add_node("C")

    # Adding edges
    G.add_edge("A", "B")
    G.add_edge("B", "C")

    # Set positions of nodes
    positions = {
        "A": (0, 0.5),
        "B": (1, 0.5),
        "C": (2, 0.5),
    }

    # Draw the graph
    plt.figure(figsize=(6, 6))  # pyright: ignore[reportUnknownMemberType, reportUndefinedVariable]
    nx.draw_networkx(G, pos=positions, with_labels=True, font_weight="bold", node_color="lightblue", edge_color="gray")
    plt.axis("off")  # pyright: ignore[reportUnknownMemberType]
    plt.show()  # pyright: ignore[reportUnknownMemberType]


def main() -> None:
    example()


if __name__ == "__main__":
    main()
