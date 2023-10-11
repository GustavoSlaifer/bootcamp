import pandas as pd

# Passo 1 - Extract

# Lê o arquivo csv cria um dataframe com os dados
df = pd.read_csv('notas.csv')

# Passo 2 - Transform

# Calcula a média e cria uma nova coluna com o resultado
for a in df['aluno']:
    n1 = df['nota1']
    n2 = df['nota2']
    
    media = (n1 + n2) / 2

    df['media'] = media


# Define contadores
aprovados = 0
reprovados = 0

# Conta a quantidade de alunos aprovados e reprovados
for i in df['media']:
    if i >= 5:
        aprovados += 1
    else:
        reprovados += 1

# Passo 3 - Load

# Imprime os resultados da contagem
print(f'Número de alunos aprovados: {aprovados}\n')
print(f'Número de alunos reprovados: {reprovados}')