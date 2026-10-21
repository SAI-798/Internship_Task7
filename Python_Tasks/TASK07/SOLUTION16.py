
# Problem: Caesar Cipher
# Link: https://www.hackerrank.com/challenges/caesar-cipher-1/problem

n = int(input())
s = input()
k = int(input())

k = k % 26
result = ""

for ch in s:
    if 'a' <= ch <= 'z':
        new_char = chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
        result += new_char
    elif 'A' <= ch <= 'Z':
        new_char = chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
        result += new_char
    else:
        result += ch

print(result)
