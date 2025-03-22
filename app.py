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
    
    # Initialize session state variables if not already done
    if 'wybor' not in st.session_state:
        st.session_state.wybor = None
    if 'obwod_talii' not in st.session_state:
        st.session_state.obwod_talii = None
    if 'dlugosc' not in st.session_state:
        st.session_state.dlugosc = None
    if 'obwod_bioder' not in st.session_state:
        st.session_state.obwod_bioder = None
    if 'wzrost' not in st.session_state:
        st.session_state.wzrost = None
    if 'liczba_klinow' not in st.session_state:
        st.session_state.liczba_klinow = None

    type_writer_effect("SYSTEM BOOTING...\n")
    time.sleep(1)

    # Step 1: Choose skirt type
    if st.session_state.wybor is None:
        type_writer_effect("Jaką spódnicę chcesz uszyć?\n1. Spódnica z koła\n2. Spódnica z połowy koła\n3. Spódnica z klinów\n")
        wybor = st.text_input("Wybierz rodzaj spódnicy:").strip()
        if wybor in ["1", "2", "3"]:
            st.session_state.wybor = wybor  # Save user's choice

    # Step 2: Ask for waist circumference
    if st.session_state.wybor is not None and st.session_state.obwod_talii is None:
        type_writer_effect("Podaj obwód talii (cm): ")
        obwod_talii = safe_float_input("Talia:")
        if obwod_talii is not None:
            st.session_state.obwod_talii = obwod_talii  # Save user's input

    # Step 3: Ask for skirt length
    if st.session_state.obwod_talii is not None and st.session_state.dlugosc is None:
        type_writer_effect("Podaj długość spódnicy (cm): ")
        dlugosc = safe_float_input("Długość:")
        if dlugosc is not None:
            st.session_state.dlugosc = dlugosc  # Save user's input

    # Step 4: Ask for hip circumference (for skirt with wedges)
    if st.session_state.dlugosc is not None and st.session_state.wybor == "3" and st.session_state.obwod_bioder is None:
        type_writer_effect("Podaj obwód bioder (cm): ")
        obwod_bioder = safe_float_input("Biodra:")
        if obwod_bioder is not None:
            st.session_state.obwod_bioder = obwod_bioder  # Save user's input

    # Step 5: Ask for height (for skirt with wedges)
    if st.session_state.obwod_bioder is not None and st.session_state.wzrost is None:
        type_writer_effect("Podaj wzrost (cm): ")
        wzrost = safe_float_input("Wzrost:")
        if wzrost is not None:
            st.session_state.wzrost = wzrost  # Save user's input

    # Step 6: Ask for number of wedges (for skirt with wedges)
    if st.session_state.wzrost is not None and st.session_state.liczba_klinow is None:
        type_writer_effect("Podaj liczbę klinów: ")
        liczba_klinow = safe_float_input("Kliny:")
        if liczba_klinow is not None:
            st.session_state.liczba_klinow = liczba_klinow  # Save user's input

    # Step 7: Calculation and output results
    if (st.session_state.dlugosc is not None and 
        (st.session_state.wybor in ["1", "2"] or (st.session_state.wybor == "3" and st.session_state.liczba_klinow is not None))):
        
        type_writer_effect("\nObliczanie...\n")
        time.sleep(1)
        type_writer_effect("\nWyniki:\n")

        if st.session_state.wybor in ["1", "2"]:
            podzial = 1 if st.session_state.wybor == "1" else 0.5
            promien_talii = oblicz_promien_talii(st.session_state.obwod_talii, podzial)
            promien_calosci = oblicz_promien_calosci(promien_talii, st.session_state.dlugosc)

            type_writer_effect(f"Promień talii: {promien_talii:.2f} cm\n")
            type_writer_effect(f"Promień spódnicy: {promien_calosci:.2f} cm\n")

        elif st.session_state.wybor == "3":
            szerokosc_talii_klina = st.session_state.obwod_talii / st.session_state.liczba_klinow
            szerokosc_bioder_klina = (st.session_state.obwod_bioder + 1) / st.session_state.liczba_klinow
            glebokosc_bioder = (st.session_state.wzrost / 10) + 4

            type_writer_effect(f"Szerokość klina w talii: {szerokosc_talii_klina:.2f} cm\n")
            type_writer_effect(f"Szerokość klina w biodrach: {szerokosc_bioder_klina:.2f} cm\n")
            type_writer_effect(f"Długość klina: {st.session_state.dlugosc:.2f} cm\n")
            type_writer_effect(f"Głębokość bioder: {glebokosc_bioder:.2f} cm\n")

        st.markdown(
            """
            <span style='color:red; font-weight:bold;'>❗ Pamiętaj, aby dodać zapasy na szwy! ❗</span>
            """,
            unsafe_allow_html=True
        )

        if st.button("Oblicz inną spódnicę"):
            # Reset session state to start over
            st.session_state.wybor = None
            st.session_state.obwod_talii = None
            st.session_state.dlugosc = None
            st.session_state.obwod_bioder = None
            st.session_state.wzrost = None
            st.session_state.liczba_klinow = None
            st.experimental_rerun()

if __name__ == "__main__":
    main()
