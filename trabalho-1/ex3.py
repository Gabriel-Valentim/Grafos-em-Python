def contaVerticeSaida(grafoLi):
  for l in range(1, 6):
      tam = len(grafoLi[l])
      print("grau de saida do vertice {} : {}".format(l, tam))

grafoLi = {1: [2, 3], 2: [3], 3: [4, 5], 4: [2], 5: [4]}
print(grafoLi)
grafo = contaVerticeSaida(grafoLi)
