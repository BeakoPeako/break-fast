import streamlit as st
import pandas as pd

login_page = st.Page("Login.py",title="Login")
Sign_in_page = st.Page("Sign-in.py",title="Sign-in")

st.session_state.pages = {
    "Login" : login_page,
    "Sign-in" : Sign_in_page
}

def swich_pages(page):
    st.session_state.Cpage = st.session_state.pages[page]
    st.rerun()

if "Cpage" not in st.session_state:
    st.session_state.Cpage = login_page

pg = st.navigation([login_page, Sign_in_page], position="sidebar")

pg.run()

