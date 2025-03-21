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
        left: 28%;
        width: 45%;
        height: 40%;
        overflow: hidden;
        text-align: left;
        background-color: black;
        padding: 10px;
        border-radius: 5px;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

def type_writer_effect(text, delay=0.05):
    placeholder = st.empty()
    displayed_text = ""
    for char in text:
        displayed_text += char
        placeholder.markdown(f"<p class='retro-text'>{displayed_text}</p>", unsafe_allow_html=True)
        time.sleep(delay)

def main():
    set_background("konsola.png")
    
    type_writer_effect("SYSTEM BOOTING...\n")
    time.sleep(1)
    type_writer_effect("WELCOME TO RETRO SKIRT CALCULATOR\n")
    time.sleep(1)
    
    type_writer_effect("Jaką spódnicę chcesz uszyć?\n1. Spódnica z koła\n2. Spódnica z połowy koła\n3. Spódnica z klinów\n")
    wybor = st.text_input("Wpisz numer spódnicy (1, 2, 3):").strip()
    
    if wybor in ["1", "2", "3"]:
        type_writer_effect("Podaj obwód talii (cm): ")
        obwod_talii = st.text_input("Obwód talii:")
        type_writer_effect("Podaj długość spódnicy (cm): ")
        dlugosc = st.text_input("Długość spódnicy:")
        
        if wybor == "3":
            type_writer_effect("Podaj obwód bioder (cm): ")
            obwod_bioder = st.text_input("Obwód bioder:")
            type_writer_effect("Podaj wzrost (cm): ")
            wzrost = st.text_input("Wzrost:")
            type_writer_effect("Podaj liczbę klinów: ")
            liczba_klinow = st.text_input("Liczba klinów:")
        
        if st.button("Oblicz"):
            type_writer_effect("\nObliczanie...\n")
            time.sleep(1)
            type_writer_effect("\nWyniki:\n")
            
            if wybor in ["1", "2"]:
                podzial = 1 if wybor == "1" else 0.5
                promien_talii = oblicz_promien_talii(float(obwod_talii), podzial)
                promien_calosci = oblicz_promien_calosci(promien_talii, float(dlugosc))
                
                type_writer_effect(f"Promień talii: {promien_talii:.2f} cm\n")
                type_writer_effect(f"Promień spódnicy: {promien_calosci:.2f} cm\n")
                
            elif wybor == "3" and liczba_klinow:
                szerokosc_talii_klina = float(obwod_talii) / int(liczba_klinow)
                szerokosc_bioder_klina = (float(obwod_bioder) + 1) / int(liczba_klinow)
                glebokosc_bioder = (float(wzrost) / 10) + 4
                
                type_writer_effect(f"Szerokość klina w talii: {szerokosc_talii_klina:.2f} cm\n")
                type_writer_effect(f"Szerokość klina w biodrach: {szerokosc_bioder_klina:.2f} cm\n")
                type_writer_effect(f"Długość klina: {float(dlugosc):.2f} cm\n")
                type_writer_effect(f"Głębokość bioder: {glebokosc_bioder:.2f} cm\n")
            
            st.markdown(
                """
                <span style='color:red; font-weight:bold;'>❗ Pamiętaj, aby dodać zapasy na szwy! ❗</span>
                """,
                unsafe_allow_html=True
            )
            
            if st.button("Oblicz inną spódnicę"):
                st.experimental_rerun()

if __name__ == "__main__":
    main()
