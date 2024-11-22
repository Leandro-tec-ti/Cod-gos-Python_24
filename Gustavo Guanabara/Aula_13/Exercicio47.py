# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

# Primeira Alternativa Feita por mim
for c in range(2, 51, 2): 
    print(c)
print("Fim")

#segunda Alternativa feita no curso
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end= " ")
print("Fim ")