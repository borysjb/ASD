from kol3testy import runtests

# Borys Jarnot-Bałuszek 419816

# podejscie bruteforce: sprawdzam dla kazdej ilosci drzew kazda 
# ilosc wycietych i cyz jest mozliwa kazda ilosc jablek modulo m. 
# zlozonosc O(n^3) (bo m<=7n, czyli m = O(n))


def orchard(T, m):
    n = len(T)
    for i in range(n):
        T[i] = T[i]%m
    arr = [[ [ False for _ in range (m)] for _ in range(n+1)] for _ in range(n+1)]
    arr[1][0][T[0]] = True
    arr[1][1][0] = True
    for i in range(2,n+1):
        for j in range(m):

            arr[i][0][j] = arr[i-1][0][j-T[i-1]] 
        
        arr[i][i][0] = True

    for i in range(1,n+1):
        for k in range(1,i):
            for j in range(m):
                arr[i][k][j] = arr[i-1][k-1][j] # mozliwosc
                # istnienia j jablek przy i drzewach i k wycietych, jest taka jak
                # mozliwosc istnienia j jablek przy i-1 drzewach i k-1 wycietych (wycinam i-te drzewo)
                if not arr[i][k][j]:
                    arr [i][k][j] = arr[i-1][k][j-T[i-1]]
                    # nie wycinam i-tego drzewa, mozliwosc taka jak dla i-1 drzew, k wycietych i j-T[i-1 jablek]

                    # dziekuje pythonowi za odwolania do tablicy na ujemnych indeksach (od tylu)
                    # to samo zalatwia kwestie modulo. <3
                    
    for i in range(n+1):
        # szukam pierwszej ilosci drzew wycietych ktora ma mozliwosc miec 0 jablek mod m (czyli ilosc podzielna przez m)
        if arr[n][i][0]:
            return i
        


runtests(orchard, all_tests=True)
