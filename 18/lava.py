import collections

dirs = [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]

class Droplet():
    def __init__(self, file):
        self.maxSize = 0
        self.cubes = collections.defaultdict(bool)
        for line in open('18/' + file).readlines():
            parse = line.strip().split(',')
            cube = (int(parse[0]),int(parse[1]),int(parse[2]))
            self.cubes[cube] = True
            self.maxSize = max(self.maxSize, cube[0], cube[1], cube[2])

        # Increment so water can go all around the boulder
        self.maxSize += 2

        # Calculate the external cubes where the water would flow
        start = (0,0,0)
        assert self.cubes[start] == False
        self.external = collections.defaultdict(bool)
        self.external[start] = True
        horizon = set([start])
        while horizon:
            cube = horizon.pop()
            for i,j,k in dirs:
                neighbourCube = (cube[0]+i, cube[1]+j, cube[2]+k)
                if neighbourCube[0] >= 0 and neighbourCube[0] <= self.maxSize and neighbourCube[1] >= 0 and neighbourCube[1] <= self.maxSize and neighbourCube[2] >= 0 and neighbourCube[2] <= self.maxSize:
                    if not(self.external[neighbourCube]) and not(self.cubes[neighbourCube]):
                        self.external[neighbourCube] = True
                        horizon.add(neighbourCube)

    def surfaceArea(self):
        area = 0
        for cube in list(self.cubes.keys()):
            if self.cubes[cube]:
                for i,j,k in dirs:
                    neighbourCube = (cube[0]+i, cube[1]+j, cube[2]+k)
                    if not(self.cubes[neighbourCube]):
                        area += 1
        return area

    def externalSurfaceArea(self):
        area = 0
        for cube in list(self.cubes.keys()):
            if self.cubes[cube]:
                for i,j,k in dirs:
                    neighbourCube = (cube[0]+i, cube[1]+j, cube[2]+k)
                    if self.external[neighbourCube]:
                        area += 1
        return area

    def externalSurfaceArea2(self):
        area = 0
        for cube in list(self.external.keys()):
            if self.external[cube]:
                for i,j,k in dirs:
                    neighbourCube = (cube[0]+i, cube[1]+j, cube[2]+k)
                    if self.cubes[neighbourCube]:
                        area += 1
        return area

    def externalSurfaceArea3(self):
        internalArea = 0
        for x in range(self.maxSize):
            for y in range(self.maxSize):
                for z in range(self.maxSize):
                    cube = (x,y,z)
                    if not(self.external[cube]) and not (self.cubes[cube]):
                        # Cube is internal
                        for i,j,k in dirs:
                            neighbourCube = (cube[0]+i, cube[1]+j, cube[2]+k)
                            if self.cubes[neighbourCube]:
                                internalArea += 1
        return self.surfaceArea() - internalArea

# Part 1

d1 = Droplet('test1.txt')
assert d1.surfaceArea() == 10

d2 = Droplet('test2.txt')
assert d2.surfaceArea() == 64

d3 = Droplet('input.txt')
print(d3.surfaceArea())

# Part 2

assert d1.externalSurfaceArea() == 10

assert d2.externalSurfaceArea() == 58

print(d3.externalSurfaceArea())
print(d3.externalSurfaceArea2())
print(d3.externalSurfaceArea3())
