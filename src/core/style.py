import streamlit as st

def page_style():
    
    hide_streamlit_style = """
    <style>
        #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
    </style>

    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    hide_top_bar="""
    <style>
        [data-testid="stDecoration"] {
            display: none;
        }

    </style>"""
    st.markdown(hide_top_bar, unsafe_allow_html=True)

    st.markdown(""" <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> """, unsafe_allow_html=True)