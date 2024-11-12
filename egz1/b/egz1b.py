from egz1btesty import runtests

# Borys Jarnot-Bałuszek 419816

# podejscie dynamiczne
# w dyna[i][j] trzymam maksymalna sume sposrod wszystkich ciagow j-spojnych 
# z koncem w i-tym elemencie z dokladnie j elementami wycietymi
# dla kazdego elementu mozemy go wyciac lub nie.
# jezeli go wycinamy: bierzemy po prostu sume dla i-1 elementow i j-1 wycietych
# jezeli go nie wycinamy: bierzemy sume dla i-1 elementow i j wycietych
# jako ze w zadaniu nie musimy wycinac dokladnie k elementow, a maksymalnie k,
# to rozwiazanie niekoniecznie jest w ostatnim rzedzie. bede po prostu trzymal maksymalna wartosc jaka gdziekowliek widzialem

# dynamik na tablicy o wymiarach n*k, zlozonosc O(nk)

def kstrong( T, k):
    strong = 0 # podobne do tresci zadania :), bedzie trzymac najwieksza spotkana wartosc
    n = len(T)
    dyna = [ [ 0 for _ in range(k+1)] for _ in range(n)] # tablica dynamiczna
     # dla danego k,n trzyma maksymalna sume z koncem w n i k zignorowanymi wartosciami
    dyna[0][0] = T[0]
    for i in range(1,n):
        dyna[i][0] = max(dyna[i-1][0]+T[i],T[i]) 
        # dla 0 ignorowanych wartosci jezeli maksymalna wartosc z koncem w i-1 jest ujemna
        # to lepiej wziac po prostu wartosc T[i]. 
        # np w tablicy przykladowej zadania, poczatek -20,5,-1
        # dla i=1 lepiej wziac tylko 5 niz obie liczby.

    for j in range(1,k+1):
        for i in range(j,n):
            dyna[i][j] = max(dyna[i-1][j-1],dyna[i-1][j]+T[i])
            # opcja 1: wycinamy i-ty element, wtedy suma z koncem w i, 
            # z j wycietymi wartosciami to dyna[i-1][j-1] (jeden mniej element i jeden mniej wyciety)

            # opcja 2: nie wycinamy i-tego elementu (dodajemy go), 
            # ma byc wyciete juz j elementow, suma do (i-1)-go i i-tego
            strong = max(strong, dyna[i][j])
    return strong


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )
