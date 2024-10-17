import random

#simula o lancamento de uma moeda
resultado = "cara" if random.randint(0, 1) == 0 else "coroa"
print(f"O resultado do lançamento de moeda é: {resultado}")
