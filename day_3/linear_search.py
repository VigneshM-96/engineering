#linear search o(n)

def linear_search(items, target):

  for i in range(len(items)):

    if items[i] == target:

      return i

  return -1

items = [19, 2, 3, 4, 5]
target = 4
print(f"Element found at {linear_search(items, target)}")