import random
def quicksort(array):
    if(len(array)<2):
        return array
    else:
        num = random.randint(0,len(array)-1)
        pivot = array[num]
        arr = array[:num] + array[num+1:]
        less = [i for i in arr if i<=pivot]
        greater = [i for i in arr if i>pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10,5,2,3]))