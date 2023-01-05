import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn as sk




st.title("Estimation la prime d’assurance " )

st.header("Entrez les informations") 

age = st.number_input("l'âge du principal bénéficiaire",value=18)

children = st.number_input("le nombre d’enfant à charge",value=0)

# bmi = st.number_input("l’indice de masse corporel (bmi)",value=28.5)

weight = st.number_input("le poid(kg)",value=60)

height = st.number_input("la taille(metre)",value=1.75)

bmi = weight/(height ** 2)

sex = st.radio("le sexe  ", ('female', 'male'), ) 

smoker = st.radio("fumeur ou non-fumeur ", ('yes', 'no'), )

region = st.radio("le zone résidentielle", ('southwest', 'southeast', 'northwest', 'northeast'), )


pickle_in = open('my_pipe_ridge.pkl', 'rb') 

my_pipe_ridge = pickle.load(pickle_in) 


donnee =np.array([[age, sex, bmi, children, smoker, region]])
df_X=pd.DataFrame(donnee,columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])

if(st.button('Calculate')): 
    prediction = my_pipe_ridge.predict(df_X)
    if prediction >= 1121:
        st.text(f"la prime d’assurance est estime à {int(prediction)}$")
    else:
        st.text(f"la prime d’assurance est estime à 1121 $")





