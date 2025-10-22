import gmpy2

def isPrime(n):
    return gmpy2.is_prime(n)

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
input()