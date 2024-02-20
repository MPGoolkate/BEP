import unittest
from edmonds_v3_1 import findMaxMatching, Graph, Vertex

class Testing(unittest.TestCase):

    def test_normal_path(self):
        G = Graph()
        M = Graph()
        for i in range(4):
            G.add_vertex(Vertex(i))
            M.add_vertex(G.get_vertex(i))

        G.add_edge(G.get_vertex(0), G.get_vertex(1))
        G.add_edge(G.get_vertex(1), G.get_vertex(2))
        G.add_edge(G.get_vertex(3), G.get_vertex(2))

        res = findMaxMatching(G, M)
        print("Matching1 0:", ", ".join(str(obj.name) for obj in res.edges[0]), " \n")
        print("Matching1 1:", ", ".join(str(obj.name) for obj in res.edges[1]), " \n")
        print("Matching1 2:", ", ".join(str(obj.name) for obj in res.edges[2]), " \n")
        print("Matching1 3:", ", ".join(str(obj.name) for obj in res.edges[3]), " \n")
        
        self.assertEqual(res.count_matching()/2, 2)

    def test_normal_path2(self):
        G = Graph()
        M = Graph()
        for i in range(4):
            G.add_vertex(Vertex(i))
            M.add_vertex(G.get_vertex(i))

        G.add_edge(G.get_vertex(0), G.get_vertex(1))
        G.add_edge(G.get_vertex(1), G.get_vertex(2))
        G.add_edge(G.get_vertex(3), G.get_vertex(2))
        # ensure that a path inversion should occur

        # M.add_vertex(G.get_vertex(1))
        # M.add_vertex(G.get_vertex(2))
        M.add_edge(M.get_vertex(1), M.get_vertex(2))
        res2 = findMaxMatching(G, M)
        self.assertEqual(res2.count_matching()/2, 2)
        
    
    def test_blossom_at_one_end(self):
        G = Graph()
        M = Graph()
        for i in range(4):
            G.add_vertex(Vertex(i))
            M.add_vertex(G.get_vertex(i))

        G.add_edge(G.get_vertex(0), G.get_vertex(1))
        G.add_edge(G.get_vertex(1), G.get_vertex(2))
        G.add_edge(G.get_vertex(1), G.get_vertex(3))
        G.add_edge(G.get_vertex(3), G.get_vertex(2))

        res = findMaxMatching(G, M)
        print("Matching1 0:", ", ".join(str(obj.name) for obj in res.edges[0]), " \n")
        print("Matching1 1:", ", ".join(str(obj.name) for obj in res.edges[1]), " \n")
        print("Matching1 2:", ", ".join(str(obj.name) for obj in res.edges[2]), " \n")
        print("Matching1 3:", ", ".join(str(obj.name) for obj in res.edges[3]), " \n")
        
        self.assertEqual(res.count_matching()/2, 2)

    def test_blossom_at_one_end2(self):
        G = Graph()
        M = Graph()
        for i in range(4):
            G.add_vertex(Vertex(i))
            M.add_vertex(G.get_vertex(i))
        G.add_edge(G.get_vertex(0), G.get_vertex(1))
        G.add_edge(G.get_vertex(1), G.get_vertex(2))
        G.add_edge(G.get_vertex(1), G.get_vertex(3))
        G.add_edge(G.get_vertex(3), G.get_vertex(2))

        # ensure that a blossom should occur
        M.add_edge(M.get_vertex(1), M.get_vertex(2))
        res2 = findMaxMatching(G, M)
        print("Matching1 0:", ", ".join(str(obj.name) for obj in res2.edges[0]), " \n")
        print("Matching1 1:", ", ".join(str(obj.name) for obj in res2.edges[1]), " \n")
        print("Matching1 2:", ", ".join(str(obj.name) for obj in res2.edges[2]), " \n")
        print("Matching1 3:", ", ".join(str(obj.name) for obj in res2.edges[3]), " \n")
        
        self.assertEqual(res2.count_matching()/2, 2)

    def test_blossom_at_both_ends(self):
        G = Graph()
        M = Graph()
        for i in range(6):
            G.add_vertex(Vertex(i))
            M.add_vertex(G.get_vertex(i))

        G.add_edge(G.get_vertex(0), G.get_vertex(1))
        G.add_edge(G.get_vertex(1), G.get_vertex(2))
        G.add_edge(G.get_vertex(0), G.get_vertex(2))
        G.add_edge(G.get_vertex(1), G.get_vertex(3))
        G.add_edge(G.get_vertex(5), G.get_vertex(3))
        G.add_edge(G.get_vertex(4), G.get_vertex(3))
        G.add_edge(G.get_vertex(4), G.get_vertex(5))

        res = findMaxMatching(G, M)
        
        self.assertEqual(res.count_matching()/2, 3)

    def test_blossom_at_both_ends2(self):
        print("!!!test\n")
        # ensure that a blossom should occur
        G = Graph()
        M = Graph()
        for i in range(6):
            G.add_vertex(Vertex(i))
            M.add_vertex(G.get_vertex(i))
        
        G.add_edge(G.get_vertex(0), G.get_vertex(1))
        G.add_edge(G.get_vertex(1), G.get_vertex(2))
        G.add_edge(G.get_vertex(0), G.get_vertex(2))
        G.add_edge(G.get_vertex(1), G.get_vertex(3))
        G.add_edge(G.get_vertex(5), G.get_vertex(3))
        G.add_edge(G.get_vertex(4), G.get_vertex(3))
        G.add_edge(G.get_vertex(4), G.get_vertex(5))

        M.add_edge(G.get_vertex(0), G.get_vertex(1))
        res2 = findMaxMatching(G, M)
        print("Matching 0:", ", ".join(str(obj.name) for obj in res2.edges[0]), " \n")
        print("Matching 1:", ", ".join(str(obj.name) for obj in res2.edges[1]), " \n")
        print("Matching 2:", ", ".join(str(obj.name) for obj in res2.edges[2]), " \n")
        print("Matching 3:", ", ".join(str(obj.name) for obj in res2.edges[3]), " \n")
        print("Matching 4:", ", ".join(str(obj.name) for obj in res2.edges[4]), " \n")
        print("Matching 5:", ", ".join(str(obj.name) for obj in res2.edges[5]), " \n")

        self.assertEqual(res2.count_matching()/2, 3)
        print("!!!einde test\n")

    def test_blossom_middle(self):
        G = Graph()
        M = Graph()
        for i in range(8):
            G.add_vertex(Vertex(i))
            M.add_vertex(G.get_vertex(i))

        G.add_edge(G.get_vertex(0), G.get_vertex(7))
        G.add_edge(G.get_vertex(1), G.get_vertex(2))
        G.add_edge(G.get_vertex(2), G.get_vertex(3))
        G.add_edge(G.get_vertex(3), G.get_vertex(4))
        G.add_edge(G.get_vertex(5), G.get_vertex(3))
        G.add_edge(G.get_vertex(4), G.get_vertex(7))
        G.add_edge(G.get_vertex(5), G.get_vertex(6))
        G.add_edge(G.get_vertex(7), G.get_vertex(6))

        res = findMaxMatching(G, M)
        self.assertEqual(res.count_matching()/2, 4)

    def test_blossom_middle2(self):
        G = Graph()
        M = Graph()
        for i in range(8):
            G.add_vertex(Vertex(i))
            M.add_vertex(G.get_vertex(i))

        G.add_edge(G.get_vertex(0), G.get_vertex(7))
        G.add_edge(G.get_vertex(1), G.get_vertex(2))
        G.add_edge(G.get_vertex(2), G.get_vertex(3))
        G.add_edge(G.get_vertex(3), G.get_vertex(4))
        G.add_edge(G.get_vertex(5), G.get_vertex(3))
        G.add_edge(G.get_vertex(4), G.get_vertex(7))
        G.add_edge(G.get_vertex(5), G.get_vertex(6))
        G.add_edge(G.get_vertex(7), G.get_vertex(6))


        # ensure that a blossom should occur
        M.add_edge(G.get_vertex(2), G.get_vertex(3))
        M.add_edge(G.get_vertex(5), G.get_vertex(6))
        M.add_edge(G.get_vertex(4), G.get_vertex(7))
        res2 = findMaxMatching(G, M)
        #print("Matching", ", ".join(str(obj.name) for obj in res2.edges), " \n")
        self.assertEqual(res2.count_matching()/2, 4)

    def test_recursion_blossom(self):
        G = Graph()
        M = Graph()
        for i in range(10):
            G.add_vertex(Vertex(i))
            M.add_vertex(G.get_vertex(i))

        G.add_edge(G.get_vertex(0), G.get_vertex(1))
        G.add_edge(G.get_vertex(1), G.get_vertex(2))
        G.add_edge(G.get_vertex(2), G.get_vertex(3))
        G.add_edge(G.get_vertex(2), G.get_vertex(4))
        G.add_edge(G.get_vertex(4), G.get_vertex(6))
        G.add_edge(G.get_vertex(3), G.get_vertex(5))
        G.add_edge(G.get_vertex(5), G.get_vertex(6))
        G.add_edge(G.get_vertex(5), G.get_vertex(7))
        G.add_edge(G.get_vertex(7), G.get_vertex(8))
        G.add_edge(G.get_vertex(8), G.get_vertex(9))
        G.add_edge(G.get_vertex(9), G.get_vertex(6))
    
        res = findMaxMatching(G, M)
        self.assertEqual(res.count_matching()/2, 5)
    
    def test_recursion_blossom2(self):
        G = Graph()
        M = Graph()
        for i in range(10):
            G.add_vertex(Vertex(i))
            M.add_vertex(G.get_vertex(i))

        G.add_edge(G.get_vertex(0), G.get_vertex(1))
        G.add_edge(G.get_vertex(1), G.get_vertex(2))
        G.add_edge(G.get_vertex(2), G.get_vertex(3))
        G.add_edge(G.get_vertex(2), G.get_vertex(4))
        G.add_edge(G.get_vertex(4), G.get_vertex(6))
        G.add_edge(G.get_vertex(3), G.get_vertex(5))
        G.add_edge(G.get_vertex(5), G.get_vertex(6))
        G.add_edge(G.get_vertex(5), G.get_vertex(7))
        G.add_edge(G.get_vertex(7), G.get_vertex(8))
        G.add_edge(G.get_vertex(8), G.get_vertex(9))
        G.add_edge(G.get_vertex(9), G.get_vertex(6))

        # ensure that a blossom in a blossom should occur
        M.add_edge(G.get_vertex(1), G.get_vertex(2))
        M.add_edge(G.get_vertex(5), G.get_vertex(3))
        M.add_edge(G.get_vertex(7), G.get_vertex(8))
        M.add_edge(G.get_vertex(6), G.get_vertex(9))
        res2 = findMaxMatching(G, M)
        self.assertEqual(res2.count_matching()/2, 5)

if __name__ == '__main__':
    unittest.main()