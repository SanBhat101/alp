import queue

arr=[]

n=int(input())
m=int(input())
for _ in range(n):
	tmp=list(map(int, input().split()))
	arr.append(tmp)
vis=[]
for i in range(n):
	tmp=[]
	for j in range(m):
		tmp.append(False)
	vis.append(tmp)
comp=0
for i in range(n):
	for j in range(m):
		if(not vis[i][j]):
			comp+=1
			q=queue.Queue(maxsize=100)
			q.put([i, j])
			while(not q.empty()):
				x, y=q.get()
				vis[x][y]=True
				if(x+1<m):
					if(arr[x+1][y]==arr[x][y] and not vis[x+1][y]):
						q.put([x+1, y])
				if(x-1>=0):
					if(arr[x-1][y]==arr[x][y] and not vis[x-1][y]):
						q.put([x-1, y])
				if(y-1>=0):
					if(arr[x][y-1]==arr[x][y] and not vis[x][y-1]):
						q.put([x, y-1])
				if(y+1<m):
					if(arr[x][y+1]==arr[x][y] and not vis[x][y+1]):
						q.put([x, y+1])

print(comp)
