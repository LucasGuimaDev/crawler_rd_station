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

Este script python faz a leitura de um arquivo .csv com uma lista de sites e então realiza a verificação de modo paralelo se esses sites utilizam a plataforma RD Station através de suas tags e então salva o resultado em um novo arquivo .csv. 

O arquivo de resposta pode vir com as informações de "yes" caso alguma tag seja encontrada, "no" caso não seja encontrada, "erro..." mensagem de erro e o tipo do erro caso o crawler não consiga estabelecer contato com o link e, por fim, "timeout" caso a requisição demore mais do que o tempo estipulado.
