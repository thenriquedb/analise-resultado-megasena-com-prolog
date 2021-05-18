## Analíse dos resultados da Mega Sena

O trabalho consiste em usar o melhor de dois paradigmas de programação diferentes. O paradigma imperativo ou orientado a objetos pode ser usado para criar interfaces, manipular arquivos textos e fornece uma base de dados formatada, além é claro, de apresentar os resultados de forma amigável. 

O paradigma lógico pode ser usado para buscar informações em uma base de dados que é representada de forma simbólica. Assim, o programador pode usar o motor de inferências do Prolog e não terá que implementar suas consultas no arquivo fornecido. O trabalha consiste em importar e exibir informações de uma base de dados sobre os jogos da mega sena. 

O programa deve importar um arquivo texto que representa os dados e criar uma base de dados simbólica com todos os resultados dos jogos da megasena até a data da apresentação do trabalho. Um exemplo de fato pode
ser: jogo(1239, 2, 5, 34, 40, 70) – o primeiro átomo informa o número do sorteio e os outros seis representam os números sorteados. Para facilitar deixe os números sorteados em ordem numérica crescentes.

O programa proporcionará formas para que o usuário possa fazer perguntas a essa base de conhecimento como:
- O número X já foi sorteado alguma vez? Por exemplo: numero_sorteado(2).
- Qual número nunca foi sorteado? Por exemplo: sorteado(X).
- O jogo (X1,X2,X3,X4,X5,X6) já foi contemplado alguma vez? Por exemplo: jogo_sorteado(2,3,5,7,9,19).
- Algum jogo completo já foi contemplado mais de uma vez? Qual?
- Um número X foi sorteado quantas vezes?
- Qual o número foi mais sorteado?

#### Fonte
**[Hisórico de resultados em formato XLSX](https://redeloteria.com.br/mega-sena/todos-os-resultados-da-mega-sena/29275)**

### :link: Referências
[Predicate csv_read_file/3](https://www.swi-prolog.org/pldoc/man?predicate=csv_read_file/3)
