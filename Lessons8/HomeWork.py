"""
HomeWork lesson 8.

Given the list of integers ( positive, negative, zeros)
Find max multiplication of three values in list

Input: [-1, 1, 2, 0, 3, 12, 4, 5, -1, 6]
Output: Max value = "360". Nums are: (12, 5, 6)

My solution:
1) Sort the list by the absolute value of each element
2) Create positive and negative lists
3) Append values to positive and negative lists
4) Find the max value and save elements in output
"""
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Sort the list by absolute value of each element
l1.sort(key=lambda x: abs(x), reverse=True)


# Separate positive and negative elements
positive, negative = [el for el in l1 if el > 0], [el for el in l1 if el <= 0]
positive_len, negative_len = len(positive), len(negative)

if 1 <= positive_len < 3:
    # if positive elements are 1 or 2
    # We multiply 1 positive element and 2 negative elements
    result = positive[0] * negative[0] * negative[1]
    output = positive[0], negative[0], negative[1]

elif positive_len >= 3:
    # if positive elements are 3 or more
    # we have 2 options: *all positive
    #                    negative elements  * positive element
    result = positive[0] * positive[1] * positive[2]
    output = (positive[0], positive[1], positive[2])
    if negative_len > 1:
        # multiply all negative elements
        result2 = positive[0] * negative[0] * negative[1]
        output2 = positive[0], negative[0], negative[1]
        if result2 > result:
            result = result2
            output = output2
else:
    # If no positive elements
    # We multiply all negative elements
    result = negative[-1] * negative[-2] * negative[-3]
    output = negative[-1], negative[-2], negative[-3]

# Print results
print(f'Max value = "{result}". Nums are: {output}')
