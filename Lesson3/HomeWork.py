"""
HomeWork after lesson 3.

1 - sort list by age and sex fields
2 - somehow you need to get new list as old list without first
two elements and last two elements. Print this new list
3 - in new list calculate total numbers of "female"  and "male"
and print it as small table.

"""

from colorama import Fore, Style


def return_list_slice(sequence: list):
    """
    Return a list, excluding the first two and the last two elements.

    Args:
        sequence (list): The input list.

    Returns:
        list: The slice of the input list.

    Raises:
        TypeError: If the input is not a list.

    """
    if isinstance(sequence, list):
        return sequence[2:-2]
    else:
        raise TypeError('Function parameter must be a list')


def count_genders(people_list: list):
    """
    Count the number of "female" and "male" in the input list.

    Args:
        people_list (list): The input list.

    Returns:
        print: The number of "female" and "male"

    """
    female, male = 0, 0
    for person in people_list:
        if person[-1] == 'female':
            female += 1
        elif person[-1] == 'male':
            male += 1
    global_width, row_width = 32, 12

    return print('-' * global_width, ' ', '    \n',
                 f"| {'Sex':^{row_width}} |  {'Count':^{row_width}} |", '\n',
                 '-' * global_width + '\n',
                 f"| {'female':^{row_width}} |  {female:^{row_width}} |", '\n',
                 f"| {'male':^{row_width}} |  {male:^{row_width}} |", '\n',
                 '-' * global_width)


people = [
    ('Alice', 32, 100, 'Johnson', 'female'),
    ('Bob', 41, 200, 'Smith', 'male'),
    ('Charlie', 27, 150, 'Jones', 'male'),
    ('David', 52, 75, 'Williams', 'male'),
    ('Eve', 18, 300, 'Davis', 'female'),
    ('Frank', 33, 50, 'Taylor', 'male'),
    ('Grace', 42, 125, 'Clark', 'female'),
    ('Henry', 26, 225, 'Lewis', 'male'),
    ('Ivy', 38, 175, 'Moore', 'female'),
    ('Jack', 20, 140, 'Harris', 'male'),
    ('Kate', 37, 110, 'Miller', 'female'),
    ('Leo', 44, 90, 'Wilson', 'male'),
    ('Mae', 29, 180, 'Brown', 'female'),
    ('Nick', 51, 70, 'Davies', 'male'),
    ('Oliver', 18, 250, 'Collins', 'male'),
    ('Pete', 36, 160, 'Green', 'male'),
    ('Quinn', 20, 230, 'Bell', 'female'),
    ('Remy', 30, 120, 'Foster', 'male'),
    ('Sara', 28, 140, 'Baker', 'female'),
    ('Tom', 47, 80, 'Scott', 'male'),
    ('Ursula', 39, 135, 'Adams', 'female'),
    ('Vivian', 25, 190, 'Ross', 'female'),
    ('Wendy', 46, 90, 'Wright', 'female'),
    ('Xavier', 31, 105, 'Reed', 'male'),
    ('Yuliana', 22, 200, 'Lopez', 'female'),
    ('Zack', 48, 60, 'Mitchell', 'male'),
    ('Adam', 35, 75, 'Davis', 'male'),
    ('Bella', 27, 125, 'Smith', 'female'),
    ('Charlie', 44, 115, 'Johnson', 'male'),
    ('Daisy', 20, 215, 'Miller', 'female'),
    ('Ethan', 33, 100, 'Taylor', 'male'),
    ('Fiona', 40, 150, 'Jones', 'female'),
    ('George', 24, 180, 'Lewis', 'male'),
    ('Hannah', 22, 200, 'Williams', 'female'),
    ('Ivan', 29, 160, 'Brown', 'male'),
    ('Julie', 55, 90, 'Clark', 'female'),
    ('Kenny', 38, 140, 'Harris', 'male'),
    ('Luna', 55, 170, 'Smith', 'female'),
    ('Mike', 55, 55, 'Johnson', 'male')]

# task 1
print(Fore.YELLOW, 'Task 1', '\n',
      Fore.RED + 'List before sorting ->' + Style.RESET_ALL,
      people, end='\n')

people.sort(key=lambda x: (x[1], x[4]))
print(Fore.GREEN, 'List after sorting ->', Style.RESET_ALL, people, end='\n\n')

# task 2
new_people_list = return_list_slice(people)
print(Fore.YELLOW, 'Task 2', '\n',
      Fore.MAGENTA + 'Exclude first and last 2 elements in list ->',
      Style.RESET_ALL, new_people_list, end='\n\n')

# task 3
print(Fore.YELLOW, 'Task 3' + Style.RESET_ALL)
count_genders(new_people_list)
