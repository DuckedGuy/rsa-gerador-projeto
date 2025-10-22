def isPrime(prime):
    if prime < 2:
        return False
    
    for i in range(2, int(prime**0.5) + 1):
        if prime % i == 0:
            return False
    return True

def text_to_number(text):
    return int(''.join(f"{ord(char):03d}" for char in text))

M = input("Mensagem a encriptar: ")
M = text_to_number(M)

with open("Publica.txt", "r") as f:
    chaves = f.read()
chaves = chaves.strip()
chaves = chaves.split(',')
n = int(chaves[0])
e = int(chaves[1])

if isPrime(n) and isPrime(e):
    print("Atenção: as chaves providas são invalidas e o resultado obtido não será correto.")

# encriptar
C = pow(M, e, n)
print(f'Mensagem criptografada: {C}')