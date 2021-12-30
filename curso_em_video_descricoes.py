import glob
from nbformat import current as nbf

lista_nomes_arquivos = glob.glob('descricoes/*.txt')

texto_titulo = 'Curso em Vídeo - Exercícios de Python 3 - Mundo'

mundos = [
    (1, 12, 0, 35),
    (12, 16, 35, 71),
    (16, 24, 71, 117)
]

for numero, mundo in enumerate(mundos):
    novo_notebook = nbf.new_notebook()
    celulas = []
    celula_titulo = nbf.new_text_cell('markdown', f"# {texto_titulo} {numero + 1}")
    celulas.append(celula_titulo)
    for nome_arquivo in lista_nomes_arquivos[mundo[2]:mundo[3]]:
        arquivo = open(nome_arquivo, 'r', encoding='utf-8')
        texto_arquivo = arquivo.read()
        texto_exercicio = texto_arquivo.partition('\n')[0].replace('Python ', '')
        nova_celula_texto = nbf.new_text_cell('markdown', '### ' + texto_exercicio)
        celulas.append(nova_celula_texto)
        nova_celula_codigo = nbf.new_code_cell('')
        celulas.append(nova_celula_codigo)
    for aula in range(mundo[0], mundo[1]):
        nova_celula_texto = nbf.new_text_cell('markdown', '## Aula ' + str(aula))
        celulas.append(nova_celula_texto)
    novo_notebook['worksheets'].append(nbf.new_worksheet(cells=celulas))
    nome_arquivo_notebook = f"curso_em_video_exercicios_python_mundo_{numero + 1}.ipynb"
    with open(nome_arquivo_notebook, 'w', encoding='utf-8') as f:
        nbf.write(novo_notebook, f, version=4)
    f.close()