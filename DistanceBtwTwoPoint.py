import math
print('''Enter the below Values:
(X1,Y1) and (Y1,Y2)''')
X1=float(input('X1:'))
Y1=float(input('X1:'))
X2=float(input('X2:'))
Y2=float(input('Y2:'))
distance=math.sqrt((X2-X1)**2+(Y2*Y1)**2)
print("Distance between (%.`0f,%.`0f)and (%.0f,%.0f) is %5.2f"%(X1,Y1,X2,Y2,distance))``