player1map = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
player2map = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}

lose = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}
win = {'Rock': 'Paper', 'Paper': 'Scissors', 'Scissors': 'Rock'}
           
points = {'Rock': 1, 'Paper': 2, 'Scissors': 3}

pointsLose = 0
pointsDraw = 3
pointsWin = 6

def calcScore(item1, item2):
    if item1 == item2:
        return pointsDraw # draw
    elif lose[item1] == item2:
        return pointsLose # loss
    else:
        return pointsWin # win

def score(round):
    return calcScore(player1map[round[0]], player2map[round[1]]) + points[player2map[round[1]]]

def score2(round):
    opponent = player1map[round[0]]
    match round[1]:
        case 'X':
            return points[lose[opponent]] + pointsLose
        case 'Y':
            return points[opponent] + pointsDraw
        case _:
            return points[win[opponent]] + pointsWin

class Tournament():

    def __init__(self, file):
        f = open('02/' + file)
        lines = f.readlines()
        self.guide = [line.strip().split(' ') for line in lines]

    def totalScore(self, s=score):
        return sum(map(s, self.guide))


## Part 1

t1 = Tournament('test.txt')
assert t1.totalScore() == 15

t2 = Tournament('input.txt')
print(t2.totalScore())

## Part 2
assert t1.totalScore(score2) == 12

print(t2.totalScore(score2))
