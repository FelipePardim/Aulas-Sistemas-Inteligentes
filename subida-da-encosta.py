# Subida da encosta

# Gerar solução
    # Necessidades de duas libs
        # String e Random
    # Def GerarSolucao(length)
# Expandir a vizinhança
    # (Solução)
    # Def ExpandirVizinhanca(Solucao)
# Função objetivo
    # Def FuncaoObjetivo(Solucao)
    # f(x) = [S1 - SO]
        # (ABS)
# Fluxo

import random
import string

def GerarSolucao(fraseObjetivo):
    length = len(fraseObjetivo)
    solucao = []
    for _ in range(length):
        solucao.append(random.choice(string.printable))
    return solucao
        
def ExpandirVizinhanca(solucao):
    index = random.randint(0, len(solucao) - 1)
    solucao[index] = random.choice(string.printable)
    return solucao

def FuncaoObjetivo(solucao, fraseObjetivo):
    objetivo = fraseObjetivo
    valor_fit = 0
    for i in range(len(objetivo)):
        # if objetivo[i] - solucao[-] = valor_fit:
        #     return "Soluca encontrada"
        # else:
        s = solucao[i]
        t = objetivo[i]
        valor_fit += abs(ord(s) - ord(t))
    return valor_fit

iteracao = 0
fraseObjetivo = "Aulas de sistemas inteligentes aplicados"
melhorSolucao = GerarSolucao(fraseObjetivo)
melhorPontuacao = FuncaoObjetivo(melhorSolucao, fraseObjetivo)

while melhorPontuacao > 0:
    iteracao += 1
    
    novaSolucao = list(melhorSolucao)
    ExpandirVizinhanca(novaSolucao)
    pontuacaoNovaSolucao = FuncaoObjetivo(novaSolucao, fraseObjetivo)
    
    if pontuacaoNovaSolucao < melhorPontuacao:
        melhorSolucao = novaSolucao
        melhorPontuacao = pontuacaoNovaSolucao
        print("Iteracao:", iteracao, " Melhor pontuacao:", melhorPontuacao, " Solucao atual:", melhorSolucao)
