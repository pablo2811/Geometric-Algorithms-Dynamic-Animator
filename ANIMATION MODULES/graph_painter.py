import matplotlib.pyplot as plt
import random


# animate finding eulerian path from given vertice
def paint_graph(g):
    n = g.numberofnodes()
    nd = g.getnodes()
    d = {}
    fig = plt.figure(figsize=(12,8))
    for i in range(n):
        x = random.randint(-15*n,15*n)
        y = random.randint(-15*n,15*n)
        d[nd[i]] = (x,y)
        ver = random.uniform(-n/2,n/2)
        hor = random.uniform(-n/2,n/2)
        plt.scatter(x,y,c='red',figure=fig,linewidths=6)
        plt.text(x+ver,y+hor,str(nd[i]),figure=fig)
    s = set()
    for node in g.getnodes():
        for con in g.getconnected(node):
            key1 = str(node)+"|"+str(con)
            key2 = str(con)+"|"+str(node)
            if key1 not in s:
                s.add(key1)
                s.add(key2)
                plt.plot([d[node][0],d[con][0]],[d[node][1], d[con][1]],color="black",figure=fig)
                z = random.uniform(-n,n)
                plt.text((d[node][0]+d[con][0])/2 + z,(d[node][1]+d[con][1])/2 + z,str(g.costofedge(node,con)),figure=fig)
    plt.axis(visible=False,figure=fig)
    plt.savefig("GRAPH.png",figure=fig)
    return d,fig

