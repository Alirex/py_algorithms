from py_algorithms.graphs.graph_by_adjacency_matrix import AdjacencyMatrix, GraphByAdjacencyMatrix, Vertex


def graph_by_adj_matrix_example() -> None:
    vertexes = ["A", "B", "C", "D"]

    adj_matrix: AdjacencyMatrix = [
        [0, 1, 0, 1],  # Вершина A
        [1, 0, 1, 0],  # Вершина B
        [0, 1, 0, 1],  # Вершина C
        [1, 0, 1, 0],  # Вершина D
    ]

    graph = GraphByAdjacencyMatrix.create(vertexes=vertexes, adj_matrix=adj_matrix)

    relation = graph.is_exist_edge(from_=Vertex("A"), to=Vertex("B"))

    # noinspection Assert
    assert relation  # noqa: S101
    print(relation)


# def graph_by_adj_list_example() -> None:
#     adj_list = {
#         "A": ["B", "D"],
#         "B": ["A", "C"],
#         "C": ["B", "D"],
#         "D": ["A", "C"],
#     }


def main() -> None:
    graph_by_adj_matrix_example()


if __name__ == "__main__":
    main()
