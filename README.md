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
docker-compose up -d
```

Maintenant, vous pouvez visitez http://localhost:8080
```
HelloWorld!
```
Vous pouvez même vérifier la route http://localhost:8080/metrics pour voir les metrics de l'application en brut.

## Conteneur Prometheus

### Configuration
Dans le fichier `prometheus.yml`, modifier la `target` pour quelle pointe vers l'IP publique du conteneur de l'application Flask (l'utilisation du service n'a pas fonctionnée).
```
    static_configs:
      - targets:
        - <IP_publique>:8080
```
