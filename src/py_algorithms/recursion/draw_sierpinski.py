from typing import TYPE_CHECKING, cast

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches
from numpy.typing import NDArray

if TYPE_CHECKING:
    from collections.abc import Sequence

    from matplotlib.axes import Axes

# https://chaosgame.drwhy.ai/examples-in-python-2.html#the-sierpinski-triangle-once-again
# https://understanding-recursion.readthedocs.io/en/latest/14%20Sierpinski.html


type Vertex = NDArray[np.float64]
type Vertices2D = NDArray[np.float64]


def draw_triangle(
    vertices: Vertices2D,
    ax: Axes,
) -> None:
    triangle = patches.Polygon(
        xy=cast("Sequence[float]", vertices),
        fill=False,
        edgecolor="black",
    )
    ax.add_patch(triangle)


def get_midpoint(point_1: Vertex, point_2: Vertex) -> Vertex:
    return np.array(
        [
            (point_1[0] + point_2[0]) / 2,
            (point_1[1] + point_2[1]) / 2,
        ],
    )


def draw_sierpinski(
    vertices: Vertices2D,
    level: int,
    ax: Axes,
) -> None:
    draw_triangle(vertices, ax)
    if level > 0:
        draw_sierpinski(
            vertices=np.array(
                [
                    vertices[0],
                    get_midpoint(vertices[0], vertices[1]),
                    get_midpoint(vertices[0], vertices[2]),
                ],
            ),
            level=level - 1,
            ax=ax,
        )
        draw_sierpinski(
            vertices=np.array(
                [
                    vertices[1],
                    get_midpoint(vertices[1], vertices[0]),
                    get_midpoint(vertices[1], vertices[2]),
                ],
            ),
            level=level - 1,
            ax=ax,
        )
        draw_sierpinski(
            vertices=np.array(
                [
                    vertices[2],
                    get_midpoint(vertices[2], vertices[0]),
                    get_midpoint(vertices[2], vertices[1]),
                ],
            ),
            level=level - 1,
            ax=ax,
        )


def draw_sierpinski_full(
    level: int,
    side_length: float = 1.0,
) -> None:
    _fig, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.set_axis_off()

    vertices: Vertices2D = np.array(
        [
            [0.0, 0.0],
            [side_length, 0.0],
            [side_length / 2, (side_length * (3**0.5)) / 2],
        ],
    )

    draw_sierpinski(vertices, level, ax)

    plt.show()


def main() -> None:
    draw_sierpinski_full(level=4)


# %%.
if __name__ == "__main__":
    main()
