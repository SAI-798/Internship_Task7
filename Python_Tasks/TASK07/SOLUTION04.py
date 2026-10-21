
# Problem: Funny String
# Link: https://www.hackerrank.com/challenges/funny-string/problem

t = int(input())

for _ in range(t):
    s = input()
    r = s[::-1]
    funny = True

    for i in range(1, len(s)):
        a = abs(ord(s[i]) - ord(s[i - 1]))
        b = abs(ord(r[i]) - ord(r[i - 1]))

        if a != b:
            funny = False
            break

    if funny:
        print("Funny")
    else:
        print("Not Funny")
