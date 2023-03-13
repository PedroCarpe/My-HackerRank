def plus_minus(arr):
    positive_counter = 0
    negative_counter = 0
    zero_counter = 0
    
    positives_ratio = 0
    negatives_ratio = 0
    zeros_ratio = 0

    length = len(arr)

    for element in arr:
        if element >= 1:
            positive_counter += 1
        if element < 0:
            negative_counter += 1    
        if element == 0:
            zero_counter += 1

    positives_ratio = positive_counter/length
    negatives_ratio = negative_counter/length
    zeros_ratio = zero_counter/length

    print(f'{positives_ratio:.6f}\n{negatives_ratio:.6f}\n{zeros_ratio:.6f}')

plus_minus([1,1,0,-1,-1])        