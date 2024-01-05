from thefuzz import fuzz
import yaml
import streamlit as st
import pandas as pd

# Load YAML file
yaml_file_path = 'app/names.yaml'
with open(yaml_file_path, 'r') as file:
    data = yaml.safe_load(file)

# Streamlit app
st.title("Company Name Matching")

# User input: DataFrame with company names
st.header("Enter Company Names for Matching")
input_name = st.text_input("Enter a name:")

# Button to trigger name matching
if st.button("Search"):
    # Number of matches
    NUMBER_OF_MATCHES = 5
    df_companies = pd.DataFrame(data, columns=["Company name"])

    # Display the matched names and scores
    st.header("Top 5 Similar Names:")

    # Calculate scores using fuzz.token_sort_ratio in a vectorized way
    df_companies["score"] = df_companies["Company name"].apply(lambda x: fuzz.token_sort_ratio(x, input_name))

    # Sort the DataFrame based on the scores
    sorted_df = df_companies.sort_values(by="score", ascending=False)

    # Display the top 5 matches
    st.table(sorted_df.head(NUMBER_OF_MATCHES))
