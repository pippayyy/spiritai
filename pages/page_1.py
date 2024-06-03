import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import sidebar


# Center-aligned header
st.markdown("<h1 style='text-align: center;'>Identify Comment Themes</h1>", unsafe_allow_html=True)

# Center-aligned paragraph
st.markdown("<p style='text-align: center;'>Upload your Spirit Beat comment extract (excel file) to perform a thematic analysis.</p>", unsafe_allow_html=True)

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
    st.image('VF_Icon_RGB_RED.png', width=100)

    # Center-aligned header
    st.markdown("<h3 style='text-align: center;'>Spirit Survey AI Analyser</h3>", unsafe_allow_html=True)

    # Divider
    st.divider()

    # Nav page links
    st.page_link("streamlit_app.py", label="Home")
    st.page_link("pages/page_1.py", label="Themes")
    st.page_link("pages/page_2.py", label="Sentiment", disabled=True)
    st.page_link("http://www.google.com", label="Chat", disabled=True)

