def contaVerticeEntrada(grafoLi):
  cont = 0

  for vertice in range(1, 6):
    for l in range(1, 6):
      tam = len(grafoLi[l])
      for c in range(0, tam):
        if vertice == grafoLi[l][c]:
          cont+=1
    print("grau de entrada do vertice {} : {}".format(vertice, cont))
    cont = 0

grafoLi = {1: [2, 3], 2: [3], 3: [4, 5], 4: [2], 5: [4]}
print(grafoLi)
grafo = contaVerticeEntrada(grafoLi)