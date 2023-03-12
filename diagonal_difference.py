import math

def diagonal_difference(arr):
    sum_primary_diagonal = 0
    sum_secondary_diagonal = 0
    result = 0
    var = len(arr)-1

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                sum_primary_diagonal += arr[i][j]
        
        sum_secondary_diagonal += arr[i][var]
        var -= 1
    
    result = int(math.fabs(sum_primary_diagonal-sum_secondary_diagonal))
    return result

print(diagonal_difference([[1,2,3],[4,5,6],[9,8,9]]))        
