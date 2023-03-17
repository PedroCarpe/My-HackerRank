#s and t are the range(the length) of the house
#a and b are the locations of the trees
#d is the distance of the fruit from its tree

def count_apples_and_oranges(s, t, a, b, apples, oranges):
        
    for apples_distance in range(len(apples)):
        apples[apples_distance] += a 
    
    apples_in_the_house = 0
    for apples_range in apples:
        if s<= apples_range <= t:
            apples_in_the_house += 1
            #print(f'{apples_range} Apple fell in the house')

    
    for oranges_distance in range(len(oranges)):
        oranges[oranges_distance] += b
    
    oranges_in_the_house = 0
    for oranges_range in oranges:
        if s<= oranges_range <= t:
            oranges_in_the_house += 1
            #print(f'{oranges_range} Oranges fell in the house')
        

    #Apples in the house 
    print(f'{apples_in_the_house}')

    #Oranges in the house 
    print(f'{oranges_in_the_house}')

count_apples_and_oranges(7,10,4,12,[4,3,-4],[3,-2,-4])
