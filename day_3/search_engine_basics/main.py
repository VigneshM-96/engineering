def linea_search(items, target):
  operations = 0
  for i in range(len(items)):
    operations += 1
    if items[i] == target:
      return i, operations
  return -1, operations

def binary_search(items, target):
  left = 0
  right = len(items) - 1
  operations = 0
  while left <= right:
    operations += 1
    mid = (left + right) // 2
    if items[mid] == target: return mid
    elif items[mid] < target: left = mid + 1
    else:
      right = mid -1