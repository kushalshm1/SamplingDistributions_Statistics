import numpy as np 
import matplotlib.pyplot as plt
import random
#---------------------------------------
#All the Variables and Arrays:
diceCount = 2
dice = 6
size = dice**diceCount
obsArray = []
medianArray = []
temp = [0]*diceCount
i = 1
#---------------------------------------
#Making an Observation Array
while(i<=dice):
    obsArray.append(i)
    i = i+(1/diceCount)
# print(obsArray)
#---------------------------------------
# #Making Frequency Array
freqArray = [0]*len(obsArray)

# #---------------------------------------
# #Calculating medians
i = 0
while(i<size):
    j = 0
    while(j<diceCount):
        rand  = random.randint(1,6)
        temp.append(rand)
        j = j+1
    medianArray.append(np.median(temp))
    i = i+1
# #---------------------------------------
medianArray.sort()
# print(medianArray)
# print(len(medianArray))
# #Filling up Values in Frequency Array
j = 0
i = 0

while(i<size):
    if medianArray[i] ==  obsArray[j]:
        freqArray[j] = freqArray[j]+1        
    else:
        j = j+1
    i = i+1
# #---------------------------------------




print(freqArray)
print(obsArray)
print(medianArray)

plt.plot(obsArray,freqArray)
plt.show()