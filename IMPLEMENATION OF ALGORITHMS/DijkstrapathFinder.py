
class Traversed_node:

    def __init__(self,fr,val,id):
        self.fr = fr
        self.val = val
        self.id = id

def isonlist(sh_const,node_id):

    i = 0
    for el in sh_const:
        if el.id == node_id:
            return i
        i += 1
    return -1

def update_pos(sh_temp,i):

    val = sh_temp[i].val
    for k in range(i+1,len(sh_temp)):
        if sh_temp[k].val <= val:
            break
        else:
            sh_temp[k],sh_temp[k-1] = sh_temp[k-1],sh_temp[k]

def insert_pos(sh_temp,t):
    if not len(sh_temp):
        sh_temp.append(t)
        return
    elif len(sh_temp) == 1:
        sh_temp.append(t)
        if sh_temp[0].val <= t.val:
            sh_temp[0],sh_temp[1] = sh_temp[1],sh_temp[0]
    else:
        # at least 2 els
        sh_temp.append(t)
        for k in range(len(sh_temp)-2,-1,-1):
            if sh_temp[k].val <= t.val:
                sh_temp[k],sh_temp[k+1] = sh_temp[k+1], sh_temp[k]
            else:
                break

def shortestDijkstra(g,a,b):

    st = Traversed_node(None,0,a)
    sh_temp = []
    sh_const = [st]

    while isonlist(sh_const,b) == -1 :
        acc = sh_const[-1]
        nei = g.getconnected(acc.id)
        for el in nei:
            i = isonlist(sh_temp,el)
            k = isonlist(sh_const,el)
            if k == -1:
                if i != - 1:
                    akt_cost = g.costofedge(el,acc.id) + acc.val
                    if sh_temp[i].val > akt_cost:
                        sh_temp[i].fr = acc.id
                        sh_temp[i].val = akt_cost
                        update_pos(sh_temp,i)
                else:
                    t = Traversed_node(acc.id,acc.val + g.costofedge(el,acc.id),el)
                    insert_pos(sh_temp,t)
        sh_const.append(sh_temp[-1])
        sh_temp.remove(sh_temp[-1])

    p = sh_const[isonlist(sh_const,b)]
    co = p.val
    path = [p.id]
    while p != st :
        path.append(p.fr)
        p = sh_const[isonlist(sh_const,p.fr)]

    return path[::-1],co








