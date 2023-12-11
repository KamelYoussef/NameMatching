# app/main.py
import streamlit as st
import yaml
from difflib import SequenceMatcher

MAX_DISPLAYED_MATCHES = 5

def find_closest_matches(input_name, name_list):
    matches = [{'name': name, 'similarity': calculate_similarity(input_name.lower(), name.lower())} for name in name_list]
    return sorted(matches, key=lambda x: x['similarity'], reverse=True)

def calculate_similarity(a, b):
    return round(SequenceMatcher(None, a, b).ratio() * 100)

def load_name_list():
    with open("data/names.yaml", "r") as file:
        return yaml.safe_load(file)

def display_similarity_bar(similarity, label):
    # Display a progress bar for similarity with additional information
    st.write(f"{label} --- {similarity}%")
    st.progress(similarity / 100.0)

def main():
    st.title("Name Matching App")

    # Load name list from YAML file
    name_list = load_name_list()

    # User input for name
    input_name = st.text_input("Enter a name:")

    if input_name:
        # Find all matches
        matches = find_closest_matches(input_name, name_list)

        # Display matches
        st.markdown(f"### Matches for {input_name}:")

        total_displayed = 0
        for match in matches:
            if total_displayed < MAX_DISPLAYED_MATCHES:
                total_displayed += 1
                display_similarity_bar(match['similarity'], f"{match['name']}")

        if total_displayed == 0:
            st.write(f"Pas de résultats similaires retrouvés")

if __name__ == "__main__":
    main()
