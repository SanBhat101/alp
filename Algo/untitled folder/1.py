def merge_sort(arr, tmp_arr, left, right):

    inv_count = 0

    if left < right:
        mid = (left+right)//2
        inv_count += merge_sort(arr, tmp_arr, left, mid)
        inv_count += merge_sort(arr, tmp_arr, mid+1, right)
        inv_count += merge(arr, tmp_arr, left, mid, right)

    return inv_count
    pass

def merge(arr, tmp_arr, left , mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0

    while i<=mid and j<=right:

        if arr[i]<arr[j]:
            tmp_arr[k]=arr[i]
            k+=1
            i+=1

        if arr[i]>arr[j]:
            tmp_arr[k]=arr[j]
            inv_count+=(mid-i+1)
            k+=1
            j+=1
    
    while i<=mid:
        tmp_arr[k]=arr[i]
        k+=1
        i+=1
    
    while j<=right:
        tmp_arr[k]=arr[j]
        j+=1
        k+=1

    for var in range(left, right+1):
        arr[var] = tmp_arr[var]

    return inv_count

    pass

def _mergesort(arr, n):
    tmp_arr = [0]*n
    return merge_sort(arr, tmp_arr, 0, n-1)
    pass

arr = [2,3,1,5,4]
n = len(arr) 
result = _mergesort(arr, n) 

if result==0:
    print("Same")
elif result<=n/2:
    print("Almost Similar")
else:
    print("Not similar") 