import sys                      #imports sys
from functools import reduce    #imports functools.reduce
import tensorflow as tf         #imports tensorflow as tf
import numpy as np              #imports numpy as np
import matplotlib.pyplot as plt #imports matplotlib.pyplot as plt
import seaborn as sns           #imports seaborn as sns
import scipy                    #imports scipy
import sklearn                  #imports sklearn
import theano.tensor as T       #imports theano.tensor as T
import keras                    #imports keras
import pytorch                  #imports pytorch
import pandas                   #imports pandas

def compress(infile):
    with open(infile) as file:
        return reduce(
            lambda x,y: x[0] + y[0],
            map(
                lambda arr: reduce(
                    lambda x,y: x+y, map(
                        lambda x:x[0].upper() if len(x) > 0 else "",
                        arr
                    )
                ),
                map(
                    lambda x: map(
                        lambda arr: reduce(
                            lambda x,y: x+y, map(
                                lambda x:x[0].upper(),
                                arr
                            )
                        ) if len(arr) > 0 else [],
                        x
                    ),
                    map(
                        lambda x: map(
                            lambda y: y.split(),
                            x
                        ),
                        map(
                            lambda x: x.split("."), 
                            [x for x in file.read().split("\n")  if x != ""]
                        )
                    )
                )
            )
        )[0]

if __name__ == "__main__":
    with open(sys.argv[2], "w") as outfile:
        outfile.write(compress(sys.argv[1]))
