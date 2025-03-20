import streamlit as st
import math

def oblicz_promien_talii(obwod_talii, podzial):
    return (obwod_talii + 0.5) / (2 * math.pi * podzial)

def oblicz_promien_calosci(promien_talii, dlugosc):
    return promien_talii + dlugosc

def main():
    st.title("Kalkulator Spódnic")
    st.write("Wybierz rodzaj spódnicy i podaj swoje wymiary, a my obliczymy potrzebne wartości!")
    
    wybor = st.radio("Wybierz rodzaj spódnicy:", ["Spódnica z pełnego koła", "Spódnica z połowy koła", "Spódnica z klinów"])
    
    obwod_talii = st.number_input("Podaj obwód talii (cm):", min_value=1.0, step=0.1)
    dlugosc = st.number_input("Podaj długość spódnicy (cm):", min_value=1.0, step=0.1)
    
    obwod_bioder = None
    wzrost = None
    liczba_klinow = None
    
    if wybor == "Spódnica z klinów":
        obwod_bioder = st.number_input("Podaj obwód bioder (cm):", min_value=1.0, step=0.1)
        wzrost = st.number_input("Podaj swój wzrost (cm):", min_value=1.0, step=0.1)
        liczba_klinow = st.number_input("Podaj liczbę klinów:", min_value=2, step=1)
    
    if st.button("Oblicz!"):
        st.subheader("Dla podanych wymiarów wyniki są następujące:")
        
        if wybor in ["Spódnica z pełnego koła", "Spódnica z połowy koła"]:
            podzial = 1 if wybor == "Spódnica z pełnego koła" else 0.5
            promien_talii = oblicz_promien_talii(obwod_talii, podzial)
            promien_calosci = oblicz_promien_calosci(promien_talii, dlugosc)
            
            st.write(f"**Promień otworu na talię:** {promien_talii:.2f} cm **(dodano 0,5 cm luzu w talii)**")
            st.write(f"**Promień całej spódnicy:** {promien_calosci:.2f} cm")
        
        elif wybor == "Spódnica z klinów" and liczba_klinow:
            szerokosc_talii_klina = obwod_talii / liczba_klinow
            szerokosc_bioder_klina = (obwod_bioder + 1) / liczba_klinow
            glebokosc_bioder = (wzrost / 10) + 4
            
            st.write(f"**Każdy klin powinien mieć szerokość w talii:** {szerokosc_talii_klina:.2f} cm")
            st.write(f"**Każdy klin powinien mieć szerokość w biodrach:** {szerokosc_bioder_klina:.2f} cm **(dodano 1 cm luzu w biodrach)**")
            st.write(f"**Długość klinów:** {dlugosc:.2f} cm")
            st.write(f"**Głębokość bioder:** {glebokosc_bioder:.2f} cm")
        
        st.markdown("""<span style='color:red; font-weight:bold;'>Pamiętaj o dodaniu zapasów na szwy i podwinięcia! ❤</span>""", unsafe_allow_html=True)
        
        if st.button("Oblicz kolejną spódnicę"):
            st.experimental_rerun()

if __name__ == "__main__":
    main()
