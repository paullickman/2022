import re
from functools import lru_cache

class Robot:
    def __init__(self, resource, oreCost, clayCost, obsidianCost):
        self.resource = resource
        self.oreCost = oreCost
        self.clayCost = clayCost
        self.obsidianCost = obsidianCost

class Blueprint:
    def __init__(self, id, oreRobotOreCost, clayRobotOreCost, obsidianRobotOreCost, obsidianRobotClayCost, geodeRobotOreCost, geodeRobotObsidianCost):
        self.id = id
        self.robots = {}
        self.robots['ore'] = Robot('ore', oreRobotOreCost, 0, 0)
        self.robots['clay'] = Robot('ore', clayRobotOreCost, 0, 0)
        self.robots['obsidian'] = Robot('ore', obsidianRobotOreCost, obsidianRobotClayCost, 0)
        self.robots['geode'] = Robot('ore', geodeRobotOreCost, 0, geodeRobotObsidianCost)

    @lru_cache
    def maxGeode(self, oreAmount, clayAmount, obsidianAmount, origOreRobots, origClayRobots, origObsidianRobots, timeRemaining):
        if timeRemaining == 1: # Not enough time to build any more geode robots
            return 0
        nextStates = [(oreAmount, clayAmount, obsidianAmount, origOreRobots, origClayRobots, origObsidianRobots, 0)]
        for robot in ['ore', 'clay', 'obsidian', 'geode']:
            newStates = []
            for state in nextStates:
                oreAmount, clayAmount, obsidianAmount, oreRobots, clayRobots, obsidianRobots, geodeRobots = state
                while self.robots[robot].oreCost <= oreAmount and self.robots[robot].clayCost <= clayAmount and self.robots[robot].obsidianCost <= obsidianAmount:
                    oreAmount -= self.robots[robot].oreCost
                    clayAmount -= self.robots[robot].clayCost
                    obsidianAmount -= self.robots[robot].obsidianCost
                    match robot:
                        case 'ore':
                            newStates.append((oreAmount, clayAmount, obsidianAmount, oreRobots+1, clayRobots, obsidianRobots, geodeRobots))
                        case 'clay':
                            newStates.append((oreAmount, clayAmount, obsidianAmount, oreRobots, clayRobots+1, obsidianRobots, geodeRobots))
                        case 'obsidian':
                            newStates.append((oreAmount, clayAmount, obsidianAmount, oreRobots, clayRobots, obsidianRobots+1, geodeRobots))
                        case 'geode':
                            newStates.append((oreAmount, clayAmount, obsidianAmount, oreRobots, clayRobots, obsidianRobots, geodeRobots+1))
            nextStates.extend(newStates)

        # Robots do mining
        nextStates = [(oreAmount+origOreRobots, clayAmount+origClayRobots, obsidianAmount+origObsidianRobots, oreRobots, clayRobots, obsidianRobots, geodeRobots) for oreAmount, clayAmount, obsidianAmount, oreRobots, clayRobots, obsidianRobots, geodeRobots in nextStates]

        timeRemaining -= 1
        # print(timeRemaining, nextStates)
        return max([state[6]*timeRemaining + self.maxGeode(state[0], state[1], state[2], state[3], state[4], state[5], timeRemaining) for state in nextStates])

class Blueprints:
    def __init__(self, file):
        self.blueprints = []
        for line in open('19/' + file).readlines():
            nums = list(map(int, re.findall(r'\d+', line)))
            self.blueprints.append(Blueprint(*nums))

b1 = Blueprints('test.txt')
print(b1.blueprints[0].maxGeode(0,0,0,1,0,0,19))