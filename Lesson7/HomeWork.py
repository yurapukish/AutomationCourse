"""
HomeWork lesson 7.

Convert a non-negative integer num to its English words representation.

Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

let's take that number always > 100
100 <= num <= 999
"""

number_dict = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

dozens_dict = {
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'}


def num_to_text_converter(num):
    """
    Convert a non-negative integer num to its English words representation.

    Should work in range 100-999.
    :param num: The non-negative integer to be converted.
    :return: The English words representation of the input number.
    """
    hundred = num // 100  # get a hundred amount
    dozens = int(str(num)[1:])  # get dozens amount
    units = int(str(num)[-1])  # get units amount

    if dozens <= 19:
        return (f'{number_dict.get(hundred)} hundred '
                f'{number_dict.get(dozens)}'.title())
    else:
        dozens = dozens - units
        return (f'{number_dict.get(hundred)} hundred '
                f'{dozens_dict.get(dozens)} {number_dict.get(units)}'.title())
