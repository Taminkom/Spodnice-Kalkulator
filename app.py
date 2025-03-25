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
        font-size: 18px;
        white-space: pre-line;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

def type_writer_effect(text, delay=0.02):
    """Efekt maszyny do pisania"""
    placeholder = st.empty()
    full_text = ""
    for char in text:
        full_text += char
        placeholder.markdown(f"<p class='retro-text'>{full_text}</p>", unsafe_allow_html=True)
        time.sleep(delay)

def safe_float_input(label):
    """Funkcja pobierająca liczbę z obsługą błędów"""
    value = st.text_input(label).strip()
    if value:
        try:
            return float(value)
        except ValueError:
            st.error("Wpisz poprawną liczbę.")
            return None
    return None

def reset_state():
    """Resetuje cały stan aplikacji"""
    for key in st.session_state.keys():
        del st.session_state[key]
    st.experimental_rerun()

def main():
    set_background("konsola.png")

    # Inicjalizacja sesji
    for key in ["wybor", "obwod_talii", "dlugosc", "obwod_bioder", "wzrost", "liczba_klinow"]:
        if key not in st.session_state:
            st.session_state[key] = None

    type_writer_effect("SYSTEM BOOTING...\n")
    time.sleep(1)

    # Krok 1: Wybór spódnicy
    if st.session_state.wybor is None:
        type_writer_effect("Jaką spódnicę chcesz uszyć?\n1. Spódnica z koła\n2. Spódnica z połowy koła\n3. Spódnica z klinów\n")
        wybor = st.text_input("Wybierz rodzaj spódnicy:").strip()
        if wybor in ["1", "2", "3"]:
            st.session_state.wybor = wybor

    # Krok 2: Obwód talii
    if st.session_state.wybor and st.session_state.obwod_talii is None:
        st.session_state.obwod_talii = safe_float_input("Podaj obwód talii (cm):")

    # Krok 3: Długość spódnicy
    if st.session_state.obwod_talii and st.session_state.dlugosc is None:
        st.session_state.dlugosc = safe_float_input("Podaj długość spódnicy (cm):")

    # Krok 4: Obwód bioder (tylko dla spódnicy z klinów)
    if st.session_state.dlugosc and st.session_state.wybor == "3" and st.session_state.obwod_bioder is None:
        st.session_state.obwod_bioder = safe_float_input("Podaj obwód bioder (cm):")

    # Krok 5: Wzrost (tylko dla spódnicy z klinów)
    if st.session_state.obwod_bioder and st.session_state.wzrost is None:
        st.session_state.wzrost = safe_float_input("Podaj wzrost (cm):")

    # Krok 6: Liczba klinów (tylko dla spódnicy z klinów)
    if st.session_state.wzrost and st.session_state.liczba_klinow is None:
        st.session_state.liczba_klinow = safe_float_input("Podaj liczbę klinów:")

    # Krok 7: Obliczenia i wyświetlenie wyników
    if st.session_state.dlugosc and (st.session_state.wybor in ["1", "2"] or (st.session_state.wybor == "3" and st.session_state.liczba_klinow)):
        type_writer_effect("\nObliczanie...\n")
        time.sleep(1)

        st.subheader("📏 Wyniki obliczeń:")
        if st.session_state.wybor in ["1", "2"]:
            podzial = 1 if st.session_state.wybor == "1" else 0.5
            promien_talii = oblicz_promien_talii(st.session_state.obwod_talii, podzial)
            promien_calosci = oblicz_promien_calosci(promien_talii, st.session_state.dlugosc)

            st.write(f"✅ **Promień talii:** {promien_talii:.2f} cm")
            st.write(f"✅ **Promień spódnicy:** {promien_calosci:.2f} cm")

        elif st.session_state.wybor == "3":
            szerokosc_talii_klina = st.session_state.obwod_talii / st.session_state.liczba_klinow
            szerokosc_bioder_klina = (st.session_state.obwod_bioder + 1) / st.session_state.liczba_klinow
            glebokosc_bioder = (st.session_state.wzrost / 10) + 4

            st.write(f"✅ **Szerokość klina w talii:** {szerokosc_talii_klina:.2f} cm")
            st.write(f"✅ **Szerokość klina w biodrach:** {szerokosc_bioder_klina:.2f} cm")
            st.write(f"✅ **Długość klina:** {st.session_state.dlugosc:.2f} cm")
            st.write(f"✅ **Głębokość bioder:** {glebokosc_bioder:.2f} cm")

        st.markdown("<span style='color:red; font-weight:bold;'>❗ Pamiętaj, aby dodać zapasy na szwy! ❗</span>", unsafe_allow_html=True)

        if st.button("🔄 Oblicz inną spódnicę"):
            reset_state()

if __name__ == "__main__":
    main()
