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
vowels = ('a', 'e', 'i', 'o', 'u')
table_style = (32, 12)
print('-' * table_style[0])
print(f"| {'vowel':^{table_style[1]}} |  {'count':^{table_style[1]}} |")
print('-' * table_style[0])
for vowel in vowels:
    print((f'| {vowel:^{table_style[1]}} -> '
          f'{poem_text.lower().count(vowel):^{table_style[1]}} |'))
print('-' * table_style[0])


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
