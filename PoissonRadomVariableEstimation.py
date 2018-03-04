import random
import matplotlib.pylab as plt
import numpy as np 
import math

sampleSize = 60
sampleArray = []
valueArray = []
i = 0
while(i<=sampleSize):
    sampleArray.append(i)
    i = i+1
freqArray = [0]*len(sampleArray)

#Filling up Values of P in Array
i = 0
while(i<=sampleSize):
    index = random.randint(0,60)
    freqArray[index] = freqArray[index]+1
    i = i+1
print(freqArray)
print(sampleArray)

plt.plot(sampleArray,freqArray)
plt.show()



