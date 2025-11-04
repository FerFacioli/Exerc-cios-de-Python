# Ex12: Lê numeros.txt, calcula soma e média e salva em resumo.txt
def processar_numeros(path_in, path_out):
    nums = []
    with open(path_in, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    nums.append(float(line))
                except ValueError:
                    pass
    soma = sum(nums)
    media = soma / len(nums) if nums else 0
    with open(path_out, 'w', encoding='utf-8') as f:
        f.write(f"Soma: {soma}\nMedia: {media}\n")
    return soma, media

if __name__ == '__main__':
    inp = 'numeros.txt'
    with open(inp, 'w', encoding='utf-8') as f:
        f.write('\n'.join(str(x) for x in [1,2,3,4,5]))
    s, m = processar_numeros(inp, 'resumo.txt')
    print(f'Soma: {s}, Media: {m} (salvo em resumo.txt)')
