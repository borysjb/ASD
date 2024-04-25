from zad1testy import Node, runtests

# Jarnot-Bałuszek Borys
# 419816

# Algorytm uzyje kolejki priorytetowej o dlugosci k+1 do trzymania najmniejszych wartosci
# w konkretnym Nodzie i k kolejnych Node'ach. Następnie będzie wyciągał pojedyncze Node-y, linkował je do nowej listy
# i wrzucal kolejna wartosc z oryginalnej listy. Na koncu podepnie koniec listy do pierwszego Noda kolejki priorytetowej
# Zwracam nowa, posortowana liste

# Algorytm ten dziala poniewaz najmniejsza liczba listy musi znajdowac sie na pierwszym, lub na k kolejnych miejscach.
# Po znalezieniu najmniejszej wartosci w calej liscie mozemy powtorzyc to rozumowanie dla reszty listy.
# To rozumowanie mozna powtorzyc do momentu w ktorym wszystkie pozostale Nody oryginalnej listy znajduja sie na kolejce priorytetowej
# w tym momencie cala reszta listy jest juz posortowana w kolejce priorytetowej, wystarczy podpiac jej poczatek na koniec posortowanej listy 

# poniewaz push w kolejce priorytetowej bez uzycia heapow jest liniowy
# to zlozonosc całego algorytmu to O(nk) 
# dla k=O(1) to O(n), dla k=O(logn) O(nlogn) a dla k=O(n) O(nn)

# moglbym zbic zlozonosc do O(nlogk) uzywajac heapa do utrzymywania kolejki priorytetowej,
# wtedy push() i pop() mialyby zlozonosc O(logk)


class priority_queue:
    def __init__ (self):
        self.begin = None

    def isEmpty(self):  
        return (self.begin == None) # yes, this returns corectly

    def front(self):
        return self.begin
    
    def pop(self):                   # pop() removes first node and returns it
        if self.isEmpty():
            return None
        else:
            ret = self.begin
            self.begin = self.begin.next
            return ret
            

    def push(self, node):    # push() accepts a node to not allocate more memory, 
                              # which apart from being memory-heavy also take a lot of time 
                              # (test 9 takes .5s like that instead of 2.5 with holding just values and creating more nodes when necessary)
                              
        if self.isEmpty():      # insert into empty queue
            node.next = None
            self.begin = node
            return
            
        else:
            if node.val < self.begin.val:    # insert into the first place
                node.next = self.begin
                self.begin = node
                return
            else:                            # insert into the middle
                temp = self.begin
                while temp.next != None:        # find first greater node
                    if temp.next.val > node.val:
                        break  
                    temp = temp.next
                node.next = temp.next           # insert node
                temp.next = node
                return
                
            

def SortH(p,k):
    # tu prosze wpisac wlasna implementacje
    
    if k==0:
        return p
    Q = priority_queue()    
    begin = Node()
    end = begin
    for i in range(k+1):    # initializing the priority queue with the given amount of nodes
        if p==None:
            break      # for k==n, this loop would try to insert too many nodes into the queue and run out of the list,
        temp = p.next    # and it needs to hold k+1 nodes because the smallest value can be in the node, or in k following (k+1 total nodes).
        Q.push(p)
        p=temp
    while p != None:    # walking through the rest of the list
        temp = Q.pop()
        end.next = temp      
        end = temp
        n = p.next
        Q.push(p)
        p=n
    end.next = Q.front()    # linking the sorted remainder of the list to the sorted part
    return begin.next   # begin is an empty node because i link the given nodes to it,
                        # so i return the next node which is the first holding an actual value

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )


