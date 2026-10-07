items = [23, 10, 2, 54, 67]
target = 10

#array traversal
for i, e in enumerate(items):
  print(f"Index {i} : Element {e}")

#searching using linear searching

found_index = -1
for i, e in enumerate(items):
  if e == target:
    found_index = i

if found_index != -1:
  print(f"Element {target} found at {found_index}")
else:
  print(f"Element {target} not found.")