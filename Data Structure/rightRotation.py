# def rightRotatio(arr,d,n):
#     for i in range(d):
#         rightRotatiobyOne(arr,n)


def rightRotatiobyOne(arr,n):
    temp=arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=temp
def printArray(arr,size):
    for i in range(size):
        print(arr[i],end=' ')


arr=[1,2,3,4,5,6,7]
rightRotatiobyOne(arr,7)
printArray(arr,7)