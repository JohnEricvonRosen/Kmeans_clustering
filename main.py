# Machine Learning Spring 2019
# John Eric von Rosen
# Sahil Mehta
# 17 - 03 - 2019

import numpy as np
import random as rand

class kmeans:
    # NOTE: k = number of clusters
    # NOTE: tolerance = when to stop iterations
    # NOTE: max_iter = number of iterations max.
    def __init__(self, k = 3, tolerance = 0.0001, max_iter = 500):
        self.k = k
        self.tolerance = tolerance
        self.max_iter = max_iter
    
    def chunks(self, seq, num):
        avg = len(seq) / float(num)
        res = []

        last = 0.0
        while last < len(seq):
            res.append(seq[int(last):int(last + avg)])
            last += avg
        
        return res

    # NOTE: this is read and parse
    def readfile(self, filename):
        values = list()
        # array size = 240 
        with open(filename, "r") as f:
            for line in enumerate(f):
                if line[0] == 1:
                    break
                else:
                    values.append(line[1].split())
        self.np_array = np.array(values)
        
    

    def compute(self):
        flag = True
        while(flag):
            for k in range(0, self.k):
                sum_vector = np.zeros((240,), dtype=np.float64)
                for j in range(0, len())


def main():
    print("Hello")
    a = kmeans()
    a.readfile("DigitsBasicRoutines/mfeat-pix.txt")



if __name__ == '__main__':
    main()