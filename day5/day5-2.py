alphabet = 'abcdefghijklmnopqrstuvwxyz'

def reduce(string):
    for i in range(len(alphabet)):
        letter = alphabet[i]
        value1 = letter + letter.capitalize()
        value2 = letter.capitalize() + letter
        string = string.replace(value1, "")
        string = string.replace(value2, "")
    return string

input = ""
try:
    while True:
        input = raw_input()

except EOFError:
    count = [len(input) for i in range(len(alphabet))]
    list_alph = list(alphabet)

    for idx, letter in enumerate(list_alph):
        start = input.replace(letter, "")
        start = start.replace(letter.capitalize(), "")

        new = ""
        while True:
            new = reduce(start)
            if (len(new) == len(start)):
                count[idx] = len(new)
                break
            start = new

    min = count[0]
    min_idx = 0
    for idx, val in enumerate(count):
        if val < min:
            min_idx = idx
            min = val

    print min
