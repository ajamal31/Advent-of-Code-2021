import os

current_dir = os.getcwd()
file_name = 'Day2Input.txt'

f = open(f'{current_dir}\\{file_name}')
lines = f.read().split('\n')
f.close()

h = d = a = 0

for line in lines:
    move, val = line.split()
    val = int(val)
    if move == 'forward':
        h += val
        d += a * val
    elif move == 'down': a += val
    else: a -= val

print(h * d)