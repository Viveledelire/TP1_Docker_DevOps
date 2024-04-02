# TP1_Docker_DevOps
Conteneurisation d'une application Flask avec monitoring Prometheus et dashboard Grafana.

## Build de l'application
```
$ git clone https://github.com/Viveledelire/tp1_docker_devops.git
$ docker build -t viveledelire/tp1_docker_devops .
```

## Téléchargement de l'image pré-créée
```
docker pull antoninlm/tp1dockerdevops
```
## Run le conteneur
```
docker run --name my-container -d -p 8080:8080 viveledelire/tp1_docker_devops ou antoninlm/tp1dockerdevops
```

Maintenant, vous pouvez visitez http://localhost:8080
```
HelloWorld!
```
