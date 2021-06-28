![Home](./docs/../mega-sena/docs/app.png)

## :book: Sobre 
O trabalho consiste em usar o melhor de dois paradigmas de programação diferentes. O paradigma imperativo ou orientado a objetos pode ser usado para criar interfaces, manipular arquivos textos e fornece uma base de dados formatada, além é claro, de apresentar os resultados de forma amigável. 

O paradigma lógico pode ser usado para buscar informações em uma base de dados que é representada de forma simbólica. Assim, o programador pode usar o motor de inferências do Prolog e não terá que implementar suas consultas no arquivo fornecido. O trabalha consiste em importar e exibir informações de uma base de dados sobre os jogos da mega sena. 

### :memo: Atividades
- [X] O programa deve importar um arquivo texto que representa os dados e criar uma base de dados simbólica com todos os resultados dos jogos da megasena até a data da apresentação do trabalho. Um exemplo de fato pode ser: jogo(1239, 2, 5, 34, 40, 70) – o primeiro átomo informa o número do sorteio e os outros seis representam os números sorteados. 
- [X] O número X já foi sorteado alguma vez? Por exemplo: numero_sorteado(2).
- [X] Qual número nunca foi sorteado? Por exemplo: sorteado(X).
- [X] O jogo (X1,X2,X3,X4,X5,X6) já foi contemplado alguma vez? Por exemplo: jogo_sorteado(2,3,5,7,9,19).
- [X] Algum jogo completo já foi contemplado mais de uma vez? Qual?
- [X] Um número X foi sorteado quantas vezes?
- [X] Qual o número foi mais sorteado?

### 🏁 Primeiros passos
Para iniciar a aplicação basta executar o arquivo `run.sh`.

```shell
chmod 777 ./run.sh 
./run 
# or
python3 src/__main__.py 'data/games.csv'

```

### 🧰 Ferramentas
- [PySwip](https://pypi.org/project/pyswip/): PySwip é uma ponte Python e SWI-Prolog que permite consultar SWI-Prolog em seus programas Python; 
- [Flask](https://flask.palletsprojects.com/en/2.0.x/): Framework Python utilizado para a criação interface web;
- [Jinja](https://jinja.palletsprojects.com/): Ferramenta de *template engine* utilizado para a criação de pagínas HTML em aplicações Python;
- [Pandas](https://pandas.pydata.org/): Usado para leitura do arquivo CSV.
- [Tailwind CSS](https://tailwindcss.com/): Framework CSS para estilização.
  
### 🏗 Estrutura do projeto
Na pasta src, temos:

- `__main__.py`: arquivo de inicialização do servidor;
- `analyze.pl`: implementação das regras de negócios;
- `controllers.py`: realiza as consultas na base de dados em Prolog;
- `server.py`: configuração dos end points da API;
- `helpers/`: classes utilitárias do projeto. Dentre elas gostaria de destacar a classe **PrologMT** que é utilizada para adicionar suporte multithreading ao `pyswip`, visto que o mesmo não oferece suporte por padrão;
- `static/`: diretório com o código CSS e JS da aplicação;
- `templates/`: diretório com o código HTML.

### :link: Referências
- [Hisórico de resultados em formato XLSX](https://redeloteria.com.br/mega-sena/todos-os-resultados-da-mega-sena/29275)
- [Implementação do multithreading no pyswip](https://github.com/yuce/pyswip/issues/3#issuecomment-355458825)
- [flask-boilerplate](https://github.com/realpython/flask-boilerplate)
