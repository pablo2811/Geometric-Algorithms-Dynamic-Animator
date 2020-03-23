import nondirectedGraph,ANIMATE


def runEuler(g):
    s = int(input("Insert starting node for Fleury's alg"))
    sc = input("Insert name of a file in which the animation of Fluery's will be saved.\n")
    ANIMATE.run_anim_eu(g, sc,s)

def runDijkstra(g):
    a = int(input("Insert starting node."))
    b = int(input("Insert finish node."))
    sc = input("Insert name of a file in which the animation of Dijkstra will be saved.\n")
    ANIMATE.run_anim_dj(g, sc,a,b)

def main():

    g = nondirectedGraph.NDGraph()
    print("----- pass edges beetwen vertices in the following way -----")
    print(" Id_start_vertex Id_end_vertex")
    print("If such vertex doesn't yet exist (or both of them), they will be created and connected.")
    n = int(input("how many edges?\n"))
    for i in range(n):
        line = input().split(" ")
        if len(line) == 3:
            g.add_edge(int(line[0]), int(line[1]),float(line[2]))
        else:
            g.add_edge(int(line[0]), int(line[1]))

    print("1 - compute dynamical animation of finding Euler's circut in the given Euler's graph (using Fluery's Algorithm)")
    print("2 - compute dynamical Dijkstra shortest path finder animation (using extended Dijkstra Algorithm)")
    print("3 - run both")
    z = int(input())
    if z == 1:
        runEuler(g)
    elif z == 2:
        runDijkstra(g)
    else:
        runEuler(g)
        runDijkstra(g)

if __name__ == "__main__":
    main()
