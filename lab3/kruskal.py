import fileinput
import re

class Kruskal:
    def __init__(self):
        self.uf = UnionFind()
        self.edges = set([])

    def add_node(self, u):
        self.uf.add(u)

    def add_edge(self, u, v, w):
        self.edges.add((u, v, w))

    def minimum_spanning_tree(self):
        minimum_spanning_tree = set([])
        total_weight = 0
        edges_sorted_by_weight = sorted(self.edges, key=lambda u: u[2])
        for u, v, w in edges_sorted_by_weight:
            if (self.uf.find(u) != self.uf.find(v)):
                self.uf.union(u, v)
                minimum_spanning_tree.add((u, v, w))
                total_weight += w
        return minimum_spanning_tree, total_weight

class UnionFind:
    def __init__(self):
        self.parent = {}

    def add(self, u):
        self.parent[u] = u

    def find(self, u):
        if self.parent[u] == u:
            return u
        return self.find(self.parent[u])

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_u] = root_v

if __name__ == '__main__':
    kruskal = Kruskal()
    stdin = fileinput.input()
    regex = re.compile(r'"?(.*?)"?--"?(.*?)"?\s\[(.*?)\]')
    for line in stdin:
        line = line.strip()
        if '--' in line:
            data = re.search(regex, line)
            u, v, w = data.group(1), data.group(2), int(data.group(3))
            kruskal.add_edge(u, v, w)
        else:
            kruskal.add_node(line.translate(None, '\n"'))
    minimum_spanning_tree, total_weight = kruskal.minimum_spanning_tree()
    print total_weight
