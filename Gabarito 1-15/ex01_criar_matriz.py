# Ex01: Criar e exibir uma matriz 3x3 preenchida manualmente
def criar_matriz():
    matriz = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    for linha in matriz:
        print(linha)
    return matriz

if __name__ == "__main__":
    criar_matriz()
