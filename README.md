# **API FastAPI + PostgreSQL (Docker & Docker Compose)**

## **Description**   
Petit projet personnel mettant en place une API Python (FastAPI) connectée à une base PostgreSQL, entièrement conteneurisée avec Docker et orchestrée via Docker Compose. L’objectif est d’avoir un environnement simple, propre et reproductible pour développer et tester une application backend avec une base SQL.


## **Fonctionnalités**   
* API FastAPI avec quelques endpoints REST (/health, /users)
* Base PostgreSQL configurée automatiquement au démarrage
* Conteneurisation complète de l’application via Docker
* Orchestration multi-services avec Docker Compose
* Persistance des données via un volume Docker

## **Stack technique**  
- Python (FastAPI) 
- PostgreSQL   
- Docker / Docker Compose   
- Uvicorn   
- psycopg2  

## **Prérequis **  
- Docker   
- Docker Compose  

## **Installation et exécution**  
1. Cloner le projet git clone https://github.com/SeybaESIG/api-postgres-docker.git cd api-postgres-docker  
2. Lancer l’environnement docker compose up --build  

L’API sera accessible sur :  http://localhost:8000  

## **Endpoints disponibles **  
- GET /health  
- GET /users  
- POST /users  

## **Variables d’environnement **  
Un fichier .env.example est fourni comme référence.  

## **Structure du projet **  
```
api-postgres-docker/
├── api/
│   ├── main.py
│   ├── db.py
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```

## **Licence**   
Libre d’utilisation pour toute expérimentation ou amélioration personnelle.


