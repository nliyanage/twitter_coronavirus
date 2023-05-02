#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
#1 - take top part of output list of top 10 values 
top10 = items[0:10]
#2 - get keys & values by indexing (item 0 is key, item 1 is value) 
keyslist = [item[0] for item in top10]
valueslist = [item[1] for item in top10]
#3 - reverse order of keys & values (we want small -> large) (reverse the list)
keyslist = keyslist[::-1]
print(range(len(keyslist)),"keyslist")
valueslist = valueslist[::-1]
print("valueslist", valueslist)
#4 - plot bar graph 
plt.bar(range(len(keyslist)), valueslist)
plt.xticks(range(len(keyslist)), keyslist)

print("hits")
print(args.key[1:] , 'args.key')
if args.input_path[-1] == 'g':
    plt.savefig(args.key[1:] + '_lang.png')
else:
    plt.savefig(args.key[1:] + '_country.png')
#add axis titles!!! 
