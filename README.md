# django Asynchronous

Este projeto utiliza django/celery para processamento de dados assincrono. 
Como exemplo, é criado um app que processa informações de linguagens de programação a partir de diferentes arquivos, 
após o processamento os dados são armazenados de forma unificada, e são apresentados ao usuário.

> O app possue apenas a estrutura inicial. 

# Arquitetura

este projeto é formado por 3 containers. O primeiro trata-se de uma servidor web com django, enquanto o segundo tem utilizadade de processar tarefas custosas de forma asincrona. 

Ambos compartilham um banco de dados (no momento é SQLite3, por simplicidade). Por útlimo, há uma plataforma de mensageria que conecta os containers iníciais.

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

Agora, o app está escutando em [localhost](http://localhost:8000).
