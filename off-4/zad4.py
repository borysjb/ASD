from zad4testy import runtests

# Borys Jarnot-Bałuszek

#Dany jest nieskierowany graf G = (V, E), którego wierzchołki reprezentują punkty nawigacyjne nad
#Bajtocją, a krawędzie reprezentują korytarze powietrzne między tymi punktami. Każdy korytarz
#powietrzny ei ∈ E powiązany jest z optymalnym pułapem przelotu pi ∈ N (wyrażonym w metrach).
#Przepisy dopuszczają przelot danym korytarzem, jeśli pułap samolotu różni się od optymalnego naj-
#wyżej o t metrów. Graf jest przerobiony na postać listy sąsiedztwa z zapisanymi pułapami,
#ui, vi ∈ N to numery punktów nawigacyjnych, a pi to optymalny pułap przelotu.
#Graf jest nieskierowany, na liście sąsiedztwa arr[ui] = [[vi,pi],[vi,pi],...]
#Zaimplementowałem funkcję Flight(L,x,y,t), która sprawdza czy istnieje możliwość prze-
#lotu z zadanego punktu x ∈ V do zadanego punktu y ∈ V w taki sposób, żeby samolot nigdy nie
#zmieniał pułapu. Algorytm jest poprawny i być może najszybszy. Szacuję złożoność czasową na O(E)

def dfs(arr,node,dest,diff,minh,maxh,visited):
    
    if maxh-minh > 2*diff:
        return False
    #print(node)    
    visited[node]=True

    if node==dest:
        return True
    
    for i in arr[node]:
        if not visited[i[0]]:
            way = dfs(arr,i[0],dest,diff,min(minh,i[1]),max(maxh,i[1]),visited)
            if way:
                return True
    
    visited[node]=False
    return False
    

def Flight(L,x,y,t):
    maxv = 0;
    for i in L:
        maxv = max(maxv,i[1])

    arr = [ [] for _ in range(maxv+1)]
    for i in L:
        arr[i[0]].append([i[1],i[2]])
        arr[i[1]].append([i[0],i[2]])

    visited = [ False for _ in range(maxv+1) ]
    return dfs(arr,x,y,t,9999999999999,-1,visited)
    # tu prosze wpisac wlasna implementacje

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )
