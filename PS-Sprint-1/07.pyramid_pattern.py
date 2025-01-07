def pyramid_pattern(height):
    for i in range(1, height + 1, 2):
        print(" " * ((height - i) // 2) + "*" * i)

    """
    for i in range(1, height + 1):
        stars_count = 2 * i - 1
        spaces = height - i

        # focus on adding spaces only BEFORE the stars
        print(" " * spaces + '*' * stars_count)
    """


if __name__ == "__main__":
    pyramid_pattern(5)
    pyramid_pattern(3)
    pyramid_pattern(6)
    pyramid_pattern(7)