import streamlit as st
import pandas as pd
import numpy as np
from requests import get 
import streamlit.components.v1 as components
from bs4 import BeautifulSoup as bs
def scrap_appart(nbre_page):
    gdf = pd.DataFrame()
    for i in range(nbre_page):
        url = 'https://sn.coinafrique.com/categorie/appartements?page={i}'
        res = get(url)
        soup = bs(res.text, 'html.parser')
        containers = soup.find_all("div",class_ = "col s6 m4 l3")        
        #Scraper plusieurs containers 
        df = []
        for container in containers:
            try:
                img_link = container.find("img",class_ = "ad__card-img")["src"]
                prix = int(container.find("p", class_="ad__card-price").text.replace(" ", "").replace("CFA", ""))
                adresse = container.find("p", class_="ad__card-location").text.replace("location_on","")
                href = container.find("a",class_ = "card-image ad__card-image waves-block waves-light")["href"]
                urll = 'https://sn.coinafrique.com' + str(href)
                resa = get(urll)
                soup = bs(resa.text, 'html.parser')
                containerr = soup.find("div",class_ = "ad__info")
                nbre_piece = int(containerr.find("span",class_ = "qt").text)
                dict_appart ={
                        "Nombre_pieces":nbre_piece,
                        "prix":prix,
                        "adresse":adresse,
                        "img_link":img_link,
                }
                df.append(dict_appart)
            except:
                pass
        DF = pd.DataFrame(df)
        gdf = pd.concat([gdf,DF],axis=0).reset_index(drop = True)
    # Standardiser la colonne "prix" et remplacer "prixsurdemande" par NaN
    gdf["prix"] = gdf["prix"].replace("Prixsurdemande", np.nan).astype(float)
    # Remplacer les NaN par la moyenne des prix et convertir en int
    gdf.fillna({"prix": gdf["prix"].mean()}, inplace = True)
    return gdf
def scrap_terrain(nbre_page):
    gdf = pd.DataFrame()
    for i in range(nbre_page):
        url = 'https://sn.coinafrique.com/categorie/terrains?page={i}'
        res = get(url)
        soup = bs(res.text, 'html.parser')
        containers = soup.find_all("div",class_ = "col s6 m4 l3")
        pdf = []
        for container in containers:
            try:
                img_link = container.find("img", class_="ad__card-img")["src"]
                prix = int(container.find("p", class_="ad__card-price").text.replace(" ", "").replace("CFA", ""))
                adresse = container.find("p", class_="ad__card-location").text.replace("location_on","")
                href = container.find("a", class_="card-image ad__card-image waves-block waves-light")["href"]
                urll = 'https://sn.coinafrique.com' + str(href)
                resa = get(urll)
                soup = bs(resa.text, 'html.parser')
                containerr = soup.find("div", class_="ad__info") 
                superficie = int(containerr.find("span", class_="qt").text.replace(" ", "").replace("m2", ""))
                dict_terrain_infos = {
                    "superficie": superficie,
                    "prix": prix,
                    "adresse": adresse,
                    "img_link": img_link,
                }
                pdf.append(dict_terrain_infos)
            except:
                pass    
        DF = pd.DataFrame(pdf)
        gdf = pd.concat([gdf,DF],axis=0).reset_index(drop = True)
    # Standardiser la colonne "prix" et remplacer "prixsurdemande" par NaN
    gdf["prix"] = gdf["prix"].replace("Prixsurdemande", np.nan).astype(float)
    # Remplacer les NaN par la moyenne des prix et convertir en int
    gdf.fillna({"prix": gdf["prix"].mean()}, inplace = True)
    return gdf         
def scrap_vehicule(nbre_page):
    #Faire un scraping sur toutes les pages 
    dats = pd.DataFrame()
    for i in range(nbre_page):
        url = "https://dakar-auto.com/senegal/voitures-4?&page={i}}"
        res = get(url)
        soup = bs(res.text,"html.parser")
        containers = soup.find_all("div",class_ = "listing-card")
        dfa = []
        for container in containers:
            try:
                gen_inf = container.find("h2",class_ = "listing-card__header__title mb-md-2 mb-0").text.strip().split()
                marque = gen_inf[0]
                modele = "".join(gen_inf[1:2])
                annee = gen_inf[-1]
                prix = container.find("h3",class_ = "listing-card__header__price font-weight-bold text-uppercase mb-0").text.strip().replace("\u202f","").replace(" F CFA","")
                adresse = container.find("span",class_ = "town-suburb d-inline-block").text.strip().replace(",","")
                reference = container.find("div",class_ = "col-12 listing-card__properties d-none d-sm-block").text.strip().replace("Ref. ","")
                gen_inf_car = container.find_all("li",class_ = "listing-card__attribute list-inline-item")
                kilometrage = gen_inf_car[1].text.split()
                kilometrage = kilometrage[0]
                boite_vitesse = gen_inf_car[2].text.strip()
                carburant = gen_inf_car[3].text.strip()
                dict_car_infos = {
                    "marque":marque,
                    "modele":modele,
                    "annee":annee,
                    "prix":prix,
                    "adresse":adresse,
                    "kilometrage":kilometrage,
                    "boite_vitesse":boite_vitesse,
                    "carburant":carburant}
                dfa.append(dict_car_infos)     
            except:
                pass
        DF = pd.DataFrame(dfa)
        dats = pd.concat([dats,DF],axis=0).reset_index(drop = True)
    return dats
def scrap_moto(nbre_page):
    #Scraping sur plusieurs pages
    gdf = pd.DataFrame()
    for i in range(nbre_page):    
        url = "https://dakar-auto.com/senegal/motos-and-scooters-3?&page={i}"
        res = get(url)
        soup = bs(res.text,"html.parser") # permet de stocker le code html dans un objet bs
        containers = soup.find_all("div", class_ = "listing-card")
        #Generaliser sur les autres container
        dafr = []
        for container in containers:
            try:
                gen_inf = container.find("h2", class_ = "listing-card__header__title mb-md-2 mb-0").text.strip().split()
                marque = gen_inf[0]
                modele = ''.join(gen_inf[1: len(gen_inf) - 1])
                annee = gen_inf[-1]
                prix = container.find("h3", class_ = "listing-card__header__price font-weight-bold text-uppercase mb-0").text.strip().replace("\u202f","").replace(" F CFA","")
                adresse = container.find("div",class_ ="col-12 entry-zone-address").text.replace("\n","")
                reference = container.find("li",class_ ="listing-card__attribute list-inline-item").text.strip().replace("Ref. ","")
                kilometrage = container.find("ul",class_ ="listing-card__attribute-list list-inline mb-0").text.strip().split()    
                kil = kilometrage[2]
                img_link = "https://dakar-auto.com" + container.find("img",class_="img-fluid")["src"]
                img_link
                dic = {
                    "marque":marque,
                    "modele":modele,
                    "annee":annee,
                    "prix":prix,
                    "adresse":adresse,
                    "reference":reference,
                    "kilometrage":kil,
                    "img_link":img_link}
                dafr.append(dic)
            except:
                pass
        DF = pd.DataFrame(dafr)
        gdf = pd.concat([gdf,DF],axis=0).reset_index(drop = True)   
    return gdf        