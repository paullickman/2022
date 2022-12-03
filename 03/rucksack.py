def priority(t):
    if t.islower():
        return ord(t) - ord('a') + 1
    else:
        return ord(t) - ord('A') + 27

def same(c1, c2):
    return [t for t in c1 if t in c2]

class Rucksack():
    def __init__(self, file):
        self.rucksacks = []
        self.items = []
        for line in open('03/' + file).readlines():
            line = line.strip()
            self.rucksacks.append(line)
            mid = len(line) // 2
            self.items.append((line[:mid],line[mid:]))

    def both(self):
        return sum(map(priority, [same(item[0], item[1])[0] for item in self.items]))

##  Chunk list into threes
    def common(self):
        total = 0
        i = 0
        while i < len(self.rucksacks):
            c = same(self.rucksacks[i], same(self.rucksacks[i+1], self.rucksacks[i+2]))[0]
            total += priority(c)
            i += 3
        return total
                   
## Part 1

r1 = Rucksack('test.txt')
assert r1.both() == 157

r2 = Rucksack('input.txt')
print(r2.both())

## Part 2

assert r1.common() == 70

print(r2.common())
