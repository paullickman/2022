from collections import namedtuple
from enum import Enum
from functools import cmp_to_key

Pair = namedtuple('Pair', 'left right')

class Result(Enum):
    ORDERED = -1
    SAME = 0
    UNORDERED = 1

def compare(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return Result.ORDERED
        elif left > right:
            return Result.UNORDERED
        else:
            return Result.SAME
    elif type(left) == list and type(right) == list:
        if left == []:
            if right == []:
                return Result.SAME
            else:
                return Result.ORDERED
        elif right == []:
            return Result.UNORDERED
        else:
            c = compare(left[0], right[0])
            if c in [Result.ORDERED, Result.UNORDERED]:
                return c
            else:
                return compare(left[1:], right[1:])
    elif type(left) == int and type(right) == list:
        return compare([left], right)
    elif type(left) == list and type(right) == int:
        return compare(left, [right])
    else:
        raise Exception('Unexpected location reached')

class Packets:
    def __init__(self, file):
        lines = [line.strip() for line in open('13/' + file).readlines()]

        self.pairs = []

        i = 0
        while i+1 < len(lines):
            self.pairs.append(Pair(eval(lines[i]), eval(lines[i+1])))

            i += 3

    def indexSum(self):
        sumIndex = 0
        for i in range(len(self.pairs)):
            if compare(self.pairs[i].left, self.pairs[i].right) == Result.ORDERED:
                sumIndex += (i+1)
        return sumIndex

    def decoderKey(self):
        divider1 = [[2]]
        divider2 = [[6]]

        packets = [p for packet in self.pairs for p in [packet.left, packet.right]] + [divider1] + [divider2]
        packets.sort(key=cmp_to_key(lambda item1, item2: compare(item1, item2).value))
        return (packets.index(divider1) + 1) * (packets.index(divider2) + 1)

# Part 1

p1 = Packets('test.txt')
assert p1.indexSum() == 13

p2 = Packets('input.txt')
print(p2.indexSum())

# Part 2

assert p1.decoderKey() == 140
print(p2.decoderKey())