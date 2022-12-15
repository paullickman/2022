class Program:
    def __init__(self, file):
        self.program = [line.strip().split(' ') for line in open('10/' + file).readlines()]

    def execute(self, draw=False):
        sumSignals = 0

        registerX = 1
        cycle = 0
        cycleRemaining = 0
        ip = -1
        while True:

            if cycleRemaining == 0:
                ip += 1
                if ip == len(self.program):
                    break
                match self.program[ip][0]:
                    case 'noop':
                        cycleRemaining = 0
                    case 'addx':
                        cycleRemaining = 1
                    case _:
                        error
            elif cycleRemaining == 1:
                match self.program[ip][0]:
                    case 'noop':
                        pass
                    case 'addx':
                        registerX += int(self.program[ip][1])
                    case _:
                        error
                cycleRemaining = 0
            else:
                cycleRemaining -= 1

            cycle += 1

            if cycle % 40 == 19:
                # print(cycle, registerX)
                sumSignals += (cycle+1) * registerX
            # print(cycle, registerX, ip, cycleRemaining)

            # Drawing routine
            if draw:
                if abs((cycle) % 40 - registerX) <= 1:
                    print('#', end='')
                else:
                    print(' ', end='')
                if cycle % 40 == 0:
                    print()

        return sumSignals

# Part 1

p1 = Program('test2.txt')
assert p1.execute() == 13140
p1.execute(True)

p2 = Program('input.txt')
print(p2.execute())
p2.execute(True)

# PRL fix displacement bug

# RKPJBPLA