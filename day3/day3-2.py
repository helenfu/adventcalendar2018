claims = []
fabric = [[0 for i in range(1000)] for j in range(1000)]

try:
    while True:
        input = raw_input()
        id, _, xy, size = input.split(" ")
        x, y = xy.split(",")
        y = y[:-1]
        width, height = size.split("x")
        claims.append((id, int(x), int(y), int(width), int(height)))
        for i in range(int(x), int(x) + int(width)):
            for j in xrange(int(y), int(y) + int(height)):
                fabric[i][j] += 1

except EOFError:
    for claim in claims:
        x = claim[1]
        y = claim[2]
        width = claim[3]
        height = claim[4]
        good = True
        for i in range(x, x + width):
            for j in xrange(y, y + height):
                if fabric[i][j] > 1:
                    good = False
                    break
        if good:
            print claim[0]
