# por Alex Aleluia

def printN(list_data: list, n: int) -> None:
    """
    Print os primeiros n elemtnos de list_data
    Argumentos:
        list_data: lista com os valores que deseja printar
        n: quantidade de prints
    Retorno:
    """
    for i in list_data[:n]:
        print(i)


def getColumnN(list_data: list, index: int) -> list:
    """
    Retorna generator da coluna index
    nao aceita indice negativo
    Argumentos:
        list_data: matrix linhas e colunas
        index: coluna que deseja extrair
    Retorno:
        retorna generator da coluna index
    """
    # pre condicao: indice de coluna valido
    if not (index >= 0 and index <= (len(list_data[0]) - 1)):
        max_value = len(list_data[0])
        template = "Indece {} incorreto para matriz com coluna de tamanho {}"
        raise Exception(template.format(index, max_value))
    
    for i in list_data:
        yield i[index]


