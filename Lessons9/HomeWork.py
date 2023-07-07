"""
HomeWork 9.

Write script that will read "input.txt" file and find there
all characters from english alphabet collect these characters
and their positions in file after info collected this info
as text write to "output.txt" file in such format.
####################
<first found letter> -> pos1
<next_letter> -> pos2
<next_letter -> pos3
etc
#######################
"""

import re

try:
    # Create file to write the output
    with open('output.txt', 'w') as output_file:
        # Add a header to the output file
        output_file.write(f'{"#" * 20}\n')

        # Step 1: Open the input.txt file and read it
        with open('input.txt', 'r') as input_file:
            text = input_file.read()

            # Step 2: Find all matches using a regular expression
            matches = re.findall(r'[a-zA-Z]', text)

        # Step 3: Write the matches and their indices to the output file
        output_file.writelines(f'{el:^7} -> {text.index(el):^7}\n'
                               for el in matches)
        # Add footer to the output file
        output_file.write(f'{"#" * 20}\n')

except Exception as g_exc:
    # Print error if occurs
    print(g_exc)
