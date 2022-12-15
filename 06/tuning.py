from collections import Counter

def marker(chars, length=4):
    i = length
    while True:
        counter = Counter(chars[i-length:i])
        if len(counter) == length:
            return i
        i += 1

assert marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7
assert marker('bvwbjplbgvbhsrlpgdmjqwftvncz') ==  5
assert marker('nppdvjthqldpwncqszvftbrmjlhg') ==  6
assert marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') ==  10
assert marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') ==  11

## Part 1

chars = open('input.txt').readlines()[0]
print(marker(chars))

## Part 2

assert marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14) == 19
assert marker('bvwbjplbgvbhsrlpgdmjqwftvncz', 14) == 23
assert marker('nppdvjthqldpwncqszvftbrmjlhg', 14) == 23
assert marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14) == 29
assert marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14) == 26
print(marker(chars, 14))

