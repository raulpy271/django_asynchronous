# django Asynchronous

Este projeto utiliza django/celery para processamento de dados assincrono. 
Como exemplo, é criado um app que processa informações de linguagens de programação a partir de diferentes arquivos, 
após o processamento os dados são armazenados de forma unificada, e são apresentados ao usuário.

O app possue apenas a estrutra inicial. 
Além disso, o container com celery não consegue conectar com o container de mensageria. Segue os passos para reproduzir o erro: 

Criar a imagem do app:

```
docker build -t app .
```

Criar a imagem das tarefas asincronas:

```
docker build -t celery -f tasks/Dockerfile .
```

Subir os containers:

```
docker-compose up -d
```

Ver conexão com o rabbitMQ:

```
docker logs djangoasynchronous_tasks_1
```
