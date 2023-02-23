from sys import stdin
import re

index = {}

for line in stdin:
    word, loc = line.split('\t')

    index.setdefault(word, {})
    
    lnum, count = loc.split(',')

    index[word].setdefault(lnum, 0)
    index[word][lnum] += int(count)

for word in index:
    postings_list = ["%s:%d" % (lnum, index[word][lnum]) for lnum in
            index[word]]

    postings = ','.join(postings_list)
    print('%s\t%s' % (word, postings))

