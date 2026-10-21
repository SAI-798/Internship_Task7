
# Problem: Weighted Uniform Strings
# Link: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

s = input()
n = int(input())
queries = []

for _ in range(n):
    queries.append(int(input()))

weights = set()
previous = ""
count = 0

for ch in s:
    weight = ord(ch) - ord('a') + 1

    if ch == previous:
        count += weight
    else:
        count = weight

    weights.add(count)
    previous = ch

for q in queries:
    if q in weights:
        print("Yes")
    else:
        print("No")
