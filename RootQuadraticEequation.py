import math
print('''
###############################################################################
#########################Quadratic Root Calculator#############################
###############################################################################
''')
while True:
    a = float(input(" Enter a: "))
    b = float(input(" Enter b: "))
    c = float(input(" Enter c: "))
    check = (b * b) - (4 * a * c)

    if(check > 0):
        ar = (-b + math.sqrt(check) / (2 * a))
        br = (-b - math.sqrt(check) / (2 * a))
        print("Roots are:",ar, br)
        temp=input('||Press Enter to Continue||')
    if(check == 0):
        ar = br = -b / (2 * a)
        print("Roots are:",ar, br)
        temp=input('||Press Enter to Continue||')

    if(check < 0):
        ar = -b / (2 * a)
        br=ar
        imaginary = math.sqrt(-check) / (2 * a)
      #  print("Imaginary Roots")
        print("Roots are :(",ar,'+j',imaginary,')and(' ,br,"-j",imaginary,')')
        temp=input('||Press Enter to Continue||')
