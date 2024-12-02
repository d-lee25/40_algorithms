# Sorting algorithms (Bubble, Merge, Insertion, Shell, Selection)

# Bubble sort
"""
- Bubble sort is the simplest and slowest for sorting
- Time complexity at its slowest is O(N^2)
- Should be used on smaller datasets
"""
def bubble_sort(l: list):
    """
    :param l: list
    Keeps highest value at the top during loop
    :return: list
    """
    last_element = len(l) - 1
    for passNo in range(last_element, 0, -1):
        for idx in range(passNo):
            if l[idx] > l[idx + 1]:
                l[idx], l[idx + 1] = l[idx + 1], l[idx]
    return l


def insert_sort(l: list):
    """
    :param l:
    :return: sorted list
    """
    return l