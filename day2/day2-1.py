from collections import Counter

twos = 0
threes = 0

try:
    while True:
        input = raw_input()
        counter = Counter(input)
        two_added = False
        three_added = False
        for letter, count in counter.items():
            if count == 2 and not two_added:
                two_added = True
                twos += 1
            if count == 3 and not three_added:
                three_added = True
                threes += 1
            if two_added and three_added:
                break

except EOFError:
    print twos * threes
