from collections import namedtuple

Valve = namedtuple('Valve', 'name rate tunnels')

State = namedtuple('State', 'locations timeRemaining closedValves score')

class Scan():
    def __init__(self, file):
        self.valves = {}
        self.closedValves = []
        for line in open('16/' + file).readlines():
            text = line.strip().split(' ')
            valve = text[1]
            flow = int(text[4].split('=')[1][:-1])
            tunnels = [t[:2] for t in text[9:]]
            self.valves[valve] = Valve(valve, flow, tunnels)
            if flow > 0:
                self.closedValves.append(valve)

    def maxPressure(self, numLocations, initialTime):
        start = State(['AA'] * numLocations, initialTime, self.closedValves, 0)
        return self.search(start)

    def calcMoves(self, baseState):
        if baseState.closedValves == [] or baseState.timeRemaining == 0:
            return []
        else:
            nextStates = [State([], baseState.timeRemaining, baseState.closedValves, baseState.score)]

            for location in baseState.locations:
                newNextStates = []

                for nextState in nextStates:

                    # See if we can open a valve
                    if location in nextState.closedValves:
                        newClosedValves = [v for v in nextState.closedValves if v != location]
                        scoreIncrement = (nextState.timeRemaining-1) * self.valves[location].rate
                        newNextStates.append(State(nextState.locations + [location], nextState.timeRemaining, newClosedValves, nextState.score + scoreIncrement))

                    for nextLocation in self.valves[location].tunnels:
                        newNextStates.append(State(nextState.locations + [nextLocation], nextState.timeRemaining, nextState.closedValves, nextState.score))

                nextStates = newNextStates

            return [State(s.locations, baseState.timeRemaining-1, s.closedValves, s.score) for s in nextStates]

    def maxPossible(self, state):
        # Calculate maximum possible remaining score
        # Used for pruning the search tree
        return sum([self.valves[v].rate * (state.timeRemaining-1) for v in state.closedValves])

    def search(self, state):
        maxScore = 0
        states = [state]
        bestPressures = {}
        while states:
            newStates = []
            for state in states:
                for newState in self.calcMoves(state):
                    key = ''.join(newState.locations) + ''.join(newState.closedValves)
                    if key not in bestPressures.keys() or bestPressures[key] < newState.score:
                        bestPressures[key] = newState.score
                        if newState.score > maxScore:
                            maxScore = newState.score

                        # Only add to search if possible to exceed current max score
                        if newState.score + self.maxPossible(newState) > maxScore:
                            newStates.append(newState)
            states = newStates
        return maxScore

# Part 1
s1 = Scan('test.txt')
assert s1.maxPressure(1, 30) == 1651

s2 = Scan('input.txt')
print(s2.maxPressure(1, 30))

# Part 2
assert s1.maxPressure(2, 26) == 1707
print(s2.maxPressure(2, 26))