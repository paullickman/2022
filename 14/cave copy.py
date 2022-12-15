import re
from collections import namedtuple

Point = namedtuple('Point', 'x y')

class Cave:
    def __init__(self, file):
        self.paths = []
        for line in open('14/' + file).readlines():
            path = []
            for pair in re.findall(r'\d+,\d+', line):
                p = pair.split(',')
                path.append(Point(int(p[0]), int(p[1])))
            self.paths.append(path)

        Xs = [p.x for path in self.paths for p in path]            
        Ys = [p.y for path in self.paths for p in path]            

        self.depth = max(Ys)
        self.width = max(Xs)
        self.leftMargin = min(Xs)

        self.cave = [['.' for _ in range(self.width+2)] for _ in range(self.depth+2)]

        self.cave[0][500] = '+'

        # Draw paths

        for path in self.paths:
            start = path[0]
            for end in path[1:]:
                if start.x == end.x:
                    yMin = min(start.y, end.y)
                    yMax = max(start.y, end.y)
                    for j in range(yMin, yMax+1):
                        self.cave[j][start.x] = '#'
                else:
                    xMin = min(start.x, end.x)
                    xMax = max(start.x, end.x)
                    for i in range(xMin, xMax+1):
                        self.cave[start.y][i] = '#'
                start = end

    def draw(self):
        for row in self.cave:
            print(''.join(row[self.leftMargin-1:]))

    def drip(self):
        sand = Point(500,0)
        moved = True
        while moved:
            # Check if sand in freefall
            if sand.y >= self.depth:
                return False

            moved = False
            if self.cave[sand.y+1][sand.x] == '.':
                sand = Point(sand.x, sand.y+1)
                moved = True
            elif self.cave[sand.y+1][sand.x-1] == '.':
                sand = Point(sand.x-1, sand.y+1)
                moved = True
            elif self.cave[sand.y+1][sand.x+1] == '.':
                sand = Point(sand.x+1, sand.y+1)
                moved = True

        self.cave[sand.y][sand.x] = 'o'
        return True

    def count(self):
        num = 0
        while self.drip():
            num += 1
        return num

c1 = Cave('test.txt')
assert c1.count() == 24

c2 = Cave('input.txt')
print(c2.count())