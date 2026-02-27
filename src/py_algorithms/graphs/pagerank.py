import matplotlib.pyplot as plt
import networkx as nx


def main() -> None:
    # Створення графа

    # Створення спрямованого графа
    g = nx.DiGraph()  # type: ignore[var-annotated] # pyright: ignore[reportUnknownVariableType]

    # Додавання вершин та ребер до графа  # noqa: RUF003
    edges = [("A", "B"), ("A", "C"), ("B", "C"), ("C", "A"), ("D", "C")]
    g.add_edges_from(edges)  # pyright: ignore[reportUnknownMemberType]

    # Застосування алгоритму PageRank
    pagerank = nx.pagerank(  # pyright: ignore[reportUnknownVariableType]
        g,  # pyright: ignore[reportUnknownArgumentType]
        alpha=0.85,  # pyright: ignore[reportUnknownArgumentType]
    )  # alpha - це фактор згладжування  # pyright: ignore[reportUnknownVariableType]

    # Виведення результатів PageRank
    for node, rank in pagerank.items():  # pyright: ignore[reportUnknownVariableType]
        print(f"{node}: {rank}")

    # Візуалізація графа:
    plt.figure(figsize=(6, 6))
    nx.draw_networkx(g, with_labels=True)  # pyright: ignore[reportUnknownArgumentType]
    plt.show()


if __name__ == "__main__":
    main()
