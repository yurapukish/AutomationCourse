"""
Second solution.

Steps:
1) Sort list of cars by price ascending
2) Go through list of cars and check if they satisfy search_criteria
3) Print up to 5 element and break
4) Print time taken by second method
"""
import time

from Lesson5.HomeWork import car_data, search_criteria

start_time = time.time()
sorted_dict = sorted(car_data.items(), key=lambda car: car[1][4])
results = 0
for key, values in sorted_dict:
    if all([
        values[1] >= search_criteria[0],
        values[2] >= search_criteria[1],
        values[4] <= search_criteria[2],
    ]):
        print(f"('{key}', {values})", end=', ')
        results += 1
        if results == 5:
            break
end_time = time.time()
elapsed_time2 = end_time - start_time
print(f'\nTime taken by second method: {elapsed_time2:.6f} seconds')
