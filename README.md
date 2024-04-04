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

## Conteneur Prometheus

### Configuration

Dans le fichier `prometheus.yml`, modifier la `target` pour quelle pointe vers l'IP publique de la machine sur laquelle seront lancé les commandes docker (l'utilisation du service n'a pas fonctionnée).
```
    static_configs:
      - targets:
        - <IP_publique>:8080
```

## Run le conteneur

### A partir du build de l'image

Dans le fichier `docker-compose.yml`, remplacez le nom de l'image référencée par le nom de l'image que vous venez de build. Renommez-la en enlevant les underscores et autre caractères spéciaux pour être sûr que ça fonctionne.
```
 flask_app:
    image: <nom_image>
    container_name: app_flask
    ports:
      - "8080:8080"
    restart: unless-stopped
```
Puis utilisez la commande : 
```
docker-compose up -d
```

### A partir de l'image pré-créée
```
docker-compose up -d
```


## Vérification

### Application Flask

Maintenant, vous pouvez visitez http://localhost:8080
```
HelloWorld!
```
Vous pouvez même vérifier la route http://localhost:8080/metrics pour voir les metrics de l'application en brut.

### Conteneur Prometheus

Vous pouvez également vous rendre sur http://localhost:9090 pour vérifier que Prometheus est bien fonctionnel et qu'il est bien lié à votre application.

## Conteneur Grafana

Rendez-vous sur http://localhost:3000, vous accéderez à l'interface Grafana.

### Configuration

Commencez par ajouter Prometheus dans les data sources : 
![image](https://github.com/Viveledelire/tp1_docker_devops/assets/97473758/401dd1b0-67b5-4cb4-ab59-dfc16dbe7264)

Ensuite, ajouter un dashboard (un graphique pour que ce soit visuel). <br />
Configurez ensuite ce graphique en selectionnant Prometheus dans les data sources (ajouté précédemment) et ajoutez la metrics `flask_http_request_total` <br />
Référence ci-dessous : 
![image](https://github.com/Viveledelire/tp1_docker_devops/assets/97473758/2e70ae86-a654-47d4-8cca-1bb1d76c85d9)

### Vérification

Vous pouvez désormais allez dans vos dashboards actif pour vérifier que la configuration a bien été prise en compte.
