from torchgen.executorch.api.types import halfT


def print_diamond(n):
    # top half
    for i in range(1, n + 1, 2):
        print(" " * ((n - i) // 2) + "*" * i)

    # bottom half: n-2 -> 1
    for i in range(n - 2, 0, -2):
        print(" " * ((n - i) // 2) + "*" * i)


if __name__ == "__main__":
    print_diamond(5)
    print_diamond(3)
    print_diamond(6)
    print_diamond(7)