#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      lbr
#
# Created:     10-10-2018
# Copyright:   (c) lbr 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


Jobs = 15
TimeLimit = 75

print("Quadratic Knapsack Problem ")

value = [7, 6, 13,16, 5, 10, 9, 23, 18, 12, 9, 22, 17, 32, 8]
Time = [13, 14, 14, 15, 15, 9, 26, 24, 13, 11, 9, 12, 25, 12, 26]

p = [[7 ,12 ,7  ,6  ,13 ,8  ,11 ,7  ,15 ,23 ,14 ,15 ,17 ,9  ,15],
    [12 ,6  ,15 ,13 ,10 ,15 ,9  ,10 ,8  ,17 ,11 ,13 ,12 ,16 ,15],
    [7  ,15 ,13 ,11 ,16 ,6  ,8  ,14 ,13 ,4  ,14 ,8  ,15 ,9  ,16],
    [6  ,13 ,11 ,16 ,10 ,13 ,14 ,14 ,17 ,15 ,14 ,6  ,24 ,13 , 4],
    [13 ,10 ,16 ,10 ,5  ,9  ,7  ,25 ,12 ,6  ,6  ,16 ,10 ,15 ,14],
    [8  ,15 ,6  ,13 ,9  ,10 ,2  ,13 ,12 ,16 ,9  ,11 ,23 ,10 ,21],
    [11 ,9  ,8  ,14 ,7  ,2  ,9  ,8  ,18 ,4  ,13 ,14 ,14 ,17 ,15],
    [7  ,10 ,14 ,14 ,25 ,13 ,8  ,23 ,9  ,16 ,12 ,3  ,14 ,14 ,27],
    [15 ,8  ,13 ,17 ,12 ,12 ,18 ,9  ,18 ,15 ,16 ,13 ,14 ,7  ,17],
    [23 ,17 ,4  ,15 ,6  ,16 ,4  ,16 ,15 ,12 ,28 ,5  ,19 ,6  ,18],
    [14 ,11 ,14 ,14 ,6  ,9  ,13 ,12 ,16 ,28 ,9  ,13 ,4  ,13 ,16],
    [15 ,13 ,8  ,6  ,16 ,11 ,14 ,3  ,13 ,5  ,13 ,22 ,11 ,19 ,13],
    [17 ,12 ,15 ,24 ,10 ,23 ,14 ,14 ,14 ,19 ,4  ,11 ,17 ,15 ,12],
    [9  ,16 ,9  ,13 ,15 ,10 ,17 ,14 ,7  ,6  ,13 ,19 ,15 ,32 ,16],
    [15 ,15 ,16 ,4  ,14 ,21 ,15 ,27 ,17 ,18 ,16 ,13 ,12 ,16 , 8]]

import random
import time
import math
import itertools
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
iteration_array = []


def calculateScore(value,Time,Jobs):
    score = []
    for i in range(Jobs):
        score.append(round((value[i]/Time[i]),3))
    print(score)
    return score



def greedyInitKnapSack(value,Time,Jobs,TimeLimit):
    sumItemsInKnapsack = 0

    #Sort items according to their score
    scoreIndexs =  calculateScore(value,Time,Jobs)
    indexofElementsInKnapsack = []
    print("s_i = {0}".format(scoreIndexs))

#    # Add item with highest score, that is below capacity W.
    for i in range(Jobs):
       indexOfLargestElement = scoreIndexs.index(max(scoreIndexs))
       if((sumItemsInKnapsack+Time[indexOfLargestElement]) <= TimeLimit ):
           indexofElementsInKnapsack.append(indexOfLargestElement)
           sumItemsInKnapsack += Time[indexOfLargestElement]
           print("Adding (",value[indexOfLargestElement],",",Time[indexOfLargestElement],") to the knapsack")
       scoreIndexs[indexOfLargestElement]=0
    print("***************************")
    print("Arrays: ")
    print("v_i = {0}".format(value))
    print("w_i = {0}".format(Time))
    print("x_i = {0}".format(indexofElementsInKnapsack))

    #Return index of set that yields maximum profit
    return indexofElementsInKnapsack


def initKnapSack(value,Time,Jobs,TimeLimit):
    sumItemsInKnapsack = 0
    indexofElementsInKnapsack = []

#    # Add item with highest score, that is below capacity W.
    for i in range(Jobs):
       if((sumItemsInKnapsack+Time[i]) <= TimeLimit ):
           indexofElementsInKnapsack.append(i)
           sumItemsInKnapsack += Time[i]
           print("Adding (",value[i],",",Time[i],") to the knapsack")
    print("***************************")
    print("Arrays: ")
    print("v_i = {0}".format(value))
    print("w_i = {0}".format(Time))
    print("x_i = {0}".format(indexofElementsInKnapsack))

    #Return index of set that yields maximum profit
    return indexofElementsInKnapsack



def calculateqsolution(SolutionList,value,p):
    Totalprofit = 0
    for i in range(len(SolutionList)):
        Totalprofit += value[SolutionList[i]]
        if (i > 0):
            j=0
            while (j < i):
                Totalprofit += p[SolutionList[j]][SolutionList[i]]
                j+=1
    return Totalprofit

def calculateweight(SolutionList,Time):
    Totalweight = 0
    for i in range(len(SolutionList)):
        Totalweight += Time[SolutionList[i]]
    return Totalweight

def ValNeighbour(CurrentSolutionList,i,j,value,p, ValueSolution):
    Totalprofit = ValueSolution - value[i] + value[j]
    for k in range(len(CurrentSolutionList)):
        if (CurrentSolutionList[k] != i):
            s=0
            Totalprofit += p[CurrentSolutionList[k]][j]
            Totalprofit -= p[CurrentSolutionList[k]][i]
    return Totalprofit

def findbestneighbourswap(CurrentSolutionList, value, p, Time, TimeLimit,curval):
    CurrentWeight= calculateweight(CurrentSolutionList,Time)
    indexolditem = len(Time)
    newitem = len(Time)
    bestneigh = 0
    bestval=curval
    if len(iteration_array) == 0:
        iteration_array.append(bestval)
    SolutionList = []
    for i in range(len(CurrentSolutionList)):
        for j in range(Jobs):
            if (j not in CurrentSolutionList):
                if (CurrentWeight-Time[CurrentSolutionList[i]]+Time[j]) <= TimeLimit:
                    tempval= ValNeighbour(CurrentSolutionList,CurrentSolutionList[i],j,value,p,curval)
                 #   print(" Remove %i insert %i and new value is: %i"  % (i,j,tempval) )
                    if (tempval > bestval):
                        print("%i Better solution %i"  % (curval,tempval) )
                        iteration_array.append(tempval)
                        bestneigh=tempval
                        indexolditem = i
                        newitem = j
                        bestval= tempval
    SolutionList.append(bestneigh)
    SolutionList.append(indexolditem)
    SolutionList.append(newitem)
    return SolutionList


def findbestneighbourswap2(CurrentSolutionList, value, p, Time, TimeLimit,curval):
    CurrentWeight= calculateweight(CurrentSolutionList,Time)
    indexolditem = len(Time)
    newitem = len(Time)
    bestneigh = 0
    bestval=curval
    SolutionList = []
    for i in range(len(CurrentSolutionList)):
        for j in range(Jobs):
            if (j not in CurrentSolutionList):
                if (CurrentWeight-Time[CurrentSolutionList[i]]+Time[j]) <= TimeLimit:
                    tempval= ValNeighbour(CurrentSolutionList,CurrentSolutionList[i],j,value,p,curval)
                 #   print(" Remove %i insert %i and new value is: %i"  % (i,j,tempval) )
                    if (tempval > bestval):
                        print("%i Better solution %i"  % (curval,tempval) )
                        bestneigh=tempval
                        indexolditem = i
                        newitem = j
                        bestval= tempval
    SolutionList.append(bestneigh)
    SolutionList.append(indexolditem)
    SolutionList.append(newitem)
    return SolutionList



def Hillclimber(Jobs,value,Time,TimeLimit,p):
  #  indexChosenElements = []
  #  sizeOfArrayOfPairs = 2
    sumWeightElementsKnapsack = 0
    sumProfit = 0
    start = time.time()
    elapsed = 0
 #   SolutionList = greedyInitKnapSack(value,Time,Jobs,TimeLimit)
    SolutionList = initKnapSack(value,Time,Jobs,TimeLimit)

    BestSolutionList = SolutionList.copy()
    CurrentSolutionList = SolutionList.copy()
    ValueBestsolution = calculateqsolution(SolutionList,value,p)
    ValueCurrentsolution= ValueBestsolution
    WeightCurrentsolution= calculateweight(SolutionList,Time)
    count = 0
    print(" Initial Value %i" % ValueBestsolution)
    iteration_array.append(ValueBestsolution)
    while(elapsed < 10):
        BestNeigh=findbestneighbourswap(CurrentSolutionList, value, p, Time, TimeLimit, ValueCurrentsolution)
        count+=1
        if (BestNeigh[0]>0):
            print("BestNieghbour %i, remove %i insert %i"  % (BestNeigh[0],  CurrentSolutionList[BestNeigh[1]],BestNeigh[2] ) )

            CurrentSolutionList[BestNeigh[1]]=BestNeigh[2]
            ValueCurrentsolution =   calculateqsolution(CurrentSolutionList,value,p)
                 #additems
            if (ValueBestsolution <  ValueCurrentsolution ):
                print("Update solution")
                BestSolutionList =CurrentSolutionList.copy()
                ValueBestsolution = ValueCurrentsolution
                iteration_array.append(ValueBestsolution)
                print("b_i = {0}".format(BestSolutionList))
        else:
            break
        elapsed = time.time() - start
    print("The Best solution found")
    print("Arrays: ")
    print("x_i = {0}".format(BestSolutionList))
    print("Value of Best : %i" % ValueBestsolution)
    print("Print iterations %i" % count)



def generateNextPossiblePoint(CurrentSolutionList, Time, TimeLimit):
    index2Remove = random.randint(0, len(CurrentSolutionList)-1) #pick random element to remove
    #pick random element to add that is not already in list and not same as the one removed
    while 1:
        index2Add = random.randint(0, len(value)-1)
        SolutionList = CurrentSolutionList
        if (index2Add not in CurrentSolutionList):
            SolutionList.remove(CurrentSolutionList[index2Remove])
            SolutionList.append(index2Add)
            TimeSum = 0
            for item in SolutionList:
                TimeSum += Time[item]
            if (TimeSum<TimeLimit):
                return SolutionList

def generateNextPossiblePoint2(CurrentSolutionList, Time, TimeLimit):
    while 1:
        num_index2Remove = random.randint(1,len(CurrentSolutionList)-1)
        num_index2Add = random.randint(1,7-len(CurrentSolutionList)+num_index2Remove)
        index2Remove = []
        index2Add = []
        #print("Start", CurrentSolutionList)

        while (len(index2Remove) != num_index2Remove):
            index = random.randint(0, len(value)-1) #pick random element to remove
            if index not in index2Remove:
                if index in CurrentSolutionList: 
                    index2Remove.append(index)
        #print("All index to remove", index2Remove)
        #pick random element to add that is not already in list and not same as the one removed

        while (len(index2Add) != num_index2Add):
            index = random.randint(0, len(value)-1)
            if index not in index2Add:
                if index not in index2Remove:
                    if index not in CurrentSolutionList:
                        index2Add.append(index)
        #print("All index to add", index2Add)

        SolutionList = CurrentSolutionList
        for i in index2Remove:
            SolutionList.remove(i)
        #print("removed", SolutionList)
        for j in index2Add:
            SolutionList.append(j)
        #print("added", SolutionList)

        TimeSum = 0
        for item in SolutionList:
            TimeSum += Time[item]
        if TimeSum <= TimeLimit:
            return SolutionList


def calculateAcceptance(Temperature, TDelta):
    prob = math.exp(TDelta/Temperature)
    #print("%f, %f , %f, %f" % (TDelta, Temperature, TDelta/Temperature, prob))
    if (prob > random.uniform(0,1)):
        return 1
    else:
        return 0
    

def Annealing(Jobs,value,Time,TimeLimit,p):
    start = time.time()
    elapsed = 0
    Temperature_start = 10
    Temperature = Temperature_start
    Temperature_step = .99
    #SolutionList = greedyInitKnapSack(value,Time,Jobs,TimeLimit)
    SolutionList = initKnapSack(value,Time,Jobs,TimeLimit)

    BestSolutionList = SolutionList.copy()
    CurrentSolutionList = SolutionList.copy()
    ValueBestsolution = calculateqsolution(SolutionList,value,p)
    ValueCurrentsolution= ValueBestsolution

    count = 0
    print(" Initial Value %i" % ValueBestsolution)
    iteration_array.append(ValueBestsolution)

    while(elapsed < 10):
        #NextSolutionList=generateNextPossiblePoint(CurrentSolutionList, Time, TimeLimit)
        NextSolutionList=generateNextPossiblePoint2(CurrentSolutionList, Time, TimeLimit)
        NextSolutionValue = calculateqsolution(NextSolutionList, value, p)
        TDelta = NextSolutionValue-ValueBestsolution
        count+=1
        if (TDelta > 0):
            #print("Higher solution value found. Old: %i, New: %i"  % (ValueBestsolution, NextSolutionValue))
            BestSolutionList = NextSolutionList
            ValueBestsolution = NextSolutionValue
            iteration_array.append(ValueBestsolution)
        #elif (calculateAcceptance(Temperature, TDelta) == 1):
        #    #print("New solution value found. Old: %i, New: %i"  % (ValueBestsolution, NextSolutionValue))
        #    BestSolutionList = NextSolutionList
        #    ValueBestsolution = NextSolutionValue
        #    iteration_array.append(ValueBestsolution)

        elapsed = time.time() - start
        Temperature *= Temperature_step
        if (Temperature <= 0 or Temperature < 0.001):
            break

    print("The Best solution found")
    print("Arrays: ")
    print("x_i = {0}".format(BestSolutionList))
    print("Value of Best : %i" % ValueBestsolution)
    print("Print iterations %i" % count)





#greedyInitKnapSack(value,Time,Jobs,TimeLimit)
#Hillclimber(Jobs,value,Time,TimeLimit,p)
Annealing(Jobs,value,Time,TimeLimit,p)

# Figures
#print ("Iteration values are: ", iteration_array)
fig, ax = plt.subplots()
x = np.arange(0, len(iteration_array), 1)
ax.plot(x, iteration_array)
#plt.xticks(np.arange(min(x), max(x)+1, 1.0))
ax.set(xlabel='iteration', ylabel='Value',
       title='Function value in each iteration')
ax.grid()   

fig.savefig("fig.png")
plt.show()





