print('''
    #############################################################################################
    ##################################Compound Interest Calculator################################
    #############################################################################################''')
detail='''

    A = Accrued Amount (principal + interest)
    P = Principal Amount
    I = Interest Amount
    R = Annual Nominal Interest Rate in percent
    r = Annual Nominal Interest Rate as a decimal
    t = Time Involved in years, 0.5 years is To calculated as 6 months, etc.
    n = number of compounding periods per unit t at the END of each period


'''
options='''
   
    1.To Calculate Accrued Amount (Principal + Interest)
        A = P(1 + r/n)nt
    2.To Calculate Principal Amount, solve for P
        P = A / (1 + r/n)nt
    3.To Calculate rate of interest in decimal, solve for r
        r = n*((A/P)1/nt - 1)
    4.To Calculate rate of interest in percent
        R = r * 100
    5. To Calculate time, solve for t
        t = math.log(A/P) / n*(math.log(1 + r/n))

   6.Details
'''
while True:
    print(options)
    C=int(input('Choose an Option From Above:'))

    if C==1:
        P=float(input("Enter the Principal Amount:"))
        r=float(input("Enter the Annual Nominal Interest Rate as a decimal:"))
        t=float(input("Enter the Time Involved in years, 0.5 years is To calculated as 6 months, etc:"))
        n=float(input("Enter the number of compounding periods per unit t at the END of each period:"))
        A = P*(1 + r/n)*n*t
        print("Total Accrued Amount (principal + interest):",A)
        temp=input('Enter To Continue:-)')
        
    if C==2:
        A=float(input("Enter the Total Accrued Amount (principal + interestTime Involved in years, 0.5 years is To calculated as 6 months, etc.:)"))
        r=float(input("Enter the Annual Nominal Interest Rate as a decimal:"))
        t=float(input("Enter the Time Involved in years, 0.5 years is To calculated as 6 months, etc:"))
        n=float(input("Enter the number of compounding periods per unit t at the END of each period:"))
        P = A / (1 + r/n)*n*t
        print("Principal Amount",P)
        temp=input('Enter To Continue:-)')
    if C==3:
        A=float(input("Enter the Total Accrued Amount (principal + interest):"))
        P=float(input("Enter the Principal Amount:"))
        t=float(input("Enter the Time Involved in years, 0.5 years is To calculated as 6 months, etc:"))
        n=float(input("Enter the number of compounding periods per unit t at the END of each period:"))
        r = n*((A/P)*1/n*t - 1)
        print("Annual Nominal Interest Rate as a decimal:",r)
        temp=input('Enter To Continue:-)')

    if C==4:
        r=float(input("Enter the Annual Nominal Interest Rate as a decimal:"))
        R = r * 100
        print ('Rate of Interest per year as a percent:',R)
        temp=input('Enter To Continue:-)')
    if C==5:
        r=float(input("Enter the Annual Nominal Interest Rate as a decimal:"))
        A=float(input("Enter the Total Accrued Amount (principal + interest):"))
        P=float(input("Enter the Principal Amount:"))
        n=float(input("Enter the number of compounding periods per unit t at the END of each period:"))
        t = (math.log(A/P) / n*(math.log(1 + r/n)))
        print('Time Involved in years, 0.5 years is To calculated as 6 months, etc:')
        temp=input('Enter To Continue:-)')
    if C==6:
        print(detail)
        temp=input('Enter To Continue:-)')
    else:
        print('Please Enter the correct Detail')
        

