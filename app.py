import streamlit as st
import awesome_streamlit as ast

import pages.dashboard
import pages.dashboard_live
import pages.dashboard2
import pages.dashboard3
import pages.spotify
import pages.arxiv
import pages.medium
import pages.youtube
import pages.about

#ast.core.services.other.set_logging_format()

PAGES = {
    "philoML": pages.dashboard_live,
    "Spotify Analytics": pages.spotify ,
    "arXiv Analytics": pages.arxiv ,
    "About": pages.about,
}


def main():
    """Main function of the App"""

    st.beta_set_page_config(
            page_title="philoML - The key to knowledge", # => Quick reference - Streamlit
            page_icon="🌊",
            layout="centered", # wide
            initial_sidebar_state="auto") # collapsed

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    category_selectbox = st.sidebar.selectbox(
    'Category',
    ('Data Science', 'Business', 'Mathematics', 'Politics')
)

    data_selectbox = st.sidebar.multiselect(
    'Data Source',
    ('Spotify', 'YouTube', 'Medium', 'arXiv'),

)

    st.sidebar.title("About")
    st.sidebar.info(
            """
            This app was made with ♥️ during batch #434 of the [Le Wagon](http://lewagon.com) Data Science bootcamp in Berlin 2020.
    """
)

    page = PAGES[selection]

    if set(data_selectbox) == {'Spotify', 'YouTube', 'Medium', 'arXiv'}:
        with st.spinner(f"Loading {selection} ..."):
            ast.shared.components.write_page(pages.dashboard)

    if set(data_selectbox) == {'Spotify', 'YouTube'}:
        with st.spinner(f"Loading {selection} ..."):
            ast.shared.components.write_page(pages.dashboard2)

    if set(data_selectbox) == {'arXiv', 'Medium'}:
        with st.spinner(f"Loading {selection} ..."):
            ast.shared.components.write_page(pages.dashboard3)

    if set(data_selectbox) == {'Spotify', 'Medium'}:
        with st.spinner(f"Loading {selection} ..."):
            ast.shared.components.write_page(page)

    if set(data_selectbox) == {'Spotify', 'arXiv'}:
        with st.spinner(f"Loading {selection} ..."):
            ast.shared.components.write_page(page)

    if set(data_selectbox) == {'Youtube', 'Medium'}:
        with st.spinner(f"Loading {selection} ..."):
            ast.shared.components.write_page(page)

    if set(data_selectbox) == {'Youtube', 'arXiv'}:
        with st.spinner(f"Loading {selection} ..."):
            ast.shared.components.write_page(page)

    if len(data_selectbox) == 1:
        with st.spinner(f"Loading {selection} ..."):
            ast.shared.components.write_page(page)

    if len(data_selectbox) == 3:
        with st.spinner(f"Loading {selection} ..."):
            ast.shared.components.write_page(page)

    if data_selectbox == []:
        with st.spinner(f"Loading {selection} ..."):
            ast.shared.components.write_page(page)



if __name__ == "__main__":
    main()
