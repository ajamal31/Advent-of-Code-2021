import requests
from collections import defaultdict

# Make sure to check that the cookie is still valid
cookie = '<session id here>'
headers = {'session': cookie}
day = 3  # Update the day as needed
url = f'https://adventofcode.com/2021/day/{day}/input'
session = requests.Session()
resp = session.get(url, cookies=headers)
lines = resp.text.split('\n')
lines.pop()

# Use this section for the sample input
# lines = """00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010"""
# lines = lines.split('\n')
# Sample input --------------------------

# Part 1
binaries = [''] * len(lines[0])

for line in lines:
    for i in range(len(binaries)):
        binaries[i] += line[i]

gamma = epsilon = ''

for binary in binaries:
    if binary.count('1') >= binary.count('0'):
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(f'Part 1: {int(gamma, 2) * int(epsilon , 2)}')

# Part 2 (refactor this if you have time)
temp = lines.copy()
i = 0
while len(temp) > 1:
    counts = defaultdict(int)

    for t in temp:
        counts[t[i]] += 1
    
    common_bit = '1' if counts['1'] >= counts['0'] else '0'
    new_list = [*filter(lambda x: x[i] == common_bit, temp)]
    temp = new_list.copy()
    i += 1

oxygen = int(temp[0], 2)

temp = lines.copy()
i = 0
while len(temp) > 1:
    counts = defaultdict(int)
    
    for t in temp:
        counts[t[i]] += 1
    
    common_bit = '0' if counts['1'] >= counts['0'] else '1'
    new_list = [*filter(lambda x: x[i] == common_bit, temp)]
    temp = new_list.copy()
    i += 1

carbon_dioxide = int(temp[0], 2)

print(f'Part 2: {oxygen * carbon_dioxide}')
