import turtle
from typing import Final

TOTAL_DEGREES: Final[int] = 360


def koch_curve(
    t: turtle.Turtle,
    order: int,
    size: float,
) -> None:
    if order == 0:
        t.forward(size)
        return

    angles = [
        60,
        -120,
        60,
        0,
    ]

    for angle in angles:
        koch_curve(t, order - 1, size / 3)
        t.left(angle)


def draw_koch_curve(
    order: int,
    size: float = 300,
) -> None:
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  # 0 is the fastest speed
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    sides = 3  # Draw a triangle, 3 sides
    angle = TOTAL_DEGREES / sides

    for _ in range(sides):
        koch_curve(t, order, size)
        t.right(angle)

    window.mainloop()


def main() -> None:
    draw_koch_curve(
        # order=3,
        order=2,
        size=200,
    )


if __name__ == "__main__":
    main()
