from typing import Literal, NewType, Self

from pydantic import BaseModel, Field, field_validator

Vertex = NewType("Vertex", str)
"""Vertex.

As node name.
"""

type VertexIndex = int
"""Vertex index.

Position in vertexes list and in adjacency matrix.
"""

type VertexRelationIExist = Literal[1]
type VertexRelationINotExist = Literal[0]

type VertexRelation = VertexRelationIExist | VertexRelationINotExist
"""Vertex relation.

For simple graph:
- 1 if edge exists.
- 0 if edge not exists.
"""

type AdjacencyMatrix = list[list[VertexRelation]]
"""Adjacency matrix.

1st dimension - vertexes (from)
2nd dimension - adjacent vertexes (to)
"""


class GraphByAdjacencyMatrix(BaseModel):
    vertexes: list[Vertex] = Field(default_factory=list)
    """Vertexes. Order is important."""

    @field_validator("vertexes")
    @classmethod
    def validate_vertexes(cls, v: list[Vertex]) -> list[Vertex]:
        if len(v) != len(set(v)):
            msg = "Vertexes must be unique."
            raise ValueError(msg)
        return v

    adj_matrix: AdjacencyMatrix = Field(default_factory=list)
    """Adjacency matrix."""

    @classmethod
    def create(
        cls,
        vertexes: list[Vertex | str],
        adj_matrix: AdjacencyMatrix,
    ) -> Self:
        return cls(
            vertexes=[Vertex(v) for v in vertexes],
            adj_matrix=adj_matrix,
        )

    def is_exist_edge(self, from_: Vertex, to: Vertex) -> bool:
        return self.adj_matrix[self.vertexes.index(from_)][self.vertexes.index(to)] == 1
