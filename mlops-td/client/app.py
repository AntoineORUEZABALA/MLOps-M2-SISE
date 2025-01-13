import streamlit as st
import requests
import pandas as pd

st.title("Prédiction Iris")

button_list = st.button("Affichez la liste des prédictions")

if button_list:
    try:
        response = requests.get("http://server:8000/liste")
        if response.status_code == 200:
            liste_iris = response.json()
            if "predis" in liste_iris:
                df = pd.DataFrame(liste_iris["predis"])  
                st.write("Liste des prédictions :")
                st.dataframe(df) 
                st.image("https://media.tenor.com/Z_G7Z7t8i3sAAAAM/otter-excited-otter.gif")
            else:
                st.error("Format de réponse inattendu : clé 'predis' manquante.")
        else:
            st.error(f"Échec de la récupération de la liste des fleurs : {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"Une erreur est survenue lors de la récupération de la liste : {e}")

st.write("Entrez les caractéristiques de la fleur :")

sepal_length = st.number_input("Longueur du sépale", min_value=0.0, step=0.1)
sepal_width = st.number_input("Largeur du sépale", min_value=0.0, step=0.1)
petal_length = st.number_input("Longueur du pétale", min_value=0.0, step=0.1)
petal_width = st.number_input("Largeur du pétale", min_value=0.0, step=0.1)

if st.button("Prédire et Ajouter"):
    data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }

    response = requests.post("http://server:8000/add_fleur", json=data)

    if response.status_code == 200:
        result = response.json()
        predicted_class = result["data"]["prediction"]  
        st.success(f"Fleur ajoutée avec succès ! Classe prédite : {predicted_class}")
        st.json(response.json()["data"]) 
        st.image("https://64.media.tumblr.com/8c327c356720bcbdb2c0e55c2180efb6/tumblr_pegg6lRzNe1tg46ico1_500.gifv")
    else:
        st.error("Erreur lors de l'ajout de la fleur.")