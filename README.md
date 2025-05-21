# API Sportsync

Este projeto é uma API RESTful construída com Django REST Framework para gerenciar dados de usuários, desempenho, planos, treinos e avaliações em uma plataforma esportiva.

## Endpoints disponíveis

A API oferece endpoints genéricos para realizar operações CRUD nos seguintes modelos principais: `usuario`, `desempenho`, `plano`, `treino` e `avaliacao`.

## Como usar a API

Os endpoints seguem o padrão:

GET /<model_name>/
  ->Lista todos os objetos do modelo.

GET /<model_name>/id/
  ->Recupera um objeto específico pelo ID.

POST /<model_name>/create/
  ->Cria um novo objeto no modelo.

PUT /<model_name>/update/id/
  ->Atualiza o objeto com o ID informado.

DELETE /<model_name>/delete/id/
  ->Remove o objeto com o ID informado.



## Tecnologias utilizadas

- Python 3.x  
- Django  
- Django REST Framework  
- Render (para deploy)

