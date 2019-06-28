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

example = generateVectors(12,3)
print(example)
print(calculateMagnitudes(example))
print(np.argsort(calculateMagnitudes(example)))
