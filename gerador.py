import math

def isPrime(prime):
    if prime < 2:
        return False
    
    for i in range(2, int(prime**0.5) + 1):
        if prime % i == 0:
            return False
    return True

p = 1
q = 1

while not (isPrime(p) and isPrime(q) and p != q):
    p = int(input("p: "))
    q = int(input("q: "))

n = p * q
phi = (p-1) * (q-1)
e = 2
while e < phi:
    if math.gcd(e, phi) == 1:
        break
    e += 1
d = pow(e, -1, phi)


with open("Publica.txt", "w") as f:
    f.write(f"{n},{e}")
with open("Privada.txt", "w") as f:
    f.write(f"{n},{d}")