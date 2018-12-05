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
    new = ""
    while True:
        new = reduce(input)
        if (len(new) == len(input)):
            print len(new)
            break
        input = new
