from collections import namedtuple

Motion = namedtuple('Motion', 'direction steps')
Point = namedtuple('Point', 'x y')

dirs = {'R': (1,0), 'L': (-1,0), 'D': (0,-1), 'U': (0,1)}

def sign(n):
    if n>0:
        return 1
    elif n<0:
        return -1
    return 0

class Motions:
    def __init__(self, file, length):
        lines = [line.strip().split() for line in open('09/' + file).readlines()]
        motions = [Motion(words[0], int(words[1])) for words in lines]

        self.rope = [Point(0,0) for _ in range(length)]
        self.tailVisited = set()

        for motion in motions:
            for _ in range(motion.steps):
                self.moveHead(motion.direction)
                for i in range(1, length):
                    self.moveTail(i)
                self.tailVisited.add(self.rope[-1])        
                # print(motion.direction, motion.steps, self.head, self.tail)

    def tailPositions(self):
        return len(self.tailVisited)

    def moveHead(self, dir):
        self.rope[0] = Point(self.rope[0].x + dirs[dir][0], self.rope[0].y + dirs[dir][1])

    def moveTail(self, i):
        diffX = self.rope[i-1].x - self.rope[i].x
        diffY = self.rope[i-1].y - self.rope[i].y

        # Check if the head is two steps directly up, down from the tail
        if (diffX == 0) and abs(diffY) == 2:
            self.rope[i] = Point(self.rope[i].x, self.rope[i].y + sign(diffY))
        # Check if the head is two steps directly left, or right from the tail
        elif (abs(diffX) == 2) and diffY == 0:
            self.rope[i] = Point(self.rope[i].x + sign(diffX), self.rope[i].y)
        else:
        # Check if the head and tail aren't touching and aren't in the same row or column
            if ((abs(diffX) >= 1) and (abs(diffY) >= 2)) or ((abs(diffX) >= 2) and (abs(diffY) >= 1)):
                self.rope[i] = Point(self.rope[i].x + sign(diffX), self.rope[i].y + sign(diffY))

# Part 1

m1 = Motions('test.txt', 2)
assert m1.tailPositions() == 13

m2 = Motions('input.txt', 2)
print(m2.tailPositions())

# Part 2

m1 = Motions('test.txt', 10)
assert m1.tailPositions() == 1

m2 = Motions('test2.txt', 10)
assert m2.tailPositions() == 36

m3 = Motions('input.txt', 10)
print(m3.tailPositions())
