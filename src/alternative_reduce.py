import pandas as pd

#every key is a day
#every key of original dict has another dict nested under it
#for the nested dict, every key is a hashtag, value of that key is the number of tweets of that hashtag (of that day)

#dictionary w the dictionary nested under it is what we want alternate reduce to output 


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
for day in 'outputs/'
    with open(path) as f:
        tmp = json.load(f)
        for k in tmp:
            total[k] += tmp[k]

# write the output path
with open(args.output_path,'w') as f:
    f.write(json.dumps(total))
'''

#loops thru every file in the outputs directory and prints the filename 
for filename in os.listdir(directory):
    if '.lang' in filename:
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            print(f)
