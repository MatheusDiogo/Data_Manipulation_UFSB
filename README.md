<h2>Bibliotecas Utilizadas</h2>
<p>O código utiliza a biblioteca <code>pandas</code> e <code>re</code>.</p>

<h2>Inicialização de Variáveis</h2>
<p>O código inicializa as seguintes variáveis:</p>
<ul>
  <li><strong>NumR:</strong> Número de linhas para repetição.</li>
  <li><strong>lstIteracao:</strong> Lista que contém os conteúdos dos blocos de 17 linhas durante a iteração.</li>
  <li><strong>listsupervisorio:</strong> Lista que contém o conteúdo do arquivo .csv.</li>
  <li><strong>newlistsupervisorio:</strong> Lista que receberá o conteúdo sem caracteres indesejados.</li>
  <li><strong>supervisoriofinal:</strong> DataFrame que conterá a formatação final desejada.</li>
</ul>

<h2>Abertura do Arquivo</h2>
<p>O código solicita ao usuário que digite o nome do arquivo a ser tratado. Em seguida, lê o arquivo CSV especificado e armazena os dados em um DataFrame.</p>

<h2>Formatação do Arquivo</h2>
<p>O código realiza as seguintes etapas de formatação:</p>
<ol>
  <li>Conversão dos dados do arquivo para uma lista.</li>
  <li>Inserção do item "TAG" na primeira posição da lista, que se refere ao título da TAG do componente dentro do arquivo.</li>
  <li>Remoção de colchetes e aspas contidos nos elementos da lista.</li>
  <li>Criação do DataFrame formatado, separado por colunas: "Tag", "Descrição" e "Unidade de medida".</li>
  <li>Os dados são organizados em blocos de NumR linhas.</li>
</ol>

<h2>Saída do Arquivo</h2>
<p>O código realiza as seguintes etapas para a saída do arquivo:</p>
<ol>
  <li>Transposição do DataFrame formatado.</li>
  <li>Remoção das linhas 0 e 2 do DataFrame final.</li>
  <li>Atribuição do valor "Data e Hora" à primeira posição do DataFrame final.</li>
  <li>Exportação do DataFrame final para um arquivo Excel, sem índice, colunas ou cabeçalho.</li>
</ol>

<p>Certifique-se de ter permissões de gravação no diretório de execução para que o arquivo de saída possa ser criado.</p>
