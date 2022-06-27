print('''
    ###########################################################
    #################Simple Interest Calculator################
    ###########################################################''')
detail='''
A = Total Accrued Amount (principal + interest:)
P = Principal Amount
I = Interest Amount
r = Rate of Interest per year in decimal; r = R/100
R = Rate of Interest per year as a percent; R = r * 100
t = Time Period involved in months or years
'''
options='''
   1.To Calculate Total Amount Accrued (Principal + Interest) A
        A = P(1 + rt)
   2.To Calculate Principal Amount P
        P = A / (1 + rt)
   3.To Calculate rate of interest: in decimal r
        r = (1/t)(A/P - 1)
   4.To Calculate rate of interest: in percent
        R = r * 100
   5.To Calculate time t
        t = (1/r)(A/P - 1)
   6.Details
'''
while True:
    print(options)
    C=int(input('Choose an Option From Above:'))

    if C==1:
        P=float(input("Enter the Principal Amount:"))
        r=float(input("Enter the Rate of Interest per year in decimal:"))
        t=float(input("Enter the Time Period involved in months or years:"))
        A = P*(1 + r*t)
        print("Total Accrued Amount (principal + interest:)",A)
        temp=input('Enter To Continue:-)')
        
    if C==2:
        A=float(input("Enter the Total Accrued Amount (principal + interest:)"))
        r=float(input("Enter the Rate of Interest per year in decimal:"))
        t=float(input("Enter the Time Period involved in months or years:"))
        P = A / (1 + r*t)
        print("Principal Amount",P)
        temp=input('Enter To Continue:-)')
    if C==3:
        A=float(input("Enter the Total Accrued Amount (principal + interest):"))
        P=float(input("Enter the Principal Amount:"))
        t=float(input("Enter the Time Period involved in months or years:"))
        r = (1/t)*(A/P - 1)
        print("Rate of Interest per year in decimal; r = R/100: ",r)
        temp=input('Enter To Continue:-)')

    if C==4:
        r=float(input("Enter the Rate of Interest per year in decimal:"))
        R = r * 100
        print ('Rate of Interest per year as a percent; R = r * 100:',R)
        temp=input('Enter To Continue:-)')
    if C==5:
        r=float(input("Enter the Rate of Interest per year in decimal:"))
        A=float(input("Enter the Total Accrued Amount (principal + interest:):"))
        P=float(input("Enter the Principal Amount:"))
        t = (1/r)*(A/P - 1)
        print('Time Period involved in months or years:')
        temp=input('Enter To Continue:-)')
    if C==6:
        print(detail)
        temp=input('Enter To Continue:-)')
    else:
        print('Please Enter the correct Detail')
        

