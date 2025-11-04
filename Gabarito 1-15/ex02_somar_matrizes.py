# Ex02: Somar duas matrizes 2x2
def somar_matrizes(a, b):
    soma = [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]
    return soma

if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    print("Soma das matrizes:", somar_matrizes(A, B))
