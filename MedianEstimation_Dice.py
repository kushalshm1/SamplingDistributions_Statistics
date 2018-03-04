import numpy as np 
import matplotlib.pyplot as plt
import random
i = 0
j = 0
dicesCount = 4
size = 6**dicesCount
obsArray = [0]*size
tempArray = [0]*dicesCount
median = [0]*size
indexes = []
finalMedian = []

#Creating a Sample Space
# sampleSpace = [0]*10000
# for x in range(0,10000):
    # sampleSpace[x] = random.randint(1,6)
# print(sampleSpace)

while i<size:
    j = 0
    while j<dicesCount:
        # randomNumber = random.randint(1,6)
        tempArray[j] = random.randint(1,6)
        j = j+1
    tempArray.sort()
    obsArray[i] = tempArray
    tempArray = [0]*dicesCount
    i = i+1
    # i = i+1

# print(obsArray)
# print(tempArray)


#Calculating Median
i = 0
while(i<size):
    index = int((len(tempArray)/2)+0.5)
    median[i] = obsArray[i][index]
    i = i+1

median.sort()
# print(median)
#Now we have to calculate the Frequency of Every Element in


i = 0
j = 0
k = 0
while(i<len(median)):
    
    if(median[i]==median[j]):
        i = i+1
    else:
        j = i
        if(k==0):
            k=j
        else:
            k = j - k  #I did this because frequencies were adding up 
        indexes.append(k)
    
print(indexes)
i = 0
while(i<len(indexes)):
    finalMedian.append(median[indexes[i]])
    i = i+1

# print(finalMedian)

plt.plot(indexes,finalMedian)
plt.show()


#_____________________________________________________________________________________________________
# print(median)
freqArray = [1]*max(median)
print(freqArray)