from vcd2df import *
from os import listdir

PATH = "../../vcds"

d = {}

for f in listdir(PATH):
    df = vcd2df(PATH + '/' + f)
    df = df[df.index.str.contains("shadow")]
    df = df[df.any(axis=1)]
    df = df.idxmax(axis=1)
    d[f] = df

print(d)
