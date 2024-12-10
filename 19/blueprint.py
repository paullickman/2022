import re
from functools import lru_cache
from collections import defaultdict
import math

elements = ['ore', 'clay', 'obsidian', 'geode']

class Blueprint:
    def __init__(self, id, oreRobotOreCost, clayRobotOreCost, obsidianRobotOreCost, obsidianRobotClayCost, geodeRobotOreCost, geodeRobotObsidianCost):
        self.id = id
        self.robotCosts = {}
        self.robotCosts['ore'] = defaultdict(int, {"ore": oreRobotOreCost})
        self.robotCosts['clay'] = defaultdict(int, {"ore": clayRobotOreCost})
        self.robotCosts['obsidian'] = defaultdict(int, {"ore": obsidianRobotOreCost, "clay": obsidianRobotClayCost})
        self.robotCosts['geode'] = defaultdict(int, {"ore": geodeRobotOreCost, "obsidian": geodeRobotObsidianCost})

    # Calcuate max possible number of geodes that could be produced
    def potential(self, robotsCount, materials, time):
        additionalRobots = defaultdict(int)
        potentialMaterials = defaultdict(int, materials)
        for _ in range(time):
            for robotType in elements:
                potentialMaterials[robotType] += robotsCount[robotType] + additionalRobots[robotType]
            for robotType in elements:
                if all(potentialMaterials[material] >= self.robotCosts[robotType][material] * (additionalRobots[robotType] + 1) for material in elements):
                    additionalRobots[robotType] += 1
        return potentialMaterials["geode"]

    def maxGeode(self, timeRemaining):

        # Calculate the most required elements across the whole blueprint
        # maxValues = {}
        # for robotType in elements:
        #     for material in elements:
        #         if amount := self.robotCosts[robotType][material] > 0:
        #             if material in maxValues.keys():
        #                 if maxValues[material] < amount:
        #                     maxValues[material] = amount
        #             else:
        #                 maxValues[material] = amount

        maxFound = 0
        # Start with one ore robot
        queue = [(defaultdict(int, {"ore": 1}), defaultdict(int), timeRemaining)]
        while queue:
            robotsCount, materials, time = queue.pop()

            # Prune search tree by only continuing if there's potential to exceed current max
            if self.potential(robotsCount, materials, time) < maxFound:
                continue

            # Look ahead to see what could be minimally produced
            minEstimate = materials['geode'] + robotsCount['geode'] * time
            if minEstimate > maxFound:
                maxFound = minEstimate

            for robotType in elements:

                # Check if there's an excess of robots so we can skip as they won't limit production
                # if robotType in maxValues.keys():
                #     if robotsCount[robotType] > maxValues[robotType]:
                #         continue

                # Determine time increment to create next robot
                # Optimisation to avoid having to step through time one minute each go
                timeIncrement = 0
                for material in elements:
                    if self.robotCosts[robotType][material] > 0:
                        materialRequirement = self.robotCosts[robotType][material] - materials[material]
                        if materialRequirement > 0:
                            if robotsCount[material] == 0:
                                # Not able to produce the required element
                                timeIncrement = math.inf
                            else:
                                timeRequired = ((materialRequirement - 1) // robotsCount[material]) + 1
                                # print(material, materialRequirement, robotsCount[material], timeRequired)
                                if timeIncrement < timeRequired:
                                    timeIncrement = timeRequired

                if (timeIncrement >= 0) and (timeIncrement < time):
                    nextRobotsCount = defaultdict(int, robotsCount)
                    # Create the new robot
                    nextRobotsCount[robotType] += 1
                    nextMaterials = defaultdict(int, materials)
                    # Increment elements due to all robots producing
                    for material in elements:
                        nextMaterials[material] += robotsCount[material] * (timeIncrement + 1)
                    # Reduce elements due to creation of new robot
                    for material in elements:
                        nextMaterials[material] -= self.robotCosts[robotType][material]
                    queue.append((nextRobotsCount, nextMaterials, time - timeIncrement - 1))

        # print(maxFound)
        return maxFound

class Blueprints:
    def __init__(self, file):
        self.blueprints = []
        for line in open('19/' + file).readlines():
            nums = list(map(int, re.findall(r'\d+', line)))
            self.blueprints.append(Blueprint(*nums))

    def sumQuality(self):
        return sum((i+1) * self.blueprints[i].maxGeode(24) for i in range(len(self.blueprints)))

    def prod(self):
        return math.prod(self.blueprints[i].maxGeode(32) for i in range(min(len(self.blueprints),3)))

b1 = Blueprints('test.txt')
assert b1.sumQuality() == 33
assert b1.prod() == 3472

b2 = Blueprints('input.txt')
print(b2.sumQuality()) # 1599
print(b2.prod()) # 14112