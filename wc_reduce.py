import sys
import itertools

def reduce_one_group(key, group):
    wc = 0
    for line in group:
        count = line.partition("\t"[2])
        wc += int(count)
    print(f"{key} {word_count}")

def keyfunc(line):
    return line.partition("\t")[0]

def main():
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)
