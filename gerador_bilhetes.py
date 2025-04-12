import itertools
import random

# Lista dos 56 bilhetes base (exemplo com 5 bilhetes)
bilhetes_base = [
    [15, 17, 30, 39, 44, 48],
    [11, 13, 19, 31, 46, 50],
    [2, 8, 19, 30, 41, 49],
    [4, 10, 5, 32, 47, 45],
    # ... Adicione os 52 bilhetes restantes aqui
]

def dividir_em_duques(bilhete):
    """Divide um bilhete de 6 números em 3 duques."""
    return [bilhete[i:i+2] for i in range(0, 6, 2)]

def gerar_1400_bilhetes(bilhetes_base):
    duques = [dividir_em_duques(bilhete) for bilhete in bilhetes_base]
    todos_duques = [duque for sublist in duques for duque in sublist]
    
    bilhetes_gerados = []
    while len(bilhetes_gerados) < 1400:
        # Escolhe 3 duques aleatórios de bilhetes base diferentes
        duques_selecionados = random.sample(todos_duques, 3)
        novo_bilhete = list(set(num for duque in duques_selecionados for num in duque))
        
        # Verifica se tem 6 números únicos e balanceamento
        if len(novo_bilhete) == 6 and balanceado(novo_bilhete):
            bilhetes_gerados.append(sorted(novo_bilhete))
    
    return list(bilhetes_gerados)

def balanceado(bilhete):
    """Verifica se o bilhete tem 3 pares/ímpares e 3 baixos/altos."""
    pares = sum(1 for num in bilhete if num % 2 == 0)
    baixos = sum(1 for num in bilhete if num <= 25)
    return pares == 3 and baixos == 3

# Gera os 1.400 bilhetes
bilhetes_finais = gerar_1400_bilhetes(bilhetes_base)

# Salva em um arquivo .txt
with open("bilhetes_dupla_sena.txt", "w") as file:
    for bilhete in bilhetes_finais:
        file.write(" ".join(map(str, bilhete)) + "\n")
