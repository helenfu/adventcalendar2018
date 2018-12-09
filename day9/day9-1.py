try:
    while True:
        input = raw_input()

except EOFError:
    inputs = input.split(" ")
    player_count = int(inputs[0])
    last_marble = int(inputs[6])

    current_index = 0
    marble_circle = [0]
    scores = [0 for _ in range(player_count)]

    for marble in range(1, last_marble + 1):
        # print "current index {}".format(current_index)
        starting_len = len(marble_circle)
        if marble > 0 and marble % 23 == 0:
            # add current marble to score
            current_player = marble % player_count
            scores[current_player] += marble
            # remove and add 7 counter-clockwise to score
            other_marble_index = (current_index - 7) % starting_len
            additional_marble = marble_circle[other_marble_index]
            scores[current_player] += additional_marble
            del marble_circle[other_marble_index]
            current_index = (other_marble_index) % starting_len
            # print "player {} removed {} from index {}".format(current_player, additional_marble, other_marble_index)
        else:
            current_index = (current_index + 2) % starting_len
            marble_circle.insert(current_index, marble)
            # print "marble {} added to index {}".format(marble, current_index)

    print max(scores)
