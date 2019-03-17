# Machine Learning Spring 2019
# John Eric von Rosen
# Sahil Mehta
# 17 - 03 - 2019

import numpy as np
import random as rand
import itertools
from matplotlib import pyplot as plt

class kmeans:
    # k = number of clusters
    def __init__(self, k = 3):
        self.k = k
    
    # this is read and parse
    def readfile(self, filename, index):
        values = list()
        lower = index*200
        upper = index*200+200
        with open(filename, "r") as f:
            for line in itertools.islice(f, lower,upper):
                    values.append(line.split())
        self.np_array = np.asarray(values, dtype=np.float64)
    
    #splits np_array into K sets    
    def chunks(self):
        self.S = []
        for i in range(0, self.k):
            self.S.append([])
        index = 0
        for chunk in np.array_split(self.np_array, indices_or_sections = self.k):
            for linechunk in chunk:
                self.S[index].append(linechunk)
            index += 1

    def compare(self, s2):
        s1 = self.S
        for i in  range(0, self.k):
            s1[i].sort(key=np.linalg.norm)
            s2[i].sort(key=np.linalg.norm)
            if(len(s1[i]) != len(s2[i])):
                return False
            for j in range(0, len(s2[i])):
                if(not np.array_equal(s1[i][j], s2[i][j])):
                    return False
        return True

    #computes means for all sets S
    def compute(self):
        min = 1000000.0
        while(True):
            sMeans = []
            for k in range(0, self.k):
                sum_vector = np.zeros((240,), dtype=np.float64)
                for j in range(0, len(self.S[k])):
                    np.add(sum_vector, self.S[k][j], out=sum_vector, casting="unsafe")
                sum_vector = np.divide(sum_vector, len(self.S[k]))
                sMeans.append(sum_vector)

            #Initialize S' and calc ||xi-uj||
            S = []
            for i in range(0, self.k):
                S.append([])
            for i in range(0,200):
                sMin = min
                index = 0
                for j in range(0, self.k):
                    distance = np.linalg.norm(self.np_array[i] - sMeans[j])
                    if distance < sMin:
                        sMin = (distance)
                        index = j
                x = self.np_array[i]
                S[index].append(x)
        
            #compare S and S'
            if self.compare(S):
                return sMeans

            #check if sets are empty
            check = 0
            while(check < self.k):
                if(len(S[check]) == 0):
                    del S[check]
                    self.k -= 1
                check += 1

            #set Sj = S'j
            for i in range(0, self.k):
                self.S[i] = S[i]
            return sMeans

def draw_graph(Sp, index, k):
    # 16 x 15 image
    reduced_dims = np.reshape(Sp[0], (16, 15))
    fig, ax = plt.subplots()
    ax.axis('off')
    ax.set_title("Input: %s\nK: %s" % (index, k))
    im = ax.imshow(reduced_dims, aspect="auto", extent=[0, 16, 0, 15], cmap=plt.cm.binary)
    plt.show()

def main():
    index = int(input("Input int [0-9]:"))
    k = int(input("Set K [>0]:"))
    a = kmeans(k)

    #Initialization
    a.readfile("DigitsBasicRoutines/mfeat-pix.txt", index)
    rand.shuffle(a.np_array)
    a.chunks()

    # Repitions. codbook: sMeans array
    codebook = a.compute()

    #Visualize results
    draw_graph(codebook, index, a.k)

if __name__ == '__main__':
    main()