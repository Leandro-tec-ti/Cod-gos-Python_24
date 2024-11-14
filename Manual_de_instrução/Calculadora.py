# Faça uma Calculadora Simples
# num1, num2, op, result,

num1 = 0
num2 = 0
result = 0
op = ''
x = True
continuar = 's'
while (x == True):
    num1 = float(input("Digite seu primeiro número ")) # ler o primeiro número em float
    op   = input('Digite a operação matemática a ser feita: ')
    num2 = float(input('Digite o segundo número: ')) # ler o segundo número
    if   op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '/':
        result = num1 / num2
    elif op == '*':
        result = num1 * num2
    else:
        print('O operação não reconhecida! ')
        break
    print(f'{num1:.1f} {op} {num2:.1f} = {result:.1f}')
    continuar =  input('Deseja continuar? S/N ').lower()
    if (continuar == "n"):
        x = False  
    

    