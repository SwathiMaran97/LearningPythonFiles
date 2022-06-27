print('''
    #############################################################################################
    ##################################Speed, Distance and Time Calculator########################
    #############################################################################################''')

options='''
   
    1.Distance = speed x time
    2.Distance = rate x time
    3.speed = distance/time
    4.Time = distance/speed
'''
while True:
    print(options)
    C=int(input('Choose an Option From Above:'))

    if C==1:
        speed=float(input("Enter the Speed(Km/h):"))
        time=float(input("Enter the Time(h):"))
        Distance = speed * time
        print("The Distance is ",Distance,"Km")
        temp=input('Enter To Continue:-)')
        
    if C==2:
        time=float(input("Enter the Time(h):"))
        rate=float(input('Enter the rate:'))
        Distance = rate * time
        print("The Distance is ",Distance,'km')
        temp=input('Enter To Continue:-)')

    if C==3:
        Distance=float(input("Enter the Distance(Km):"))
        time=float(input("Enter the Time(h):"))
        speed = Distance/time
        print('The Speed is',speed,'km/h')
        temp=input('Enter To Continue:-)')
    if C==4:
        Distance=float(input("Enter the Distance(Km):"))
        speed=float(input("Enter the Speed(km/hr):"))
        Time = Distance/speed
        print('The time is',Time,'hr')
        temp=input('Enter To Continue:-)')
    else:
        print('Please Enter the correct Choice')
        

