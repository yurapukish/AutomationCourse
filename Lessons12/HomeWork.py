"""
HomeWork 12.

Given list of list of list etc of integers
write recursive function that will accept
as argument target list and return sum of
all integers inside it
Input:
[[[[1, 4, 5], [[6, 9],[[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]
Output: Target sum = 72
"""


y = [[[[1, 4, 5], [[6, 9], [[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]


def sum_lists_values(list_with_values: list, count: int = None) -> int:
    """Recursive function: accept as argument target list and return sum of."""
    count = 0 if count is None else count
    for obj in list_with_values:
        # Add value to count if it is int
        if type(obj) == int:
            count += obj
        else:
            # Go inside the list
            count = sum_lists_values(obj, count)
    return count


print(f'Final result is: {sum_lists_values(y)}')
