class Graph():
    def __init__(self, V):
        self.V=V
        self.graph=[[0 for column in range(V)]for row in range(V)]

        self.colorarr=[-1 for i in range(self.V)]

    def bipartitechk(self,src):
        q=[]
        q.append(src)
        while q:
            u=q.pop()
            if self.graph[u][u]==1:
                return False
        
            for v in range(self.V):
                if self.graph[u][v]==1 and self.colorarr[v]==-1:
                    self.colorarr[v]=1-self.colorarr[u]
                    q.append(v)
                elif self.graph[u][v]==1 and self.colorarr[v]==self.colorarr[u]:
                    return False
        return True
    
    def isBipartite(self):
        #self.colorarr=[-1 for i in range(self.V)]
        for i in range(self.V):
            if self.colorarr[i]==-1:
                if not self.bipartitechk(i):
                    return False
        return True

g=Graph(4)
g.graph=[[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]]

if g.isBipartite():
    print("YES")
else:
    print("NO")