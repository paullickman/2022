rocks = [['####'], ['.#.', '###', '.#.'], ['###', '..#', '..#'], ['#', '#', '#', '#'], ['##', '##']]
jetDir = {'<': -1, '>': 1}
width = 7
gap = 3

class Flow():
    def __init__(self, file):
        self.jets = list(open('17/' + file).readline().strip())
        self.jetPointer = 0

        self.chamber = [[True] * width]
        self.currentHeight = 0
        self.nextRock = 0

    def draw(self):
        for line in self.chamber[::-1]:
            print('¦', end='')
            for b in line:
                if b:
                    print('#', end='')
                else:
                    print('.', end='')
            print('¦')
        print('+-------+')
        print()

    def extend(self):
        requiredGap = 4 + gap
        while len(self.chamber) < requiredGap or self.chamber[-requiredGap] != [False] * width:
            self.chamber.append([False] * width)

    def drop(self, numRocks):
        for _ in range(numRocks):
            self.extend()
            self.dropRock()
            self.nextRock = (self.nextRock + 1) % len(rocks)

    def incr(self):
        prevHeight = self.currentHeight
        self.extend()
        self.dropRock()
        self.nextRock = (self.nextRock + 1) % len(rocks)
        return self.currentHeight - prevHeight

    def dropRock(self):
        self.rockX = 2
        self.rockY = self.currentHeight + gap + 1
        #print(self.rockY)
        while True:
            # Lateral movement
            dir = (jetDir[self.jets[self.jetPointer]], 0)
            self.jetPointer = (self.jetPointer + 1) % len(self.jets)
            # print('Jet', self.jetPointer)
            if self.clear(dir):
                self.moveRock(dir)
            # Downward movement
            dir = (0, -1)
            if not(self.clear(dir)):
                break
            else:
                self.moveRock(dir)

        # Settle rock at final destination
        for j in range(len(rocks[self.nextRock])):
            for i in range(len(rocks[self.nextRock][j])):
                if rocks[self.nextRock][j][i] == '#':
                    assert self.chamber[self.rockY + j][self.rockX + i] == False
                    self.chamber[self.rockY + j][self.rockX + i] = True

        # Could be dropped below current height
        self.currentHeight = max(self.currentHeight, self.rockY + len(rocks[self.nextRock]) - 1)

    def clear(self, dir):
        for j in range(len(rocks[self.nextRock])):
            for i in range(len(rocks[self.nextRock][j])):
                if rocks[self.nextRock][j][i] == '#':
                    x = self.rockX + i + dir[0]
                    y = self.rockY + j + dir[1]
                    if x<0 or y<0 or x>=width or self.chamber[y][x] == True:
                        return False
        return True

    def height(self):
        return self.currentHeight

    def moveRock(self, dir):
        self.rockX += dir[0]
        self.rockY += dir[1]

    def searchPeriod(self):
        length = 1
        numIterations = 20
        maxNums = 100000
        start = 5000

        incrs = [self.incr() for _ in range(maxNums)]

        while True:
            s = sum(incrs[start:start+length])
            index = start
            i = numIterations
            while i > 0:
                index += length
                if sum(incrs[index:index+length]) != s:
                    break
                i -= 1
            if i == 0:
                return length, s
            length += 1

    def largeHeight(self, target):
        period, increment = self.searchPeriod()
        numLoops = target // period - 2
        initialRocks = target - numLoops * period
        height = sum([f1.incr() for _ in range(initialRocks)]) + numLoops * increment
        return height

# Part 1

f1 = Flow('test.txt')
f1.drop(2022)
assert f1.height() == 3068

f2 = Flow('input.txt')
f2.drop(2022)
print(f2.height())

# Part 2
target = 1000000000000

f1 = Flow('test.txt')
assert f1.largeHeight(target) == 1514285714286

f2 = Flow('input.txt')
print(f2.largeHeight(target))