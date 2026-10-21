
# Problem: Game of Thrones - I
# Link: https://www.hackerrank.com/challenges/game-of-thrones/problem

from collections import Counter

s = input()
freq = Counter(s)
odd = 0

for value in freq.values():
    if value % 2 != 0:
        odd += 1

if odd <= 1:
    print("YES")
else:
    print("NO")
