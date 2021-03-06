# źródło danych [https://www.kaggle.com/c/titanic/](https://www.kaggle.com/c/titanic)

import streamlit as st
import pickle
from datetime import datetime
startTime = datetime.now()
# import znanych nam bibliotek

filename = "model.sv"
model = pickle.load(open(filename,'rb'))
# otwieramy wcześniej wytrenowany model

pclass_d = {0:"Pierwsza",1:"Druga", 2:"Trzecia"}
embarked_d = {0:"Cherbourg", 1:"Queenstown", 2:"Southampton"}
# o ile wcześniej kodowaliśmy nasze zmienne, to teraz wprowadzamy etykiety z ich nazewnictwem
sex_d = {0:"Kobieta", 1:"Mezczyzna"}

def main():

	st.set_page_config(page_title="Zajecia5")
	overview = st.container()
	left, right = st.columns(2)
	prediction = st.container()

	st.image("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/sunset-quotes-21-1586531574.jpg?crop=1.00xw:0.752xh;0,0.0601xh&resize=768:*")

	with overview:
		st.title("Zajecia5 - s20479")

	with left:
		sex_radio = st.radio( "Płeć", list(sex_d.keys()), format_func=lambda x : sex_d[x] )
		embarked_radio = st.radio( "Port zaokrętowania", list(embarked_d.keys()), index=2, format_func= lambda x: embarked_d[x] )
		pclass_radio = st.radio("Klasa", list(pclass_d.keys()), format_func=lambda x : pclass_d[x])

	with right:
		age_slider = st.slider("Wiek", value=1.0, min_value=0.42, max_value=80.0, step=1.0)
		sibsp_slider = st.slider("Liczba rodzeństwa i/lub partnera", min_value=0, max_value=8)
		parch_slider = st.slider("Liczba rodziców i/lub dzieci", min_value=0, max_value=6)
		fare_slider = st.slider("Cena biletu", min_value=0.0, max_value=512.3292, step=1.0)

	data = [[pclass_radio, sex_radio,  age_slider, sibsp_slider, parch_slider, fare_slider, embarked_radio]]
	survival = model.predict(data)
	s_confidence = model.predict_proba(data)

	with prediction:
		st.subheader("Czy taka osoba przeżyłaby katastrofę?")
		st.subheader(("Tak" if survival[0] == 1 else "Nie"))
		st.write("Pewność predykcji {0:.2f} %".format(s_confidence[0][survival][0] * 100))

if __name__ == "__main__":
    main()
