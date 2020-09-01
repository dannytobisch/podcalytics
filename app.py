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
    "Medium Analytics": pages.medium,
    "YouTube Analytics": pages.youtube,
    "About": pages.about,
}


def main():
    """Main function of the App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    category_selectbox = st.sidebar.selectbox(
    'Category',
    ('Data Science', 'Business', 'Mathematics', 'Politics')
)

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)

if __name__ == "__main__":
    main()
