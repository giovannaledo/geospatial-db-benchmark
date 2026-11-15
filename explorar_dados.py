import pandas as pd

# 1. Definir o nome do arquivo (coloque o nome exato do arquivo que você baixou)
arquivo_csv = 'SurveilDrone-Net23.csv' 

print(f"--- Abrindo o arquivo: {arquivo_csv} ---")

# 2. Carregar os dados no Pandas (DataFrame)
try:
    df = pd.read_csv(arquivo_csv)
    
    # 3. Mostrar as 5 primeiras linhas
    print("\n--- Primeiras 5 linhas dos dados ---")
    print(df.head())
    
    # 4. Mostrar informações gerais (quantidade de linhas, colunas e tipos de dados)
    print("\n--- Informações do Dataset ---")
    print(df.info())
    
    # 5. Verificar se existem valores nulos (vazios) ou faltando
    print("\n--- Quantidade de valores nulos por coluna ---")
    print(df.isnull().sum())

    # 6. Teste de Sanidade: Ver os limites das coordenadas e altitude
    print("\n--- Estatísticas das coordenadas e altitude ---")
    print(df[['gps_lat', 'gps_lon', 'altitude_m']].describe())
    
except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo_csv}' não foi encontrado. Verifique se ele está na mesma pasta do script.")