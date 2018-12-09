class Node:
    prev = None
    next = None
    val = 0

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def goToNext(self, count):
        if count == 0:
            return self
        else:
            return self.next.goToNext(count - 1)

    def goToPrev(self, count):
        if count == 0:
            return self
        else:
            return self.prev.goToPrev(count - 1)

    def delete(self):
        temp_prev = self.prev
        self.prev.next = self.next
        self.next.prev = temp_prev

    def addNext(self, nextVal):
        temp_next = self.next
        self.next = Node(nextVal, self, self.next)
        temp_next.prev = self.next

try:
    while True:
        input = raw_input()

except EOFError:
    inputs = input.split(" ")
    player_count = int(inputs[0])
    last_marble = int(inputs[6])

    current = Node(0)
    current.next = current
    current.prev = current
    scores = [0 for _ in range(player_count)]

    for marble in range(1, last_marble + 1):
        # print "current index {}".format(current_index)
        if marble > 0 and marble % 23 == 0:
            # add current marble to score
            current_player = marble % player_count
            scores[current_player] += marble
            # remove and add 7 counter-clockwise to score
            other_marble = current.goToPrev(7)
            scores[current_player] += other_marble.val
            current = other_marble.next
            other_marble.delete()
            # print "player {} removed {}".format(current_player, other_marble.val)
        else:
            insertion_marble = current.goToNext(1)
            insertion_marble.addNext(marble)
            current = insertion_marble.next
            # print "marble {} added".format(marble)
        # if marble % 10000 == 0:
        #     print marble

    print max(scores)
