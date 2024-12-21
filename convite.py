import streamlit as st

st.set_page_config(
    page_title="Convite Luísa",
    page_icon="🎀",
    )


st.title("Aniversário da Luísa")

invite, local, suggestion = st.tabs(["Convite", "Localização", "Sugestão de Presente"])


with invite:
    st.write("CONVITE")
    
with local:
    st.write("LOCAL")
    
with suggestion:
    st.write("SUGESTÃO DE PRESENTE")