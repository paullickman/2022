import re

class Monkey:
    def __init__(self, items, operation, test, throwTrue, throwFalse):
        self.items = items
        self.operation = operation
        self.test = test
        self.throwTrue = throwTrue
        self.throwFalse = throwFalse
        self.count = 0

class Monkeys:
    def __init__(self, file):
        lines = [line.strip() for line in open('11/' + file).readlines()]

        self.monkeys = []
        self.divFactor = 1
        i = 0

        while i < len(lines):

            i += 1
            items = list(map(int, re.findall(r'\d+', lines[i])))
            i += 1
            operation  = lines[i].split('= ')[1]
            i += 1
            test  = int(re.search(r'\d+', lines[i])[0])
            i += 1
            throwTrue  = int(re.search(r'\d+', lines[i])[0])
            i += 1
            throwFalse  = int(re.search(r'\d+', lines[i])[0])
            self.monkeys.append(Monkey(items, operation, test, throwTrue, throwFalse))
            self.divFactor *= test
            i += 2

        self.counts = [0] * len(self.monkeys)

    def play(self, rounds, worry=True):
        turn = 0
        for i in range(rounds):
            for m in self.monkeys:
                for item in m.items:
                    old = item
                    new = eval(m.operation) % self.divFactor
                    #print(new)
                    if worry:
                        new //= 3
                    if new % m.test == 0:
                        self.monkeys[m.throwTrue].items.append(new)
                    else:
                        self.monkeys[m.throwFalse].items.append(new)
                    self.counts
                    m.count += 1
                m.items = []
            # print(i)
        counts = sorted([m.count for m in self.monkeys], reverse=True)
        return counts[0] * counts[1]

# Part 1

m1 = Monkeys('test.txt')
assert m1.play(20) == 10605

m2 = Monkeys('input.txt')
print(m2.play(20))

# Part 2

m1 = Monkeys('test.txt')
assert m1.play(10000, False) == 2713310158

m2 = Monkeys('input.txt')
print(m2.play(10000, False))