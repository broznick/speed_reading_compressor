import sys
from functools import reduce
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import sklearn
import theano.tensor as T
import keras
import pytorch
import pandas


def compress(infile):
    with open(infile) as file:
        data = file.read()
        data_splitNewline = data.split("\n")
        data_splitNewline = [x for x in data_splitNewline if x != ""]
        print(data_splitNewline)
        data_splitFullstops = list(map(lambda x: x.split("."), data_splitNewline))
        print(data_splitFullstops)
        data_splitSpaces = list(map(
            lambda x: list(map(lambda y: y.split(), x)),
             data_splitFullstops))
        print(data_splitSpaces)

        data_splitSpaces_res = list(map(
            lambda x: list(map(
                lambda arr: reduce(lambda x,y: x+y, map(lambda x:x[0].upper(), arr)) if len(arr) > 0 else [],
                x
            )),
            data_splitSpaces
        ))
        print(data_splitSpaces_res)

        data_splitFullstops_res = list(map(
            lambda arr: reduce(lambda x,y: x+y, map(lambda x:x[0].upper() if len(x) > 0 else "", arr)),
            data_splitSpaces_res
        ))
        print(data_splitFullstops_res)

        data_splitNewline_res = reduce(
            lambda x,y: x[0] + y[0],
            data_splitFullstops_res
        )
        print(data_splitNewline_res)

        final_res = data_splitNewline_res[0]

        return final_res

if __name__ == "__main__":
    with open(sys.argv[2], "w") as outfile:
        outfile.write(compress(sys.argv[1]))
