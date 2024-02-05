import unittest
from edmonds_v2_copy import findMaxMatching, Graph, Vertex

class Testing(unittest.TestCase):

    def test_normal_path(self):
        G = Graph()
        for i in range(4):
            G.add_vertex(Vertex(i))

        G.add_edge(G.get_vertex(0), G.get_vertex(1))
        G.add_edge(G.get_vertex(1), G.get_vertex(2))
        G.add_edge(G.get_vertex(3), G.get_vertex(2))

        M = Graph()
        res = findMaxMatching(G, M)
        self.assertEqual(len(res.vertices)/2, 2)

        # ensure that a path inversion should occur
        M.add_edge(M.get_vertex(1), M.get_vertex(2))
        res2 = findMaxMatching(G, M)
        self.assertEqual(len(res2.vertices)/2, 2)
        
    
    def test_blossom_at_one_end(self):
        print("starting test 2")
        G = Graph()
        for i in range(4):
            G.add_vertex(Vertex(i))

        G.add_edge(G.get_vertex(0), G.get_vertex(1))
        G.add_edge(G.get_vertex(1), G.get_vertex(2))
        G.add_edge(G.get_vertex(1), G.get_vertex(3))
        G.add_edge(G.get_vertex(3), G.get_vertex(2))

        M = Graph()
        res = findMaxMatching(G, M)
        self.assertEqual(len(res.vertices)/2, 2)

        # ensure that a blossom should occur
        M.add_edge(M.get_vertex(1), M.get_vertex(2))
        res2 = findMaxMatching(G, M)
        self.assertEqual(len(res2.vertices)/2, 2)
        print("finished test 2")

    def test_blossom_at_both_ends(self):
        G = Graph()
        for i in range(6):
            G.add_vertex(Vertex(i))

        G.add_edge(G.get_vertex(0), G.get_vertex(1))
        G.add_edge(G.get_vertex(1), G.get_vertex(2))
        G.add_edge(G.get_vertex(0), G.get_vertex(2))
        G.add_edge(G.get_vertex(1), G.get_vertex(3))
        G.add_edge(G.get_vertex(5), G.get_vertex(3))
        G.add_edge(G.get_vertex(4), G.get_vertex(3))
        G.add_edge(G.get_vertex(4), G.get_vertex(5))

        M = Graph()
        res = findMaxMatching(G, M)
        self.assertEqual(len(res.vertices)/2, 3)

        # ensure that a blossom should occur
        G = Graph()
        M = Graph()
        for i in range(6):
            G.add_vertex(Vertex(i))
        
        G.add_edge(G.get_vertex(0), G.get_vertex(1))
        G.add_edge(G.get_vertex(1), G.get_vertex(2))
        G.add_edge(G.get_vertex(0), G.get_vertex(2))
        G.add_edge(G.get_vertex(1), G.get_vertex(3))
        G.add_edge(G.get_vertex(5), G.get_vertex(3))
        G.add_edge(G.get_vertex(4), G.get_vertex(3))
        G.add_edge(G.get_vertex(4), G.get_vertex(5))

        M.add_vertex(G.get_vertex(0))
        M.add_vertex(G.get_vertex(1))
        M.add_edge(G.get_vertex(0), G.get_vertex(1))
        res2 = findMaxMatching(G, M)
        self.assertEqual(len(res2.vertices)/2, 3)

    def test_blossom_middle(self):
        G = Graph()
        for i in range(8):
            G.add_vertex(Vertex(i))

        G.add_edge(G.get_vertex(0), G.get_vertex(7))
        G.add_edge(G.get_vertex(1), G.get_vertex(2))
        G.add_edge(G.get_vertex(2), G.get_vertex(3))
        G.add_edge(G.get_vertex(3), G.get_vertex(4))
        G.add_edge(G.get_vertex(5), G.get_vertex(3))
        G.add_edge(G.get_vertex(4), G.get_vertex(7))
        G.add_edge(G.get_vertex(5), G.get_vertex(6))
        G.add_edge(G.get_vertex(7), G.get_vertex(6))

        M = Graph()
        res = findMaxMatching(G, M)
        self.assertEqual(len(res.vertices)/2, 4)

        # ensure that a blossom should occur
        M.add_vertex(G.get_vertex(2))
        M.add_vertex(G.get_vertex(3))
        M.add_edge(G.get_vertex(2), G.get_vertex(3))
        M.add_vertex(G.get_vertex(5))
        M.add_vertex(G.get_vertex(6))
        M.add_edge(G.get_vertex(5), G.get_vertex(6))
        M.add_vertex(G.get_vertex(4))
        M.add_vertex(G.get_vertex(7))
        M.add_edge(G.get_vertex(4), G.get_vertex(7))
        res2 = findMaxMatching(G, M)
        self.assertEqual(len(res2.vertices)/2, 4)

    def test_recursion_blossom(self):
        G = Graph()
        for i in range(10):
            G.add_vertex(Vertex(i))

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

        M = Graph()
        res = findMaxMatching(G, M)
        self.assertEqual(len(res.vertices)/2, 5)

        # ensure that a blossom in a blossom should occur
        M.add_vertex(G.get_vertex(1))
        M.add_vertex(G.get_vertex(2))
        M.add_edge(G.get_vertex(1), G.get_vertex(2))
        M.add_vertex(G.get_vertex(3))
        M.add_vertex(G.get_vertex(5))
        M.add_edge(G.get_vertex(5), G.get_vertex(3))
        M.add_vertex(G.get_vertex(8))
        M.add_vertex(G.get_vertex(7))
        M.add_edge(G.get_vertex(7), G.get_vertex(8))
        M.add_vertex(G.get_vertex(6))
        M.add_vertex(G.get_vertex(9))
        M.add_edge(G.get_vertex(6), G.get_vertex(9))
        res2 = findMaxMatching(G, M)
        self.assertEqual(len(res2.vertices)/2, 5)

if __name__ == '__main__':
    unittest.main()