from zad3testy import runtests

# Borys Jarnot-Bałuszek

# algorytm uzyje czesci counting sorta aby policzyc 
# ilosc punktow po lewej i pod spodem od kazdego punktu
# nastepnie z tej informacji prosto wyciagnac 
# ilosc po prawej i nad kazdym punktem (czyli punkty nie dominowane)
# n-(nie dominowane) da nam ilosc dominowanych 
# (czasami za malo, ale interesuja nas tylko punkty nie dominowane przez zaden inny gdzie to dziala)
# znajdujemy maxa z ilosci dominowanych i zwracamy

# zlozonosc czasowa O(n), bo tylko przejezdzam po tablicy 3 razy

def dominance(P):
  # tu prosze wpisac wlasna implementacje
    #print(P)
    n = len(P)
    X=[0]*(n+1)
    Y=[0]*(n+1)
    for i in P:
        X[i[0]]+=1
        Y[i[1]]+=1
    
    for i in range(1,n):
        X[i] += X[i-1]
        Y[i] += Y[i-1]

    #print(X)
    #print(Y)
    maxd = 0
    for i in P:
        und = n-X[i[0]-1]+n-Y[i[1]-1]
        #print(i[0]-1)
        domin = n-und+1
        maxd = max(maxd, domin)
    #print (maxd)
    return maxd

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
#P = [(2, 7), (6, 7), (6, 3), (10, 9), (2, 3), (10, 5), (10, 1), (4, 3), (10, 7), (4, 7)]


#dominance(P)