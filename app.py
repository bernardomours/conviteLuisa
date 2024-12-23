import streamlit as st
import base64
import mysql.connector

st.set_page_config(
    page_title="1 Aninho da Luísa",
    page_icon="🎀",
    layout="wide",
    initial_sidebar_state='collapsed'
)

# Configurações de evento
EVENT_DATE = "Sábado, 11 de Janeiro de 2024"
EVENT_TIME = "18h00 às 22h00"
VENUE = "Magic fest Buffet, R. Antônio Cirilino, 62 - Abolição, Mossoró - RN"
PARENTS_CONTACT = "(84) 9 8629-8159 - Roxanna\n(84) 9 8629-7626 - Lucas"

# Função para carregar imagens GIF
def load_gif_image(file_path):
    with open(file_path, "rb") as f:
        content = f.read()
    return base64.b64encode(content).decode("utf-8")


# CSS para estilizar o documento
st.markdown(
    """
    <style>
        #MainMenu {
            visibility: hidden;
        }
        .stAppHeader {
            visibility: hidden;
            background-color: #ffffff;
            padding: 0px;
        }
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
        .stButtonGroup {
            border: 0px;
            padding-top: 0px;
            padding-bottom: 20px; 
            padding-left: 20px;
            padding-right: 20px;
        }
        .stTextInput {
            border: 0px;
            padding-top: 0px;
            padding-bottom: 20px; 
            padding-left: 20px;
            padding-right: 20px;
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
            padding-left: 0px;
            padding-right: 0px; 
        }
        .container2 {
            background-color: #f09db1;
            padding-top: 10px;
            padding-bottom: 40px; 
            padding-left: 20px;
            padding-right: 30px; 
        }
        .container3 {
            background-color: #ffffff;
            padding-top: 10px;
            padding-bottom: 0px; 
            padding-left: 20px;
            padding-right: 30px; 
        }
        .container4 {
            background-color: #ffffff;
            padding-top: 10px;
            padding-bottom: 40px; 
            padding-left: 20px;
            padding-right: 30px; 
        }
        img {
            border-radius: 15px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

## CONVITE
with st.container():
    backgroundImg = load_gif_image("images/background-desktop.gif")
    testImg = load_gif_image("images/clothes.gif")
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
                    src="https://www.canva.com/design/DAGaE0fB8mw/FgxiT58lNN_e74-SBD0Bmg/view?embed">
                </iframe>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

## LOCALIZAÇÃO
with st.container():
    st.markdown(
        """
        <div class="container2">
            <h3 style="color: #ffffff; font-size: 30px; padding-bottom: 0px;">
                LOCALIZAÇÃO
            </h3>
            <p></p>
            <iframe 
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1986.7914538145997!2d-37.35306239001534!3d-5.170590171969311!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x7ba0703d0ed4ef3%3A0x145466ba02ac977c!2sMagic%20fest%20buffet!5e0!3m2!1spt-BR!2sbr!4v1734888634958!5m2!1spt-BR!2sbr" 
                width="100%" 
                height="300" 
                style="border:0; border-radius: 15px" 
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
            <h3 style="color: #f09db1; font-size: 30px; padding-bottom: 0px;">
                SUGESTÃO DE PRESENTE
            </h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    colShoes, colClothes, colToys = st.columns(3)

    # Presente 1
    with colShoes:
        shoesImg = load_gif_image("images/shoes.gif")
        st.markdown(
            f'<img src="data:image/gif;base64,{shoesImg}">', unsafe_allow_html=True
        )

    # Presente 2
    with colClothes:
        cloImg = load_gif_image("images/clothes.gif")
        st.markdown(
            f'<img src="data:image/gif;base64,{cloImg}">', unsafe_allow_html=True
        )

    # Presente 3
    with colToys:
        toyImg = load_gif_image("images/toys.gif")
        st.markdown(
            f'<img src="data:image/gif;base64,{toyImg}">', unsafe_allow_html=True
        )

with st.container():
    
    col1, col3 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="container3">
                <h3 style="color: #f09db1; font-size: 30px; padding-bottom: 0px;">
                    CONFIRMAÇÃO
                </h3>
            </div>
            """,
            unsafe_allow_html=True
        )

        ## formulario
        with st.form("form"):
            name = st.text_input("Seu Nome")
            options = ["Sim", "Não", "Estou em dúvida"]
            confirm = st.pills("Irá ao Aniversário?", options, selection_mode="multi")
            names = st.text_input(
                "Se você marcou sim, digite os nomes das pessoas que irão, incluindo você.",
                placeholder="Ex.: Lucas, Roxanna e Luísa."
            )

            submitted = st.form_submit_button("Enviar")
            
            if submitted:
                if confirm == 'Sim':
                    st.write("Obrigado! Ficaremos muito felizes com sua presença! :stuck_out_tongue:")
                
                if confirm == 'Não':
                    st.write("Que pena que não poderá ir. :confused: De toda forma agradecemos por fazer parte disso.")
                
                if confirm == "Estou em dúvida":
                    st.write("Ah, entendo! :disappointed_relieved: Caso decida ir nos procure até dia 02 de Janeiro.")
        
    with col3:
        st.markdown(
            f"""
            <div style="background-color: #ffffff; padding: 20px; border-radius: 15px;">
                <b><h3 style="color: #f09db1; font-size: 30px; padding-bottom: 10px;">INFORMAÇÕES GERAIS</h3></b>
                <h6>DATA</h6><p>{EVENT_DATE}</p>
                <h6>HORÁRIO</h6><p>{EVENT_TIME}</p>
                <h6>ENDEREÇO</h6><p>{VENUE}</p>
                <h6>CONTATO DOS PAPAIS</h6><p>{PARENTS_CONTACT}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# Função para conectar ao banco de dados
if submitted:
    cnx = mysql.connector.connect(
        user='main', password='getrolucas102030', host='34.151.230.176', database='conf_convidados'
    )
    cursor = cnx.cursor()

    query = """
        INSERT INTO confirmacao (nome, confirmacao, acompanha)
        values (%s, %s, %s)
        """
    vals = (name, confirm, names if names else "")

    cursor.execute(query, vals)
    cnx.commit
