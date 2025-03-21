import streamlit as st
import math
import base64
import time

def oblicz_promien_talii(obwod_talii, podzial):
    return (obwod_talii + 0.5) / (2 * math.pi * podzial)

def oblicz_promien_calosci(promien_talii, dlugosc):
    return promien_talii + dlugosc

def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded_string = base64.b64encode(image.read()).decode()
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
    }}
    .retro-text {{
        font-family: "Courier New", Courier, monospace;
        color: #00FF00;
        white-space: pre-line;
        font-size: 18px;
        position: absolute;
        top: 25%;
        left: 20%;
        width: 60%;
        height: 50%;
        overflow: hidden;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

def type_writer_effect(text):
    placeholder = st.empty()
    displayed_text = ""
    for char in text:
        displayed_text += char
        placeholder.markdown(f"<p class='retro-text'>{displayed_text}</p>", unsafe_allow_html=True)
        time.sleep(0.05)

def main():
    set_background("konsola.png")
    
    type_writer_effect("Kalkulator Spódnic - Retro Styl\n")
    type_writer_effect("Wybierz rodzaj spódnicy i podaj swoje wymiary, a my obliczymy potrzebne wartości!\n")
    
    wybor = st.selectbox("Wybierz rodzaj spódnicy:", ["Spódnica z pełnego koła", "Spódnica z połowy koła", "Spódnica z klinów"])
    
    if wybor:
        obwod_talii = st.text_input("Podaj obwód talii (cm):")
        dlugosc = st.text_input("Podaj długość spódnicy (cm):")
        
        obwod_bioder = None
        wzrost = None
        liczba_klinow = None
        
        if wybor == "Spódnica z klinów":
            obwod_bioder = st.text_input("Podaj obwód bioder (cm):")
            wzrost = st.text_input("Podaj swój wzrost (cm):")
            liczba_klinow = st.text_input("Podaj liczbę klinów:")
        
        if st.button("Oblicz!"):
            type_writer_effect("\nDla podanych wymiarów wyniki są następujące:\n")
            
            if wybor in ["Spódnica z pełnego koła", "Spódnica z połowy koła"]:
                podzial = 1 if wybor == "Spódnica z pełnego koła" else 0.5
                promien_talii = oblicz_promien_talii(float(obwod_talii), podzial)
                promien_calosci = oblicz_promien_calosci(promien_talii, float(dlugosc))
                
                type_writer_effect(f"Promień otworu na talię: {promien_talii:.2f} cm")
                type_writer_effect(f"Promień całej spódnicy: {promien_calosci:.2f} cm")
                
            elif wybor == "Spódnica z klinów" and liczba_klinow:
                szerokosc_talii_klina = float(obwod_talii) / int(liczba_klinow)
                szerokosc_bioder_klina = (float(obwod_bioder) + 1) / int(liczba_klinow)
                glebokosc_bioder = (float(wzrost) / 10) + 4
                
                type_writer_effect(f"Szerokość klina w talii: {szerokosc_talii_klina:.2f} cm")
                type_writer_effect(f"Szerokość klina w biodrach: {szerokosc_bioder_klina:.2f} cm")
                type_writer_effect(f"Długość klinów: {float(dlugosc):.2f} cm")
                type_writer_effect(f"Głębokość bioder: {glebokosc_bioder:.2f} cm")
            
            st.markdown(
                """
                <span style='color:red; font-weight:bold;'>❗ Pamiętaj o dodaniu zapasów na szwy i podwinięcia! ❗</span>
                """,
                unsafe_allow_html=True
            )
            
            if st.button("Oblicz kolejną spódnicę"):
                st.experimental_rerun()

if __name__ == "__main__":
    main()
