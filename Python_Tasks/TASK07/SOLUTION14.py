
# Problem: Anagram
# Link: https://www.hackerrank.com/challenges/anagram/problem

from collections import Counter

t = int(input())

for _ in range(t):
    s = input()
    n = len(s)

    if n % 2 != 0:
        print(-1)
    else:
        first = s[:n // 2]
        second = s[n // 2:]

        count1 = Counter(first)
        count2 = Counter(second)

        changes = 0

        for ch in count1:
            if count1[ch] > count2[ch]:
                changes += count1[ch] - count2[ch]

        print(changes)
