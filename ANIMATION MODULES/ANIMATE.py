import matplotlib.pyplot as plt
import matplotlib.animation as A
import graph_painter,Eulerian_cycle,DijkstrapathFinder


def saving(sc,a):
    plt.rcParams['animation.ffmpeg_path'] = 'C:\\Python36\\tam\\ffmpeg-20200315-c467328-win64-static\\bin\\ffmpeg.exe'
    FFwriter = A.FFMpegWriter(fps=3, extra_args=['-vcodec', 'libx264'])
    a.save(sc + ".mp4", writer=FFwriter)

def run_anim_eu(g,sc,starter):

    pos,fig = graph_painter.paint_graph(g)
    eu = Eulerian_cycle.fleurysalgorithm(g, starter)
    plt.title(f"EULER'S CIRCUT PATH FINDER STARTING FROM VERTEX {starter}")
    anim = A.FuncAnimation(fig,nextframe,3*len(eu)-3,fargs=(eu,pos,fig))
    saving(sc,anim)

def run_anim_dj(g,sc,a,b):

    pos, fig = graph_painter.paint_graph(g)
    r,CO = DijkstrapathFinder.shortestDijkstra(g,a,b)
    plt.title(f"LOWEST-COST PATH FROM NODE {a} TO NODE {b} (cost={CO})")
    anim = A.FuncAnimation(fig,nextframe,3*len(r)-3,fargs=(r,pos,fig))
    saving(sc,anim)


def nextframe(frame_number,path,posi,fig):

    p1 = posi[path[(frame_number)//3]]
    p2 = posi[path[(frame_number+3)//3]]
    plt.plot([p1[0],p2[0]],[p1[1],p2[1]],color="g",figure=fig,linewidth=4)
    frame_number += 1
    return fig