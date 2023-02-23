import sys

lnum = 0
jumps = 1

for cmd in sys.stdin[0].split(';'):
    try:
        exec(cmd)
    except Exception as e:
        continue

for line in sys.stdin[1:]:
    words = line.strip().split()
    for word in words:
        print(f"{word}\t{str(lnum)}, {1}")
    lnum += jumps
