# Ex13: Ler tabela.csv e salvar aprovados.csv (nota >= 7) usando csv module
import csv

def filtrar_aprovados(path_in, path_out, nota_min=7.0):
    with open(path_in, 'r', newline='', encoding='utf-8') as fin, open(path_out, 'w', newline='', encoding='utf-8') as fout:
        reader = csv.DictReader(fin)
        writer = csv.DictWriter(fout, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            try:
                nota = float(row.get('nota', 0))
            except ValueError:
                continue
            if nota >= nota_min:
                writer.writerow(row)

if __name__ == '__main__':
    sample = 'tabela.csv'
    import csv
    with open(sample, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['id','nome','nota'])
        w.writeheader()
        w.writerows([{'id':1,'nome':'Ana','nota':8.5},{'id':2,'nome':'Bruno','nota':6.0},{'id':3,'nome':'Clara','nota':7.2}])
    filtrar_aprovados(sample, 'aprovados.csv') 
    print('Arquivo aprovados.csv gerado.')
