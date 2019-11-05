class Graph:
	def __init__(self,graph):
		self.graph = graph
		self.n = len(graph)

	def BFS(self,s, t, parent):
		visited =[False]*(self.n)
		queue=[]
		queue.append(s)
		visited[s] = True
		while queue:
			u = queue.pop(0)
			for ind, val in enumerate(self.graph[u]):
				if visited[ind] == False and val > 0 :
					queue.append(ind)
					visited[ind] = True
					parent[ind] = u
		return True if visited[t] else False

	def FordFulkerson(self, source, sink):
		parent = [-1]*(self.n)
		max_flow = 0
		print("augmenting paths:")
		while self.BFS(source, sink, parent) :
			path = []
			path_flow = float("Inf")
			s = sink
			while(s != source):
				path_flow = min (path_flow, self.graph[parent[s]][s])
				s = parent[s]
			max_flow += path_flow
			v = sink
			path.append(v)
			while(v != source):
				u = parent[v]
				path.append(u)
				self.graph[v][u] += path_flow
				self.graph[u][v] -= path_flow
				v = parent[v]
			path.reverse()
			print(path)
			print(path_flow)
			print(self.graph)
		return max_flow

graph = [[0, 16, 0, 0, 0, 13],
		[0, 0, 12, 0, 0, 0],
		[0, 0, 0, 20, 4, 9],
		[0, 0, 0, 0, 0, 0],
		[0, 0, 7, 4, 0, 10],
		[0, 4, 0, 0, 14, 0]]
g = Graph(graph)
source = 0; sink = 3
print ("The maximum possible flow is %d " % g.FordFulkerson(source, sink))
