import random
import matplotlib.pyplot as plt

G={int(i):[] for i in range(2)}

def plot(n):
    #for i in range(1,MAX+1):
    #   if i%50==0 and i!=0:
        c=["c"+str(i) for i in range(n)]
        s=["s"+str(i) for i in range(n)]
        #print(c)
        #print(s)

        def meme(p):
            cs={s[i]:[] for i in range(n)}
            t=[c[i] for i in range(n)]
            for j in range(3):
                for i in range(n):#created algo. #
                    if (p[s[i]][j] in t) and not cs[s[i]]:
                        cs[s[i]].append(p[s[i]][j])
                        t.remove(p[s[i]][j])
            print(cs)
            warn(cs)
            #plot_data(p,cs,1)

        def meme2(p):
            cs2={s[i]:[] for i in range(n)}
            t=[c[i] for i in range(n)]
            for i in range(n):#random comp. #
                for j in range(3):
                    x=random.choice(t)
                    if x in t:
                        cs2[s[i]].append(x)
                        t.remove(x)
                        break
            print(cs2)
            warn(cs2)
            #plot_data(p,cs2,2)
        
        def meme3(p):
            cs3={s[i]:[c[i]] for i in range(n)}#simple random assign.  #
            #print(cs3)
            #plot_data(p,cs3,2)

        def f_pref(p,d):
            count=0
            for i in s:
                if d[i][0]==p[i][0]:
                    count+=1
            return count

        def plot_data(p,d,i):   #not #for every 50
            x=len(p)
            y=f_pref(p,d)
            G[i-1].append([x,y])
            print(G)
            #X=[]
            #Y=[]
            #for j in range(2):
            #    if len(G[j]):
            #        print(G[j])
            #        for k in G[j]:
            #            X.append(k[0])
            #            Y.append(k[1])            
            f=open("/home/sanbhat/Documents/netw/plot"+str(i)+".dat",'a')
            f.write(str(x)+' '+str(y)+'\n')
            #plt.scatter(X,Y)
            #b=plt.hist(X,len(X))
            #plt.plot(b,Y)
            #plt.show()

        def warn(d):
            for i in s:
                if not d[i]:
                    print("Someone not assigned!")
                    return 0

        #driver code
        p={i:[] for i in s}    #preferences
        for i in range(n):     #setting up random prefers.
            p[s[i]]=random.sample(c,3)     #for j in range(n):#.append(random.choice(c)#c[random.randint(0,n-1)])
        print(p)
        meme(p)
        meme3(p)

#graph output
#n=int(input("Enter n:"))

#n=5
#plot(n)
n=10
plot(n)
#n=15
#plot(n)