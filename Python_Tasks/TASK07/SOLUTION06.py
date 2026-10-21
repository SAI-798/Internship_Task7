
# Problem: Pangrams
# Link: https://www.hackerrank.com/challenges/pangrams/problem

s = input().lower()
letters = set()

for ch in s:
    if ch >= 'a' and ch <= 'z':
        letters.add(ch)

if len(letters) == 26:
    print("pangram")
else:
    print("not pangram")
