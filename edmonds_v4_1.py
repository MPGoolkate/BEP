class Obj:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def __iter__(self):
        obj = self.head
        while obj != None:
            yield obj.vertex
            obj = obj.next
    
    # O(n)
    def copy(self):
        new = DoublyLinkedList()
        for vertex in self:
            new.add(vertex)
        return new
    
    # O(1)
    def add(self, vertex):
        obj = Obj(vertex)
        if self.head == None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj
        self.len += 1
    
    # O(1)
    def add_obj(self, obj, length = 1): 
        if self.head == None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj
        self.len += length

    # O(1)
    def remove(self, obj):
        if obj.prev != None:
            obj.prev.next = obj.next
        else:
            self.head = obj.next
        if obj.next != None:
            obj.next.prev = obj.prev
        else:
            self.tail = obj.prev
        self.len -= 1

    # O(n)
    def isIn(self, vertex):
        obj = self.head
        while obj != None:
            if obj.vertex == vertex:
                return True
            obj = obj.next
        return False

    # O(n)
    def retrieve(self, vertex):
        obj = self.head
        while obj != None:
            if obj.vertex == vertex:
                return obj
            obj = obj.next
        return None   
    
    # O(1)
    def get_first(self):
        return self.head
    
    # O(1)
    def add_first(self, vertex):
        obj = Obj(vertex)
        if self.head == None:
            self.head = obj
            self.tail = obj
        else:
            self.head.prev = obj
            obj.next = self.head
            self.head = obj
        self.len += 1

    # O(n) may be possible to do in O(1)
    def reorder(self, vertex):
        obj = self.retrieve(vertex) # O(n)
        new = DoublyLinkedList() # O(1)
        while obj != None: # total of O(n)	
            new.add(obj.vertex) # O(1)
            obj = obj.next # O(1)
        obj = self.head
        while obj.vertex != vertex: # total of O(n)
            new.add(obj.vertex) # O(1)
            obj = obj.next # O(1)
        return new
    
    # O(1)
    def get_index(self, index):
        obj = self.head
        for i in range(index):
            obj = obj.next
        return obj.vertex
    
    # O(1)
    def pop(self):
        obj = self.head
        self.head = obj.next
        self.len -= 1
        return obj.vertex

class Tree:
    def __init__(self, root):
        self.root = root
        self.children = []

class ForestNode:
    def __init__(self, depth=float("inf")):
        self.depth = depth  # set of trees
        self.parent = self
        self.root = self
    
class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = set()
        self.parent = self
        self.blossomParent = self
        self.blossomRoot = self
        self.blossomChildren = DoublyLinkedList()

class Blossom:
    def __init__(self):
        self.vertices = []
        self.edges = {}
        self.matching = {}
        self.matching_vertices = set()

class Graph:
    def __init__(self):
        self.vertices = DoublyLinkedList()
        self.edges = []
        self.blossoms = []

    # Goal: add a vertex to the graph
    # Runningtime: O(1+1) = O(n) where n is the number of vertices in the graph
    def add_vertex(self, vertex):
        self.vertices.add(vertex) # O(1)
        self.edges.append( DoublyLinkedList()) # O(1) note the vertices need to be added in order O(1)

    # Goal: add an edge between two vertices
    # Runningtime: O(1+1) = O(1) 
    def add_edge(self, vertex1, vertex2):
        self.edges[vertex1.name].add(vertex2) # O(1) 
        self.edges[vertex2.name].add(vertex1) # O(1) 

    # Goal: get the neighbors of a vertex
    # Runningtime: O(n) = O(n) where n is the number of vertices in the graph
    # might be able to move this to the construction of the blossom
    def get_neighbors(self, vertex):
        edges = DoublyLinkedList() # O(1)

        iteration = vertex.blossomChildren.copy() # O(n)
        iteration.add(vertex)
        for vertexIter in iteration: # O(m)
            for neighbor in self.edges[vertexIter.name]:
                if neighbor.blossomRoot != vertex: # O(1)
                    edges.add(neighbor.blossomRoot) # O(1)

        return edges
        
        
    # Goal: get a vertex by name
    # Runningtime: O(n) where n is the number of vertices in the graph    
    def get_vertex(self, name):
        for vertex in self.vertices: # O(n)
            if vertex.name == name: # O(1)
                return vertex
        return None

    # Goal: get an edge by two vertices
    # Runningtime: O(n+n+m) = O(m) where n is the number of vertices, and m the number of edges in the graph
    def get_edge(self, vertex1, vertex2):
        if self.vertices.isIn(vertex1) and self.vertices.isIn(vertex2): # O(n)
            if self.edges[vertex1].isIn(vertex2) and self.edges[vertex2].isIn(vertex1): #O(n+m)
                return (vertex1, vertex2)
        return None

    # Goal: remove a vertex from the graph
    # Runningtime: O(n+n+n^2) = O(n^2) where n is the number of vertices
    def remove_vertex(self, vertex):
        obj = self.vertices.retrieve(vertex) # O(n)
        if obj != None: # O(1)
            vertex = obj.vertex
            self.vertices.remove(obj) # O(1)

            if vertex in self.edges: # O(n) -> might not be neccesary
                del self.edges[vertex] # O(n) -> doubly linked list in edges makes this constant
            for edges in self.edges.values(): # n times O(n+n) so O(n^2)
                if edges.isIn(vertex): # O(n) -> might not be neccesary
                    edges.remove(edges.retrieve(vertex)) # O(n) -> doubly linked list makes constant

    # Goal: remove an edge between two vertices
    # Runningtime: O(n) where n is the number of vertices
    # becomes O(n) if doubly linked list is used
    def remove_edge(self, vertex1, vertex2):
        self.edges[vertex1.name].remove(self.edges[vertex1.name].retrieve(vertex2)) #O(n) -> retrieve is O(n) rest is O(1)
        self.edges[vertex2.name].remove(self.edges[vertex2.name].retrieve(vertex1)) #O(n) 
    
    # Goal: remove an edge between two vertices by their objects
    # Runningtime: O(n+n+1+1) = O(n) where n is the number of vertices
        # might check unnecacrily if the vertices are in the graph
    def remove_edge_obj(self, vertex1, vertex2):
        if self.vertices.isIn(vertex1) and self.vertices.isIn(vertex2):
            if self.edges[vertex1].isIn(vertex2) and self.edges[vertex2].isIn(vertex1):
                self.edges[vertex1].remove(vertex2) #O(1)
                self.edges[vertex2].remove(vertex1) #O(1)

        
    # Goal: write a tuple of verixes in order of their names
    # Runningtime: O(1)
    def sort(self, v, w):
        if v.name > w.name: # O(1)
            return (w, v) 
        else:
            return (v, w)
    
    # Goal: count the number of matching edges
    # Runningtime: O(n) where n is the number of vertices in the graph
    def count_matching(self):
        count = 0
        for edges in self.edges:
            if edges.head != None:
                count += 1
        return count

# Goal: find the root of a vertex
# runnint time: O(n) as a tree may have n vertices
def root(v):
    if v.parent == v: # this check is O(1)
        return v 
    else:
        return root(v.parent) # here is a recurison that runs O(d) where d is the depth of the tree

# Goal: check if a vertex is exposed
# running time: O(n) where n is the number of vertices in the graph
def exposed(v, M):
    if M.get_neighbors(v).get_first() != None or v.blossomParent != v: # O(n)
        return False
    else:
        return True

# Goal: find the distance between two vertices
# running time: O(d) where d is the distance between the two vertices
def distance(v, w):
    if v == w:
        return 0
    else:
        # here the functino recurses O(d) times
        if v.parent == v: # this check is O(1)
            return 1+ distance(v, w.parent) 
        else:
            return 1 + distance(v.parent, w)
        
# Goal: create the augmenting path from the trees of v and w
# Running time: O(d_1+d_2) where d_1 is the depth of the tree containing v and d_2 is the depth of the tree containing w
# we note that d_1+d_2 is the length of the augmenting path. So a total running time of O(n)
def augmentingPath(v, w):
    path = DoublyLinkedList()#O(1)
    path.add(v) # O(1)
    path.add(w) # O(1)
    while v != root(v): # O(d_1) where d_1 is the depth of the tree containing v
        path.add_first(v.parent) # O(1) (it needs to move all elements one step to the right) -> doubly linked list can do this in O(1)
        v = v.parent
    while w != root(w): # O(d_2) where d_2 is the depth of the tree containing w
        path.add(w.parent) # O(1)
        w = w.parent
    return path

# Goal: invert the matching on a path
# Running time: O(n^2)
def invertPath(M, path):
    for i in range(path.len): #O(n) times so O(n^2) in total
        if i % 2 == 0 and i < path.len - 1: 
            M.add_edge(path.get_index(i) , path.get_index(i+1)) #O(n)
        elif i<path.len-1: # O(1) check length
            M.remove_edge(path.get_index(i), path.get_index(i+1)) #O(n+n+n)=O(n)
    return M #O(1)

# Goal: find the blossom containing v and w
# Running time: O(n) where n is the number of vertices in the graph
def findBlossom(v, w, G, M):
    blossom = DoublyLinkedList() # O(1)
    blossom.add(v) # O(1)
    blossom.add(w) # O(1)
    while v.parent != w.parent: # O(n) time (lenght of the blossom) so whole loop is #O(n^2)
        if v.parent != v:
            v = v.parent # O(1)
            blossom.add_first(v) # O(1)
        if w.parent != w:
            w = w.parent # O(1)
            blossom.add(w) # O(1)
    if v.parent != v and w.parent != w: # O(1)
        blossom.add(v.parent) # O(1)
    
    return blossom

def relable(blossom, blossomRoot):
    for vertex in blossom:
        vertex.blossomParent = blossomRoot # O(1)
        vertex.blossomRoot = blossomRoot # O(1)
        children = vertex.blossomChildren # O(1)
        if children.get_first() != None:
            relable(children, blossomRoot) # O(n)

# Goal: contract a blossom
# Running time: O(n) where n is the number of vertices in the graph
def contract(M, blossom):
    # update the blossom tree of the nodes
    newVertex = blossom.get_first().vertex # O(1)
    for vertex in blossom: # O(b_2) times (length of the blossom), within we can iterate over all other blossoms so whole loop is O(n) 
        vertex.blossomParent = newVertex # O(1)
        vertex.blossomRoot = newVertex.blossomRoot # O(1)
        children = vertex.blossomChildren # O(1)
        if children.get_first() != None:
            relable(children, newVertex.blossomRoot) # o(b_1)

        if vertex != newVertex:
            newVertex.blossomChildren.add(vertex) # O(1)
    
    # remove the matching within the blossom
    for vertex in blossom: # O(n) times (length of the blossom) so whole loop is O(n)
        match = M.edges[vertex.name].get_first() # O(1)
        if match != None and blossom.isIn(match.vertex): # O(n) -> becomes O(1)
            M.edges[vertex.name] = DoublyLinkedList() # O(1)    

    return M
    

# Goal: lift a blossom
# Running time: O(n^2)
# we get a blossm, graph and a matching, we need to alter the matching in accrodance with the blossom
def liftBlossom(G, M, blossom):
    # first, we find the matched edge and unmatched edge that attach to the blossom
    base = blossom.get_first() # O(1)

    # get the matched vertex that connects to the blossom (the stem of the blossom)
    for neighbor in G.get_neighbors(base.vertex): # max O(n) times so O(n^2) in total
        if not blossom.isIn(neighbor) and M.edges[neighbor.name].get_first() != None : # O(n) 
            stem = neighbor # O(1) 
            break
    
    # get the vertex in the blossom that connects to the stem
    for neighbor in G.get_neighbors(stem): # max O(n) times so O(n^2) in total
        if blossom.isIn(neighbor): # O(n)
            connected_vert = neighbor # O(1)
            break

    # get the blossom vertices in the right order 
    blossom_path = blossom.reorder(connected_vert) #  O(n)
    
    # adapt the matching in the blossom starting from the connected vertex
    v = blossom_path.get_first() # O(1)
    w = v.next
    i = 0
    #for i in range(len(blossom_path)-1): # O(n) times; so O(n^3) in total
    while w != None: # O(n) times; so O(n^2) in total
        if i % 2 == 0:
            # we need the even edges to be unmatched
            M.remove_edge_obj(v, w) #O(n)
        else:
            # we need to odd edges to be matched
            M.add_edge(v.vertex, w.vertex) #O(1)
        v = w
        w = w.next
        i += 1

    return M   


# Goal: find a maximum matching
# running time: recusion O(n) times the running time of findAugmentingPath, which is O(n^2)
# so the total running time is O(n^3)
def findMaxMatching(G, M):
    # try to find an augmenting path
    
    path = findAugmentingPath(G, M) # O(n^2)
    if path == None: # O(1)
        # no augmenting path found => M is a maximum matching
        for blossom in G.blossoms: # doen we max O(n) keer; dus O(n^3) in totaal. 
            if blossom.head != None:
                M = liftBlossom(G, M, blossom) # functie is O(n^2)
        return M # O(1)
    else:
        # invert the path to increase the matching
        M = invertPath(M, path) # O(n^2)
        # recurse to find another augmenting path
        return findMaxMatching(G, M) # recursion of max O(n) times
    
# Goal: find an augmenting path
# Running time: worst case we have a recursion of O(n) times, each taking O(n) time, a total of O(n^2)
def findAugmentingPath(G, M):
    # create empty forest
    forest = [] # O(1)
    queue = DoublyLinkedList() # O(1)

    for v in G.vertices: # O(n) times so total of O(n^2)
        if exposed(v, M): # O(n) wordt O(1)
            forest.append(ForestNode(0)) # O(1)
            queue.add(v) # O(1)
        else:
            forest.append(ForestNode()) # O(1)
    
    # find an augmenting path
    # Running time: in the worst case we find a blossom in each iteration of the recursion,
    # Each recursion takes O(n) (always finding another blossom), for a total run time of O(n^2)
    while queue.head != None:  #This together with the for loop below loops past all edges
        v = queue.pop() # O(1)

        neighbors = G.get_neighbors(v) # O(n)
        for w in neighbors:
            if forest[w.name].depth % 2 == 1 or forest[v.name].parent == forest[w.name]:
                # do nothing
                pass
            else:
                if forest[w.name].depth != float("inf"): #and forest[w.name].depth >= forest[v.name].depth:
                    if forest[v.name].root != forest[w.name].root:
                        # found an augmenting path
                        return augmentingPath(v, w)
                    else:
                        # found a blossom
                        blossom = findBlossom(v, w, G, M)
                        G.blossoms.append(blossom)
                        M = contract(M, blossom)
                        return findAugmentingPath(G, M)
                else:
                    # w is matched, so add w and w matched edge to the forest
                    forest[w.name].depth = forest[v.name].depth + 1 # O(1)
                    w.parent = v # O(1)
                    forest[w.name].parent = forest[v.name] # O(1)
                    forest[w.name].root = forest[v.name].root # O(1)
                    matchedVertex = M.get_neighbors(w).get_first().vertex # O(n) with fix O(1)
                    forest[matchedVertex.name].depth = forest[w.name].depth + 1 # O(1)
                    forest[matchedVertex.name].parent = forest[w.name] # O(1)
                    matchedVertex.parent = w # O(1)
                    forest[matchedVertex.name].root = forest[w.name].root # O(1)  
                    queue.add(matchedVertex) # O(1)
    return None
