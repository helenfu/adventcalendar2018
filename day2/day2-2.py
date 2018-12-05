all_input = []

try:
    while True:
        input = raw_input()
        all_input.append(input)

except EOFError:
    for i in range(0, len(all_input) - 1):
        for j in range(i + 1, len(all_input)):
            diff_count = 0
            same_str = ""
            first = all_input[i]
            second = all_input[j]
            for k in xrange(len(first)):
                if first[k] == second[k]:
                    same_str += first[k]
                else:
                    diff_count += 1
                    if diff_count > 1:
                        continue
            if diff_count == 1:
                print same_str
                break
