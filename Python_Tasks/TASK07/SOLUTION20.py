
# Problem: Super Reduced String
# Link: https://www.hackerrank.com/challenges/reduced-string/problem

s = input()
result = []

for ch in s:
    if result and result[-1] == ch:
        result.pop()
    else:
        result.append(ch)

if len(result) == 0:
    print("Empty String")
else:
    print("".join(result))
