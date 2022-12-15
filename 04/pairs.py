import re

def contain(p1, p2):
    return (p1[0] <= p2[0]) and (p1[1] >= p2[1])

def within(x, p):
    return (x >= p[0]) and (x <= p[1])

def overlap(p1, p2):
    return within(p2[0], p1) or within(p2[1], p1)

class Pairs():
    def __init__(self, file):
        self.pairs = []
        for line in open('04/' + file).readlines():
            m = re.match(r'(\d+)-(\d+),(\d+)-(\d+)', line)
            self.pairs.append(((int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))))

    def num(self, f):
        return len(list(filter(lambda p: f(p[0],p[1]) or f(p[1],p[0]), self.pairs)))

## Part 1

p1 = Pairs('test.txt')
assert p1.num(contain) == 2

p2 = Pairs('input.txt')
print(p2.num(contain))

## Part 2

assert p1.num(overlap) == 4

print(p2.num(overlap))
