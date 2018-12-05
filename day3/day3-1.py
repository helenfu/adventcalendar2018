fabric = [[0 for i in range(1000)] for j in range(1000)]

try:
    while True:
        input = raw_input()
        _, _, xy, size = input.split(" ")
        x, y = xy.split(",")
        y = y[:-1]
        width, height = size.split("x")
        for i in range(int(x), int(x) + int(width)):
            for j in xrange(int(y), int(y) + int(height)):
                fabric[i][j] += 1

except EOFError:
    squares = 0
    for i in xrange(len(fabric)):
        for j in range(1000):
            if fabric[i][j] > 1:
                squares += 1
    print squares
