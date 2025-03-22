import streamlit as st
import math
import base64
import time
import os

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
        max-width: 80%; /* Limiting width of text to fit the background */
        word-wrap: break-word; /* Breaking long words */
        margin: 10px auto; /* Adding margin to center the text */
        padding: 10px; /* Padding for better appearance */
    }}
    .stTextInput {{
        width: 75% !important;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

def type_writer_effect(text, delay=0.05):
    placeholder = st.empty()  # Reset the previous text
    displayed_text = ""
    for char in text:
        displayed_text += char
        placeholder.markdown(f"<p class='retro-text'>{displayed_text}</p>", unsafe_allow_html=True)
        time.sleep(delay)

def safe_float_input(prompt):
    user_input = st.text_input(prompt).strip()
    try:
        return float(user_input)
    except ValueError:
        st.error("Wpisz poprawną liczbę.")
        return None

def main():
    set_background("konsola.png")  # Ustawiamy tło z pliku "konsola.png"
    
    type_writer_effect("SYSTEM BOOTING...\n")
    time.sleep(1)
    type_writer_effect("WELCOME TO RETRO SKIRT CALCULATOR\n")
    time.sleep(1)
    
    # Pytanie o wybór spódnicy
    wybor = st.text_input("Jaką spódnicę chcesz uszyć? Wpisz numer (1 - Spódnica z koła, 2 - Spódnica z połowy koła, 3 - Spódnica z klinów):").strip()
    
    if wybor in ["1", "2", "3"]:
        type_writer_effect("Podaj obwód talii (cm): ")
        obwod_talii = safe_float_input("Talia:")
        
        if obwod_talii is None:
            return
        
        type_writer_effect("Podaj długość spódnicy (cm): ")
        dlugosc = safe_float_input("Długość:")
        
        if dlugosc is None:
            return
        
        # Spódnica z koła lub połowy koła
        if wybor in ["1", "2"]:
            podzial = 1 if wybor == "1" else 0.5
            promien_talii = oblicz_promien_talii(obwod_talii, podzial)
            promien_calosci = oblicz_promien_calosci(promien_talii, dlugosc)
            
            type_writer_effect(f"Promień talii: {promien_talii:.2f} cm\n")
            type_writer_effect(f"Promień spódnicy: {promien_calosci:.2f} cm\n")
        
        # Spódnica z klinów
        elif wybor == "3":
            type_writer_effect("Podaj obwód bioder (cm): ")
            obwod_bioder = safe_float_input("Biodra:")
            if obwod_bioder is None:
                return
            
            type_writer_effect("Podaj wzrost (cm): ")
            wzrost = safe_float_input("Wzrost:")
            if wzrost is None:
                return
            
            type_writer_effect("Podaj liczbę klinów: ")
            liczba_klinow = safe_float_input("Kliny:")
            if liczba_klinow is None:
                return
            
            szerokosc_talii_klina = obwod_talii / liczba_klinow
            szerokosc_bioder_klina = (obwod_bioder + 1) / liczba_klinow
            glebokosc_bioder = (wzrost / 10) + 4
            
            type_writer_effect(f"Szerokość klina w talii: {szerokosc_talii_klina:.2f} cm\n")
            type_writer_effect(f"Szerokość klina w biodrach: {szerokosc_bioder_klina:.2f} cm\n")
            type_writer_effect(f"Długość klina: {dlugosc:.2f} cm\n")
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
