import pickle
import streamlit as st

# Load the wine model
wine_model = pickle.load(open('wine_model.sav', 'rb'))

# Web Title
st.title('Data Mining Prediksi Class Wine')

col1, col2 = st.columns(2)

with col1:
    Alcohol = st.text_input('Input Nilai Alcohol')

with col2:
    Malic_Acid = st.text_input('Input Nilai Malic Acid')

with col1:
    Ash = st.text_input('Input Nilai Ash')

with col2:
    Alcalinity_of_Ash = st.text_input('Input Nilai Alcalinity of Ash')

with col1:
    Magnesium = st.text_input('Input Nilai Magnesium')

with col2:
    Total_Phenols = st.text_input('Input Nilai Total Phenols')

with col1:
    Flavanoids = st.text_input('Input Nilai Flavanoids')

with col2:
    Nonflavanoid_Phenols = st.text_input('Input Nilai Nonflavanoid Phenols')

with col1:
    Proanthocyanins = st.text_input('Input Nilai Proanthocyanins')

with col2:
    Color_Intensity = st.text_input('Input Nilai Color Intensity')

with col1:
    Hue = st.text_input('Input Nilai Hue')

with col2:
    Diluted_Wines = st.text_input('Input Nilai OD280/OD315 of Diluted Wines')

with col1:
    Proline = st.text_input('Input Nilai Proline')

# code untuk prediksi
class_hasil = ''

# membuat tombol prediksi
if st.button('Test Prediksi'):
    try:
        # Convert input values to float
        Alcohol = float(Alcohol)
        Malic_Acid = float(Malic_Acid)
        Ash = float(Ash)
        Alcalinity_of_Ash = float(Alcalinity_of_Ash)
        Magnesium = float(Magnesium)
        Total_Phenols = float(Total_Phenols)
        Flavanoids = float(Flavanoids)
        Nonflavanoid_Phenols = float(Nonflavanoid_Phenols)
        Proanthocyanins = float(Proanthocyanins)
        Color_Intensity = float(Color_Intensity)
        Hue = float(Hue)
        Diluted_Wines = float(Diluted_Wines)
        Proline = float(Proline)

        class_prediction = wine_model.predict([[Alcohol, Malic_Acid, Ash, Alcalinity_of_Ash, Magnesium, Total_Phenols, Flavanoids, Nonflavanoid_Phenols, Proanthocyanins, Color_Intensity, Hue, Diluted_Wines, Proline]])

        if class_prediction[0] == 1:
            class_hasil = "Class 1"
        elif class_prediction[0] == 2:
            class_hasil = "Class 2"
        elif class_prediction[0] == 3:
            class_hasil = "Class 3"
        else:
            class_hasil = "Class tidak ditemukan"

        st.success(class_hasil)  # Display the result as a success message
    except ValueError:
        st.error("Input values must be valid numbers.")
