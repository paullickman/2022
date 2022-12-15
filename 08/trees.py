class Trees:

    def __init__(self, file):
        self.grid = list(line.strip() for line in open('08/' + file).readlines())
        self.width = len(self.grid[0])
        self.height = len(self.grid)

    def visible(self, x, y):
        h = self.grid[y][x]
        # Left 
        if all(self.grid[y][i] < h for i in range(0, x)):
            return True
        # Right
        if all(self.grid[y][i] < h for i in range(x+1, self.width)):
            return True
        # Up 
        if all(self.grid[j][x] < h for j in range(0, y)):
            return True
        # Down
        if all(self.grid[j][x] < h for j in range(y+1, self.height)):
            return True
        return False

    def numVisible(self):
        total = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.visible(x,y):
                    total += 1
        return total

    def scenic(self, x, y):
        h = self.grid[y][x]
        score = 1
        for d in [(-1,0), (1,0), (0,-1), (0,1)]:
            i = x + d[0]
            j = y + d[1]
            lineScore = 0
            while (i>=0) and (i<self.width) and (j>=0) and (j<self.height):
                lineScore += 1

                if self.grid[j][i] >= h:
                    break

                i += d[0]
                j += d[1]

            score *= lineScore

        return score

    def maxScenic(self):
        return max(self.scenic(x,y) for x in range(self.width) for y in range(self.height))

# Part 1

t1 = Trees('test.txt')
assert t1.numVisible() == 21

t2 = Trees('input.txt')
print(t2.numVisible())

# Part 2

assert t1.maxScenic() == 8

print(t2.maxScenic())