from zad8testy import runtests

def parking(X,Y):

    i = 1
    out=10000000000
    dist = [ [ None  for _ in range(len(Y))] for _ in range(len(X)) ]
    for i in range(len(Y)):
        dist[0][i] = abs(X[0]-Y[i])
    #print(dist[0])
    while i<len(X):
        mind = 100000000000
        for j in range(i,len(Y)):
            for k in range(i):
                mind = min(mind,dist[i-1][k])
            dist[i][j] = mind+abs(X[i]-Y[j])
    for i in dist[len(X)-1]:
        if i!=None:
            out = min(out,i)
        
  # tu prosze wpisac wlasna implementacje
    return out
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = False )
