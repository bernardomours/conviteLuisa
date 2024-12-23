import streamlit as st
import base64
import os

st.set_page_config(
    page_title="1 Aninho da Luísa",
    page_icon="🎀",
    layout="wide",
    initial_sidebar_state='collapsed'
)

# CSS para estilizar o documento
st.markdown(
    """
    <style>
        .stMainBlockContainer {
            border: 0px;
            padding-top: 0px;
            padding-bottom: 20px; 
            padding-left: 20px;
            padding-right: 20px; 
        }
        .stVerticalBlock {
            border : 0px;
        }
        .stAppHeader {
            visibility: hidden;
            background-color: #ffffff;
            padding: 0px;
        }
        #MainMenu {
            visibility: hidden;
        }

        .stHorizontalBlock {
            background-color: #ffffff;
            padding: 0.1rem;
        }
        .container-content {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .stHeaderActionElements {
            visibility: hidden;
        }
        .stColumn {
            border: 0px;
            padding-top: 0px;
            padding-bottom: 20px; 
            padding-left: 20px;
            padding-right: 20px; 
        }
        .stMarkdownContainer {
            border: 0px;
            padding-top: 0px;
            padding-bottom: 20px; 
            padding-left: 20px;
            padding-right: 20px;             
        }
        .block-container { 
            padding-top: 0px;
            padding-left: 0rem;
            padding-right: 0rem; 
        }
        .container1 {
            background-color: #ffffff;
            border: 0px;
        }
        .container2 {
            background-color: #f09db1;
            padding-top: 20px;
            padding-bottom: 40px; 
            padding-left: 40px;
            padding-right: 40px; 
        }
        .container3 {
            background-color: #ffffff;
            padding-top: 20px;
            padding-bottom: 0px; 
            padding-left: 40px;
            padding-right: 20px; 
        }
        .container4 {
            background-color: #ffffff;
            padding-top: 20px;
            padding-bottom: 0px; 
            padding-left: 20px;
            padding-right: 20px; 
        }
    </style>
    """,
    unsafe_allow_html=True,
)

## CONVITE
with st.container():
    st.markdown(
        """
        <div class="container1">
        <div 
            style="position: 
            relative; 
            width: 100%; 
            height: 0; 
            border: 0px;
            padding-top: 36.7188%;
            padding-bottom: 0; 
            overflow: hidden;">
            <iframe 
                loading="lazy" 
                style="position: 
                    absolute; 
                    width: 100%; 
                    height: 100%; 
                    top: 0; 
                    left: 0; 
                    border: none; 
                    padding: 0;
                    margin: 0;"
                src="https://www.canva.com/design/DAGaE0fB8mw/FgxiT58lNN_e74-SBD0Bmg/view?embed" >
            </iframe>
            </div>
        """, 
        unsafe_allow_html=True
    )

## LOCALIZAÇÃO
with st.container():
    st.markdown(        
        """
        <div class="container2">
            <h3 style=\"color: #ffffff; font-size: 30px\">
                LOCALIZAÇÃO
            </h3>
            <p></p>
            <iframe 
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1986.7914538145997!2d-37.35306239001534!3d-5.170590171969311!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x7ba0703d0ed4ef3%3A0x145466ba02ac977c!2sMagic%20fest%20buffet!5e0!3m2!1spt-BR!2sbr!4v1734888634958!5m2!1spt-BR!2sbr" 
                width="100%" 
                height="400" 
                style="border:0;" 
                allowfullscreen="" 
                loading="lazy" 
                referrerpolicy="no-referrer-when-downgrade">
            </iframe>
        </div>
        """, 
        unsafe_allow_html=True
    )

## PRESENTES
with st.container():
    st.markdown(
        """
        <div class="container3">
            <h3 style=\"color: #f09db1; font-size: 30px\">
                SUGESTÃO DE PRESENTE
            </h3>
        </div>
        """, 
        unsafe_allow_html=True
    )

    colShoes, colClothes, colToys = st.columns(3, gap='small', vertical_alignment='center', border=True)
    
    ## PRESENTE 1
    with colShoes:
        shoesFile = open("images/shoes.gif", "rb")
        shoesContent = shoesFile.read()
        shoesImg = base64.b64encode(shoesContent).decode("utf-8")
        shoesFile.close()
        st.markdown(
            """
            <style>
                img {
                    border-radius: 15px;
                }
            </style>
            """, unsafe_allow_html=True
        )
        st.markdown(
            f'<img src="data:image/gif;base64,{shoesImg}">',
            unsafe_allow_html=True,
        )

    ## PRESENTE 2
    with colClothes:
        cloFile = open("images/clothes.gif", "rb")
        cloContent = cloFile.read()
        cloImg = base64.b64encode(cloContent).decode("utf-8")
        cloFile.close()
        st.markdown(
            """
            <style>
                img {
                    border-radius: 15px;
                }
            </style>
            """, unsafe_allow_html=True
        )
        st.markdown(
            f'<img src="data:image/gif;base64,{cloImg}">',
            unsafe_allow_html=True,
        )   

    ## PRESENTE 3
    with colToys:
        toyFile = open("images/toys.gif", "rb")
        toyContent = toyFile.read()
        toyImg = base64.b64encode(toyContent).decode("utf-8")
        toyFile.close()
        st.markdown(
            """
            <style>
                img {
                    border-radius: 15px;
                }
            </style>
            """, unsafe_allow_html=True
        )
        st.markdown(
            f'<img src="data:image/gif;base64,{toyImg}">',
            unsafe_allow_html=True,
        )
    
with st.container():
    col1, col3 = st.columns(2, vertical_alignment='center', border=True)
    with col1:
        st.markdown(
            """
            <div class="container4">
                <b><h3 style=\"color: #f09db1; font-size: 30px\">
                    INFORMAÇÕES GERAIS
                </h3></b>
                <h6>DATA</h6>
                    <p>Sábado, 11 de Janeiro de 2024</p>
                <h6>HORÁRIO</h6>
                    <p \"padding: 0px;\">Início às 18h00 e encerramento às 22h00</p>
                <h6>ENDEREÇO</h6>
                    <p>Magic fest Buffet, R. Antônio Cirilino, 62 - Abolição, Mossoró - RN, 59619-630</p>
                <br>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown(
            """
            <div class="container4">
                <h3></h3>
                <h6>CONTATO DOS PAPAIS</h6>
                <p>(84) 9 8629-8159 - Roxanna
                <br>(84) 9 8629-7626 - Lucas</p>
            </div>
            <br><br><br><br><br><br>
            """, 
            unsafe_allow_html=True
        )
    