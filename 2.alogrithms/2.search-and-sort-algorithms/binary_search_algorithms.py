#Binary Search Alogrithm involves taking sorted array and comparign target to the middle
def binar_search_algo(arr1, target):
    a = arr1.copy()
    a.sort()
    n = len(a)
    start = 0
    end = n-1
    for i in range(n):
        mid = (start+end)//2
        if a[mid] == target:
            return arr1.index(a[mid])
        elif a[mid] <target:
            start = mid+1
        elif a[mid] >target:
            end = mid-1
    return -1

arr= [1,100,1021,34,60] 
t1= 4
print(binar_search_algo(arr, t1))
t2=1
print(binar_search_algo(arr, t2))
t3=60
print(binar_search_algo(arr, t3))
