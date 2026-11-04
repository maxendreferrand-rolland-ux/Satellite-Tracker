# 🛰️ Satellite Tracker

Suivi en temps réel des stations spatiales à partir de données orbitales réelles.

Le projet est découpé en deux parties :
- **un serveur Python** qui récupère les données orbitales et calcule la position des satellites
- **un client Java (JavaFX)** qui affichera les satellites sur une carte du monde *(à venir)*

> 🚧 Projet en cours de développement

## Fonctionnalités actuelles

- Téléchargement des données orbitales (TLE) des stations spatiales depuis [CelesTrak](https://celestrak.org)
- Calcul de la position actuelle d'un satellite : latitude, longitude et altitude
- Affichage de la position de l'ISS et de la station spatiale chinoise Tiangong

## Comment ça marche ?

Un **TLE** (*Two-Line Element*) est un format qui décrit l'orbite d'un satellite en deux lignes de données (inclinaison, excentricité, nombre de révolutions par jour…). CelesTrak publie gratuitement ces données, mises à jour régulièrement.

À partir d'un TLE, la librairie [Skyfield](https://rhodesmill.org/skyfield/) utilise le modèle de propagation **SGP4** pour calculer la position du satellite à n'importe quel instant, puis la convertit en coordonnées géographiques.

## Technologies

| Partie | Technologies |
|---|---|
| Serveur | Python, Skyfield |
| Client | Java, JavaFX *(à venir)* |

## Structure du projet

```
satellite-tracker/
├── serveur/
│   ├── tracker/
│   │   ├── donnees.py      # récupération des TLE et affichage des positions
│   │   ├── calculs.py
│   │   └── api.py
│   ├── tests/
│   └── requirements.txt
├── client/
└── README.md
```

## Installation

```bash
git clone https://github.com/maxendreferrand-rolland-ux/satellite-tracker.git
cd satellite-tracker/serveur
python -m venv .venv
```

Activation de l'environnement virtuel :

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (Git Bash)
source .venv/Scripts/activate

# Linux / macOS
source .venv/bin/activate
```

Installation des dépendances :

```bash
pip install -r requirements.txt
```

## Utilisation

Depuis le dossier `serveur/`, avec l'environnement virtuel activé :

```bash
python -m tracker.donnees
```

Exemple de sortie :

```
ISS (ZARYA)
Latitude : -51.68
Longitude : -118.33
Altitude : 435.63 km

CSS (TIANHE)
Latitude : 12.47
Longitude : 87.21
Altitude : 389.14 km
```

## Feuille de route

- [x] Récupération des TLE et calcul de la position des stations spatiales
- [ ] Mise en cache des données et tests unitaires (pytest)
- [ ] Prédiction des passages visibles au-dessus d'un lieu donné
- [ ] API REST avec FastAPI
- [ ] Client JavaFX : liste des satellites
- [ ] Carte du monde avec positions en temps réel
- [ ] Trace au sol des orbites
- [ ] Intégration continue avec GitHub Actions

## Sources des données

Données orbitales fournies par [CelesTrak](https://celestrak.org).

## Auteur

**Maxendre Ferrand-Rolland**, étudiant en BUT Informatique à l'IUT de Rodez