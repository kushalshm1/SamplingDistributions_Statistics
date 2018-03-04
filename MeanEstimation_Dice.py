import numpy as np
import matplotlib.pyplot as pyplot
import random 
import math
diceCount = 3
size = 6**diceCount
obsArray = [0]*size
tempArray = [0]*diceCount
meanArray = [0]*size
frequencyArray = []
i = 0
#Now I am filing up the observations
while(i<size):
    j = 0
    while(j<diceCount):
        # tempArray = [0]*diceCount
        tempArray[j] = random.randint(1,6)
        # tempArray.sort()
        j = j+1
    obsArray.append(tempArray)
    tempArray = [0]*diceCount
    i = i+1

#This Function return average of an Array
# def avg(index):
    # i = 0
    # add = 0
    # j = 0

#This function calculates frequency
    # while(i<size):
        # while(j<diceCount):
            # meanArray[i] = np.mean(obsArray[i])
            # add = add+temp
            # j = j+1
        # i = i+1
    # average = add/size
    # print(average)
    # return average

i = 0
while(i<size):
    meanArray[i] = np.mean(obsArray[i]) 
    i = i+1
# meanArray.sort()
# print(meanArray) 

i = 0
j = 0
print(meanArray)
while(i<size):
    if(meanArray[i]/meanArray[j]==1):
        # print(meanArray[i],meanArray[j])
        i = i+1 
        # print("Kushal")
        # print(i)
    else:
        j = i
        print(i)
        frequencyArray.append(i) #Problem: Value is not Appending 
        
print(frequencyArray)

    #Now Calculating mean 
    # meanArray = obsArray.append()



# print(obsArray)
