# Benchmark de Bancos de Dados Geoespaciais
**Português (BR) | [English](README.md)**

### Proposta de Iniciação Científica

**Aluna:** Giovanna Oliveira Ledo de Souza
**Título Provisório:** Análise de Desempenho e Arquitetura de Bancos de Dados Espaço-Temporais sob Cenários de Alta Concorrência

### 1. O Problema
Sistemas modernos que lidam com localização — como rastreamento de frotas, aplicativos de entrega e análise de rotas de drones — geram um volume massivo de dados geográficos a cada segundo. O grande desafio técnico atual é que, se o banco de dados não for otimizado para coordenadas (latitude/longitude), o sistema fica lento, travando as consultas e afetando a operação. O projeto propõe uma análise comparativa de performance entre dois modelos de bancos de dados: o relacional **PostgreSQL com PostGIS** e o NoSQL **MongoDB**, avaliando como cada um lida com dados geoespaciais reais em cenários de alto estresse (múltiplos acessos simultâneos). Adicionalmente, será avaliada a inclusão de uma camada de cache com **Redis** para otimização de consultas.

### 2. Justificativa e Relevância
A escolha da arquitetura de banco de dados impacta diretamente no custo de infraestrutura (consumo de RAM) e na experiência do usuário (latência).
*   **Lacuna Científica:** A literatura atual carece de testes que utilizem dados reais com ruídos (como trajetórias de drones e GPS) sob simulações de alta concorrência. A maioria dos estudos usa dados sintéticos e consultas isoladas.
*   **Relevância Prática:** Entender a fundo o funcionamento dos índices espaciais (como o *R-Tree* do PostGIS e o *2dsphere* do MongoDB) é essencial para projetar sistemas escaláveis de cidades inteligentes e monitoramento.
*   **Alinhamento Acadêmico:** O projeto une a base de Engenharia de Software e Banco de Dados com aplicações reais de geolocalização, preparando o terreno para pesquisas avançadas na área de GIS.

### 3. Metodologia
O estudo será conduzido como uma pesquisa experimental aplicada (benchmarking), seguindo estas etapas:
1.  **Obtenção de Dados:** Utilização de datasets públicos reais de trajetórias (ex: dados de drones ou GPS de veículos) para garantir que os testes reflitam a complexidade do mundo real.
2.  **Configuração do Ambiente:** Instalação e configuração do PostgreSQL/PostGIS, MongoDB e Redis (isolados via Docker para padronização do ambiente).
3.  **Ingestão de Dados:** Desenvolvimento de scripts em Python para popular os bancos de dados com os registros geográficos e criar os índices espaciais adequados.
4.  **Simulação de Carga (Stress Test):** Utilização de ferramentas (como Locust ou JMeter) para simular centenas de requisições simultâneas de busca por proximidade (ex: *"encontrar todos os veículos em um raio de 5 km"*).
5.  **Coleta e Análise de Métricas:** Medição do tempo de resposta (latência em milissegundos) e do consumo de memória RAM de cada solução. Os resultados serão documentados em gráficos comparativos para embasar a conclusão sobre qual arquitetura é mais eficiente para cada tipo de carga de trabalho.

---
*Este projeto faz parte de uma iniciativa de Iniciação Científica e visa embasar uma futura candidatura de Mestrado na área de Sistemas de Informação Geográfica.*
