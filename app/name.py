import streamlit as st
import pandas as pd
import yaml
from name_matching.name_matcher import NameMatcher
from utils.display_utils import display_similarity_bar

# Load YAML file
yaml_file_path = 'app/names.yaml'
with open(yaml_file_path, 'r') as file:
    data = yaml.safe_load(file)

# Convert to Pandas DataFrame
df_companies_a = pd.DataFrame(data, columns=["Company name"])


# Streamlit app
st.title("Company Name Matching")

# User input: DataFrame with company names
st.header("Enter Company Names for Matching")
input_name = st.text_input("Enter a name:")
df_companies_b = pd.DataFrame({
    "name": [input_name]
})

# Button to trigger name matching
if st.button("Search"):
    # Number of matches
    NUMBER_OF_MATCHES = 5

    # Initialize the name matcher
    matcher = NameMatcher(number_of_matches=NUMBER_OF_MATCHES,
                          legal_suffixes=True,
                          common_words=False,
                          top_n=50,
                          verbose=True)

    # Adjust the distance metrics to use
    matcher.set_distance_metrics(['bag', 'typo', 'refined_soundex'])

    # Load and process the master data
    matcher.load_and_process_master_data(column='Company name',
                                         df_matching_data=df_companies_a,
                                         transform=True)

    # Perform the name matching on the data
    matches = matcher.match_names(to_be_matched=df_companies_b,
                                  column_matching='name')

    # Display the matched names and scoresb
    st.header("Top 5 Similar Names:")
    for i in range(NUMBER_OF_MATCHES):
        display_similarity_bar(matches[f'score_{i}'][0], f"{matches[f'match_name_{i}'][0]}")
