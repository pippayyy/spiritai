import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import sidebar
import os
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import sidebar
import matplotlib.pyplot as plt  
import squarify
import time

# Used for styling
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

# Set spinner visbility to true
showSpinner = True

# Sidebar
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


# Main page

# Center-aligned header
st.markdown("<h1 style='text-align: center;'>Identify Comment Themes</h1>", unsafe_allow_html=True)

# Center-aligned paragraph
st.markdown("<p style='text-align: center;'>Upload your Spirit Beat comment extract (excel file) to perform a thematic analysis.</p>", unsafe_allow_html=True)

# Spacer
st.markdown("<div style='padding: 10px 5px;'></div>", unsafe_allow_html=True)




import pandas as pd

# File Uploader
uploaded_files = st.file_uploader("Choose an .xlsx file", accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        # Read the file into a Pandas DataFrame
        input_data = pd.read_excel(uploaded_file)
        
        # Display the filename
        st.write("Filename:", uploaded_file.name)



import streamlit as st
import pandas as pd
import plotly.express as px

# Colors for the treemap
colors = ['#9C2AA0', '#5E2750', '#00B0CA', '#007C92', '#A8B400', '#FECB00', '#EB9700']

# File Uploader
uploaded_files_output = st.file_uploader("Temp", accept_multiple_files=True)

# Check if any files have been uploaded
if uploaded_files_output:
    time.sleep(4) # Sleep for 4 seconds
    showSpinner = False
    for uploaded_file_output in uploaded_files_output:
        # Read the file into a Pandas DataFrame
        output_data = pd.read_excel(uploaded_file_output)
        
        # Display the filename
        st.write("Filename:", uploaded_file_output.name)
        
        # Display the DataFrame
        st.dataframe(output_data)

        # Check if 'theme_name' column exists in the DataFrame
        if 'theme_name' in output_data.columns:
            # Aggregate the data to count occurrences of each theme
            theme_counts = output_data['theme_name'].value_counts().reset_index()
            theme_counts.columns = ['theme_name', 'count']
            
            # Create the treemap
            fig = px.treemap(
                theme_counts,
                path=['theme_name'],
                values='count',
                color='theme_name',
                color_discrete_sequence=colors
            )
            
            # Plot the chart
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.write("The uploaded file does not contain a 'theme_name' column.")





# Spinner Animation
import json
import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install streamlit-lottie

# Load animation JSON file - function
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Load animation JSON file - call function using URL
lottie_coding = load_lottiefile("images/VF_Living_Speechmark_Rotation_drawn_on_Lottie_Red_300.json")  # replace link to local lottie file

# Add columns to centralise loading spinner
col1, col2, col3 = st.columns(3)


# Add loading spinner
if showSpinner:
    with col2:
        st_lottie(
            lottie_coding,
            width=300
        )


# # Treemap
# from docx import Document  
# from docx.shared import Inches  
# import io  
  
# # Function to save the treemap figure to a BytesIO object  
# def save_treemap_to_bytes(fig):  
#     buf = io.BytesIO()  
#     fig.savefig(buf, format='png')  
#     buf.seek(0)  
#     return buf  
  
# # Function to create a .docx file with the treemap image  
# def create_treemap_docx(fig_buf, filename='treemap.docx'):  
#     # Create a new Document  
#     doc = Document()  
#     doc.add_heading('Treemap', 0)  
  
#     # Add the treemap image to the document  
#     doc.add_picture(fig_buf, width=Inches(6))  
      
#     # Save the document to a BytesIO object  
#     doc_buf = io.BytesIO()  
#     doc.save(doc_buf)  
#     doc_buf.seek(0)  
      
#     return doc_buf  
 
# volume = [350, 220, 170, 150, 50]
# labels = ['Do the right thing', 'Pay us more',
#          'Management = BAD', 'We should\n work together',
#          'I dont know']
# color_list = ['#e60000', '#4a4d4e', '#9c2aa0',
#              '#00b0ca', '#eb9800', '#5e2750']
 
# fig, ax = plt.subplots()
# plt.rc('font', size=14)
# squarify.plot(sizes=volume, label=labels,
#              color=color_list)
# plt.axis('off')
# # Display the treemap
# st.pyplot(fig)
 
 
# # Save the figure to a BytesIO object  
# fig_buf = save_treemap_to_bytes(fig)  
    
# # Create a .docx file with the treemap image  
# doc_buf = create_treemap_docx(fig_buf)  
    
# # Use Streamlit's download button to offer the .docx file for download  
# st.download_button(  
#     label='Download Treemap as DOCX',  
#     data=doc_buf,  
#     file_name='treemap.docx',  
#     mime='application/vnd.openxmlformats-officedocument.wordprocessingml.document'  
# )  






# import numpy as np
# import plotly.express as px

# colors = ['#9C2AA0',  '#5E2750', '#00B0CA', '#007C92', '#A8B400', '#FECB00', '#EB9700']

# # Create distplot with custom bin_size
# fig = px.treemap(
#     names = ["Eve","Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
#     parents = ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"],
# )

# # Plot!
# st.plotly_chart(fig, use_container_width=True)

