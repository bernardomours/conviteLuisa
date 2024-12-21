import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Convite Luísa",
    page_icon="🎀",
    )


# st.title("Aniversário da Luísa")

# invite, local, suggestion = st.tabs(["Convite", "Localização", "Sugestão de Presente"])
# with invite:
#     st.write("CONVITE")
    
# with local:
#     st.write("LOCAL")
    
# with suggestion:
#     st.write("SUGESTÃO DE PRESENTE")\



with st.container():
    selected = option_menu(
        menu_title= "CONTAMOS COM SUA PRESENÇA!",
        options=["Convite", "Local", "Sugestão de Presente"],
        icons=["envelope", "house", "gift"],    
        menu_icon="star",
        default_index=0,
        orientation="horizontal",  
    )

st.write(f"Você selecionou: {selected}, Bem-vind")

