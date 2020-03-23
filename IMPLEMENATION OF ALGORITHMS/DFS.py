
def DFS(G,node):
    nodes = G.getnodes()
    visited = {}
    for n in nodes:
        visited[n] = False #trying to avoid the need to id nodes from 1..n
    DFS_util(G,node,visited)
    return list(visited.values()).count(True) - 1

def DFS_util(G,curr,visited):

    con = G.getconnected(curr)
    visited[curr] = True
    for n in con:
        if not visited[n]:
            DFS_util(G,n,visited)

