class Job: 
    def __init__(self, start, finish, profit): 
        self.start  = start 
        self.finish = finish 
        self.profit  = profit 

def sortSecond(job):
    return job.finish

def jobComparator(job1, job2):
    return job1.finish < job2.finish

def latestNonConflict(jobs, i):

    for j in range(i-1,-1,-1):
        # print(j)
        if jobs[j].finish<=jobs[i].start:
            return j
    return -1

def findMaxProfit(jobs, n):
    jobs.sort(key = sortSecond)
    # for i in jobs:
    #     print (i.finish)
    table = [None]*n
    table[0]=jobs[0].profit
    # print(table[0])

    for i in range(1,n):
        # print("i",i)
        inclProf = jobs[i].profit
        # print (inclProf)
        l = latestNonConflict(jobs,i)
        # print("check",l)
        if l!=-1:
            inclProf+= table[l]

        table[i] = max(inclProf, table[i-1])
    
    result = table[n-1]
    return result

if __name__ == "__main__":
    jobs = [Job(1, 2, 50), Job(3, 5, 20),  
      Job(6, 19, 100), Job(2, 100, 15)]
    print(findMaxProfit(jobs,4))




