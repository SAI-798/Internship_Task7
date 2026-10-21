
# Problem: Separate the Numbers
# Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem

q = int(input())

for _ in range(q):
    s = input()
    found = False

    for i in range(1, len(s)):
        first = s[:i]
        num = int(first)
        current = first

        while len(current) < len(s):
            num += 1
            current += str(num)

        if current == s:
            print("YES", first)
            found = True
            break

    if not found:
        print("NO")
