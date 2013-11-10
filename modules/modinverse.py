#returns a number c such that d*a + c*b = gcd(a,b) for some d


def extgcd(a, b):
    aux1 = 0
    aux2 = 1
    n = a
    while b != 0:
        q = a / b
        r = a % b
        a = b
        b = r
        temp = aux2
        aux2 = aux1-q*aux2
        aux1 = temp
    if temp < 0:
        temp = n + temp
    return temp

