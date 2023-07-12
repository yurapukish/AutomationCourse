"""
HomeWork 11.

Write a generator function that takes a range value and chunk_size as input
and produces output as lists with length equal to chunk size.
Example:
Call: chunk_generator(range(11), chunk_size=3)
Output:
[0, 1, 2]
[3, 4, 5]
[6, 7, 8]
[9, 10]
"""


def chunk_generator(sequence, chunk_size):
    """
    Generate chunk of the sequence.

    :param sequence: range value
    :param chunk_size: int
    :return: produces  lists with length equal to chunk size
    """
    start, end = 0, chunk_size
    # determine the number of sub-chunks
    sub_chunks = (len(sequence) // chunk_size
                  if len(sequence) % chunk_size == 0
                  else (len(sequence) // chunk_size) + 1)
    for _ in range(sub_chunks):
        yield list(sequence[start:end])
        start, end = start + chunk_size, end + chunk_size


for chunk in chunk_generator(range(11), chunk_size=3):
    print(chunk)
