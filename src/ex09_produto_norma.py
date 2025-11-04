# Ex09: Produto escalar e norma de vetores
import numpy as np
def produto_e_norma(a,b):
    dot = np.dot(a,b)
    na = np.linalg.norm(a)
    nb = np.linalg.norm(b)
    return dot, na, nb

if __name__ == "__main__":
    a = np.array([1,2,3])
    b = np.array([4,5,6])
    dot, na, nb = produto_e_norma(a,b)
    print("Produto escalar:", dot)
    print("Norma a:", na)
    print("Norma b:", nb)
