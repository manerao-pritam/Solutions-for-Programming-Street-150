def is_balanced(s):
    if not s:
        return True

    stk = []
    brackets = {'(': ')', '[': ']', '{': '}'}

    for c in s:
        if c in brackets.keys():
            stk.append(c)
        elif not stk or brackets[stk.pop()] != c:
            return False

    return not stk


if __name__ == "__main__":
    print(is_balanced("{[())]}"))  # False
    print(is_balanced("{[()]}"))   # True
    print(is_balanced("))))"))     # False
    print(is_balanced("{[({})]}")) # True
    print(is_balanced(""))         # True
    print(is_balanced("{"))        # False
    print(is_balanced("]"))        # False