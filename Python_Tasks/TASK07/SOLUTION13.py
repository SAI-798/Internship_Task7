
# Problem: Sherlock and the Valid String
# Link: https://www.hackerrank.com/challenges/sherlock-and-the-valid-string/problem

from collections import Counter

s = input()
freq = Counter(s)
values = list(freq.values())
counts = Counter(values)

if len(counts) == 1:
    print("YES")
elif len(counts) == 2:
    keys = list(counts.keys())
    a, b = keys[0], keys[1]

    if (a == 1 and counts[a] == 1) or (b == 1 and counts[b] == 1):
        print("YES")
    elif abs(a - b) == 1 and (counts[a] == 1 or counts[b] == 1):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
