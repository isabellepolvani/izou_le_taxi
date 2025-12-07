import streamlit as st
import pandas as pd


#On configure la page
st.set_page_config(page_title="Site Web d'Izou", layout="centered")

#On configure les titres
st.title("Bienvenue chez Tax'Izou")
st.write("Les meilleurs taxis des States")

st.write("Indiquez votre arrondissement de récupération")

#On récupère les données
url="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv"
df_taxi=pd.read_csv(url)

#On crée une variable pour la liste de choix des arrondissements, en supprimant des données vides et en gardant des données uniques
choix_arrond=sorted(df_taxi["pickup_borough"].dropna().unique())

#On créé la liste déroulante avec une selectbox
mon_choix=st.selectbox("Liste des quartiers", choix_arrond)
st.write(f'Wow quel super quartier : {mon_choix}')

#On crée un dictionnaire d'images
im_bronx="https://upload.wikimedia.org/wikipedia/commons/e/e3/Bronx_Walk_of_Fame_1.jpg"
im_manhattan="https://upload.wikimedia.org/wikipedia/commons/a/ad/View_of_Manhattan_from_Circle_Line_Sightseeing_boat%2C_NYC%2C_20231001_1044_0909.jpg"
im_queens="https://upload.wikimedia.org/wikipedia/commons/d/dd/Long_Island_City_New_York_May_2015_panorama_3.jpg"
im_brook="https://upload.wikimedia.org/wikipedia/commons/f/f4/Dumbo_-_Brooklyn%2C_New_York_City.jpg"

image_ville={'Manhattan':im_manhattan,'Queens':im_queens,'Bronx':im_bronx, 'Brooklyn':im_brook}

st.image(image_ville[mon_choix], use_container_width=True)

