"""
HomeWork after lesson 5.

Exists some car data with color, year, engine_volume, car type , price
We have search_criteria as tuple of ( year>= , engine_volume >= , price<=)
write code that will help us to get cars that satisfy search_criteria.
Cars should be sorted by price ascending. We should print up to
five first found elements
"""
import time

car_data = {
    'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
    'Audi': ('black', 2020, 2.0, 'sedan', 55000),
    'BMW': ('white', 2018, 3.0, 'suv', 70000),
    'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
    'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
    'Honda': ('red', 2017, 1.5, 'sedan', 30000),
    'Ford': ('green', 2019, 2.3, 'suv', 40000),
    'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
    'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
    'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
    'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
    'Kia': ('white', 2020, 2.0, 'sedan', 28000),
    'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
    'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
    'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
    'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
    'Jeep': ('green', 2021, 3.0, 'suv', 50000),
    'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
    'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
    'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
    'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
    'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
    'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
    'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
    'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
    'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
    'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
    'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
    'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
    'Acura': ('white', 2017, 2.4, 'suv', 40000),
    'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
    'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
    'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
    'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
    'Ram': ('black', 2019, 5.7, 'pickup', 40000),
    'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
    'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
    'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
    'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)}

search_criteria = (2017, 1.6, 36000)

"""
For real life I would rather use first method, cause second method is
something new for that I learned on the course. Also for 1 method we can
use  list comprehension, but it's the next lessons).

First solution:
1) Create empty list
2) Add all cars that satisfy search_criteria
3) Sort list by price ascending
4) Print first 5 cars
5) Print time taken by first method
"""
start_time = time.time()
# first create list of cars that satisfy search_criteria
searched_cars = []
for key, values in car_data.items():
    if all(values[1] >= search_criteria[0],
           values[2] >= search_criteria[1],
           values[4] >= search_criteria[2]):
        searched_cars.append((key, values))
# sort list of cars by price ascending and return first 5 results
searched_cars.sort(key=lambda car: car[1][4])
end_time = time.time()
elapsed_time = end_time - start_time
print(searched_cars[:5])
print(f'Time taken by first method: {elapsed_time:.6f} seconds')

"""
Second solution:
1) Sort list of cars by price ascending
2) Go through list of cars and check if they satisfy search_criteria
3) Print up to 5 element and break
4) Print time taken by second method
"""
start_time = time.time()
sorted_dict = sorted(car_data.items(), key=lambda car: car[1][4])
results = 0
for key, values in sorted_dict:
    if all(values[1] >= search_criteria[0],
           values[2] >= search_criteria[1],
           values[4] >= search_criteria[2]):
        print(f"('{key}', {values})", end=', ')
        results += 1
        if results == 5:
            break
end_time = time.time()
elapsed_time2 = end_time - start_time
print(f'\nTime taken by second method: {elapsed_time2:.6f} seconds')
print(f'Second method longer for: {(elapsed_time2 - elapsed_time):.6f}'
      if elapsed_time2 > elapsed_time
      else 'Second method shorter for: '
           f'{(elapsed_time - elapsed_time2):.6f} seconds')
