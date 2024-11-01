#crie um programa que leia o nome completo de uma pessoa e mostre
#O nome com todoas as letras maiúscula e minusculas.
#quantas letras ao todo (sem considerar espaços)
#quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome completo: ")).strip()
print("analisando seu nome...")
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')

print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')} letras')
print(f'Seu primeiro nome tem {nome.find(' ')}')

