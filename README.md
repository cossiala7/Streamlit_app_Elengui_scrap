# Elengui Scrap

## Description

Elengui Scrap est une application Streamlit intuitive permettant l'extraction, l'analyse et la visualisation de données issues de sites d'annonces en ligne. Elle repose sur le web scraping pour récupérer des informations en temps réel et propose des outils de visualisation interactifs.

## Fonctionnalités

### 1. **Scraping avec BeautifulSoup**
- Extraction de données depuis **Coin Afrique Sénégal** (Appartements, Terrains) et **Dakar Auto** (Véhicules, Motos).
- Définition du nombre de pages à scraper.
- Exportation des données en **CSV**.

### 2. **Exploration de jeux de données**
- Accès à une bibliothèque de datasets.
- Téléchargement en format **CSV**.

### 3. **Visualisation interactive**
- Chargement et exploration de fichiers **CSV** et **Excel**.
- Affichage des statistiques descriptives.
- Création de graphiques dynamiques (Histogramme, Boxplot, Scatter plot, Heatmap, Diagramme en barres et circulaire).

### 4. **Évaluation de l’application**
- Formulaire intégré pour recueillir les avis des utilisateurs.

## Technologies utilisées
- **Python** (Streamlit, Pandas, NumPy, Matplotlib, Seaborn, BeautifulSoup, Requests)

## Installation
1. **Cloner le dépôt**
```bash
    git clone https://github.com/votre-repo/ElenguiScrap.git
    cd ElenguiScrap
```

2. **Créer un environnement virtuel et installer les dépendances**
```bash
    python -m venv env
    source env/bin/activate  # macOS/Linux
    env\Scripts\activate  # Windows
    pip install -r requirements.txt
```

3. **Lancer l’application**
```bash
    streamlit run app.py
```

## Utilisation
1. Sélectionner une option dans la barre latérale : **Accueil, Scrap, Datasets ou Visualisation**.
2. Configurer les paramètres de scraping ou télécharger un dataset.
3. Analyser et visualiser les données obtenues.
4. Partager vos retours via le formulaire d’évaluation.

## Contribution
Les contributions sont les bienvenues ! Forkez ce dépôt et soumettez vos Pull Requests.

## Licence
Ce projet est sous licence **MIT**.

