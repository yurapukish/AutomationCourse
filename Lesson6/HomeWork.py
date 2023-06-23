"""
HomeWork after lesson 6.

we have two lists with equal or different size
ex. l1=[1,3,5,7]  l2=[1,4,5]

task:
create list that will store such values
list_target = [(1,1), (3,4), (5,5), (7,0)]
zero (0) is our default value that we set if no
such element by index was found in certain list.
code should work and vise versa
ex. l1=[1,4,5] l2=[1,3,5,7] input data should
produce list_target = [(1,1), (4,3), (5,5), (0,7)]
your solution should include comprehension constructions

Advices:
set of (list1 indexes union list2 indexes) could
be helpful to get larger indexes scope ( or use if-else)
dict as you remember has default value if key was
not found d1.get(key, 0)
"""

l1 = [2, 4, 6, 8, 10]
l2 = [1, 2, 3]

"""
Here is the solution:
1) create dict with keys from l1 and values from l2
2) get longer dict length for next comprehension
3) form final result as values from dicts
"""

# Step 1
dict_a = dict(enumerate(l1, start=0))
dict_b = dict(enumerate(l2, start=0))

# Step 2
dict_len = len(dict_a) if len(dict_a) >= len(dict_b) else len(dict_b)

# Step 3
final_result = [(dict_a.get(i, 0), dict_b.get(i, 0)) for i in range(dict_len)]
print(final_result)
