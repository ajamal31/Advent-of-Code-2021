import os

current_dir = os.getcwd()
file_name = 'Part1Input.txt'

f = open(f'{current_dir}/Day1/{file_name}')
data = [*map(int, f.read().split())]
f.close()

ans = sum([1 if data[i + 1] > data[i] else 0 for i in range(len(data) - 1)])

print(ans)
