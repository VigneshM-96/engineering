def binary_search(sorted_list, target):

  left = 0
  right = len(sorted_list) - 1

  while left <= right:

    mid = (left + right) // 2

    if sorted_list[mid] == target:
      return mid
    elif sorted_list[mid] < target:
      left = mid + 1
    else:
      right = mid - 1

  return -1

if __name__ == "__main__":

  #datas must be sorted;
  #direct/random
  #comparable

  my_data = [3, 14, 15, 20, 25, 26, 43]
  target = 26

  element_index = binary_search(my_data, target)

  if element_index != -1:
    print(f"Element {target} is found at {element_index}")
  else:
    print(f"Element {target} is not found.")