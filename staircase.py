def staircase(n):
    spaces = 0
    
    for number in range(n+1):
        spaces = n-number
        if number >= 1:
            print(spaces*' '+number*'#')

staircase(6)        