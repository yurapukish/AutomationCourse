poem_text = """I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze.

Continuous as the stars that shine
And twinkle on the Milky Way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance."""

# task 1
"""
Logic:
1) Create a list of vowels
2) Iterate over the text and count each vowel
3) Print the result
"""
vowels_be_counted = ('a', 'e', 'i', 'o', 'u')
global_width, row_width = 32, 12
print('-' * global_width)
print(f"| {'vowel':^{row_width}} |  {'count':^{row_width}} |")
print('-' * global_width)
for vowel in vowels_be_counted:
    print((f'| {vowel:^{row_width}} -> '
           f'{poem_text.lower().count(vowel):^{row_width}} |'))
print('-' * global_width)

# task 2
"""
Logic:
1) Create a function with a parameter
2) Iterate over the text and replace each vowel
3) Return the result
"""


def replace_symbols(text):
    """
    Replace vowels in the text.

    Args:
        text (str): The input text.

    Returns:
        str: The modified text with changed vowels.
    """
    symbols_be_replaced = {'A': 'À', 'a': 'à', 'E': 'É', 'e': 'é', 'I': 'Í',
                           'i': 'í', 'O': 'Ó', 'o': 'ó', 'U': 'Ú', 'u': 'ú'}

    for symbol in symbols_be_replaced:
        text = text.replace(symbol, symbols_be_replaced[symbol])
    print(text)
    return text


replace_symbols(poem_text)
