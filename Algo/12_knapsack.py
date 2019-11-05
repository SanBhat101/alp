import random
import matplotlib.pyplot as plt

def compare(v,w,n,W):
    items = []
    for i in range(n):
        items.append((v[i]/w[i],v[i],w[i]))
    items.sort(reverse=True)
    
    
    items1 = []
    for i in range(n):
        items1.append((random.randint(1,1000),v[i],w[i]))
    items1.sort(reverse=True)
    return calValue(items,W),calValue(items1,W)   

def calValue(items,W):
    weight = 0
    value = 0
    
    for d,v,w in items:
        if w < W:
            value += v
            W -= w
        else:
            value += W*(v/w)
            break
    return value

n = 10
v = [60, 50, 40, 10, 100, 50, 30, 80, 45, 50]
w = [10, 20, 15, 25, 5, 15, 30, 25, 10, 25]
W = 60
val = []
val.append((compare(v,w,n,W)))

n = 20
v = [60, 50, 10, 35, 45, 10, 20, 40, 100, 70, 15, 45, 60, 25, 35, 70, 45, 30, 10, 65]
w = [10, 15, 45, 20, 35, 10, 15, 20, 25, 15, 10, 20, 15, 10, 35, 40, 10, 35, 15, 20]
W = 150
val.append((compare(v,w,n,W)))

n = 30
v = [60, 50, 10, 35, 45, 10, 20, 40, 100, 70, 15, 45, 60, 25, 35, 70, 45, 30, 10, 65, 60, 50, 40, 10, 100, 50, 30, 80, 45, 50]
w = [10, 15, 45, 20, 35, 10, 15, 20, 25, 15, 10, 20, 15, 10, 35, 40, 10, 35, 15, 20, 10, 20, 15, 25, 5, 15, 30, 25, 10, 25]
W = 250
val.append((compare(v,w,n,W)))
    
print(val)

x = [1, 2, 3]
y1 = [val[0][0], val[1][0], val[2][0]]
y2 = [val[0][1], val[1][1], val[2][1]]

plt.plot(x, y1, label = "label1")
plt.plot(x, y2, label = "label2")

plt.legend()
plt.show()
