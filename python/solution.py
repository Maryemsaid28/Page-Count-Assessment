# solution.py

def pageCount(n: int, p: int) -> int:
    """
    Calculate the minimum number of pages to turn to reach page `p`
    in a book with `n` pages.

    You can start turning pages from the front or the back.
    Each page turn flips exactly one sheet (2 pages if possible).

    Args:
        n (int): Total number of pages in the book
        p (int): Target page number

    Returns:
        int: Minimum number of page turns required
    """
    # TODO: Implement the logic
    from_start = p // 2
    if n % 2 == 0:
        from_end = (n - p + 1) // 2
    else:
        from_end = (n - p) // 2
    return min(from_start, from_end)


def pageCountMultiple(n: int, targets: list[int]) -> list[int]:
    """
    Calculate the minimum number of pages to turn for multiple target pages
    in a book with `n` pages.

    Args:
        n (int): Total number of pages in the book
        targets (list[int]): List of target pages

    Returns:
        list[int]: List of minimum page turns for each target page
    """
    # TODO: Implement the logic
    result = []
    for p in targets:
        from_start = p // 2
        if n % 2 == 0:
            from_end = (n - p + 1) // 2
        else:
            from_end = (n - p) // 2
        result.append(min(from_start, from_end))
    return result
if __name__ == "__main__":
print(pageCount(6, 2))         # Attendu: 1
print(pageCount(5, 4))         # Attendu: 0
print(pageCountMultiple(100, [2, 50, 99]))  # Attendu: [1, 25, 0]
