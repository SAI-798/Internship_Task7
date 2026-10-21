
# Problem: String Construction
# Link: https://www.hackerrank.com/challenges/string-construction/problem

t = int(input())

for _ in range(t):
    s = input()
    letters = set(s)

    print(len(letters))
