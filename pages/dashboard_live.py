import streamlit as st
from modules.recommender import recommendation_system_labeled
import pandas as pd
# pylint: disable=line-too-long

def write():
    """Used to write the page in the app.py file"""
    #with st.spinner("Loading Dashboard ..."):
        #ast.shared.components.title_awesome("")

    #st.write()


    page_bg_img = '''
                  <style>
                  body {
                  background-image: url("https://images.unsplash.com/photo-1474390690775-517486716e55?ixlib=rb-1.2.1&auto=format&fit=crop&w=1955&q=80");
                  background-size: cover;
                    }
                  </style>
                  '''

    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.title('philoML - The key to knowledge')

    user_input = st.text_input("Topic (please enter up to two keywords)", 'Data Science', key = '2')

    #user_input = input.lower().replace(' ','_')


