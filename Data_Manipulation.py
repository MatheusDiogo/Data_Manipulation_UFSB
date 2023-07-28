!pip install --upgrade xlrd

##################################################################################
#                         Campo de Bibliotecas                                   #
##################################################################################

import pandas as pd
import re

##################################################################################
#                         Abertura do Arquivo                                    #
##################################################################################

abrir = input("Digite o nome do arquivo para tratamento de dados: ") # variavel que guarda o caminho do arquivo
filename = abrir+".xlsx" #nome do arquivo de saida

abre_Arquivo = pd.read_csv(abrir, encoding='ISO-8859-1', delimiter = ';') #variavel do tipo data frame que guardara o arquivo

##################################################################################
#                         Inicializando variaveis                                #
##################################################################################
NumR = abre_Arquivo['TAG'].eq('Descrição').idxmax()+1 #Numero de linhas para repetição
lstIteracao = [] # Variavel do tipo lista que ira conter os conteudos dos blocos de 17 linhas na iteracao
listsupervisorio = [] # Variavel do tipo lista que ira conter o conteudo do arquivo .csv
newlistsupervisorio = [] # Variavel do tipo lista que ira receber a lista com o conteudo sem caracteres indesejados
supervisoriofinal = pd.DataFrame() # Variavel do tipo data frame que ira conter a formatacao final desejada

##################################################################################
#                         Formatacao do Arquivo                                  #
##################################################################################

listsupervisorio = abre_Arquivo.values.tolist() # Conversao dos dados do arquivo para armazenar na variavel do tipo lista

listsupervisorio.insert(0,'TAG') # Inserindo item na primeira posicao da lista, item refere-se ao titulo da TAG do componente dentro do arquivo

# Laco para exclusao de colchetes e aspas contidos nos elementos da lista
for i in range( len(listsupervisorio)):
    res = re.sub('[\[\'\]]', '', str(listsupervisorio[i])) # Uso de expressao regular para a remocao dos caracteres indesejados
    newlistsupervisorio.append(res) # Criacao de nova lista formatada sem caracteres indesejados

# Laco para criacao do data frame formatado e separado por colunas sendo as tres colunas inicias
# -> Tag - Descricao - Unidade de medida
# O valor da variavel de iteracao n varia de 0 ao valor da quantidade de linhas, sendo NumR o valor de repeticao dos blocos
for n in range(int(len(newlistsupervisorio)/NumR)):
  for x in range(n*NumR,NumR*(n+1)): # O valor de x calculado para criacao de lista com blocos de NumR linhas
    lstIteracao.append(newlistsupervisorio[x]) # Lista que ira conter o conteudo dos blocos de NumR linhas
  supervisoriofinal[n] = pd.Series(lstIteracao) # Criando as colunas do novo data frame formatado
  lstIteracao.clear() # Esvaziando a lista para o proximo bloco de iteracao

##################################################################################
#                         Saída do Arquivo                                       #
##################################################################################
supervisoriofinal = supervisoriofinal.T
supervisoriofinal = pd.DataFrame(supervisoriofinal.drop([0,2]))
supervisoriofinal.reset_index(drop = True, inplace = True)
supervisoriofinal.at[0, 0] = "Data e Hora"
supervisoriofinal

supervisoriofinal.to_excel(filename,index=False,columns=None,header=False) #convertendo para planilha excel
