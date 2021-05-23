# django Asynchronous

Este projeto utiliza django/celery para processamento de dados assincrono. 
Como exemplo, é criado um app que processa informações de linguagens de programação a partir de diferentes arquivos, 
após o processamento os dados são armazenados de forma unificada, e são apresentados ao usuário.

> No momento, toda a arquitetura está pronta(os containers conseguem conectar com o rabbit e com o db). Além disso, são processados dados em arquivos `csv`, `tsv`, excel, `yml`, `json`e `pdf`. Como melhoria, eu sugiro fazer o paginação dos dados enviados pela API ao client, isto torna mais leve as respostas do servidor, e o faz responder mais rápido.

# Arquitetura

![Imagem da arquitetura, retirado de: https://www.bogotobogo.com](https://www.bogotobogo.com/DevOps/Docker/images/Docker-minikube-3/django_celery_architecture.png)

este projeto é formado por 3 containers. O primeiro trata-se de uma servidor web com django, enquanto o segundo tem utilizadade de processar tarefas custosas de forma asincrona. 

Ambos compartilham um banco de dados (no momento é SQLite3, por simplicidade). Por útlimo, há uma plataforma de mensageria que conecta os containers iníciais.

# Como executar

Criar a imagem do app:

```
docker build -t app .
```

Subir os containers:

```
docker-compose --log-level INFO up -d
```

Agora, o app está escutando em [localhost](http://localhost:8000).
