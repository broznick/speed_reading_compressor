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
        return file.read()[0]

if __name__ == "__main__":
    with open(sys.argv[2], "w") as outfile:
        outfile.write(compress(sys.argv[1]))