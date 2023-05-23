import os
#Diretorio dos arquivos que precisam ser filtrados
Caminho = os.getcwd()
nome_do_arquivo = input("Digite o nome do arquivo com sua extenção : ")
caminho_completo = Caminho+"\\Arquivos\\"+nome_do_arquivo

lote = 0
contador = 22
Filtrada = "Nome | Numero de Controle | Valor | Protocolo | Lote | Data de Pagamento ---"

manipulador = open(caminho_completo,'r')

for linha in manipulador:
    print(linha)
"""

    linha = linha.rstrip(" ")
#Filtrando os nomes
    if contador == 22:
        Filtrada = Filtrada + str(linha)
        contador = 0
    contador = contador+1

    if contador == 6:
        Filtrada = Filtrada + str(linha)
#Filtrando os lotes
    if lote != 0:
        Filtrada = Filtrada + str(linha) + "---"
        lote = 0
    if "Lote:" in linha:
        lote =+1
#filtrando os valores    
    if ("valor"in linha) or ("Valor" in linha):
        Filtrada = Filtrada + str(linha)
"""    
manipulador.close()
Filtrada = Filtrada.replace("	", "")
Filtrada = Filtrada.replace("\n", "	")
Filtrada = Filtrada.replace("---", "\n")
Filtrada = Filtrada.replace("Valor: R$", "")
Filtrada = Filtrada.replace("valor: R$", "")
	
print(Filtrada)
arquivo = open(caminho_completo,'w')
arquivo.write(Filtrada)
arquivo.close()