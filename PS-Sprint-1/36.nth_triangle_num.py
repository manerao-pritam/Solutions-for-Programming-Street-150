"""
it's nothing but sum of the first n natural numbers
"""
def get_nth_triangle_num(n):
    return n * (n + 1) // 2


if __name__ == "__main__":
    print(get_nth_triangle_num(3))
    print(get_nth_triangle_num(4))
    print(get_nth_triangle_num(5))