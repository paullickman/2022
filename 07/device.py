from collections import namedtuple

File = namedtuple("File","size filename")

class Filesystem:
    def __init__(self):
        self.parent = None
        self.name = None
        self.subfolders = {}
        self.files = []
        self.totalSize = 0

class Device:
    def __init__(self, file):
        terminal = [line.strip().split(' ') for line in open('07/' + file).readlines()]

        # Parse terminal

        self.rootFolder = None
        currentFolder = self.rootFolder

        for line in terminal:
            if line[0] == '$':
                if line[1] == 'cd':
                    if line[2] == '/':
                        self.rootFolder = Filesystem()
                        currentFolder = self.rootFolder
                        currentFolder.name = '/'
                    elif line[2] == '..':
                        currentFolder = currentFolder.parent
                    else:
                        currentFolder = currentFolder.subfolders[line[2]]
                elif line[1] == 'ls':
                    pass
            elif line[0] == 'dir':
                if line[1] not in currentFolder.subfolders.keys():
                    newFolder = Filesystem()
                    newFolder.parent = currentFolder
                    newFolder.name = line[1]
                    currentFolder.subfolders[line[1]] = newFolder
            else:
                newFile = File(int(line[0]), line[1])
                currentFolder.files.append(newFile)

    def dirSum(self):
        return sum([n for n in calcSizes(self.rootFolder) if n<=100000])

    def smallest(self):
        extraRequiredSpace = spaceRequired - (totalSpace - self.rootFolder.totalSize)
        return min([s for s in calcSizes(self.rootFolder) if s >= extraRequiredSpace])

def calcSizes(folder):
    folder.totalSize = sum(f.size for f in folder.files)
    for f in folder.subfolders.values():
        for s in calcSizes(f):
            yield s
        folder.totalSize += f.totalSize
    yield folder.totalSize

#  Part 1

d1 = Device('test.txt')
assert d1.dirSum() == 95437

d2 = Device('input.txt')
print(d2.dirSum())

#  Part 2

totalSpace = 70000000
spaceRequired = 30000000

assert d1.smallest() == 24933642

print(d2.smallest())