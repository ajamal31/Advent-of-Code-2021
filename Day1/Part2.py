import os

current_dir = os.getcwd()
file_name = 'Part2Input.txt'

f = open(f'{current_dir}/Day1/{file_name}')
data = [*map(int, f.read().split())]
f.close()

windows = []
ans = 0

for i in range(len(data) - 2):
    cur = sum(data[i:i+3])
    ans += 1 if windows and cur > windows[-1] else 0
    windows.append(cur)

print(ans)
