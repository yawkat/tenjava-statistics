#!/usr/bin/env python

# example usage: ./compare.py Java code [reverse]

import sys
import json

with open("cloc.json") as f:
    total = json.load(f)

lang = sys.argv[1]
categ = sys.argv[2]

final = {}

for k in total:
    e = total[k]
    if not lang in e:
        continue
    final[k] = e[lang][categ]

if len(sys.argv) > 3 and sys.argv[3] == "reverse":
    mul = -1
else:
    mul = 1

for e in sorted(final.iteritems(), key=(lambda tup: mul * tup[1])):
    print e[0] + "\t" + str(e[1])
