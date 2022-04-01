grafoMa = ([[0, 1, 1, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 1, 1],
         [0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0]])

print("Abaixo podemos ver o grafo na forma de matriz de adjacência")
for l in range(0, 5):
      for c in range(0, 5):
        print(grafoMa[l][c], end='')
      print()

print("Abaixo podemos ver o grafo na forma de lista de adjacência")
grafoLi = {1: [2, 3], 2: [3], 3: [4, 5], 4: [2], 5: [4]}
cont = 1
while True:
  print(grafoLi[cont])
  cont+=1
  if cont == 6:
    break
