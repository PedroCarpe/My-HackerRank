def time_conversion(s):
    _24_hr_clock = 0
    hr_12 = int(s[0:2])

     
    if s[-2:] == 'AM':
        if s[0:2] == '12': 
            _24_hr_clock = '00'+s[-8:-2]
        elif 1 <= hr_12 <= 11:
            _24_hr_clock = s[0:8]    
    else:
        if s[0:2] == '12':
            _24_hr_clock = s[0:8]
        else:
            hr_update = int(s[0:2])+12
            _24_hr_clock = str(hr_update)+s[-8:-2]

    
    return(_24_hr_clock)

print(time_conversion('10:40:22AM'))    