import sys

for line in sys.stdin[1:]:
    words = line.strip().split()
    for word in words:
        print(f"{word}\t1)
