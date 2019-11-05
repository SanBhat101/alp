import heapq

if __name__ == "__main__":
    m = int(input("Enter the m value:"))
    n = int(input("Enter the n value:"))
    pt = []
    for i in range(n):
        temp = int(input())
        pt.append(temp)
    load = [0 for i in range(m)]
    
    heapq.heapify(load)
    
    pt.sort()
    
    for i in range(n):
        load[0] += pt[i]
        heapq.heapify(load)
        
    makeSpan = load[0]
    
    for i in range(1,len(load)):
        makeSpan = max(makeSpan,load[i])

    print("Load on machine:")
    for i in range(len(load)):
        print(load[i])
    
    print("Maximum Load",makeSpan)
    
