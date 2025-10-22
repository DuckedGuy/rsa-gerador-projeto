import gmpy2

def isPrime(n):
    return gmpy2.is_prime(n)

def number_to_text(number):
    text = str(number)
    resto = len(text) % 3
    text = text.zfill(len(text) + resto - 1)
    chars = [chr(int(text[i:i+3])) for i in range(0, len(text), 3)]
    return ''.join(chars)

C = int(input("Mensagem a descriptografar: "))

with open("Privada.txt", "r") as f:
    chaves = f.read()
chaves = chaves.strip()
chaves = chaves.split(',')
n = int(chaves[0])
d = int(chaves[1])

if isPrime(n) and isPrime(d):
    print("Atenção: as chaves providas são invalidas e o resultado obtido não será correto.")

# descriptografar
M = pow(C, d, n)
M = number_to_text(M)
print(f'Mensagem descriptografada: {M}') 
input()