# Ex03: Multiplicar duas matrizes 2x2
def multiplicar_matrizes(a, b):
    resultado = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                resultado[i][j] += a[i][k] * b[k][j]
    return resultado

if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[2, 0], [1, 2]]
    print("Produto das matrizes:", multiplicar_matrizes(A, B))
