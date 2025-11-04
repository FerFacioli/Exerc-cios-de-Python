# Ex11: Conta linhas e palavras em dados.txt
def contar_arquivo(path):
    linhas = 0
    palavras = 0
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            linhas += 1
            palavras += len(line.split())
    return linhas, palavras

if __name__ == '__main__':
    sample = 'dados.txt'
    with open(sample, 'w', encoding='utf-8') as f:
        f.write("Olá mundo\nEsta é uma linha\nMais uma linha com três palavras\n")
    l, p = contar_arquivo(sample)
    print(f'Linhas: {l}, Palavras: {p}')
