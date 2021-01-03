from random import random
import numpy as np
import matplotlib.pyplot as plt
pVal=2/3 # Probability of walking right
qVal=1-pVal #Probability of walking left
xInt=1 #Initial Position
xFall=0 #Poistion of falling
xSafe=50 #Position to safety
tSafe=0 #Initial times made to safety
t=100000 #NUmber of simulations
i=0 # value to start
minStep=1000
maxStep=0
nStep=0 #value to see average steps when safe
tStep=0
less100=0
less125=0
less150=0
less175=0
more200=0
while i < t:
    i=i+1
    while (xInt > xFall) & (xInt < xSafe):
        if  random() < pVal:
            xInt=xInt+1
            nStep=nStep+1
        else:
            xInt=xInt-1
            nStep=nStep+1
    if xInt == xSafe:
        tSafe=tSafe+1
        tStep=tStep+nStep
        if nStep <100:
            less100+=1
            if minStep > nStep:
                minStep = nStep
        elif nStep <125:
            less125+=1
        elif nStep <150:
            less150+=1
        elif nStep <175:
            less175+=1
        else:
            more200+=1
            if maxStep < nStep:
                maxStep = nStep
    xInt=1 #Reset initial Position
    nStep=0
fracSafe=tSafe/t
aveStep= tStep/tSafe
print(fracSafe)
print(aveStep)
print(minStep,maxStep)
fig=plt.figure(figsize=(15,8))
ax = fig.add_axes([0,0,1,1])
labels = ['Less than 100','125-149','150-174','175-199','more than 200']
values=[less100,less125,less150,less175,more200]
ax.bar(labels,values)

    
