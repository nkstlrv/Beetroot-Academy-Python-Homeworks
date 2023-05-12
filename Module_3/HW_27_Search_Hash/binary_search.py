
def simple_binary_search(lst, target, lo, hi):
    """
    Time complexity is log2(n)
    """

    tries = 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid] == target:
            return f"Index - {mid}, Tries - {tries}"
        elif lst[mid] < target:
            tries += 1
            lo = mid + 1
        elif lst[mid] > target:
            tries += 1
            hi = mid - 1
    return False


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(simple_binary_search(a, target=88, lo=0, hi=len(a)-1))

