import math
def two_crystal_balls(arr):
    JUMP_LENGTH = math.floor(math.sqrt(len(arr)))
    p = 0
    for i in range(JUMP_LENGTH, len(arr)+1,JUMP_LENGTH):
        if arr[i] == 1:
            p=(i - JUMP_LENGTH)
            break
        else:
            p=i
    for j in range(0,JUMP_LENGTH,1):
        if arr[p] == 1:
            return "floor " + str(p)
        p+=1
    return "Does not break"
    

print(two_crystal_balls([0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1]))