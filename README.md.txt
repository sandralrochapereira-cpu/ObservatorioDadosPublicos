 UFCD10806 - Linguagens Scripting e Linha de comandos

----- Recolha e Automatização de dados em Python -----

      Atividade Orientada + Desafio Autónomo


O objetivo desta atividade é praticar e consolidar os conhecimentos adquiridos neste módulo, ou seja, organizar e limpar dados de uma API bem como de uma página Web de demonstração de scraping, guardando-os em .csv ,  partilhando a evolução deste projeto no GitHub, matéria do módulo anterior. Tenho também por objetivo sugerir uma melhoria à minha escolha, desenvolvendo-a e explicando-a.



Deve executar o código executando o seguinte código no terminal:

import sys
print(sys.executable)
import requests
from bs4 import BeautifulSoup
print("Ambiente Preparado")

A não inserção deste código no terminal impedi-lo-á de executar o programa corretamente, pois instala as bibliotecas de recurso necessários para a execução correta do programa.

Depois da mensagem "Ambiente Preparado" no terminal, pode executar o programa.
A fonte de url utilizada para o Ex.5 foi : https://jsonplaceholder.typicode.com/users
				Ex.6 foi: https://quotes.toscrape.com/
				

Respostas de desenvolvimento do .5:

5.5
Significado de requests.get(): Significa que está a fazer um pedido à fonte da variável)
 
	       timeout=10: Significa que o programa deve tentar executar o pedido no tempo máximo de 10 segundos antes de dedisdtir e imprimir uma mensagem de erro.

	       raise_for_status(): Faz o código parar e responder ao erro em vez de tentar ler os dados corrompidos.
	       
	       resposta.json(): É a lista de dados provenientes do site json.

5.6 Na lista "utilizadores" foram detectados o campo "nome" e o campo "email", sendo possível aceder aos mesmos percorrendo a lista com um for:
"for pessoa in utilizadores:
        print(pessoa["name"], "-", pessoa["email"])"

5.7 O número de utilizadores obtidos aparece no IDE Spyder antes da lista, com a mensagem "Total de utilizadores: (neste caso o total foi) 10)"


Respostas de desenvolvimento do .6:

6.9 
A função de BeautifulSoup é transformar os dados brutos num texto mais coerente e de onde seja fácil extrair dados.

A função de find_all() é encontrar nesse texto todos os registos que estão na condição descrita entre().

A função de select_one() é escolher um registo que corresponda à condição descrita entre ().

A função de append() é adicionar à lista os valores entre ().

6.10
A estrutura HTML da página pode influenciar o funcionamento do script na medida em que dependendo do encoding utilizado pode transformar certos caracteres em símbolos devido á diferente encriptação dos dados.


Respostas de desenvolvimento do .7:

O encoding=utf-8-sig serve para denominar a linguagem do encoding,
O delimiter=";" Serve para separar as colunas por ";"
O writeheader() serve para escrever o cabeçalho
O writerows() serve para escrever as linhas.

Para a parte B da atividade decidi implementar a melhoria "A", que consiste em filtrar os resultados de uma pesquisa onde se pode procurara apenas por parte do nome para obter os possíveis resultados.



