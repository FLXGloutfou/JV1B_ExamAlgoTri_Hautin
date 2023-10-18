stock = 0
MyTable = [10,51,24,84,55,2,14,65,41,6]

#indice u et v change en fonction de l'indice des 2 case que l'on veut permuter
# stock = MyTable[u] 
# MyTable [u] = MyTable [v]
# MyTable [v] = stock

#exemple avec les case 0 et 1
stock = MyTable[0] 
MyTable [0] = MyTable [1]
MyTable [1] = stock

print (MyTable)