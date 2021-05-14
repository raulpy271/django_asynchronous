# django Asynchronous

Este projeto utiliza django/celery para processamento de dados assincrono. 
Como exemplo, é criado um app que processa informações de linguagens de programação a partir de diferentes arquivos, 
após o processamento os dados são armazenados de forma unificada, e são apresentados ao usuário.

> O app possue apenas a estrutra inicial. 

# Como executar

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
docker-compose --log-level INFO up -d
```

