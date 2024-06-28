from zad5testy import runtests
from queue import PriorityQueue

def spacetravel( n, E, S, a, b ):
    # tu prosze wpisac wlasna implementacje
    visited = [None] * n
    #visited[a] = 0
    neigh = [ [] for _ in range(n)]
    for i in E:
        neigh[i[0]].append((i[2],i[1]))
        neigh[i[1]].append((i[2],i[0]))
    for i in S:
        for j in S:
            if i!=j:
                neigh[i].append((0,j))
                neigh[j].append((0,i))
    Q = PriorityQueue()
    Q.put((0,a))
    while not Q.empty():
        node = Q.get()
        if node[1]==b:
            return node[0]
        if visited[node[1]] != None:
                continue
        visited[node[1]] = node[0]
        for i in neigh[node[1]]:
            if visited[i[1]] == None:
                Q.put((i[0]+node[0],i[1]))
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )

#E = [(0,1, 5),
#     (1,2,21),
#     (1,3, 1),
#     (2,4, 7),
#     (3,4,13),
#     (3,5,16),
#     (4,6, 4),
#     (5,6, 1)]
#S = []
#spacetravel(7,E,S,1,5)
