"""
@author: Anas Temouden
@Date: 15-11-2023
@Title: Kruskal's Algorithm using Union-Find Data Structure
""" 
from collections import defaultdict
 
 
class Graph():
    def __init__(self, vertices):
        """ Constructor of graph class """
        self.E = {}
        self.V = vertices
 
    def addEdge(self, u, v, w):
        """ Add an edge to the graph """
        self.E[(u, v)] = w
    
    def isCyclic (self):
        """ Check if the graph contains a cycle"""
        parent = dict()
        rank = dict()
        for v in range(self.V):
            parent[v] = v
            rank[v] = 0
        for e in self.E:
            x = self.find(parent, e[0])
            y = self.find(parent, e[1])
            if x == y:
                return True
            self.union(parent, rank, x, y)
        return False
    
    def find(self, parent, i):
        """ Find the parent (set representative) of an element i """
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    
    def union(self, parent, rank, x, y):
        """ Union of two sets x and y """
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else :
            parent[yroot] = xroot
            rank[xroot] += 1

    def Kuruskal(self):
        """ Kruskal's algorithm to find the minimum spanning tree """
        sorted_edges = sorted(self.E.items(), key=lambda x: x[1])
        mst = Graph(self.V)
        for e in sorted_edges:
            mst.addEdge(e[0][0], e[0][1], e[1])
            if mst.isCyclic():
                mst.E.pop(e[0])
        
        cost = 0
        for e in mst.E:
            cost += mst.E[e]
        print("Cost: ", cost)
        return mst.E
    

if __name__ == "__main__":
    g = Graph(9)
    g.addEdge(0, 1, 4)
    g.addEdge(1,2,8)
    g.addEdge(2,3,7)
    g.addEdge(3,4,9)
    g.addEdge(4,5,10)
    g.addEdge(5,6,2)
    g.addEdge(6,7,1)
    g.addEdge(7,0,8)
    g.addEdge(7,1,11)
    g.addEdge(7,8,7)
    g.addEdge(8,6,6)
    g.addEdge(8,2,2)
    g.addEdge(2,5,4)
    g.addEdge(3,5,14) 
    print(g.Kuruskal())

    print("=====================================")

    g2 = Graph(4)
    g2.addEdge(0, 1, 10)
    g2.addEdge(0, 2, 6)
    g2.addEdge(0, 3, 5)
    g2.addEdge(1, 3, 15)
    g2.addEdge(2, 3, 4)
    print(g2.Kuruskal())



