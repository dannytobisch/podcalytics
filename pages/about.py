import streamlit as st

# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading ..."):
        #ast.shared.components.title_awesome("")
        st.write()
        st.title('About')
        st.balloons()

        page_bg_img2 = '''
                  <img src="https://i.pinimg.com/564x/b0/13/43/b01343bd27e853ad98d255c8b6748d85.jpg"\
                      style="align:center">
                  '''

        st.markdown(page_bg_img2, unsafe_allow_html=True)

