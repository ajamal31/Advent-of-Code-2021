import requests
from collections import defaultdict

# Make sure to check that the cookie is still valid
cookie = '53616c7465645f5f4852c18401ca934d9e2f5fc81011f8929d0adfa1f55408c117830a916fcb36e38722b641344548d3'
headers = {'session': cookie}
day = 6  # Update the day as needed
url = f'https://adventofcode.com/2021/day/{day}/input'
session = requests.Session()
resp = session.get(url, cookies=headers)
lines = resp.text
# lines.pop()

# Use this section for the sample input
# lines = """3,4,3,1,2"""
# lines = lines.split('\n')
# Sample input --------------------------

DAYS = 256

data = [*map(int, lines.split(','))]
counts = defaultdict(int, {key: 0 for key in range(9)})

for num in data:
    counts[num] += 1

for j in range(DAYS):
    cur_counts = list(counts.values())
    for i in range(0, 9):
        if i == 8:
            counts[8] = cur_counts[0]
        else:
            counts[i] = cur_counts[i + 1]
            if i == 6:
                counts[6] += cur_counts[0]

print(sum(counts.values()))
