import streamlit as st

def display_similarity_bar(similarity, label):
    # Display a progress bar for similarity with additional information
    st.write(f"{label} --- {int(similarity)}%")
    st.progress(similarity / 100)
