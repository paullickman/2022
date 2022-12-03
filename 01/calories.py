class Calories():
    def __init__(self, file):
        f = open('01/' + file)
        lines = list(map(lambda x: x.strip(), f.readlines()))

        self.calList = []
        calories = []
        for line in lines:
            if line == '':
                self.calList.append(calories)
                calories = []
            else:
                calories.append(int(line))   
        self.calList.append(calories)

    def largest(self):
        return max(map(sum, self.calList))

    def sum3(self):
        return sum(sorted(map(sum, self.calList))[-3:])

## Part 1

c1 = Calories('test.txt')
assert c1.largest() == 24000

c2 = Calories('input.txt')
print(c2.largest())

## Part 2

assert c1.sum3() == 45000

print(c2.sum3())
