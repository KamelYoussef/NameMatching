# app/main.py
import streamlit as st
import yaml
from fuzzywuzzy import process, fuzz


def find_closest_matches(input_name, name_list):
    matches = process.extract(input_name, name_list, limit=None, scorer=fuzz.partial_ratio)
    filtered_matches = [{'name': name, 'similarity': score} for name, score in matches]
    return filtered_matches


def load_name_list():
    with open("data/names.yaml", "r") as file:
        return yaml.safe_load(file)


def main():
    st.title("Name Matching App")

    # Load name list from YAML file
    name_list = load_name_list()

    # User input for name
    input_name = st.text_input("Enter a name:")

    if input_name:
        # Find all matches
        matches = find_closest_matches(input_name, name_list)

        # Display results
        st.markdown(f"### Matches for '{input_name}':")

        # Display up to 5 matches above the 70% threshold
        above_threshold = [match for match in matches if match['similarity'] >= 70][:5]
        for match in above_threshold:
            st.write(f"{match['name']}, Similarity: {match['similarity']}%")

        # Display up to (5 - len(above_threshold)) matches below the 70% threshold in another font style
        st.markdown("#### Weak matches:")
        below_threshold = [match for match in matches if match['similarity'] < 70][:5 - len(above_threshold)]
        for match in below_threshold:
            st.write(f"{match['name']}, Similarity: {match['similarity']}%")


if __name__ == "__main__":
    main()
