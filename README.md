## Crawler RD Statiom
### Pacotes e bibliotecas utilizadas
- **csv**
- **requests**
- **re**
- **tldextract**
- **time**
- **os**
- **joblib**
- **pathlib**

_Pode ser necessário a instalção de algumas bibliotecas e pacotes para a utilização do código_

### Projeto

Existem dois arquivos .py presentes nesse repositório que servem para identificar a presença de tags relacionados ao RD Station presentes nos sites. Basicamente é realizada a leitura de um arquivo .csv com os sites que se deseja fazer a pesquisa e em seguida um novo arquivo . csv é criado com duas colunas separadas por "," uma com o link e a outra com a resposta da requisição: "s" caso exista alguma tag presente no site verificado, "n" caso não exista, 'timeout' caso a requisição ultrapasse o limite de tempo e por último "erro: ..." caso dê erro na requisição com o número e o tipo do erro . Existe um arquivo .csv com sites neste repositório para a realização de testes


Os dois arquivos .py são basicamente iguais, porém o "crawler_rd_station_paralelo.py" utiliza paralelização para a realização da extração.

De acordo com os testes realizados com os dois arquivos obteve-se uma certa diferença no tempo de processamento. Segue abaixo:

- **crawler_rd_station_paralelo.py -** obteve um tempo médio de +/- 40 segundos.
- **crawler_rd_station.py -** obteve um tempo médio de +/- 270 segundos.
