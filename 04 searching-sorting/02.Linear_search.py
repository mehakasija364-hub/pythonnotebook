def linear_search(arr,target):
    for index in range(len(arr)):
        if(arr[index]==target):
            return index
    return -1


my_list=[10,23,45,70,11]
target=23
result=linear_search(my_list,target)
print(result)