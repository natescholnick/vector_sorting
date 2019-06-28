# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 23:23:37 2019

@author: Nate
"""

import numpy as np

def generateVectors(number, dimensions, scale=1):
    vectorSet = np.random.rand(number, dimensions)*scale
    return vectorSet

def calculateMagnitudes(vectors):
    magnitudes = np.zeros(np.size(vectors,0))
    for i in range(len(vectors)):
        magnitudes[i] = np.linalg.norm(vectors[i])
    return magnitudes

def vectorSorter(vectors):
    sortedRowArg = np.argsort(calculateMagnitudes(vectors))
    return vectors.take(sortedRowArg,0)

if __name__ == "__main__":
    print("Here are 10 randomly generated 3D vectors with coordinates between 0 and 1.")
    example = generateVectors(10,2)
    print(example)
    print("These are their respective magnitudes:")
    print(calculateMagnitudes(example))
    print("And here we can see them sorted by magnitude.")
    print(vectorSorter(example))

    
