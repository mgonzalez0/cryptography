def gcd(a,b):
    cociente = 0
    if a > b:
        cociente = int(a / b)
        residuo = a%b
        print("Cociente: %f" %cociente)
        print("Residuo: %f" % residuo)
        if residuo != 0:
            a = b
            b = residuo
            gcd(a,b)
        else:
            print("El GCD es: %d" %b)
    else:
        print("a no puede ser mayor que b")

gcd(385,78)