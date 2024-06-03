import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import sidebar
import os

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

        [data-testid=stSidebarUserContent] {
            padding-bottom: 0px;
        }

        .sidebar .sidebar-content {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .wrap {
            height: 260px;
            margin: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .wrap span {
            align-self: flex-end;
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
    st.page_link("pages/themes.py", label="Themes")
    st.page_link("pages/sentiment.py", label="Sentiment", disabled=True)
    st.page_link("http://www.google.com", label="Chat", disabled=True)

    # Center-aligned paragraph
    st.markdown("<div style='text-align: center;' class='wrap'><span style='text-align: center;'>Developed by VBTS UK</span></div>", unsafe_allow_html=True)



# Center-aligned header
st.markdown("<h1 style='text-align: center;'>Identify Comment Themes</h1>", unsafe_allow_html=True)

# Center-aligned paragraph
st.markdown("<p style='text-align: center;'>Upload your Spirit Beat comment extract (excel file) to perform a thematic analysis.</p>", unsafe_allow_html=True)



uploaded_files = st.file_uploader("Choose an .xlsx file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)