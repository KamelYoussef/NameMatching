import streamlit as st
from utils.data_loader import load_name_list
from utils.similarity_calculator import find_closest_matches
from utils.display_utils import display_similarity_bar

MAX_DISPLAYED_MATCHES = 5

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
            st.write(f"No similar results found.")

if __name__ == "__main__":
    main()
