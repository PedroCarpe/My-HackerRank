def compareTriplets(a,b):
    
    result = []
    counter_a = 0
    counter_b = 0

    for index in range(len(a)):
        if a[index] > b[index]:
            counter_a += 1
        elif a[index] < b[index]:
            counter_b += 1
                   
    result.insert(0,counter_a)
    result.insert(1,counter_b) 
    
    return result

print(compareTriplets([1,2,3],[3,2,1]))        