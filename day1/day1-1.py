total = 0
try:
    input = raw_input()

    while (input):
        total += int(input)
        input = raw_input()

except EOFError:
    print total
