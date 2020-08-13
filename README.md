# Simplemooc-django

Projeto de aprendizagem de aplicação web usando django e Docker.


### Instalação

Rode o terminal na pasta raiz do projeto, onde se encontra o arquivo Dockerfile.
Se qualquer alteração for feita em qualquer arquivo será preciso executar novamente o comando

```sh
$ docker build -t simple-dj-docker .
```

### Rodando o Container

Ao terminar o processo de build, execute o comando abaixo 
```sh
$ docker run -it -p 8000:8000 simple-dj-docker
```
Se o deu certo entre no link abaixo no navegador para acessar a pagina (espero que funcione)
```sh
$ http://localhost:8000
```

