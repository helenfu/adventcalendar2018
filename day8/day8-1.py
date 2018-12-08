sum = 0

def add(inputs):
  children_count = int(inputs[0])
  metadata_count = int(inputs[1])
  last_index = 2
  sum = 0

  if children_count != 0:
    for index in range(last_index, children_count + last_index):
      next_index, new_sum = add(inputs[last_index:])
      last_index += next_index
      sum += new_sum


  for index in range(last_index, metadata_count + last_index):
    sum += int(inputs[index])
  last_index += metadata_count

  return (last_index, sum)

try:
    while True:
        input = raw_input()

except EOFError:
    inputs = input.split(' ')
    print add(inputs)
