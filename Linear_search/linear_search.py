def linear_search(arr,val):
    for i in range(len(arr)):
        if arr[i] == val:
            return True
    return False

print(linear_search([1,2,3,4,5], int(input("please input value to find: "))))
