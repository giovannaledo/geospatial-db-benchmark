# Diário de Bordo (Logbook) - Iniciação Científica

**Projeto:** Benchmark de Bancos de Dados Geoespaciais (PostGIS vs. MongoDB)
**Aluna:** Giovanna Oliveira Ledo de Souza
**Orientador:** Prof. Ms. Valdomiro Santos

---

## Registros de Atividades

### 28/10/2026 - Definição do Projeto e Estruturação Inicial
- **Definição do Tema:** Escolha do tema focado em Engenharia de Software e Bancos de Dados Geoespaciais, alinhando o interesse técnico com a aplicação em dados reais (drones e GPS).
- **Criação do Repositório:** Estruturação do projeto no GitHub (`geospatial-db-benchmark`), incluindo documentação inicial (README em português e inglês) detalhando o Problema, Justificativa e Metodologia.
- **Alinhamento com o Orientador:** Apresentação da proposta ao Prof. Valdomiro, que aprovou a ideia, sugeriu a inclusão de análise estatística (Regressão Linear) e apoiou a conexão com o projeto para a bolsa FAPESP.

### 04/11/2026 - Configuração do Ambiente de Bancos de Dados
- **PostgreSQL + PostGIS:** Instalação e configuração do banco de dados relacional com a extensão espacial.
- **Validação do PostGIS:** Teste de conexão via pgAdmin 4 e execução do comando `SELECT postgis_full_version();` com sucesso.
- **MongoDB:** Instalação do MongoDB Community Server e da interface gráfica MongoDB Compass. Criação do banco de dados `gis_benchmark` e da coleção `trajetorias`.

### 10/11/2026 - Exploração e Análise de Dados
- **Obtenção dos Dados:** Download do dataset **SurveilDrone-Net23** (Kaggle) contendo 140.256 registros de telemetria real de drones (incluindo coordenadas GPS e altitude).
- **Análise Exploratória:** Criação do script `explorar_dados.py` utilizando a biblioteca Pandas.
- **Descobertas:** Validação de que o dataset não possui valores nulos, as altitudes estão em metros e as colunas de GPS estão no formato adequado (`float64`). 

### 15/11/2026 - Configuração do Ambiente Python e Integração
- **Migração para Miniconda:** Devido a conflitos de compilação do Python 3.15 no Windows (erro `pyyaml`), foi instalado o Miniconda para garantir um ambiente profissional e reprodutível.
- **Ambiente Virtual:** Criação do ambiente isolado `ic_geo` (Python 3.11) e instalação das bibliotecas essenciais: Pandas, NumPy, Matplotlib, PyMongo, Psycopg2 e Jupyter.
- **Integração Python-MongoDB:** Criação do notebook `ingestao_dados.ipynb`. Escrita do código de conexão via `pymongo` e realização do primeiro teste de ingestão.
- **Resultado:** Inserção bem-sucedida dos primeiros 5 registros do dataset no MongoDB, visualizados e validados através do MongoDB Compass.

---

## Próximos Passos (To-Do List)

- [ ] Desenvolver o script de ingestão em massa (em lotes/chunks) para inserir os 140 mil registros no MongoDB.
- [ ] Desenvolver o script de ingestão equivalente para o PostGIS (conversão de coordenadas para geometria 3D via `ST_GeomFromText`).
- [ ] Criar os índices espaciais (`GIST` no PostGIS e `2dsphere` no MongoDB).

## Registro de Problemas e Soluções (Troubleshooting)

- **Problema:** Erro `Failed to build pyyaml` ao tentar instalar o Jupyter no Windows usando Python 3.15.
  - **Causa:** Incompatibilidade de compilação do pacote no Windows.
  - **Solução:** Migração para o gerenciador de pacotes Miniconda, criando um ambiente isolado (`ic_geo`) com Python 3.11 para garantir a estabilidade e reprodutibilidade do projeto.

- **Problema:** Arquivo `SurveilDrone-Net23.csv` com tamanho de 50MB impedindo o upload direto para o GitHub.
  - **Solução:** Criação do arquivo `.gitignore` para evitar o envio de grandes volumes de dados e documentação do link de origem do dataset no README.
- [ ] Desenvolver as queries de teste (consultas de proximidade e raio).
- [ ] Estudar NumPy e Matplotlib para aplicar a Regressão Linear nos resultados (em conjunto com o Prof. Valdomiro).
- [ ] Integrar o projeto ao escopo da bolsa FAPESP (em andamento com a coordenação).
