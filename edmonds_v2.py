class Tree:
    def __init__(self, root):
        self.root = root
        self.children = []

class Forest:
    def __init__(self):
        self.trees = set()  # set of trees
        self.vertices = set()

    # Goal: add w as a child of v in the forest
    # Runningtime: O(1+f+f+f) = O(f) where f is the number of trees in the forest
    def add(self, v, w): 
        # Set v as the parent of w
        w.parent = v # O(1)

        # Add w to the children of the tree containing v
        for tree in self.trees: # we do f times O(1) making this O(f)
            if tree.root == v:
                tree.children.append(w) # O(1)
                break

        # Remove the tree w from the forest
        self.trees.discard(w) # O(f) 
        # add it to the forest
        self.vertices.add(w) # O(f)

class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = set()
        self.parent = self

class Blossom:
    def __init__(self):
        self.vertices = []
        self.edges = {}
        self.matching = {}
        self.matching_vertices = set()

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}
        self.blossoms = []

    # Goal: add a vertex to the graph
    # Runningtime: O(n+n+1) = O(n) where n is the number of vertices in the graph
    def add_vertex(self, vertex):
        if vertex not in self.vertices: # O(n)
            self.vertices.add(vertex) # O(n)
            self.edges[vertex.name] = [] # O(1)

    # Goal: add an edge between two vertices
    # Runningtime: O(n+n+n) = O(n) where n is the number of vertices in the graph
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices: # O(n)
            self.edges[vertex1.name].append(vertex2.name) # O(n)
            self.edges[vertex2.name].append(vertex1.name) # O(n)

    # Goal: get the neighbors of a vertex
    # Runningtime: O(n+n) = O(n) where n is the number of vertices in the graph
    def get_neighbors(self, vertex):
        if vertex in self.vertices: # O(n)
            return self.edges[vertex.name] # O(n)
        else:
            return []
        
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
        if vertex1 in self.vertices and vertex2 in self.vertices: # O(n)
            if vertex2.name in self.edges[vertex1.name] and vertex1.name in self.edges[vertex2.name]: #O(n+m)
                return (vertex1.name, vertex2.name)
        return None

    # Goal: remove a vertex from the graph
    # Runningtime: O(n+n+n^2) = O(n^2) where n is the number of vertices
    def remove_vertex(self, vertex):
        if vertex in self.vertices: # O(n)
            self.vertices.discard(vertex) # O(n)
            if vertex.name in self.edges: # O(n)
                del self.edges[vertex.name] # O(n)
            for edges in self.edges.values(): # n times O(n+n) so O(n^2)
                if vertex.name in edges: # O(n)
                    edges.remove(vertex.name) # O(n)

    # Goal: remove an edge between two vertices
    # Runningtime: O(n+n+n^2+n^2) = O(n^2) where n is the number of vertices
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices: # O(n)
            if vertex2.name in self.edges[vertex1.name] and vertex1.name in self.edges[vertex2.name]: #O(n)
                self.edges[vertex1.name].remove(vertex2.name) #O(n^2)
                self.edges[vertex2.name].remove(vertex1.name) #O(n^2)
    
    # Goal: contract an edge between two vertices
    # Runningtime: O(n^2+n^2+n^2+n+n^2) = O(n^2) where n is the number of vertices
    def contract_edge(self, v, w):
        # first, we remove the edge between v and w
        self.remove_edge(v, w) #O(n^2)
        # then, we add the edges between the neighbors of v and w
        for neighbor in self.edges[w.name]: #O(n)
            if neighbor != v.name: #O(1)
                self.add_edge(v, self.get_vertex(neighbor)) #O(n)
        # finally, we remove w from the graph
        self.remove_vertex(w)#O(n^2)

        # remove any empty lists from the edges
        dels = []
        for key in self.edges: #O(n)
            if self.edges[key] == []: #O(1)
                dels.append(key) #O(1)

        for key in dels: #O(n)
            del self.edges[key] #O(1)
            self.remove_vertex(self.get_vertex(key)) #O(n^2+n)=O(n^2)

        
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
    if v in M.vertices: # O(n)
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
# Running time: O(d_1*n+d_2) where d_1 is the depth of the tree containing v and d_2 is the depth of the tree containing w
# we note that d_1+d_2 is the length of the augmenting path.  
def augmentingPath(v, w):
    path = [v, w] # O(1)
    while v != root(v): # O(d_1) where d_1 is the depth of the tree containing v
        path.insert(0, v.parent) # O(n) (it needs to move all elements one step to the right) -> deque can do this in O(1)
        v = v.parent
    while w != root(w): # O(d_2) where d_2 is the depth of the tree containing w
        path.append(w.parent) # O(1)
        w = w.parent
    return path

# Goal: invert the matching on a path
# Running time: O(1/2*n*(n+m)+1/2*n*n^2) = O(n^3) where n is the number of vertices and m the number of edges in the graph
def invertPath(M, path):
    for i in range(len(path)): # we loop over the vertices in the path of lenght max n
        if i % 2 == 0 and i < len(path) - 1: # 
            M.add_vertex(path[i]) #O(n)
            M.add_vertex(path[i+1]) #O(n)
            M.add_edge(path[i], path[i+1]) #O(m)
        elif i<len(path)-1: # O(1) check length
            M.remove_edge(path[i], path[i+1]) #O(n^2)
    return M #O(1)

# Goal: find the blossom containing v and w
# Running time: O(n^2) where n is the number of vertices in the graph
def findBlossom(v, w, G, M):
    blossom = Blossom() # O(1)
    path = [v, w] # O(1)
    while v.parent != w.parent: # O(n) time (lenght of the blossom) so whole loop is #O(n^2)
        if v.parent != v:
            v = v.parent # O(1)
            path.insert(0, v) # O(n)
        if w.parent != w:
            w = w.parent # O(1)
            path.append(w) # O(1)
    if v.parent != v and w.parent != w: # O(1)
        path.append(v.parent) # O(1)
    blossom.vertices = path #O(n)
    for vertex in blossom.vertices: # O(n) times (length of the blossom) so whole loop is O(n^2)
        blossom.edges[vertex.name] = G.edges[vertex.name].copy() # O(n)
        if vertex in M.vertices: # O(n)
            blossom.matching[vertex.name] = M.edges[vertex.name].copy() # O(n)
            blossom.matching_vertices.add(vertex) # O(1)
    return blossom # O(1)

# Goal: contract a blossom
# Running time: O(n^3) where n is the number of vertices in the graph
def contract(G, M, blossom):
    base = blossom.vertices[-1] # O(1)

    for v in blossom.vertices[:-1]: # O(n) times (length of the blossom) so whole loop is O(n^3)
        G.contract_edge(base, G.get_vertex(v.name)) # O(n^2)
        if v in M.vertices: # O(n)
            M.contract_edge(base, M.get_vertex(v.name)) # O(n^2)

    return G, M

# Goal: lift a blossom
# Running time: O(n^3+n^3+n+n^3)=O(n^3)
# we get a blossm, graph and a matching, we need to alter the matching in accrodance with the blossom
def liftBlossom(G, M, blossom):
    # first, we find the matched edge and unmatched edge that attach to the blossom
    base = blossom.vertices[-1] # O(1)

    # get the matched vertex that connects to the blossom (the stem of the blossom)
    for neighbour in G.edges[base.name]: # max O(n) times so O(n^2) in total
        if G.get_vertex(neighbour) in M.vertices: # O(n)
            stem = G.get_vertex(neighbour) # O(n) -> easy fix, overal zelfde referenties (i.e niet met naam werken maar met het object)
            break
    
    # get the vertex in the blossom that connects to the stem
    for neighbour in G.edges[stem.name]: # max O(n) times so O(n^2) in total
        if G.get_vertex(neighbour) in blossom.vertices: # O(n)
            connected_vert = G.get_vertex(neighbour) # O(n) -> easy fix (overal zelfde reverenties)
            break

    # get the blossom vertices in the right order
    blossom_path = blossom.vertices[blossom.vertices.index(connected_vert):] + blossom.vertices[:blossom.vertices.index(connected_vert)] # O(n)
    
    # adapt the matching in the blossom starting from the connected vertex
    for i in range(len(blossom_path)-1): # O(n) times; so O(n^3) in total
        if i % 2 == 0:
            # we need the even edges to be unmatched
            M.remove_edge(blossom_path[i], blossom_path[i+1]) #O(n^2)
        else:
            # we need to odd edges to be matched
            M.add_vertex(blossom_path[i]) #O(n)
            M.add_vertex(blossom_path[i+1]) #O(n)
            M.add_edge(blossom_path[i], blossom_path[i+1]) #O(n)

    return M   

# Goal: find a maximum matching
# running time: recusion O(n) times the running time of findAugmentingPath, which is O(n^4)
# so the total running time is O(n^5)
def findMaxMatching(G, M):
    # try to find an augmenting path
    path = findAugmentingPath(G, M) # O(n^4) -> O(nm)
    if path == None: # O(1)
        # no augmenting path found => M is a maximum matching
        for blossom in G.blossoms: # doen we max O(n) keer; dus O(n^4) in totaal. 
            M = liftBlossom(G, M, blossom) # functie is O(n^3)
        return M # O(1)
    else:
        # invert the path to increase the matching
        M = invertPath(M, path) # O(n^3)
        # recurse to find another augmenting path
        return findMaxMatching(G, M) # recursion of max O(n) times
    
# Goal: find an augmenting path
# Running time: worst case we have a recursion of O(n) times, a total of O(n^4)
def findAugmentingPath(G, M):
    # create empty forest
    forest = Forest() # O(1)
    # update the markings of the edges
    marked = {} # O(1)
    for v in G.edges: # total of O(n^2)
        for w in G.edges[v]: # O(n)
            if w>v:
                marked[(v,w)] = False  # O(1)
            else:
                marked[(w,v)] = False # O(1)
    for v in M.edges: # total of O(n^2)
        for w in M.edges[v]: # O(n)
            if w>v:
                marked[(v,w)] = True # O(1)
            else:
                marked[(w,v)] = True # O(1)

    # create trees for all exposed vertices
    for v in G.vertices: # runs O(n) times so total of O(n^2)
        if exposed(v, M): # O(n)
            # v is exposed => add it to the forest
            forest.trees.add(Tree(v))  # O(n)
            forest.vertices.add(v) # O(n)
            # undo any tree structure of previous runs
            v.parent = v # O(1)
    
    # find an augmenting path
    # Running time: in the worst case we find a blossom in each iteration of the recursion,
    # Each recursion takes O(n^3) (always finding another blossom), for a total run time of O(n^4)
    while forest.vertices != set(): 
        v = forest.vertices.pop() # O(1)
        # pick an unmarked vertex in the forest
        if distance(v, root(v)) % 2 == 1: # O(n)
            # do nothing
            pass
        else: 
            # tree = forest.trees.pop()
            # v = tree.root 
            for e in  G.get_neighbors(v):  # this together with the while forst creates a loop past all edges
                edge = tuple(sorted((v.name, e))) # O(1)
                if not marked[edge]: # O(n)
                    # pick an unmarked edge incident to v
                    w = G.get_vertex(e) # O(n)
                    if w in forest.vertices: # O(n)
                        if distance(w, root(w))%2 == 1: # O(n)
                            # should never get here
                            pass 
                        else:
                            if root(v) != root(w): # O(n)
                                # found an augmenting path
                                return augmentingPath(v, w) # O(n)
                            else:
                                # found a blossom
                                blossom = findBlossom(v, w, G, M) # O(n^2)
                                G.blossoms.append(blossom) # O(1)
                                G, M = contract(G, M, blossom) # O(n^3)
                                return findAugmentingPath(G, M) # recursion of max O(n) times
                                #path = liftBlossom(G, M, blossom) # O(n^2)
                                #return path
                    else:
                        # w is matched, so add e and w matched edge to the forest
                        forest.add(v, w) # O(n)
                        # get the edge from M
                        matchedVertex = M.get_vertex(M.edges[w.name][0]) # O(n)
                        forest.add(w, matchedVertex) # O(n)
                # mark e
                marked[edge] = True # O(1)
            # mark v
            marked[v] = True # O(1)
    # no augmenting path found
    return None