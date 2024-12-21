import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Convite Luísa",
    page_icon="🎀",
)


with st.container():
    selected = option_menu(
        menu_title= "CONTAMOS COM SUA PRESENÇA!",
        options=["Convite", "Local", "Sugestão de Presente"],
        icons=["envelope", "house", "gift"],    
        menu_icon="star",
        default_index=0,
        orientation="horizontal",  
    )

if selected == "Convite":
    st.title("Você é nosso(a) convidado(a)!")
    st.write("**Estamos muito felizes em convidá-lo(a) para o aniversário de 1 ano da nossa Luísa!**")
    st.write("### Detalhes do evento:")
    st.write("- Data: 11 de janeiro de 2025")
    st.write("- Horário: 19h")
    
    
elif selected == "Local":
    st.title("Local do Evento")
    st.write("### Endereço:")
    st.write("Rua Antônio Alcivan Alves da Silva, 875, Bairro: Planalto Treze de Maio")

    maps = "https://www.google.com.br/maps/place/R.+Antonio+Alcivan+Alves+da+Silva,+875+-+Planalto+Treze+de+Maio,+Mossor%C3%B3+-+RN,+59631-485/@-5.2171053,-37.3402616,19.75z/data=!4m6!3m5!1s0x7ba064cab937977:0xeddae276e101c074!8m2!3d-5.2170159!4d-37.3402064!16s%2Fg%2F11jysc5qfp?entry=ttu&g_ep=EgoyMDI0MTIxMS4wIKXMDSoASAFQAw%3D%3D"
    st.markdown(
        f"[📍 Ver no Google Maps]({maps})")