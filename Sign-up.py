import streamlit as st
import pandas as pd

st.title("Sign-up Page")
Duser = st.text_input("username")
Dpassword = st.text_input("password", type="password")

csv_file = "Data/users.csv"

if st.button("Create new account"):
    user = Duser.strip()
    password = Dpassword.strip()
    
    if not user or not password:
        st.error("Please enter both the user and the password")
    else:
        df = pd.read_csv(csv_file)

        if user in df["username"].astype(str).values:
            st.error("this user has been already used")
        else:
            new_data = pd.DataFrame([{"username":user,"password":password}])
            new_data.to_csv(csv_file, mode="a",header=False, index=False)
            st.success("account created successfully")

if st.button("Login"):
    st.switch_page("Login.py")
        
