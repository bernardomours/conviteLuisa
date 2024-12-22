import streamlit as st


st.set_page_config(
    page_title="1 Aninho da Luísa",
    page_icon="🎀",
    layout="wide",
)

# CSS para estilizar o documento
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        .block-container { 
            padding-top: 3rem;
            padding-left: 0.001rem;
            padding-right: 0.0001rem; 
        }
        .container1 {
            background-color: #FFFFFF;
            padding: 20px;
        }
        .container2 {
            background-color: #f09db1;
            padding: 20px;
        }
        .container3 {
            background-color: #FFFFFF;
            padding: 20px;
        }
        .container-content {
            margin: 0;
    </style>
    """,
    unsafe_allow_html=True,
)

## convite
with st.container():
    st.markdown(
        """
        <div class="container1">
            <h3 lass=\"container-content\" style=\"color: #f09db1;\">
                CONVITE
            </h3>
            <img 
                src="background.jpg" 
                width="100%" 
                height=300px>
            </img>
        </div>
        """, 
        unsafe_allow_html=True
    )

## presentes
with st.container():
    st.markdown(
        """
        <style>
            .stHorizontalBlock {background-color: #f09db1;}
        </style>
        <div class="container2" style="background-color: #f09db1; padding: 20px;">
            <h3 class=\"container-content\" style=\"color: white;\">
                SUGESTÃO DE PRESENTE
            </h3>
        </div>
        """, 
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3, gap='small', vertical_alignment='center', border=True)

    with col1:
        st.markdown(
            """
            <div style="background-color: #f09db1; padding: 10px;">
                <h4 class=\"container-content\" style=\"color: white;\">
                    Sapatinhos tamanho 12
                </h4>
                <img 
                src="https://down-br.img.susercontent.com/file/br-11134201-23030-mzaeus8qmdov35" 
                width="100%" 
                height="100%">
                </img>
            </div>
            """, 
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style="background-color: #f09db1; padding: 10px;">
                <h4 lass=\"container-content\" style=\"color: white;\">
                    Roupinhas tamanho 18 meses
                </h4>
                <img 
                src="https://img.bestdealplus.com/ae04/kf/Hffe397335f1647d7ad58d2d775e7e2662.jpg" 
                width="100%" 
                height="100%">
                </img>
            </div>
            """, 
            unsafe_allow_html=True
        )    

    with col3:
        st.markdown(
            """
            <div style="background-color: #f09db1; padding: 10px;">
                <h4 lass=\"container-content\" style=\"color: white;\">
                    Brinquedos Educativos
                </h4>
                <img 
                src="https://acdn.mitiendanube.com/stores/001/773/125/products/h4058562874ad403ab036d3c3465c5f7e7-fbd83cad39018ca9d516453684680902-1024-1024.jpg" 
                width="100%" 
                height="100%">
                </img>
            </div>
            """, 
            unsafe_allow_html=True
        )  

## localizacao
with st.container():
    st.markdown(        
        """
        <div class="container3">
            <h3 lass=\"container-content\" style=\"color: #f09db1;\">
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
