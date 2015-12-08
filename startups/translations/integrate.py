import glob
import pandas as pd
import numpy as np

"""
all_data = pd.DataFrame()
for f in glob.glob("./*"):
    df = pd.read_csv(f)
    all_data = all_data.append(df,ignore_index=True)

print all_data.describe()
print all_data.head()
"""

# goes up to 155600169800
fout=open("out.csv","a")
# first file:
for line in open("05000.csv"):
    fout.write(line)
# now the rest:    
for num in range(0,11):
    f = open(str(num * 14200 + 13600)+str((num+1) * 14200 + 13600)+".csv")
    f.next() # skip the header
    for line in f:
         fout.write(line)
    f.close() # not really needed
fout.close()
