
# Problem: Gemstones
# Link: https://www.hackerrank.com/challenges/gem-stones/problem

n = int(input())
common = set(input().strip())

for i in range(n - 1):
    rock = set(input().strip())
    common = common.intersection(rock)

print(len(common))
