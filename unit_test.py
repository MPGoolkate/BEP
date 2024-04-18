import unittest
from edmonds_v4_4 import findMaxMatching, Graph, Vertex

class Testing(unittest.TestCase):

    def test_normal_path(self):
        G = Graph()
        for i in range(4):
            G.add_vertex(Vertex(i))

        G.add_edge(G.get_vertex(0), G.get_vertex(1))
        G.add_edge(G.get_vertex(1), G.get_vertex(2))
        G.add_edge(G.get_vertex(3), G.get_vertex(2))

        res = findMaxMatching(G)
        
        self.assertEqual(res.count_matching()/2, 2)

    def test_normal_path2(self):
        G = Graph()
        for i in range(4):
            G.add_vertex(Vertex(i))

        G.add_edge(G.get_vertex(0), G.get_vertex(1))
        G.add_edge(G.get_vertex(1), G.get_vertex(2))
        G.add_edge(G.get_vertex(3), G.get_vertex(2))
        # ensure that a path inversion should occur

        # M.add_vertex(G.get_vertex(1))
        # M.add_vertex(G.get_vertex(2))
        G.matching = [-1, G.get_vertex(2), G.get_vertex(1), -1]
        res2 = findMaxMatching(G)
        self.assertEqual(res2.count_matching()/2, 2)
        
    
    def test_blossom_at_one_end(self):
        G = Graph()
        for i in range(4):
            G.add_vertex(Vertex(i))

        G.add_edge(G.get_vertex(0), G.get_vertex(1))
        G.add_edge(G.get_vertex(1), G.get_vertex(2))
        G.add_edge(G.get_vertex(1), G.get_vertex(3))
        G.add_edge(G.get_vertex(3), G.get_vertex(2))

        res = findMaxMatching(G)
        
        self.assertEqual(res.count_matching()/2, 2)

    def test_blossom_at_one_end2(self):
        G = Graph()
        for i in range(4):
            G.add_vertex(Vertex(i))
        G.add_edge(G.get_vertex(0), G.get_vertex(1))
        G.add_edge(G.get_vertex(1), G.get_vertex(2))
        G.add_edge(G.get_vertex(1), G.get_vertex(3))
        G.add_edge(G.get_vertex(3), G.get_vertex(2))

        # ensure that a blossom should occur
        G.matching = [-1, G.get_vertex(2), G.get_vertex(1), -1]
        res2 = findMaxMatching(G)
        
        self.assertEqual(res2.count_matching()/2, 2)

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

        res = findMaxMatching(G)
        
        self.assertEqual(res.count_matching()/2, 3)

    def test_blossom_at_both_ends2(self):
        # ensure that a blossom should occur
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

        G.matching = [G.get_vertex(1), G.get_vertex(0), -1, -1, -1, -1]
        res2 = findMaxMatching(G)

        self.assertEqual(res2.count_matching()/2, 3)

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

        res = findMaxMatching(G)
        self.assertEqual(res.count_matching()/2, 4)

    def test_blossom_middle2(self):
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


        # ensure that a blossom should occur
        G.matching = [-1, -1, G.get_vertex(3), G.get_vertex(2), G.get_vertex(7), G.get_vertex(5), G.get_vertex(6), G.get_vertex(4)]

        res2 = findMaxMatching(G)
        self.assertEqual(res2.count_matching()/2, 4)

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
    
        res = findMaxMatching(G)
        self.assertEqual(res.count_matching()/2, 5)
    
    def test_recursion_blossom2(self):
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

        # ensure that a blossom in a blossom should occur
        G.matching = [-1, G.get_vertex(2), G.get_vertex(1), G.get_vertex(5), -1, G.get_vertex(3),
                       G.get_vertex(9), G.get_vertex(8), G.get_vertex(7), G.get_vertex(6)]
        res2 = findMaxMatching(G)
        self.assertEqual(res2.count_matching()/2, 5)
    
    def test_big_blossom(self):
        G = Graph()
        for i in range(10):
            G.add_vertex(Vertex(i))

        G.add_edge(G.get_vertex(0), G.get_vertex(1))
        G.add_edge(G.get_vertex(1), G.get_vertex(2))
        G.add_edge(G.get_vertex(2), G.get_vertex(3))
        G.add_edge(G.get_vertex(3), G.get_vertex(4))
        G.add_edge(G.get_vertex(4), G.get_vertex(0))
        G.add_edge(G.get_vertex(3), G.get_vertex(5))
        G.add_edge(G.get_vertex(5), G.get_vertex(6))
        G.add_edge(G.get_vertex(6), G.get_vertex(7))
        G.add_edge(G.get_vertex(2), G.get_vertex(8))
        G.add_edge(G.get_vertex(8), G.get_vertex(9))
        G.add_edge(G.get_vertex(9), G.get_vertex(0))

        res = findMaxMatching(G)
        self.assertEqual(res.count_matching()/2, 5)

if __name__ == '__main__':
    unittest.main()