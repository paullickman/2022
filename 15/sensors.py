import re
from collections import namedtuple

Point = namedtuple('Point', 'x y')
Sensor = namedtuple('Sensor', 'location closest distance')

def dist(p1, p2):
    return abs(p1.x-p2.x) + abs(p1.y-p2.y)

def remove(delRange, ranges):
    newRanges = []
    for range in ranges:
        if delRange[0]<=range[0] and delRange[1]>=range[1]:
            pass
        elif delRange[1] < range[0]:
            newRanges.append(range)
        elif delRange[0] <= range[0] and delRange[1] < range[1]:
            newRanges.append((delRange[1]+1, range[1]))
        elif delRange[0]>range[0] and delRange[1]<range[1]:
            newRanges.append((range[0], delRange[0]-1))
            newRanges.append((delRange[1]+1, range[1]))
        elif delRange[0]<=range[1] and delRange[1]>=range[1]:
            newRanges.append((range[0], delRange[0]-1))
        elif delRange[0]>range[1]:
            newRanges.append(range)
        else:
            raise Exception('Unhandled case:', delRange, range)
    return newRanges       

assert remove((0,10), [(20,50)]) == [(20,50)]
assert remove((10,30), [(20,50)]) == [(31,50)]
assert remove((30,40), [(20,50)]) == [(20,29), (41,50)]
assert remove((40,60), [(20,50)]) == [(20,39)]
assert remove((60,70), [(20,50)]) == [(20,50)]
assert remove((0,70), [(20,50)]) == []

class Sensors:
    def __init__(self, file):

        self.sensors = []
        self.beacons = set()
        for line in open('15/' + file).readlines():
            nums = re.findall(r'-?\d+', line)
            location = Point(int(nums[0]), int(nums[1]))
            closest = Point(int(nums[2]), int(nums[3]))
            self.sensors.append(Sensor(location, closest, dist(location, closest)))
            self.beacons.add(closest)

        self.minX = min(s.location.x - s.distance for s in self.sensors)
        self.maxX = max(s.location.x + s.distance for s in self.sensors)

    def inside(self, point):
        for sensor in self.sensors:
            if dist(point, sensor.location) <= sensor.distance:
                return True
        return False

    def rowCount(self, row):

        # Count how many beacons already in row
        numBeacons = len(list(filter(lambda b: b.y == row, self.beacons)))

        # PRL first just naive 1 cell at a time (then skip) i.e. use part 2 optimisation
        count = 0
        for x in range(self.minX, self.maxX+1):
            if self.inside(Point(x, row)):
                count += 1
        return count - numBeacons

    def locate(self, size):
        for y in range(size+1):
            ranges = [(0,size)]
            for sensor in self.sensors:
                yDiff = abs(y - sensor.location.y)
                if yDiff <= sensor.distance:
                    delRange = (sensor.location.x - (sensor.distance - yDiff), sensor.location.x + (sensor.distance - yDiff))
                    ranges = remove(delRange, ranges)
            if len(ranges) > 0:
                return 4000000*ranges[0][0] + y

# Part 1

s1 = Sensors('test.txt')
assert s1.rowCount(10) == 26

s2 = Sensors('input.txt')
print(s2.rowCount(2000000))

# Part 2

assert s1.locate(20) == 56000011

print(s2.locate(4000000))