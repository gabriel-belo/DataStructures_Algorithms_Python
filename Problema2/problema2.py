#Problema- Rotação de uma lista
from jovian.pythondsa import evaluate_test_cases

#obtido pela rotação de uma lista ordenada um número desconhecido de vezes escreva uma função para
#determinar o número mínimo de vezes que a lista ordenada original foi rotacionada para obter a
#lista fornecida. Sua função deve ter a complexidade do pior caso de O(lg n), onde n é o
#comprimento da lista. Você pode assumir que todos os números na lista são únicos.

#A definição de rotação de lista é remover o último elemento da lista e adicionar ele antes do
#primeiro elemento. Exemplo: [3, 2, 4, 1] produz [1, 3 ,2 4].

#Solução

#Solução O(n)
def count_rotations(nums):

    cont=0

    for i in range(len(nums)):
        if nums[i -1]> nums[i]:
            rotacoes= cont
            return rotacoes
        cont += 1
    return 0

#Objetivo é solução O(log n):

#Casos teste:
#1. Lista com 10 elementos e 3 rotações.
test1={
    'input':{
        'nums':[19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}

#2. Lista com n elemento e n-1 rotações, onde n é o tamanho da lista.
#n= 10
test2={
    'input':{
        'nums': [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
    },
    'output': 9
}

#3. Lista com 10 elementos e nehuma rotação.
test3={
    'input':{
        'nums':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    },
    'output': 0
}

#4. Lista vazia sem rotações.
test4={
    'input':{
        'nums':[]
    },
    'output':0
}

#5. Lista com n elemento e n rotações, onde n é o tamanho da lista.
test5={
    'input':{
        'nums':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    },
    'output': 0
}

#6. Lista com um elemento.
test6={
    'input':{
        'nums':[1]
    },
    'output':0
}

#7. Lista com 1 rotação
test7={
    'input':{
        'nums': [2,1]
    },
    'output': 1
}

#8. Lista com 8 elementos e 5 rotações.
test8={
    'input':{
        'nums':[4, 5, 6, 7, 8, 1, 2, 3]
    },
    'output': 5
}

#9. Lista que tem rotação igual a metade do tamanho da lista.
test9={
    'input':{
        'nums':[ 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
    },
    'output': 5
}

tests=[test1, test2, test3, test4, test5, test6, test7, test8, test9]
evaluate_test_cases(count_rotations, tests)


def count_rotationsBinarySearch(nums):
    inicio= 0
    fim= len(nums)
    meio= (inicio + fim) //2
    while True:

        if len(nums) == 0 or nums[inicio] < nums[fim]:
            return 0

        elif nums[meio] < nums[meio - 1]:
            rotacoes= meio
            return rotacoes

        inicio= meio + 1
        meio = (inicio + fim) // 2

