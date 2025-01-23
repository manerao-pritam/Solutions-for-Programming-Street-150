"""
considering the Input: string = "The numbers are 12 and 34"
"""
def get_sum(s):
    tokens = s.strip().split()
    result = 0

    for token in tokens:
        if token.isnumeric():
            try:
                result += int(token)
            except ValueError:
                print(f"invalid conversion for: {token}", ValueError)
                pass

    return result


if __name__ == "__main__":
    print(get_sum("The numbers are 12 and 34"))  # 46
    print(get_sum("The numbers are 120    and 304   "))  # 424
    print(get_sum("The numbers are 34"))  # 34
    print(get_sum("The numbers are"))  # 0
    print(get_sum("1,000 is a number"))  # 0 (comma-separated numbers won't be summed)