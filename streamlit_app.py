import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import sidebar

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

        [data-testid=stSidebarUserContent] {
            padding-bottom: 0px;
        }

        .title-text {
        color: #E60000;
        }

        @font-face {
        font-family: 'Futura PT Light';
        font-style: normal;
        font-weight: normal;
        src: local('Futura PT Light'), url('fonts/WOFF.woff') format('woff');
        }
        html, body, [class*="css"] {
        font-family: 'Futura PT Light', sans-serif;
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

    # Center-aligned paragraph
    st.markdown("<div style='text-align: center;' class='wrap'><span style='text-align: center;'>Developed by VBTS UK</span></div>", unsafe_allow_html=True)



# Center-aligned header
st.markdown("<h1 style='text-align: center;'>Spirit AI Tool</h1>", unsafe_allow_html=True)

# Center-aligned paragraph
st.markdown("<p style='text-align: center;'>This tool uses AI to analyse spirit comments quickly, making it easier for Spirit Ambassadors to provide a high-level view of comments.</p>", unsafe_allow_html=True)

# Left-aligned header
st.markdown("<h1 style='text-align: left;'>How it works?</h1>", unsafe_allow_html=True)

# Left-aligned paragraph
st.markdown("<p style='text-align: left;'>Blah blah blahhhh</p>", unsafe_allow_html=True)

# Divider
st.divider()



# Left-aligned header
st.markdown("<h1 style='text-align: left;'>Why is this beneficial?</h1>", unsafe_allow_html=True)

# Left-aligned paragraph
st.markdown("<p style='text-align: left;'>Using AI to analyse Spirit Beat data enables Spirit Ambassadors to identify common themes and key insights fast. Using this technology is crucial for efficiently processing large volumes of feedback.</p>", unsafe_allow_html=True)

# Divider
st.divider()



