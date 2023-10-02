import streamlit as st

from streamlit_option_menu import option_menu
from core.style import page_style
from core.pages import (
     info,
     chat,
     file,
)


st.set_page_config(page_title="The omniscient referee", layout="wide")

page_style()

st.markdown("<h1 style='text-align: center;'>Ask the Rule Book Master🏀</h1>", unsafe_allow_html=True)

selected_footer = option_menu(
    menu_title=None,
    options=[
        "Info",
        "Chat",
        "File",
    ],
    icons=["info-circle", "chat-square-text", "folder"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)
match selected_footer:
    case "Info":
        info()
    case "Chat":
        chat()
    case "File":
        file()
    case _:
        info()

