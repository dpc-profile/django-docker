# PlataCourses-django

Projeto de aprendizagem de aplicação web usando django e Docker.

### Instalação

Rode o terminal na pasta raiz do projeto, onde se encontra o arquivo Dockerfile.
Se qualquer alteração for feita em qualquer arquivo será preciso executar novamente o comando

```sh
$ docker build -t platacourses-docker .
```

### Rodando o Container

Ao terminar o processo de build, execute o comando abaixo 
```sh
$ docker run -it -d -p 8000:8000 platacourses-docker
```
Se o deu certo entre no link abaixo no navegador para acessar a pagina (espero que funcione)
```sh
http://localhost:8000
```

### Alterando o projeto

Para modificar algo no projeto primeiro é preciso ativar o ambiente virtual do python, o pipenv.
A versão do python do projeto é 3.8

Na pasta raiz do projeto execute:

```sh
$ pipenv shell
```
Caso não tenha o pipenv instalado rode no terminal:

```sh
$ sudo pip3 install pipenv
```

Com o ambiente do python ativo execute o comando na pasta raiz
```sh
$ pip3 install -r  requirements.txt 
```
O pip então ira instalar as bibliotecas necessarias que estão no arquivo, para que então seja possivel iniciar o projeto.


Se então todas as bibliotecas foram instaladas corretamente, rode o server.

```sh
$ python manager.py runserver
```

