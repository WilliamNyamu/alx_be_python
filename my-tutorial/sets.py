# Imagine you're hosting a gathering of friends from diverse backgrounds,
#  each with their unique identity. Now, picture this gathering as a set – 
# a collection where each individual is distinct, much like the elements of a set in Python.

# Just as no two guests at your gathering share the same identity, 
# no two elements in a set are identical. 
# This notion of uniqueness lies at the heart of sets.

# Syntax: creating sets using curly braces
guest_set1 = {"Alice", "Bob", "Charlie", "David", "Eve"}
print(guest_set1)
# Syntax:  creating set using the set() constructor

guest_set2 = set(["David", "Eve", "Frank", "Grace", "Helen"])
print(guest_set2)

# Adding elements using the add() method
guest_set1.add("William")
print(guest_set1)

# Use remove() or discard() to remove an element from a set
guest_set1.remove("Charlie")
print(guest_set1)

# Use len() to determine the length of a set
print(len(guest_set1))

# Union of sets using the union() method
# This also ensures there are no duplicates

all_guests = guest_set1.union(guest_set2)
print(all_guests)

# Intersection -  How to find Common Interests
common_guests = guest_set1.intersection(guest_set2)
print(common_guests)


# Difference - How to find unique attributes
unique_to_guest_set1 = guest_set1.difference(guest_set2)
print(unique_to_guest_set1)

# The difference() method identifies the guests presents in guest_set1 but not in guest_set2.


# Symmetric Difference - How to find exclusive elements
exclusive_guests = guest_set1.symmetric_difference(guest_set2)
print(exclusive_guests)

# The symmetric_difference() method identifies guests present exclusively in either guest_et1 or guest_set2, storing them in the set exclusive_guests.


# Use the clear() method to clear a set
guest_set1.clear()
print(guest_set1)
