
# Problem: Beautiful Binary String
# Link: https://www.hackerrank.com/challenges/beautiful-binary-string/problem

n = int(input())
s = input()
count = 0

for i in range(len(s) - 2):
    if s[i:i + 3] == "010":
        count += 1

print(count)
