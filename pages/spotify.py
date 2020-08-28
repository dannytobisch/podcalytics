import streamlit as st

# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading Dashboard ..."):
        #ast.shared.components.title_awesome("")
        st.write()
        st.title('Spotify - Analytics')
