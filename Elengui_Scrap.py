import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from requests import get 
import necessary as ns
import streamlit.components.v1 as components
from bs4 import BeautifulSoup as bs
from pathlib import Path

# Contenu de la sidebar
st.sidebar.title("📌 Menu")
option = st.sidebar.selectbox("🎯 Choisissez une option", ["Accueil","Scrap avec Beautifulsoup","Datasets" ,"Visualisation"],index = 0, )
st.sidebar.write("---")
st.sidebar.write(""" Elengui Scrap
votre assistant data!
données temps réel,
analyse instantanée,
multi-plateformes,
export simple.
La donnée n'a jamais été aussi accessible !""")
st.sidebar.write("---")

st.sidebar.link_button("Evaluer l'app","https://ee.kobotoolbox.org/i/d1fEvstv")
# Ajout de styles CSS personnalisés

st.markdown(""" 
    <style>
        .st-emotion-cache-4tlk2p egexzqm0{
            width : 270px;
        }
        .st-emotion-cache-jp5qej efj1jhq2{
            display: inline-flex;
            -moz-box-align: center;
            align-items: center;
            -moz-box-pack: center;
            justify-content: center;
            font-weight: 400;
            padding: 0.25rem 0.75rem;
            border-radius: 0.5rem;
            min-height: 2.5rem;
            margin: 0px;
            line-height: 1.6;
            text-decoration: none;
            user-select: none;
            background-color: rgb(249, 249, 251);
            color: rgb(49, 51, 63);
            border: 1px solid rgba(49, 51, 63, 0.2);
            width: 270px;
        }
        @media (prefers-color-scheme: dark) {
            body {
                background-color: black;
                color: white;
            }
        }

        @media (prefers-color-scheme: light) {
            body {
                background-color: white;
                color: black;
            }
        }
        /* Titres et sous-titres en bleu foncé */
        h1, h2, h3 {
            text-align: center;
        }

        /* Boutons et sélections */
        .stSelectbox label {
            font-weight: bold;
        }

        /* Cartes et blocs de contenu */
        .css-1lcbmhc {
            background: white;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        [data-testid="stSidebar"] button {
        width: 100%;
        color: #4B5320;
        }
    </style>
""", unsafe_allow_html=True)
# Titre principal
# Contenu principal
if option == "Accueil":
    st.title("✨ Bienvenue sur Elengui scrap")
    st.header(" ")
    st.write("""
    Elengui Scrap est une application puissante et intuitive de Web Scraping dédiée à l'extraction et à l'analyse des annonces  en ligne. Grâce à ses fonctionnalités avancées, vous pouvez facilement récupérer, télécharger et visualiser des données essentielles pour mieux comprendre le marché .
    🚀 Quelles sont les fonctionnalités clés ?

    🔍 1. Scraper les données en temps réel
        Scrapez les annonces  sur deux sites différents, avec la possibilité de choisir entre deux catégories par site.
        Collectez des informations précieuses comme la superficie, le prix, l'adresse et bien plus encore.
        Utilisation de BeautifulSoup pour un scraping efficace et structuré.

    📥 2. Télécharger des jeux de données variés
        En plus des données brutes extraites, nous mettons à disposition plusieurs jeux de données pour vous permettre de comparer et d’analyser différentes sources.
        Il vous suffit de sélectionner le jeu de données qui vous intéresse !

    📊 3. Visualiser les données
        Analysez rapidement les tendances grâce à des graphiques et visualisations interactives.
        Obtenez une vue d’ensemble claire des prix, des superficies et d’autres indicateurs clés du marché immobilier.

    📝 4. Évaluer l’application
        Donnez-nous votre avis via un formulaire unique dédié aux retours utilisateurs.
        Vos suggestions sont essentielles pour améliorer en continu l’expérience Elengui Scrap.
    
    💡 Pourquoi choisir Elengui Scrap ?
    
    ✅ Facile d’utilisation – Une interface intuitive qui vous guide à chaque étape.
    
    ✅ Rapide et efficace – Un scraping optimisé pour extraire un maximum d’informations en un minimum de temps.
    
    ✅ Analyse complète – Téléchargez, explorez et visualisez les données en quelques clics.
    
    Sélectionnez simplement une option dans le menu et profitez pleinement !""")

elif option == "Scrap avec Beautifulsoup":
    st.title("Beautifulsoup Elengui")
    st.write("Avec l'option Scraper avec Beautifulsoup d'Elengui Scrap, scrapez facilement les données de deux catégories distinctes des sites [Coin Afrique Sénégal](https://sn.coinafrique.com) et [Dakar auto](https://dakar-auto.com/). Définissez vous-même le nombre de pages à extraire !")
    with st.form("bs_forms"):
        data_scrap = st.selectbox("Quel site voulez vous scrapez?",["","Coin Afrique Sénégal","Dakar Auto"])
        if data_scrap == "Coin Afrique Sénégal":
            data = st.radio(" Vous êtes sur la catégorie **Terrains**. Souhaitez-vous en choisir une autre ?",["Terrains","Appartements"])
        elif data_scrap == "Dakar Auto" :
            data = st.radio("Quelles données voulez vous recuperer pour ce site?",["Vehicules","Motos"]) 
        else:
            pass    
        nbre_page = st.number_input("Entrez le nombre de page que vous voulez scraper", min_value=1, max_value=100)
        file_name= st.text_input("Entrez le nom du csv")   
        submit = st.form_submit_button("Commencez le scrap✅")            
    if submit:
        if  not file_name:
            if st.form_submit_button:
                st.write("❌ Impossible d'extraire les données veuillez verifier les champs...")
            else:
                pass    
        else:    
            with st.spinner("Scraping en cours..."):
                if data_scrap =="Coin Afrique Sénégal" and data == "Appartements":
                    gdf = ns.scrap_appart(nbre_page)
                    st.write(f"Dimension du jeu de données: {gdf.shape[0]} lignes et {gdf.shape[1]} colonnes")  
                    st.write(gdf)      
                    # Convertir le DataFrame en CSV (sans index)
                    csv2 = gdf.to_csv(index=False).encode('utf-8')
                    # Bouton de téléchargement
                    st.download_button(
                        label="Télécharger les données en CSV",
                        data=csv2,
                        file_name= str(file_name) + ".csv",
                        mime="text/csv")        
                elif data_scrap =="Coin Afrique Sénégal" and data == "Terrains":
                    #Faire un scraping sur toutes les pages 
                    gdf = ns.scrap_terrain(nbre_page) 
                    st.write(f"Dimension du jeu de données: {gdf.shape[0]} lignes et {gdf.shape[1]} colonnes")  
                    st.write(gdf)      
                    # Convertir le DataFrame en CSV (sans index)
                    csv2 = gdf.to_csv(index=False).encode('utf-8')
                    # Bouton de téléchargement
                    st.download_button(
                        label="Télécharger les données en CSV",
                        data=csv2,
                        file_name= str(file_name) + ".csv",
                        mime="text/csv")   
                    #Gdf["prix"] = Gdf["prix"].astype(int)
                elif data_scrap == "Dakar Auto" and data ==  "Vehicules":
                    dr = ns.scrap_vehicule(nbre_page)
                    st.write(f"Dimension du jeu de données: {dr.shape[0]} lignes et {dr.shape[1]} colonnes")  
                    st.write(dr)      
                    # Convertir le DataFrame en CSV (sans index)
                    csv2 = dr.to_csv(index=False).encode('utf-8')
                    # Bouton de téléchargement
                    st.download_button(
                        label="Télécharger les données en CSV",
                        data=csv2,
                        file_name= str(file_name) + ".csv",
                        mime="text/csv")   
                elif data_scrap == "Dakar Auto" and data ==  "Motos":
                    mt = ns.scrap_moto(nbre_page) 
                    st.write(f"Dimension du jeu de données: {mt.shape[0]} lignes et {mt.shape[1]} colonnes")  
                    st.write(mt)      
                    # Convertir le DataFrame en CSV (sans index)
                    csv2 = mt.to_csv(index=False).encode('utf-8')
                    # Bouton de téléchargement
                    st.download_button(
                        label="Télécharger les données en CSV",
                        data=csv2,
                        file_name= str(file_name) + ".csv",
                        mime="text/csv")
                else:
                    pass            
elif option == "Datasets":
    st.title("Fenetres datasets")
    st.write("""Explorez une sélection de datasets prêts à l'emploi pour tester vos analyses et visualisations.
        Ces jeux de données couvrent divers domaines et vous permettent de vous entraîner. Téléchargez un dataset et commencez votre exploration !""")
    path = Path("./data")
    csv_files = [f.name for f in path.glob("*.csv")]
    dtwnt = st.selectbox("Quel jeu de données voulez-vous télécharger ?", csv_files)
    if dtwnt:  
        file_path = path / dtwnt  # Construire le chemin complet
        file = pd.read_csv(file_path)  # Lire le CSV
        st.write(file)  # Afficher les données
        csv_data = file.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Télécharger les données en CSV",
            data=csv_data,
            file_name=dtwnt,
            mime="text/csv"
        )
elif option == "Visualisation":
    st.title("Visualisation des fichiers")
    st.markdown("""
    📂 **Chargez un fichier pour afficher son contenu**  
    Vous pouvez importer des fichiers **Excel ou CSV**, et leur contenu sera affiché automatiquement.  
    Cela vous permet d'explorer rapidement vos données directement dans l'application.

    ⚠️ Pour une bonne visualisation des données, **assurez-vous que le type de chaque colonne est valide** 
    """)
    # Bouton pour charger un fichier
    uploaded_file = st.file_uploader("Choisissez un fichier", type=["csv", "xlsx"])

    if uploaded_file is not None:
        st.success("Fichier chargé avec succès !")
        # Vérification du type de fichier et affichage du contenu
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file, sep=None, engine="python")
            st.subheader("Type des colonnes")
            st.dataframe(pd.DataFrame(df.dtypes, columns=["Type"]).T) 
            st.subheader("📊 Statistiques descriptives")
            st.write(df.describe())
            st.subheader("Aperçu des données")
            st.write(df.head())
            st.subheader("Visualisation graphique des données")
            cate = df.select_dtypes(include = "object" ) 
            columns_cat = cate.columns.tolist()
            numeric = df.select_dtypes(include="number")
            columns_numeric = numeric.columns.tolist()
            type_avr = st.selectbox("Quelles types de données voulez-vous visualiser ?",["Numérique","Categorielle"])
            if type_avr == "Numérique":
                op_vis = st.selectbox("Quelles données voulez-vous visualiser ?", columns_numeric)
                # 📊 Sélection du type de visualisation
                chart_type = st.selectbox("Choisissez un type de visualisation", 
                                        [" Histogramme", 
                                        " Boxplot", 
                                        " Scatter plot", 
                                        " Heatmap (Corrélations)"])
                try:
                    # 🔵 Affichage des graphiques en fonction du choix
                    fig, ax = plt.subplots(figsize=(8, 5))
                    if chart_type == " Histogramme":
                        ax.hist(df[op_vis], bins=20, color='skyblue', edgecolor='black')
                        ax.set_title(f"Histogramme de {op_vis}")
                        ax.set_xlabel(op_vis)
                        ax.set_ylabel("Fréquence")
                        st.pyplot(fig)
                    elif chart_type == " Boxplot":
                        sns.boxplot(y=df[op_vis], ax=ax, color="lightblue")
                        ax.set_title(f"Boxplot de {op_vis}")
                        st.pyplot(fig)
                    elif chart_type == " Scatter plot":
                        y_var = st.selectbox("Sélectionnez une autre variable numérique", columns_numeric)
                        sns.scatterplot(x=df[op_vis], y=df[y_var], ax=ax, color="blue")
                        ax.set_title(f"Relation entre {op_vis} et {y_var}")
                        ax.set_xlabel(op_vis)
                        ax.set_ylabel(y_var)
                        st.pyplot(fig)
                    elif chart_type == " Heatmap (Corrélations)":
                        fig, ax = plt.subplots(figsize=(8, 6))
                        sns.heatmap(numeric.corr(), annot=True, cmap="coolwarm", ax=ax)
                        st.pyplot(fig)
                except:
                    st.error("Impossible d'affichier le graphe veuillez verifier votre dataset")    
            else:
                op_cat = st.selectbox("Choisissez une variable catégorielle :", columns_cat)
                # Sélection du type de graphique
                chart_type_cat = st.selectbox("Choisissez un type de graphique :", 
                                            [" Diagramme en barres", 
                                            " Diagramme circulaire", 
                                            " Boxplot (comparaison avec une variable numérique)"])

                fig, ax = plt.subplots(figsize=(8, 5))
                try:
                    if chart_type_cat == " Diagramme en barres":
                        sns.countplot(x=df[op_cat], ax=ax, palette="viridis", order=df[op_cat].value_counts().index)
                        ax.set_title(f"Répartition des catégories de {op_cat}")
                        ax.set_xlabel(op_cat)
                        ax.set_ylabel("Nombre d’occurrences")
                        ax.tick_params(axis='x', rotation=45)
                        st.pyplot(fig)

                    elif chart_type_cat == " Diagramme circulaire":
                        data_count = df[op_cat].value_counts()
                        ax.pie(data_count, labels=data_count.index, autopct='%1.1f%%', colors=sns.color_palette("pastel"))
                        ax.set_title(f"Répartition des catégories de {op_cat}")
                        st.pyplot(fig)

                    elif chart_type_cat == " Boxplot (comparaison avec une variable numérique)":
                        # Sélectionner une variable numérique pour comparer avec la variable catégorielle
                        y_var = st.selectbox("Sélectionnez une variable numérique :", numeric.columns.tolist())
                        sns.boxplot(x=df[op_cat], y=df[y_var], ax=ax, palette="coolwarm")
                        ax.set_title(f"Distribution de {y_var} selon {op_cat}")
                        ax.tick_params(axis='x', rotation=45)
                        st.pyplot(fig)
                except:
                    st.error("Impossible d'affichier le graphe veuillez verifier votre dataset")
        elif uploaded_file.name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file, sep=None, engine="python")
            st.dataframe(pd.DataFrame(df.dtypes, columns=["Type"]).T) 
            st.subheader("📊 Statistiques descriptives")
            st.write(df.describe())
            st.subheader("Aperçu des données")
            st.write(df.head())
            numeric = df.select_dtypes(include="number")
        else:
            st.error("Format de fichier non pris en charge.")
            

           
