#what is big o notation?
#Big O notation is mathematical framework in computer science to describe how the time or space of an algorithm scales as per the input size grows

#1. O(1) - constant - very fastest
def get_item(items):
  return items[0]

items = [10, 109, 100]
print(get_item(items))

#2. O(log n) - logarithmic - good
def binary_search(items, target):
  l = 0
  h = len(items)
  m = (l + h) // 2
  while l <= h:
    m = (l + h) // 2
    if target == items[m]: return m
    elif target < items[m]: h = m - 1
    else: l = m + 1

  return -1

print(binary_search([2, 10, 34], 4))

#3. O(n) - linear - fair
def read_all_items(items):
  for item in items:
    print(item)

read_all_items([10, 1, 5, 4])

#4. O(n^2) - quadratic - poor(slow)
def print_pairs(items):
  for i in items:
    for j in items:
      print(i, j)

print(print_pairs([10, 20, 30]))
      
    