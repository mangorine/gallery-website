# Galerie Ponthé

## Rôle de la galerie

La galerie Ponthé est un site web géré par le club Ponthé de l'Ecole des Ponts ParisTech. Il permet aux étudiants de l'école d'accéder aux photos prises par les membres du club lors des différents évènements.

## Documentation

La galerie se compose :
- d'un backend Django
- d'un frontend React
- d'une gestion du traffic ainsi que du service des statics et des medias par l'intermédiaire de Nginx
- d'un déploiement avec gestion des dépendances entièrement géré par Docker

### Déploiement

Importer le repository git avec la commande :
```
git clone git@github.com:adcrry/gallery-website.git
```

Configurer le .env avec les variables adéquates

<ins>**NB :**</ins> Ne pas oublier de modifier la 'SECRET_KEY' ainsi que le mot de passe de la base de donnée 'DB_PASSWORD'

Lancer l'ensemble des services de la galerie (back, db, webinstaller et nginx pour le déploiement en production) à l'aide de docker compose (et  pas docker-compose !) :
```
docker compose -f docker-compose-prod.yml up --build -d
```

Lorsque le build et le lancement sont terminés, il est possible de stoper et de relancer la galerie à l'aide des commandes suivantes :
```
docker compose -f docker-compose-prod.yml start
docker compose -f docker-compose-prod.yml stop
```

Si des modifications sont appliquées notamment au niveau du Docker, il est nécessaire de reconstruire les images afin d'appliquer les modifications, pour cela, il est possible d'utiliser :
```
docker compose -f docker-compose-prod.yml up --build -d
```
OU
```
docker compose -f docker-compose-prod.yml build
docker compose -f docker-compose-prod.yml start
```
### Problèmes de déploiement

Lors du lancement des commandes précédentes, il est possible que dans certains cas, le serveur ne démarre pas. Cela est souvent dû au passage du mode dévelopement au mode production (si l'on oublie l'option -f docker-compose-prod.yml)

Si vous souhaitez détecter les potentielles erreurs de déploiement, vous pouvez excécutez la commande suivante :
```
docker compose -f docker-compose-prod.yml up --build
```

1)``` Access denied to '/src/galerie/static/react/'```
Deux options sont possibles : simplement supprimer le dossier en question dans le repo, ou de manière plus brutale, donner toutes les permissions au dossier avec
```
chmod -r 777 /src/galerie/static/react/
```

2)```Tempory failure in name resolution```
Ce problème provient de la base donnée qui n'arrive pas à être détécté par Django. Cela peut provenir d'un changement de l'adresse de la db ou bien du passage de dévelopement vers production.

La solution est souvent de supprimer le dossier database/ est de relancer le déploiement.

3)```Could not connect to server: Connection refused```
Ce problème est dû à un changement du mot de passe de la db sans avoir supprimé le dossier database/.

3)``` [emerg] host not found in upstream 'back:8000'```
Cette erreur est souvent engendrée par un problème préalable dans le déploiement. Si aucun autre problème n'est observable, la meilleure solution est de réinstaller le repo est de lancer la commande de déploiement.

### Backend

### Frontend

### Nginx

### Docker
