# Move entry at position a to position b
def insert(nums, a, b):
    if a < b:
        return nums[:a] + nums[a+1:b+1] + [nums[a]] + nums[b+1:]
    elif b < a:
        return nums[:b] + [nums[a]] + nums[b:a] + nums[a+1:]
    else:
        return nums

assert insert([1,2,3,4,5], 2, 2) == [1,2,3,4,5]
assert insert([1,2,3,4,5], 2, 3) == [1,2,4,3,5]
assert insert([1,2,3,4,5], 2, 1) == [1,3,2,4,5]
assert insert([1,2,3,4,5], 2, 0) == [3,1,2,4,5]
assert insert([1,2,3,4,5], 2, 4) == [1,2,4,5,3]

# Adjust positional pointers for a moving to b
# positions[i] is the current location of the original i-th number
def adjust(positions, a, b):

    if a < b:
        for i in range(len(positions)):
            if positions[i] >= a+1 and positions[i] <= b:
                positions[i] -= 1
            elif positions[i] == a:
                positions[i] = b
    elif b < a:
        for i in range(len(positions)):
            if positions[i] >= b and positions[i] < a:
                positions[i] += 1
            elif positions[i] == a:
                positions[i] = b
    return positions

class Grove:
    def __init__(self, file):
        self.nums = list(map(int, open('20/' + file).readlines()))
        self.length = len(self.nums)

    def mix(self):
        nextNums = list(range(self.length))
        for i in range(self.length):
            nextNum = nextNums[i]

            insertPoint = nextNum + self.nums[nextNum]
            if insertPoint < 0:
                insertPoint -= 1
            elif insertPoint >= self.length:
                insertPoint += 1
            insertPoint = (insertPoint + self.length) % self.length
            self.nums = insert(self.nums, nextNum, insertPoint)
            nextNums = adjust(nextNums, nextNum, insertPoint)

            # nums2 = []
            # for j in range(self.length):
            #     pos = nextNums.index(j)
            #     nums2.append(self.nums[pos])
            # print(self.nums, nums2, nextNums)

    def pos(self, n):
        return self.nums[(self.nums.index(0) + n) % self.length]

    def coordSum(self):
        return self.pos(1000) + self.pos(2000) + self.pos(3000)

g1 = Grove('test.txt')
g1.mix()
print(g1.coordSum())

g2 = Grove('input.txt')
g2.mix()
print(g2.coordSum())
# 3644 too low