from typing import Coroutine
import requests
from collections import defaultdict

# Make sure to check that the cookie is still valid
cookie = '<session ID here>'
headers = {'session': cookie}
day = 5  # Update the day as needed
url = f'https://adventofcode.com/2021/day/{day}/input'
session = requests.Session()
resp = session.get(url, cookies=headers)
# lines = resp.text.split('\n')
# lines.pop()

# Use this section for the sample input
lines = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
lines = lines.split('\n')
# Sample input --------------------------

counts = defaultdict(int)

for line in lines:
    start, end = line.split('->')
    x1, y1 = map(int, start.split(','))
    x2, y2 = map(int, end.split(','))

    if x1 == x2:
        y1, y2 = min(y1, y2), max(y1, y2)
        for i in range(y1, y2 + 1):
            coordinate = (x1, i)
            counts[coordinate] += 1
    elif y1 == y2:
        x1, x2 = min(x1, x2), max(x1, x2)
        for i in range(x1, x2 + 1):
            coordinate = (i, y1)
            counts[coordinate] += 1
    elif x1 <= x2 and y1 >= y2:  # left to right and down to up
        while x1 <= x2 and y1 >= y2:
            coordinate = (x1, y1)
            counts[coordinate] += 1
            x1 += 1
            y1 -= 1
    elif x1 >= x2 and y1 <= y2:  # right to left and up to down
        while x1 >= x2 and y1 <= y2:
            coordinate = (x1, y1)
            counts[coordinate] += 1
            x1 -= 1
            y1 += 1
    elif x1 <= x2 and y1 <= y2:  # left to right and up to down
        while x1 <= x2 and y1 <= y2:
            coordinate = (x1, y1)
            counts[coordinate] += 1
            x1 += 1
            y1 += 1
    else:
        while x1 >= x2 and y1 >= y2:  # right to left and down to up
            coordinate = (x1, y1)
            counts[coordinate] += 1
            x1 -= 1
            y1 -= 1

print(sum(1 if counts[key] >= 2 else 0 for key in counts))
