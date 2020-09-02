import streamlit as st
import awesome_streamlit as ast

import pages.dashboard
import pages.spotify
import pages.arxiv
import pages.medium
import pages.youtube
import pages.about

#ast.core.services.other.set_logging_format()

PAGES = {
    "Dashboard": pages.dashboard,
    "PodCalytics": pages.spotify ,
    "arXiv Analytics": pages.arxiv ,
    "About": pages.about,
}


def main():
    """Main function of the App"""

    st.beta_set_page_config(
            page_title="Podcalytics", # => Quick reference - Streamlit
            page_icon="🚀",
            layout="centered", # wide
            initial_sidebar_state="auto") # collapsed

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    category_selectbox = st.sidebar.selectbox(
    'Category',
    ('Data Science', 'Business', 'Mathematics', 'Politics')
)

    st.sidebar.title("About")
    st.sidebar.info(
            """
            This app was made with ♥️ during batch #434 of the [Le Wagon](https://lewagon.com) Data Science bootcamp in Berlin 2020.
    """
)

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)




if __name__ == "__main__":
    main()
