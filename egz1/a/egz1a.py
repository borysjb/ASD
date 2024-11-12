from egz1atesty import runtests
import queue

#Borys Jarnot-Bałuszek 419816

# modyfikowana dijkstra
# gdy znajdziemy rower, a jeszcze nie mamy jakiegos wzietego 
# to wrzucamy do dijkstry 2 elementy zamiast jednego: z rowerem i bez.
# oczywiscie interesuje mnie tylko najlepszy rower dostepny na danym polu

# zlozonosc O(E log (V)), to 
# ze wrzucam dodatkowe elementy nie ma wiekszego znaczenia 
# bo dla kazdego V wrzucam maksymalnie 2

def armstrong( B, G, s, t):
    n = 0
    for i in G:
        n = max(n,i[0],i[1])
    n+=1
    bikes = [ 1 for _ in range (n) ]
    graph = [ [] for _ in range (n) ] 
    for i in G: # przerobienie grafu na moj preferowany sposob prezentacji
    # na pierwszym miejscu krotki odleglosc, na drugim wierzcholek do ktorego prowadzi sciezka
        graph[i[0]].append((i[2],i[1]))
        graph[i[1]].append((i[2],i[0]))

        
    for i in B:
        bikes[i[0]] = min(bikes[i[0]],i[1]/i[2]) # interesuje nas tylko najlepszy rower dostepny na miejscu
        
    Q = queue.PriorityQueue()
    Q.put((0,s,1))  # na pozycji 0 odleglosc, na 1 miejsce, na 2 mnoznik dlugosci trasy z racji posiadania roweru (bedzie zmieniany gdy wezmiemy rower)

    visited = [ 2 for _ in range(n) ] # visited dziala tu nieco ciekawie, bo trzyma najlepszy rower jakim przejezdzalismy przez dany wierzcholek
    # robi to poniewaz istnieje mozliwosc ze bedziemy znowu przejezdzac przez ten sam wierzcholek, ale lepszym rowerem i ostatecznie wyprzedzimy pierwotne przejscie
    
    while not Q.empty():
        node  = Q.get()
        time  = node[0]
        place = node[1] # zwiekszenie czytelnosci
        bike  = node[2]
        
        if visited[place]<=bike: # bylismy tu juz z mniejsza odlegloscia i nie gorszym rowerem 
            continue
            
        visited[place]=bike
            
        
        if place==t: # doszlismy do celu
            return int(time)
            
        for i in graph[place]:
            dest  = i[1]
            trail = i[0]
            if visited[dest]>bike:
                Q.put((time+(trail*bike),dest,bike))  # nie bierzemy roweru z danego miejsca (mozemy miec juz wziety wczesniej)
        
        if bike==1: # nie mamy wzietego roweru, bierzemy
            new_bike = bikes[place]
            if new_bike<1: # nie dodaje bezuzytecznych elementow (bez roweru lub z rowerem nie przyspieszajacym biegu)
                for i in graph[place]:
                    dest  = i[1]
                    trail = i[0]
                    if visited[dest]>new_bike:
                        Q.put((time+(new_bike*trail),dest,new_bike)) # nowy rower uzywamy juz na najblizszej trasie
      

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )
