def dfs(val,f):
	if(f==0):
		for i in range(n):
			if(a[i]==1):
				ans.append(i)
				k=dfs(i,1)
				if(k): return k
				del ans[-1]
	if(f==1):
		for i in range(len(b[0])):
			if(b[val][i]==1):
				ans.append(i)
				k=dfs(i,2)
				if(k): return k
				del ans[-1]
	if(f==2):
		if(c[val]==1): return True
		return False
	return False

n=int(input("Enter no of advertisers: "))
a=[1 for i in range(n)]
b=[[] for i in range(n)]
c=[]
tot=[]
user=1
while(True):
	k=int(input("Press 1 to add another user else 0: "))
	if(k==0): break
	if(k==1):
		edge=list(map(int,input("Enter edge matrix: ").split()))
		for i in range(n):
			b[i].append(edge[i])
		ans=[0]
		c.append(1)
		f=dfs(0,0)
		if(f):
			tot.append(ans)
			a[ans[1]]=0
			b[ans[1]][ans[2]]=0
			c[ans[2]]=0
			print("(",ans[1]+1,",",chr(ans[2]+97),")")
print("Total paths:",len(tot))
