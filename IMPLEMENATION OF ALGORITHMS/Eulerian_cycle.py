import copy,DFS


def fleurysalgorithm(g,starter):

    for n in g.nodes:
        if g.getdegree(n)%2: # meaning equal to 1
            raise Exception("Graph is not Eulerian")
    g_copy = copy.deepcopy(g)
    path = [starter]
    acc = starter
    while g_copy.getnumberedges()>0:
        w = copy.deepcopy(g_copy.getconnected(acc))
        if len(w) == 1:
            # if we have only one way to go, then we have no choice whatsoever
            path.append(w[0])
            c = g_copy.costofedge(acc,w[0])
            g_copy.remove_edge(acc,w[0],c)
            acc = w[0]
        else:
            reachable = DFS.DFS(g_copy,acc)
            for el in w:
                c = g_copy.costofedge(el,acc)
                g_copy.remove_edge(acc,el,c)
                now_reachable = DFS.DFS(g_copy,acc)
                if reachable == now_reachable:
                    path.append(el)
                    acc = el
                    break
                else:
                    g_copy.add_edge(acc,el,c)
    return path










