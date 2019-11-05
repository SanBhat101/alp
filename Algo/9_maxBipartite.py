class BiPartite:
    def __init__(self,graph):
        self.graph = graph
        self.ppl = len(graph)
        self.slots = len(graph[0])

    def bpm(self, u, matchR, seen):
        for v in range(self.slots):
            if self.graph[u][v] and seen[v] == False:
                seen[v] = True
                if matchR[v] == -1 or self.bpm(matchR[v],
                                               matchR, seen):
                    matchR[v] = u
                    return True
        return False

    def maxBPM(self):
        matchR = [-1] * self.slots
        result = 0
        for i in range(self.ppl):
            seen = [False] * self.slots
            if self.bpm(i, matchR, seen):
                result += 1
        return result

bpGraph =[[0, 1, 0, 1],
			[1, 0, 1, 0],
			[0, 1, 0, 1],
			[1, 0, 1, 0]
			]
g = BiPartite(bpGraph)

print ("Maximum number of applicants that can get job is %d " % g.maxBPM())
