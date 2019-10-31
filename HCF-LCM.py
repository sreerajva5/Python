#HCF and LCM calculator python

n = float(input("Enter the First Number : "))
n1 = float(input("Enter the Second Number : "))

a,b=n,n1

while(n1 != 0):
    t = n1
    n1 = n % n1
    n = t
lcm=(a*b)/n   
print("HCF of {0} and {1} = {2}".format(a, b, n))
print("LCM of {0} and {1} = {2}".format(a, b, lcm))
