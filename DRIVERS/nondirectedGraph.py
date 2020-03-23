# nondirected graph class
class NDGraph:

    def __init__(self, dict=None):
        if dict is None:
            dict = {}
        self.graph = dict
        self.nodes = list(dict.keys())

    def add_edge(self,u,v,cost=1):
        self.add_edge_util(v,u,cost)
        self.add_edge_util(u,v,cost)

    def add_edge_util(self,u,v,cost):
        e = Edge(v,cost)
        if u not in self.graph.keys():
            self.graph[u] = [e]
            self.nodes.append(u)
        else:
            self.graph[u].append(e)

    def remove_edge(self,u,v,cost=1):
        self.remove_edge_util(u,v,cost)
        self.remove_edge_util(v,u,cost)

    def remove_edge_util(self,u,v,cost):
        counter = []
        for e in self.graph[u]:
            if e.where == v :
                counter.append(e)
        if len(counter) == 0:
            raise Exception(f"Nodes {u, v} not connected")
        else:
            for e in counter:
                if e.val == cost:
                    self.graph[u].remove(e)

    def costofedge(self,u,v):
        for e in self.graph[u]:
            if e.where == v:
                return e.val

    # def add_vertice(self,n):
    #     if n in self.graph.keys():
    #         raise Exception("Following node already exists")
    #     else:
    #         self.graph[n] = []
    #         self.nodes.append(n)

    def remove_vertice(self,n):

        if n in self.graph.keys():
            raise Exception("Following node doesn't exist")
        else:
            for node in self.graph[n]:
                self.graph[node].remove(n)
            del self.graph[n]
            self.nodes.remove(n)

    def numberofnodes(self):
        return len(self.graph.keys())

    def getconnected(self,u):
        con = []
        for e in self.graph[u]:
            con.append(e.where)
        return con

    def getnodes(self):
        return self.nodes

    def getdegree(self,u):
        return len(self.graph[u])

    def getnumberedges(self):
        # little brute force aint killed nbd
        s = 0
        for n in self.nodes:
            s += len(self.graph[n])
        return int(s/2)

class Edge:

    def __init__(self,where,val):
        self.where = where
        self.val = val









