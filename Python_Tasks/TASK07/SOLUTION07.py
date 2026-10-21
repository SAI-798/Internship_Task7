
# Problem: Alphabet Rangoli
# Link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    letters = "abcdefghijklmnopqrstuvwxyz"
    lines = []

    for i in range(size):
        left = letters[size - 1:size - i - 1:-1]
        right = letters[size - i - 1:size]
        row = "-".join(left + right)
        lines.append(row.center(4 * size - 3, "-"))

    for i in range(size - 2, -1, -1):
        lines.append(lines[i])

    print("\n".join(lines))

n = int(input())
print_rangoli(n)
