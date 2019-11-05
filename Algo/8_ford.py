class Graph:
    def __init__(self,graph):
        self.graph=graph
        self.ROW=len(graph)

    def bfs(self,s,t,par):
        v=[False]*(self.ROW)
        q=[]
        q.append(s)
        v[s]=True
        while q:
            u=q.pop()
            for i,val in enumerate(self.graph[u]):
                if v[i]==False and val>0:
                    q.append(i)
                    v[i]=True
                    par[i]=u
        return True if v[t] else False
    
    def ford(self,source,sink):
        par=[-1]*(self.ROW)
        max_flow=0
        while self.bfs(source,sink,par):
            path_flow=float("Inf")
            s=sink
            while(s!=source):
                path_flow=min(path_flow,self.graph[par[s]][s])
                s=par[s]
            max_flow+=path_flow
            v = sink 
            while(v !=  source): 
                u = par[v] 
                self.graph[u][v] -= path_flow 
                self.graph[v][u] += path_flow 
                v = par[v]
        return max_flow


#driver
graph = [[0, 16, 13, 0, 0, 0], 
        [0, 0, 10, 12, 0, 0], 
        [0, 4, 0, 0, 14, 0], 
        [0, 0, 9, 0, 0, 20], 
        [0, 0, 0, 7, 0, 4], 
        [0, 0, 0, 0, 0, 0]] 
  
g = Graph(graph)

source=0
sink=5
print("Max. Flow=",g.ford(source,sink))