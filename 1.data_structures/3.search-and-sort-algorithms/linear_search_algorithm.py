def linear_search(lst,target):
    n= len(lst)
    for i in range(n):
        if lst[i] == target:
            #print(lst[i])
            return i
        
    return -1



arr = [1,45,87,67,55,101]
target = 45
ta1= 1
ta2 = 101

print(linear_search(arr,target))
print(linear_search(arr,ta1))
print(linear_search(arr,ta2))