"""
Question doesn't say if the lists:
    - are of the same sizes
    - are sorted in any order
    OR
    - should we consider the items that are repeated in the same list i.e., list containing duplicates

Simple approach:
    - convert one list to a set
    - iterate over the other list checking if the num exists in the set
"""
"""
Set intersection
"""
def get_common_unique(A, B):
    return list(set(A) & set(B))


"""
Set comprehension
"""
def get_common_unique(A, B):
    return list({num for num in B if num in set(A)})        # considering unique are expected; if not, use list comprehension instead


if __name__ == '__main__':
    print(get_common_unique([1, 2, 3, 4], [3, 4, 5, 6]))
    print(get_common_unique([1, 2, 3, 5, 6], [3, 4, 5, 6, 6]))