def factorial(n: int) -> int:
    return 1 if n == 1 else n * factorial(n - 1)


def factorial_with_acc(n: int, acc: int = 1) -> int:
    return acc if n == 1 else factorial_with_acc(n - 1, n * acc)


def main() -> None:
    print(factorial(5))


if __name__ == "__main__":
    main()
