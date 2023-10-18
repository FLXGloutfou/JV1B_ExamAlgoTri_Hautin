stop = 1
stock = 0
MyTable = [10,51,24,84,55,2,14,65,41,6]

while (stop != 0):
    stop = 0
    for i in range (len(MyTable)-1):
        if (MyTable[i] > MyTable[i+1]):
            stock = MyTable[i] 
            MyTable [i] = MyTable [i+1]
            MyTable [i+1] = stock
            stop += 1

print (MyTable)

#Ici pour que mon program termine quand le tableau est trié j'ai mit une variable "stop"
#Celle si permet de continué la boucle tant que le programme effectue des echange !
#Une fois que le programme fait un tour "dans le vide" sans echange c'est que le tableau est trié donc il peux stop
