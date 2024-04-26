import math

def roots(a, b, c):
    disc= b**2-4*a*c
    if disc == 0:
        r1= float(-b/(2*a))
        return f"({r1})"
    elif disc > 0:
        r2=float((-b + math.sqrt(disc))/(2*a))
        r3=float((-b -math.sqrt(disc))/(2*a))
        return f"({r2}, {r3})"
    else:
        return"( )"
    
    print(roots)   
      


def value_y(a, b, c, x):
    f = a * x ** 2+ b * x +c
    return f
print(value_y)

def to_string(a, b, c):
    if a== 0 and b ==0:
        return f"f(x) = {c}"
    elif a == 0:
        return f"f(x) = {b} * X + {c}"
    elif b == 0:
        return f"f(x) = {a} * X^2 + {c}"
    else:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
print(to_string)


def derivation(a, b):
    if b == 0 and a!=0:
        first= f"f\'(x)= {a * 2} * X"
        return first
    elif a ==0 and b!=0:
        sec=f"f\'(x)={b}"
        return sec
    elif a ==0 and b==0:
        thr=f"f\'(x)=0"
        return thr
    else:
        dev=f"f\'(x)={a * 2} * X + {b}"
        return dev
print(derivation)
