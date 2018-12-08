sum = 0

def add(inputs):
  children_count = int(inputs[0])
  metadata_count = int(inputs[1])
  child_sums = [0 for _ in range(children_count)]
  last_index = 2
  sum = 0

  if children_count != 0:
    child_index = 0
    for index in range(last_index, children_count + last_index):
      next_index, new_sum = add(inputs[last_index:])
      last_index += next_index
      child_sums[child_index] = new_sum
      child_index += 1

  for index in range(last_index, metadata_count + last_index):
    metadata_val = int(inputs[index])
    if (children_count != 0):
      metadata_idx = metadata_val - 1
      if metadata_idx >= 0 and metadata_idx < len(child_sums):
        sum += child_sums[metadata_idx]
    else:
      sum += metadata_val
  last_index += metadata_count

  return (last_index, sum)

try:
    while True:
        input = raw_input()

except EOFError:
    inputs = input.split(' ')
    print add(inputs)
