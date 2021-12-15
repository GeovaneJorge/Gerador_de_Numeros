import random

print("Este programa gera um número aleatório entre dois números informados")
low = int(input("Qual é o limite inferior?"))
high = int(input("Qual é o limite superior? "))
num = random.randint(low, high)
print(f"Seu número gerado aleatoriamente é: {num}")
name = input("Até mais ver !: ")