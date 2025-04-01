# Faça um programa que tenha uma função notas() 
# que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#– Quantidade de notas
#– A maior nota
#– A menor nota
#– A média da turma
#– A situação (opcional)

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas deos alunos (aceita Várias)
    :param sit: valor opcional, indicando se deve ou não adcionar a situação
    :return: Dicio nário com várias informações sobre a situação da turma.

    """
    r = {}
    r["total"] = len(n)
    r["maior"] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = "Boa"
        elif r['média'] >= 5:
            r['situação'] = "Razoavel"
        else:
            r['situação'] = "Ruim"
    return r


# Programa principal
resposta = notas (10, 5.5, 2.5, 9, 8.5, sit=True)
print(resposta)
help(notas)