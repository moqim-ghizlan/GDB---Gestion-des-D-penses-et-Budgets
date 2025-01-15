# GDB - Gestion des Dépenses et Budgets

## Description

GDB est une application web conçue pour la gestion des dépenses et des budgets. Basée sur le framework Django, cette plateforme offre des outils intuitifs pour suivre et analyser les dépenses mensuelles, tout en fournissant une gestion sécurisée des utilisateurs.

### Fonctionnalités Principales

- **Suivi des Dépenses** : Ajout et gestion des dépenses mensuelles.

- **Analyse Budgétaire** : Visualisation des dépenses par catégories.

- **Gestion des Utilisateurs** : Inscription, connexion et gestion des profils.

- **Interface Moderne** : Pages web interactives avec CSS et JavaScript.


## Structure du Projet

- `src/gdb/` : Configuration principale de l'application Django.

  - **`settings.py`** : Configuration globale.

  - **`urls.py`** : Routage principal.

- `src/spent/` : Gestion des dépenses.

  - **`models.py`** : Définition des modèles de données pour les dépenses.

  - **`views.py`** : Vues pour les opérations liées aux dépenses.

  - **`templates/`** : Modèles HTML pour les pages de dépenses.

- `src/user/` : Gestion des utilisateurs.

  - **`models.py`** : Modèles de données pour les utilisateurs.

  - **`views.py`** : Vues pour l'authentification et la gestion des utilisateurs.

- `static/assets/` : Fichiers CSS et JavaScript pour l'interface utilisateur.

- `templates/` : Modèles HTML globaux et composants.


## Installation

1. Clonez le dépôt :

   ```bash

   git clone <url-du-dépôt>

   cd gdb/src

   ```


2. Créez un environnement virtuel et activez-le :

   ```bash

   python -m venv env

   source env/bin/activate

   ```


3. Installez les dépendances :

   ```bash

   pip install -r requirements.txt

   ```


4. Configurez la base de données et appliquez les migrations :

   ```bash

   python manage.py makemigrations

   python manage.py migrate

   ```


5. Lancez l'application :

   ```bash

   python manage.py runserver

   ```


6. Accédez à l'application via [http://localhost:8000](http://localhost:8000).


## Prérequis

- **Python 3.8+**

- **Django** : Framework backend.

- **Virtualenv** : Gestion des environnements virtuels.


## Utilisation

1. Connectez-vous ou créez un compte utilisateur.

2. Ajoutez vos dépenses et analysez-les par catégories.

3. Visualisez les données budgétaires via des graphiques et des tableaux interactifs.


## Auteurs

Ce projet a été développé pour offrir une solution simple et efficace à la gestion des finances personnelles et professionnelles.

## Licence

Le projet est sous licence libre. Consultez le fichier LICENSE pour plus d'informations.
