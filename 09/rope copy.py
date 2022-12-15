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

# class Motions:
#     def __init__(self, file):
#         lines = [line.strip().split() for line in open('09/' + file).readlines()]
#         motions = [Motion(words[0], int(words[1])) for words in lines]

#         self.head = Point(0,0)
#         self.tail = Point(0,0)
#         self.tailVisited = set()

#         for motion in motions:
#             for _ in range(motion.steps):
#                 self.moveHead(motion.direction)
#                 self.moveTail()
#                 self.tailVisited.add(self.tail)        
#                 # print(motion.direction, motion.steps, self.head, self.tail)

        
#     def tailPositions(self):
#         return len(self.tailVisited)

#     def moveHead(self, dir):
#         self.head = Point(self.head.x + dirs[dir][0], self.head.y + dirs[dir][1])

#     def moveTail(self):
#         diffX = self.head.x - self.tail.x
#         diffY = self.head.y - self.tail.y

#         # Check if the head is two steps directly up, down from the tail
#         if (diffX == 0) and abs(diffY) == 2:
#             self.tail = Point(self.tail.x, self.tail.y + sign(diffY))
#         # Check if the head is two steps directly left, or right from the tail
#         elif (abs(diffX) == 2) and diffY == 0:
#             self.tail = Point(self.tail.x + sign(diffX), self.tail.y)
#         else:
#         # Check if the head and tail aren't touching and aren't in the same row or column
#             if ((abs(diffX) >= 1) and (abs(diffY) >= 2)) or ((abs(diffX) >= 2) and (abs(diffY) >= 1)):
#                 self.tail = Point(self.tail.x + sign(diffX), self.tail.y + sign(diffY))

class Motions2:
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

# m1 = Motions('test.txt')
# assert m1.tailPositions() == 13

# m2 = Motions('input.txt')
# print(m2.tailPositions())

# Part 2

m1 = Motions2('test.txt', 10)
print(m1.tailPositions())

m2 = Motions2('test2.txt', 10)
print(m2.tailPositions())

m3 = Motions2('input.txt', 10)
print(m3.tailPositions())
