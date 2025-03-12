#Alice tem algumas cartas com números ercritos nas cartas. Ela organizou as cartas em ordem decrescente,
#e virou as cartas para o lado que não apresenta o número. Ela desafiou Bob a pegar uma carta com certo
#número tentando virar o menor número de cartas possível. Escreva uma função para ajudar Bob a
#achar a carta.

#Estratégia que usaremos para solucionar o problema
#1. Declarar o problema de forma clara. Identificar os formatos de entrada e saída.
#2. Trazer alguns exemplos de entrada e saída. Tentar cobrir todos os casos possíveis.
#3. Trazer uma solução correta para o problema
#4. Implementar a solução e testar a mesma usando alguns exemplos de inputs. Fixar bugs
#5. Analizar a complexidade e se temos alguma ineficiência no algoritmo.
#6. Caso tenha algum tipo de ineficiência, aplicar a técnica certa para superar a ineficiência.

#Solução
#Neste caso o número a buscar é 7.

#1. Precisamos encontrar a carta com o número requisitado pela Alice da forma mais eficiente possível.
#Entrada: [13, 12, 10, 7, 4, 3, 1, 0]
#Pergunta: Um número, no qual a posição na lista será determinado. Exemplo número 7
#Saída: Como saída receberemos a posição da carta

def locate_card(carta, query):
    pass

#Dicas:
#Nomear a função apropriadamente e pense cuidadosamente sobre a assinatura
#Discutir o problema com o entrevistador se não tiver certeza de como enquadrá-lo em termos abstratos
#Usae nome de variaveis descritiveis


#2 Trazer alguns exemplos de inputs e output. Tentar cobrir todos os casos possíveis.
cards= [13, 12, 11, 10, 7, 4, 3, 1, 0]
query= 7
output= 3

#result= localizar_carta(cards, query)

#result == output

#Representação do teste como um dicionario para ser mais fácil testar depois de escrevemos o código para implementação.
test={
    'input':{
        'cartas': [13, 12, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3

}

#Chamando a função, o uso de ** Significa que está desempacotando um dicionário (test['input']) e passando seus pares chave-valor como argumentos
#nomeados (keyword arguments) para a função locate_card().
#localizar_carta(**test['input']) == test['output'] # localizar_carta(**test['input']) é igual a isto locate_card(cards=[13, 11, 9, 7, 5, 3, 1], query=7)

#A função deve ser capaz de trabalhar com qualquer tipo de input válido que receber, aqui está uma lista das possíveis situações:
#O número na variável query ocorre em qualquer lugar no meio da lista cards
#O número da variável query é o primeiro elemento em cards
#O número da variável query é o último elemento em cards
#A lista cards contém só um elemento, que é query
#A lista cards não contém o valor em query
#A lista cards está vazia
#A lista cards contém números repetidos
#O valor em query ocorre em mais de uma posição na lista

#Criando as situações
tests=[]

#Caso 1: query ocorre no meio da lista
tests.append({
    'input':{
        'cards': [13, 12, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

#Caso 2: query ocorre no início da lista
tests.append({
    'input':{
        'cards': [13, 12, 11, 10, 7, 4, 3, 1, 0],
        'query': 13
    },
    'output': 0
})

#Caso 3: query ocorre no fim da lista
tests.append({
    'input':{
        'cards': [13, 12, 11, 10, 7, 4, 3, 1, 0],
        'query': 0
    },
    'output': 8
})

#Caso 4: cards contém só um elemento
tests.append({
    'input':{
        'cards': [3],
        'query': 3
    },
    'output': 0
})

#Caso o problema não fale oq fazer na situação
#1. Leia novamente a declaração
#2. Analise os exemplos dados junto com o problema
#3. Pergunto por uma explicação
#4. Faça uma suposição razoável, declare-a e siga em frente

#Caso 5: A lista cards não contém o valor em query
#Neste caso iremos assumir que a função irá retornar  -1
tests.append({
    'input':{
        'cards': [3],
        'query': 7
    },
    'output': -1
})

#Caso 6: A lista cards está vazia
tests.append({
    'input':{
        'cards': [],
        'query': 3
    },
    'output': -1
})

#Caso 7: Números se repetem em cards
tests.append({
    'input':{
        'cards': [8, 8, 8, 8, 4, 4, 4, 2, 2, 2, 2, 3, 0, 0, 0],
        'query': 3
    },
    'output': 11
})

#Caso 8: A query ocorre mais de uma vez
#Neste caso iremos assumir a primeira vez em que o valor aparece como a resposta,
#poderiamos procurar o valor mais de uma vez, mas iria gerar uma função muito complexa
tests.append({
    'input':{
        'cards': [8, 8, 8, 8, 4, 4, 4, 2, 2, 2, 2, 3, 0, 0, 0],
        'query': 4
    },
    'output': 4
})

print(tests)

#Trazer uma solução correta para o problema
#O objetivo sempre deve ser gerar uma solução correta para o problema, a qual deve ser a solução mais eficiente para o problema

#Dica: Sempre tente expressar(escrevendo ou falando) o algoritmo em suas próprias palavras antes de iniciar a codar.

#Meu código
def locate_card_Linear_Search(cards, query):
    position=0
    while True:

        if position >= len(cards) - 1 or len(cards) == 0:
            return -1

        elif cards[position] == query:
            return position

        position+=1


#Código com recursão
def locate_card_Linear_Search3(cards, query, position):
    # Condição de parada: fim da lista ou lista vazia
    if position >= len(cards) or len(cards) == 0:
        return -1

    # Se encontrou o valor
    if cards[position] == query:
        return position

    # Chamada recursiva, indo para a próxima posição
    return locate_card_Linear_Search3(cards, query, position + 1)


cartas= [13, 12, 11, 10, 7, 4, 3, 1, 0]
query= 3
print(locate_card_Linear_Search3(cartas, query, position=0))

#Versão CHATGPT, Versão iterativa (sem recursão):
def locate_card_iterative(cards, query):
    for position, card in enumerate(cards):
        if card == query:
            return position
    return -1

#Código do vídeo
def loctae_card_LinearSearch2(cards, query):
    position=0
    while True:
        if position < len(cards):
            return position
        position +=1
    return -1



#print(locate_card_Linear_Search(cartas, query))

#Utilizando a biblioteca jovian
#from jovian.pythondsa import evaluate_test_case, evaluate_test_cases

#verificando todos os testes
#evaluate_test_cases(locate_card_Linear_Search, tests)

#verificando todos os testes
#for test in tests:
#    print(locate_card(**tests['input']) == test['output'])

#Toda vez que uma alteração no código é feita devemos voltar e verificar todos os casos, pois ao corrigir um erro podemos estar introduzindo outro erro.

#Dica: Em uma entrevista real ou avaliação de codificação, você pode pular a etapa de implementar e testar a solução de força bruta no interesse do tempo.
# Geralmente é bem fácil descobrir a complexidade da solução bruta a partir da descrição simples em inglês

#5. Analizar a complexidade do algoritmoe identificar ineficiências, se tivermos alguma.
#Analizar a complexidade de um algoritmo é compreender sua necessidade e a forma de tentar executar sua ação da forma mais eficiênte possível

#Um computador requwr uma certa quantidade de tempo finito para executar cada instrução. Então cada matriz AIS na verdade leva um tempo embora seja tão
# rápido que não conseguimos ver, especialmente para inputs pequenos

#Complexidade e notação Big O
#Complexidade de um algoritmo é mensurar a quantidade de tempo ou/e espaço requerido por um algiritmo para uma entrada de um determinado tamanho
#por exemplo N. O termo complexidade sempre se refere ao pior caso de complexidade(o maior tempo e espaço gasto por um programa/algoritmo para
# processar um input)

#Utilizando o caso da busca linear como exemplo:
#1. A complexidade do tempo para este algoritmo é cN, c sendo uma variável constante que é a variável da qual o computador leva para executar uma busca,
# vezes N que é o número máximo de iterações que podemos executar em uma iteração, a multiplicação dos dois resulta no tempo de execução.
#2. a complexidade do espaço é uma constante c(independente de N), pois precisamos apenas de uma única variável position para iterar pelo array, e ela
# ocupa um espaço constante na memória do computador (RAM)