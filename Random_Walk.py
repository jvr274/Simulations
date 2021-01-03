from random import random
pVal=2/3 # Probability of walking right
qVal=1-pVal #Probability of walking left
xInt=1 #Initial Position
xFall=0 #Poistion of falling
xSafe=50 #Position to safety
tSafe=0 #Initial times made to safety
t=100000 #NUmber of simulations
i=0 # value to start
nStep=0 #value to see average steps when safe
tStep=0
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
    xInt=1 #Reset initial Position
    nStep=0
fracSafe=tSafe/t
aveStep= tStep/tSafe
print(fracSafe)
print(aveStep)
    
