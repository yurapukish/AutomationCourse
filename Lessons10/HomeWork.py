"""
HomeWork 10.

open input.txt file and find all small english letters
that match such conditions:
target small letter round exactly with three capital
english letters on the left and on the right
Match examples:
sdTRYaUVKn  -> matches "a"
NTRSjARTb   -> no match ( not exactly 3 capital letters on the left)
zDFGbOPNq   -> matches "b"
Print Output as : "Result: "<your_found_human_readable_string">
"""

import re

try:
    # Step 1: Open the input.txt file and read it
    with open('input.txt', 'r') as input_file:
        text = input_file.read()

        # Step 2: Find all matches using a regular expression
        pattern = r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]'
        matches = re.findall(pattern, text)

        # Step 3: Write the matches
        print(f"Result: \"{''.join(matches)}\"")


except Exception as g_exc:
    # Print error if occurs
    print(g_exc)
