
# Problem: Two Strings
# Link: https://www.hackerrank.com/challenges/two-strings/problem

p = int(input())

for _ in range(p):
    s1 = input()
    s2 = input()

    if set(s1) & set(s2):
        print("YES")
    else:
        print("NO")
