from collections import namedtuple
import re

class Stacks():
    def __init__(self, filename):
        lines = open(filename).readlines()

        gap = lines.index('\n')
        self.numStacks = int(lines[gap-1].strip().split(' ')[-1])
        
        self.stacks = [[] for _ in range(self.numStacks)]

        for row in range(gap-2, -1, -1):
            for stack in range(self.numStacks):
                col = stack*4+1
                if col < len(lines[row]):
                    c = lines[row][col]
                    if c.isalpha():
                        self.stacks[stack].append(lines[row][col])

        Move = namedtuple("Move", "numCrates fromStack toStack")
        self.moves = []
        for line in lines[gap+1:]:
            nums = re.findall(r'\d+', line)
            self.moves.append((Move(int(nums[0]), int(nums[1]), int(nums[2]))))
            

    def process(self, move):
        for _ in range(move.numCrates):
            self.stacks[move.toStack-1].append(self.stacks[move.fromStack-1].pop())

    def process2(self, move):
        self.stacks[move.toStack-1].extend(self.stacks[move.fromStack-1][-move.numCrates:])
        self.stacks[move.fromStack-1] = self.stacks[move.fromStack-1][:-move.numCrates]

    def run(self):
        for move in self.moves:
            self.process(move)

    def run2(self):
        for move in self.moves:
            self.process2(move)

    def message(self):
        return ''.join(s[-1] for s in self.stacks)

## Part 1

s1 = Stacks('test.txt')
s1.run()
assert s1.message() == 'CMZ'

s2 = Stacks('input.txt')
s2.run()
print(s2.message())

## Part 2

s1 = Stacks('test.txt')
s1.run2()
assert s1.message() == 'MCD'

s2 = Stacks('input.txt')
s2.run2()
print(s2.message())
