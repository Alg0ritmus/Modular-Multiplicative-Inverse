"""
Algorithm taken from:
https://www.researchgate.net/profile/Nikolay-Kyurkchiev/publication/344712990_New_Algorithms_for_Finding_Modular_Multiplicative_Inverse/links/5f8afd7ea6fdccfd7b65d11c/New-Algorithms-for-Finding-Modular-Multiplicative-Inverse.pdf

"""

# problem: a mod b
# find a**-1
#
# condition: a,b > 0



from timeit import default_timer as timer





# eeacmi is result
def modular_inverse_algo1(a,b):
    x1 = 1
    x2 = 0
    b0 = b
    while (b>0):
        q=a//b
        r=a%b
        a=b
        b=r
        t=x2
        x2=x1-q*x2
        x1=t

    if a==1:
        if x1<0:
            x1+=b0
        eeacmi = x1
    else:
        eeacmi = 0

    return eeacmi



# this is faster
def modular_inverse_algo3(a,b):
    b0=b
    if a>b:
        x1=1
        x2=0
        while True:
            q = a //b
            a %= b
            t = x2
            x2 =x1 - q * x2
            x1 = t
            if a<1:
                gcd = b
                break
            q = b // a
            b %= a
            t = x2 
            x2 = x1 -q*x2
            x1=t
            if b<1:
                gcd = a
                break
    else:
        x1 = 0
        x2 = 1

        while True:
            q = b // a
            b %= a
            t = x2 
            x2 = x1 -q*x2
            x1=t
            if b<1:
                gcd = a
                break
            q = a //b
            a %= b
            t = x2
            x2 =x1 - q * x2
            x1 = t
            if a<1:
                gcd = b
                break
    
    if gcd == 1:
        if x1 <0:
            x1 += b0
        eecami = x1
    else:
        eecami=0

    return eecami

a=19
b=26
#result 15
print(modular_inverse_algo1(a,b))
print(modular_inverse_algo3(a,b))


"""
    

#range_ = 100_000_001 
#b_val = 200_000_002


range_ = 50_000_001 
b_val = 100_000_002

t_start = timer()
for i in range(1,range_,1):
    a=i
    b=b_val - i
    modular_inverse_algo1(a,b)

t_end = timer()
print("modular_inverse_algo1:",t_end-t_start)



range_ = 50_000_001 
b_val = 100_000_002

t_start = timer()
for i in range(1,range_,1):
    a=i
    b=b_val - i
    modular_inverse_algo3(a,b)

t_end = timer()
print("modular_inverse_algo3",t_end-t_start)




"""

