def recursive_b_search(lst, target, lo, hi):
    """
    Time complexity of the recursive binary search algorithm is log2(n), the same as for
    simple binary search without recursion
    """
    if lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            return recursive_b_search(lst, target, mid+1, hi)
        else:
            return recursive_b_search(lst, target, lo, mid-1)
    return False


r = [1, 20, 44, 999, 23444]
print(recursive_b_search(r, 999, 0, len(r)-1))

