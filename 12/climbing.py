from collections import namedtuple

Point = namedtuple('Point', 'x y')

class Map:
    def __init__(self, file):
        self.grid = [line.strip() for line in open('12/' + file).readlines()]

        self.width = len(self.grid[0])
        self.height = len(self.grid)

        for j in range(self.height):
            for i in range(self.width):
                match self.grid[j][i]:
                    case 'S':
                        self.start = Point(i,j)
                    case 'E':
                        self.end = Point(i,j)

    def elevation(self, p):
        if self.grid[p.y][p.x] == 'S':
            return ord('a')
        if self.grid[p.y][p.x] == 'E':
            return ord('z')
        else:
            return ord(self.grid[p.y][p.x])

    def moveCriteria(self, current, next):
        return self.elevation(next) <= (self.elevation(current) + 1)

    def moveCriteria2(self, current, next):
        return self.elevation(next) >= (self.elevation(current) - 1)

    def possible(self, current, moveFunction):
        for u,v in [(0,1), (1,0), (-1,0), (0,-1)]:
            next = Point(current.x + u, current.y + v)
            if next.x >= 0 and next.x < self.width and next.y >=0 and next.y < self.height and moveFunction(current, next):
                yield next

    def goal(self, next):
        return next == self.end

    def goal2(self, next):
        return self.elevation(next) == ord('a')

    def search(self, begin, moveFunction, goalFunction):
        self.shortest = [[None] * self.width for _ in range(self.height)]

        frontier = {begin}
        self.shortest[begin.y][begin.x] = 0

        while True:
            newFrontier = set()
            for current in frontier:
                for next in self.possible(current, moveFunction):
                    nextShortest = self.shortest[current.y][current.x] + 1
                    if self.shortest[next.y][next.x] == None or self.shortest[next.y][next.x] > nextShortest:
                        if goalFunction(next):
                            return nextShortest
                        newFrontier.add(next)
                        self.shortest[next.y][next.x] = nextShortest
            frontier = newFrontier

# Part 1

m1 = Map('test.txt')
assert m1.search(m1.start, m1.moveCriteria, m1.goal) == 31

m2 = Map('input.txt')
print(m2.search(m2.start, m2.moveCriteria, m2.goal))

# Part 2

assert m1.search(m1.end, m1.moveCriteria2, m1.goal2) == 29
print(m2.search(m2.end, m2.moveCriteria2, m2.goal2))
