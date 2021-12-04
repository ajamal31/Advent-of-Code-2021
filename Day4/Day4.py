import requests
from collections import defaultdict

# Make sure to check that the cookie is still valid
cookie = '53616c7465645f5f4852c18401ca934d9e2f5fc81011f8929d0adfa1f55408c117830a916fcb36e38722b641344548d3'
headers = {'session': cookie}
day = 4  # Update the day as needed
url = f'https://adventofcode.com/2021/day/{day}/input'
session = requests.Session()
resp = session.get(url, cookies=headers)
lines = resp.text.split('\n')
lines.pop()

# Use this section for the sample input
# lines = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7"""
# lines = lines.split('\n')
# Sample input --------------------------

nums = lines.pop(0).split(',')
matrix = []

while '' in lines:
    lines.remove('')

for i in range(0, len(lines), 5):
    temp = [lines[i].split(), lines[i + 1].split(), lines[i + 2].split(), lines[i + 3].split(), lines[i + 4].split()]
    matrix.append(temp)

def column_checker(matrix, column):
    for i in range(len(matrix)):
        if matrix[i][column] != 'found':
            return False

    return True

winners = set()
def moves():
    for num in nums:
        for i in range(len(matrix)):
            if i not in winners:
                for j in range(len(matrix[i])):
                    for k in range(len(matrix[i][j])):
                        if matrix[i][j][k] == num:
                            matrix[i][j][k] = 'found'
                            if matrix[i][j].count('found') == 5 or column_checker(matrix[i], k):
                                winners.add(i)
                                return [int(num), i]

winning_num, b = moves()
s = 0

winning_board = matrix[b]

for row in winning_board:
    for num in row:
        if num != 'found':
            s += int(num)

print(f'Part 1: {winning_num * s}')

while len(winners) < len(matrix):
    winning_num, board_num = moves()

s = 0

winning_board = matrix[board_num]

for row in winning_board:
    for num in row:
        if num != 'found':
            s += int(num)

print(f'Part 2: {winning_num * s}')

