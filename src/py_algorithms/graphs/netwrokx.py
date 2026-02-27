import matplotlib.pyplot as plt
import networkx as nx


def main() -> None:
    g = nx.complete_graph(8)  # pyright: ignore[reportUnknownMemberType, reportUnknownVariableType]
    nx.draw(g, with_labels=True)  # pyright: ignore[reportUnknownArgumentType]
    plt.show()


if __name__ == "__main__":
    main()
