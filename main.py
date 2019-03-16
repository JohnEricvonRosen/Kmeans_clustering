# Machine Learning Spring 2019
# John Eric von Rosen
# Sahil Mehta
# 17 - 03 - 2019

import numpy as np
import random as rand
import itertools

class kmeans:
    # NOTE: k = number of clusters
    # NOTE: tolerance = when to stop iterations
    # NOTE: max_iter = number of iterations max.
    def __init__(self, k = 3, tolerance = 0.0001, max_iter = 500):
        self.k = k
        self.tolerance = tolerance
        self.max_iter = max_iter
        self.S = np.array([])
        self.avg = 0.0
    
    # NOTE: this is read and parse
    def readfile(self, filename, index):
        values = list()
        lower = index*200
        upper = index*200+200
        with open(filename, "r") as f:
            for line in itertools.islice(f, lower,upper):
                    values.append(line.split())
        self.np_array = np.array(values, dtype=np.float64)
    
    #NOTE: splits np_array into K sets    
    def chunks(self):
        self.S = np.split(self.np_array, indices_or_sections = self.k)

    def compare(self, s2):
        s1 = self.S
        for i in  range(0, self.k):
            s1[i].sort(key=np.linalg.norm)
            s2[i].sort(key=np.linalg.norm)
            if(len(s1[i]) != len(s2[i])):
                return False
            for j in range(0, len(s2[i])):
                if(not np.array_equal(s1[i][j], s2[i][j]))
                    return False
        return True

    #NOTE: computes means for all sets S
    def compute(self):
        iterations = 0
        min = 1000000.0
        while(flag):
            sMeans = []
            for k in range(0, self.k):
                sum_vector = np.zeros((240,), dtype=np.float64)
                for j in range(0, len(self.S[k])):
                    np.add(sum_vector, self.S[k][j], out=sum_vector, casting="unsafe")
                sum_vector = np.divide(sum_vector, len(self.S[k]))
                sMeans.append(sum_vector)

            #NOTE: Initialize S' and calc ||xi-uj||
            S = np.empty(self.k,200)
            for j in range(0,200):
                sMin = min
                index = 0
                for i in range(0, self.k):
                    distance = np.linalg.norm(self.np_array[i], sMeans[j]
                    if distance < sMin):
                        sMin = (distance)
                        index = j
                S[index].append(self.np_array[i])
        
        #NOTE: compare S and S'
        if self.S.compare(S):
            return self.S

        #NOTE: check if sets are empty
        check = 0
        while(check < self.k):
            if(len(S[check]) == 0):
                del S[check]
                self.k -= 1
            check += 1

        #NOTE: set S = S'
        for i in range(0, self.k):
            self.S = S[i]
            iterations += 1
        return S

def main():
    index = int(input("Input int [0-9]:"))
    k = int(input("Set K:"))
    tolerance = 0.0001
    max_iter = 500
    a = kmeans(k,tolerance,max_iter)
    a.readfile("DigitsBasicRoutines/mfeat-pix.txt", index)
    rand.shuffle(a.np_array)
    a.chunks()
    S = a.compute()


if __name__ == '__main__':
    main()