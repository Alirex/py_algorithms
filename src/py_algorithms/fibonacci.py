def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_iterative(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def main() -> None:
    n = 10

    print(f"Fibonacci number at position {n} is {fibonacci(n)}")

    print(f"Fibonacci number at position {n} is {fibonacci_iterative(n)}")


if __name__ == "__main__":
    main()
