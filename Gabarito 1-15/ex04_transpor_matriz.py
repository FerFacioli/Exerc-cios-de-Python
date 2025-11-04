# Ex04: Transpor uma matriz 3x2
def transpor(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

if __name__ == "__main__":
    M = [[1, 2], [3, 4], [5, 6]]
    print("Matriz transposta:", transpor(M))
