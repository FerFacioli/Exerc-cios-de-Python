# Ex15: Usando pandas, ler dados.csv, calcular média e salvar novo CSV com coluna normalizada
import pandas as pd

def processar_csv(path_in, path_out, coluna='valor'):
    df = pd.read_csv(path_in)
    if coluna not in df.columns:
        raise ValueError(f'Coluna {coluna} não encontrada')
    media = df[coluna].mean()
    df['valor_normalizado'] = df[coluna] / media
    df.to_csv(path_out, index=False)
    return media

if __name__ == '__main__':
    sample = 'dados.csv'
    import pandas as pd
    pd.DataFrame({'valor':[10,20,30,40]}).to_csv(sample, index=False)
    m = processar_csv(sample, 'dados_com_media.csv', coluna='valor')
    print(f'Média calculada: {m} (arquivo dados_com_media.csv criado)')
