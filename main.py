import csv
import requests
import pandas
from config import URL

# requisição para o link do arquivo CSV
# o metodo get da função request retorna uma resposta e um conteudo
# a resposta é baseada nos códigos de resposta do html
# o conteudo a gente consegue usando o método content (resposne.content)
response = requests.get(URL)

# criando e salvando o arquivo CSV
# with open já sabemos que é a função para abrir, ler ou escrever um arquivo
# 'w' é o modo de abertura escolhido, no caso w de write ou de escrever no arquivo
# newline poara remover as quebras de linha
with open('covid19.csv', 'w', newline='\n') as novo_arquivo:
    writer = csv.writer(novo_arquivo)                       # criando a var tipo csv com função de escrever os dados
    for linha in response.iter_lines():                     # percorrendo cada linha da response usando o método iter_lines
        writer.writerow(linha.decode('utf-8').split(','))   # escrevendo cada lonha no arquivo csv
        # decode utf-8 para formatar os dados e split para separar os dados

# abrir e ler o arquivo criado anteriormente
with open('covid19.csv') as arquivo:                            # abrindo o arquivo
    leitor = csv.reader(arquivo)                                # criando a var com função de ler os dados
    for linha in leitor:                                        # percorrendo cada linha do arquivo (que agora cada linha é uma lista)
        if linha[2] == 'Brazil':
            print(f"Linha - {leitor.line_num} {linha}")         # o  método line_num verifica o num da linha do arquivo


# abrir e ler um arquivo usando o PANDAS
arquivo_csv = pandas.read_csv('covid19.csv')                    # é só isso mesmo

print("----------------------------------------")
print(f"Imprimindo o arquivo todo com pandas. \n")
print(arquivo_csv)

print("----------------------------------------")
print(f"Imprimindo o arquivo com pandas, usando o método head() que pega só os 5 primeiros. \n")
print(arquivo_csv.head())

print("----------------------------------------")
print(f"Imprimindo o arquivo com pandas, usando o método head() que pega só os 5 primeiros. \n")
print(f"E usando o método to_string() que converte para string \n")
print(arquivo_csv.head().to_string())

print("----------------------------------------")
print(f"Imprimindo o arquivo com pandas escolhendo a informação \n")
print(arquivo_csv['total_cases_per_million'])

# abrir com pandas escolhendo os dados
arq_csv = pandas.read_csv('covid19.csv', usecols=['location', 'date', 'total_cases_per_million'], index_col='date')
print(arq_csv)

# filtrando dados
print("----------------------------------------")
print(f"Imprimindo o arquivo com pandas com filtros \n")
df = arq_csv.loc[(arq_csv.index == '2020-12-12')]
print(df)
