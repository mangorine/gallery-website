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
### Backend

### Frontend

### Nginx

### Docker
