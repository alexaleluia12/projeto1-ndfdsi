# Projeto 1 NanoDegree Data Science 1 Udacity

Neste projeto, você usará os dados fornecidos pelo Motivate, um provedor de sistema de bicicletas compartilhadas para 
diversas grandes cidades dos Estados Unidos, para descobrir os padrões de uso do compartilhamento de bicicletas. 
Você analisará o uso do sistema de uma das maiores cidades dos Estados Unidos: Chicago.

## Rodar
```
(precisa do arquivo chicago.csv com os dados. O Github limita subir arquivos maiores que 100MB)
git clone https://github.com/alexaleluia12/projeto1-ndfdsi.git projeto1
cd projeto1
pip install -r requirements.txt
python chicago_bikeshare_pt.py
```

## TODO
- Tarefa 1: Mostre as 20 primeiras amostras (linhas) da base de dados
- Tarefa 2: Mostre o gênero (coluna) das 20 primeiras amostras
- Tarefa 3: Cria uma função para pegar colunas como lista
- Tarefa 4: Conte quantas pessoas de cada gênero
- Tarefa 5: Crie uma função para contar os gêneros
- Tarefa 6: Mostre o gênero mais popular
- Tarefa 7: Mostre um gráfico usando os dados anteriores
- Tarefa 8: Responda o motivo do número de homens e mulheres não bater com a quantidade de amostras
- Tarefa 9: Encontre o valor mínimo, máximo, média e mediana da duração de viagens
- Tarefa 10: Mostre todas estações da base de dados
- Tarefa 11: Crie uma função que conte a ocorrência de qualquer coluna (opcional)


---
### dados
    Horário de início (ex., 2017-01-01 00:07:57)
    Horário de término (ex., 2017-01-01 00:20:53)
    Duração da viagem (em segundos, ex., 776)
    Estação inicial (ex., Broadway & Barry Avenue)
    Estação final (ex., Sedgwick St & do North Ave)
    Tipo de usuário (assinante ou cliente)
    Gênero
    Ano de nascimento




### Padrão definir documentação em funções/metodos
```py
# def new_function(param1: int, param2: str) -> list:
      """
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.

      """
```