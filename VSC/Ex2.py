stock = 0
MyTable = [10,51,24,84,55,2,14,65,41,6]

for i in range (len(MyTable)-1):
    if (MyTable[i] > MyTable[i+1]):
        stock = MyTable[i] 
        MyTable [i] = MyTable [i+1]
        MyTable [i+1] = stock

print (MyTable)

#Le 84 termine bien a la fin donc il est "remonté"