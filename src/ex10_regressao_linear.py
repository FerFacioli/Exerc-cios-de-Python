# Ex10: Regressão linear simples via mínimos quadrados (sem sklearn)
import numpy as np

def ajustar_regressao(x, y):
    X = np.vstack([x, np.ones_like(x)]).T
    coef = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
    return coef  # [a, b]

if __name__ == "__main__":
    rng = np.random.default_rng(42)
    x = np.linspace(0,9,10)
    y = 2*x + 1 + rng.normal(0,1,size=x.shape)
    a,b = ajustar_regressao(x,y)
    print(f"Coeficientes: a = {a:.4f}, b = {b:.4f}")
