# Ex14: Ler config.json e exibir formatado
import json
def ler_config(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    sample = 'config.json'
    exemplo = {'nome':'MeuProjeto','versao':'1.0.0','parametros':{'alpha':0.1,'beta':2}}
    import json
    with open(sample,'w',encoding='utf-8') as f:
        json.dump(exemplo,f,indent=2)
    cfg = ler_config(sample)
    if 'versao' in cfg:
        print(f"Nome: {cfg.get('nome')}, Versão: {cfg.get('versao')}")
    else:
        print('Campo versao não encontrado.')
    print('Parametros:')
    for k,v in cfg.get('parametros',{}).items():
        print(f' - {k}: {v}')
