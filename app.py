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
        top: 20%;
        left: 23%;
        width: 54%;
        height: 50%;
        overflow: hidden;
        text-align: left;
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
    
    type_writer_effect("SYSTEM BOOTING...\n")
    time.sleep(1)
    type_writer_effect("WELCOME TO RETRO SKIRT CALCULATOR\n")
    time.sleep(1)
    
    type_writer_effect("Select skirt type:\n- Full Circle\n- Half Circle\n- Panel Skirt\n")
    wybor = st.text_input("Enter your choice:").strip().lower()
    
    if wybor in ["full circle", "half circle", "panel skirt"]:
        type_writer_effect("Enter your waist circumference (cm): ")
        obwod_talii = st.text_input("Waist circumference:")
        type_writer_effect("Enter skirt length (cm): ")
        dlugosc = st.text_input("Skirt length:")
        
        if wybor == "panel skirt":
            type_writer_effect("Enter your hip circumference (cm): ")
            obwod_bioder = st.text_input("Hip circumference:")
            type_writer_effect("Enter your height (cm): ")
            wzrost = st.text_input("Height:")
            type_writer_effect("Enter number of panels: ")
            liczba_klinow = st.text_input("Number of panels:")
        
        if st.button("Calculate"):
            type_writer_effect("\nCalculating...\n")
            time.sleep(1)
            type_writer_effect("\nResults:\n")
            
            if wybor in ["full circle", "half circle"]:
                podzial = 1 if wybor == "full circle" else 0.5
                promien_talii = oblicz_promien_talii(float(obwod_talii), podzial)
                promien_calosci = oblicz_promien_calosci(promien_talii, float(dlugosc))
                
                type_writer_effect(f"Waist radius: {promien_talii:.2f} cm\n")
                type_writer_effect(f"Skirt radius: {promien_calosci:.2f} cm\n")
                
            elif wybor == "panel skirt" and liczba_klinow:
                szerokosc_talii_klina = float(obwod_talii) / int(liczba_klinow)
                szerokosc_bioder_klina = (float(obwod_bioder) + 1) / int(liczba_klinow)
                glebokosc_bioder = (float(wzrost) / 10) + 4
                
                type_writer_effect(f"Panel width at waist: {szerokosc_talii_klina:.2f} cm\n")
                type_writer_effect(f"Panel width at hips: {szerokosc_bioder_klina:.2f} cm\n")
                type_writer_effect(f"Panel length: {float(dlugosc):.2f} cm\n")
                type_writer_effect(f"Hip depth: {glebokosc_bioder:.2f} cm\n")
            
            st.markdown(
                """
                <span style='color:red; font-weight:bold;'>❗ Remember to add seam allowances! ❗</span>
                """,
                unsafe_allow_html=True
            )
            
            if st.button("Calculate another skirt"):
                st.experimental_rerun()

if __name__ == "__main__":
    main()
