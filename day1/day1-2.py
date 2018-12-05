def check_value(total, seen):
    if total in seen:
        return True
    else:
        seen[total] = True
    return False

def solution():
    total = 0
    seen = {0: True}
    input_list = []

    try:
        while True:
            input = raw_input()
            value = int(input)
            input_list.append(value)
            total += value
            if check_value(total, seen):
                print total
                return

    except EOFError:
        while True:
            for value in input_list:
                total += value
                if check_value(total, seen):
                    print total
                    return

solution()