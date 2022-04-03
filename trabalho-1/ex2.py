def transformaGrafo(grafoLi):
    grafo = [[0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0]]

    for l in range(0, 5):
      tam = len(grafoLi[l])
      for c in range(0, tam):
          grafo[l][(grafoLi[l][c]-1)] = 1

    
    return grafo
        

grafoLi = {0: [2, 3], 1: [1, 3, 4], 2: [1, 2, 4, 5], 3: [2, 3, 5], 4: [3, 4]}
grafoMa = transformaGrafo(grafoLi)

print(grafoLi)

for l in range(0, 5):
      for c in range(0, 5):
        print(grafoMa[l][c], end='')
      print()