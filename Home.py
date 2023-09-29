import streamlit as st
import streamlit.components.v1 as components



OpenAI_Key = st.secrets["OpenAI_Key"]

st.set_page_config(
    page_title="Grape Chat Bot",
    page_icon="https://www.flaticon.com/free-icon/grapes_5246707?term=grape&page=1&position=15&origin=search&related_id=5246707",
    layout="wide",
    initial_sidebar_state="expanded",
)
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

st.image("images/eduquest-logo2.png", width= 400)

st.markdown("""

            Grape
""")

            
