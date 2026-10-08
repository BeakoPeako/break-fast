import streamlit as st
import pandas as pd

csv_file = "Data/users.csv"

st.title("Login Page")
Duser = st.text_input("username")
Dpassword = st.text_input("password", type="password")

user = Duser.strip()
password = Dpassword.strip()

if st.button("Login"):
    df = pd.read_csv(csv_file)

    matched = False

    if user in df["username"].astype(str).values:
        passwordd = df.loc[df["username"] == user, "password"]
        matched = (password == passwordd.item())
    # print(matched,passwordd)
    if matched:
        st.success("login successful")

    else:
        st.error("wrong username or password.")

if st.button("New account"):
    st.switch_page("Sign-in.py")