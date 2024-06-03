import streamlit as st

st.markdown(
    """
    <style>
        [data-testid=stSidebar] [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
        .sidebar .sidebar-content {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

    </style>
    """, unsafe_allow_html=True
)

with st.sidebar:
    # VF Icon
    st.image('images/VF_Icon_RGB_RED.png', width=100)

    # Center-aligned header
    st.markdown("<h3 style='text-align: center;'>Spirit Survey AI Analyser</h3>", unsafe_allow_html=True)

    # Divider
    st.divider()

    # Nav page links
    st.page_link("streamlit_app.py", label="Home")
    st.page_link("pages/themes.py", label="Themes")
    st.page_link("pages/sentiment.py", label="Sentiment", disabled=True)
    st.page_link("http://www.google.com", label="Chat", disabled=True)
