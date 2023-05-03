#import pandas as pd

#every key is a day
#every key of original dict has another dict nested under it
#for the nested dict, every key is a hashtag, value of that key is the number of tweets of that hashtag (of that day)

#dictionary w the dictionary nested under it is what we want alternate reduce to output 

'''
# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths',nargs='+',required=False)
parser.add_argument('--output_path',required=False)
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
directory = 'outputs'

# load each of the input paths
total = defaultdict(lambda: Counter())
'''

'''
for day in 'outputs/'
    with open(path) as f:
        tmp = json.load(f)
        for k in tmp:
            total[k] += tmp[k]

# write the output path
with open(args.output_path,'w') as f:
    f.write(json.dumps(total))
'''
'''
#loops thru every file in the outputs directory and prints the filename 
for filename in os.listdir(directory):
    if '.lang' in filename:
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            print(f)
'''

import matplotlib
import numpy as np
import json
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import argparse
from collections import Counter, defaultdict
from glob import glob

# command line args
parser = argparse.ArgumentParser()
parser.add_argument('--input_dir', required=True)
parser.add_argument('--keys', nargs='+', required=True)
args = parser.parse_args()

input_files = glob(args.input_dir + '/*')

for key in args.keys:
    yaxis = []
    total = defaultdict(lambda: Counter())

    for path in sorted(input_files):
        with open(path) as f:
            tmp = json.load(f)
            sumofnum = 0
            try:
                for k in tmp[key]:
                    sumofnum += tmp[key][k]
            except:
                pass
            yaxis.append(sumofnum)
    plt.plot(np.arange(len(yaxis)), yaxis, label=key)

plt.xlabel("Date in 2020")
plt.ylabel("# of Tweets")
plt.title("# of Tweets with a certain hashtag by each day in 2020")
plt.legend()
plt.xticks([0, 60, 121, 182, 244, 305], ["Jan", "Mar", "May", "Jul", "Sept", "Nov"])
plt.savefig("myplot4.png", bbox_inches="tight")
