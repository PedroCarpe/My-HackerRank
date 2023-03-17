#comments to make ease of reading and refactoring

def grading_students(grades):
    
    for g in grades:
        counter = 1
        #print(f'***{g}***')
        
        if g >= 38:
            while counter*5 <= g:
                #print(f'{counter * 5} {g}') 
                counter += 1
            #print(f'Here: {counter * 5}')

            #print(f'Here: {counter*5}-{g} = {counter*5-g}')
            if (counter * 5 - g) < 3:
                index_grade = grades.index(g)
                grades[index_grade] = counter*5           
        #else:
        #    print(f'Value out of range {g}')

    return grades
print(grading_students([73,67,38,33]))      