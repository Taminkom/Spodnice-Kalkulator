import streamlit as st
import math
import base64
import time

def oblicz_promien_talii(obwod_talii, podzial):
    return (obwod_talii + 0.5) / (2 * math.pi * podzial)

def oblicz_promien_calosci(promien_talii, dlugosc):
    return promien_talii + dlugosc

def set_background(image_file):
    try:
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
            max-width: 90%; /* Limiting width of text */
            word-wrap: break-word; /* Breaking long words */
        }}
        .stTextInput {{
            width: 75% !important;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("Plik tła nie został znaleziony.")

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
    set_background("konsola.png")
    
    type_writer_effect("SYSTEM BOOTING...\n")
    time.sleep(1)
    type_writer_effect("WELCOME TO RETRO SKIRT CALCULATOR\n")
    time.sleep(1)
    
    type_writer_effect("Jaką spódnicę chcesz uszyć?\n1. Spódnica z koła\n2. Spódnica z połowy koła\n3. Spódnica z klinów\n")
    wybor = st.radio("Wybierz rodzaj spódnicy:", ["Spódnica z koła", "Spódnica z połowy koła", "Spódnica z klinów"])
    
    obwod_talii = safe_float_input("Podaj obwód talii (cm):")
    if obwod_talii is None:
        return
    
    dlugosc = safe_float_input("Podaj długość spódnicy (cm):")
    if dlugosc is None:
        return
    
    if wybor == "Spódnica z koła" or wybor == "Spódnica z połowy koła":
        podzial = 1 if wybor == "Spódnica z koła" else 0.5
        promien_talii = oblicz_promien_talii(obwod_talii, podzial)
        promien_calosci = oblicz_promien_calosci(promien_talii, dlugosc)
        
        type_writer_effect(f"Promień talii: {promien_talii:.2f} cm\n")
        type_writer_effect(f"Promień spódnicy: {promien_calosci:.2f} cm\n")
        
    elif wybor == "Spódnica z klinów":
        obwod_bioder = safe_float_input("Podaj obwód bioder (cm):")
        if obwod_bioder is None:
            return
        
        wzrost = safe_float_input("Podaj wzrost (cm):")
        if wzrost is None:
            return
        
        liczba_klinow = safe_float_input("Podaj liczbę klinów:")        
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
