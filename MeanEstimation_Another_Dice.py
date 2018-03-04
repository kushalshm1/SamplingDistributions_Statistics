import numpy as np 
import matplotlib.pyplot as plt 
import random

dice = 6
diceCount = 3
size = dice**diceCount
obsArray = []
meanArray = []
tempArray = [0]*diceCount
i = 1

while(i<=dice):
    obsArray.append(i)
    i = i+(1/diceCount)

# print(obsArray)

freqArray = [0]*len(obsArray)

#Calculating Mean
i = 0
j = 0

while(i<size):
    j = 0
    while(j<diceCount):
        rand = random.randint(1,6)
        tempArray[j] = rand
        j = j+1
        tempMean = np.mean(tempArray)
    
    meanArray.append(tempMean)
    tempArray = [0]*diceCount
    i = i+1


meanArray.sort()
print(meanArray)

#Calculating Frequency
i = 0
j = 0
while(i<size):
    if(meanArray[i]==obsArray[j]):
        freqArray[j] = freqArray[j]+1
    else:
        j = j + 1
        print("dfdf: ",j)
    i = i+1

print("somoetin")
print(freqArray)


plt.plot(obsArray,freqArray)
plt.show()