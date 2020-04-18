import random

#  create 2 sets, each populated by 5 random integers between 1 and 10, inclusive.
#  display the sets
set1 = set()
set2 = set()

for i in range(5):
    set1.add(random.randint(1, 10))
    set2.add(random.randint(1, 10))
print("set 1: ", set1)
print("set 2: ", set2)
print()

#  find and display the union of sets 1 & 2
union_set = set1.union(set2)
print("set1 U set2: ", union_set)

#  use set comprehension to select odd numbers from the union, store them in a set
#  display odd numbers set
odd_set = {x for x in union_set if x % 2 != 0}
print("Odd numbers in union of set1 and set2: ", odd_set)

#  find and display the intersection of set 1 & 2
print("set1 intersect set2: ", set1 & set2)
print("set1 symmetric difference set2: ", set1 ^ set2)

