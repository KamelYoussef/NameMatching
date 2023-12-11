# Name Matching App

## Overview

This is a simple Python app that helps match input names with a list of predefined names, displaying the top matches along with their similarity scores. The app is built using the Streamlit framework and utilizes the fuzzy string matching library, fuzzywuzzy.

## Features

- Allows users to enter a name and find the closest matches in a predefined list.
- Displays the top matches above a specified similarity threshold (70% by default).
- Limits the total number of displayed matches to 5.
- Provides a clean and user-friendly interface for interaction.

## Project Structure

The project is organized as follows:

- **app/**: Main directory for the Streamlit app.
  - **main.py**: Entry point for the Streamlit application.
  - **utils/**
    - **__init__.py**: Empty file to make the directory a Python package.
    - **name_matching.py**: Utility module for name matching.

- **data/**: Directory containing data files.
  - **names.yaml**: YAML file containing the predefined list of names.

- **requirements.txt**: File listing project dependencies.

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/name-matching-app.git
    cd name-matching-app
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:

    ```bash
    streamlit run app/main.py
    ```

5. Open your web browser and navigate to [http://localhost:8501](http://localhost:8501) to interact with the app.

## Customization

- **Adjusting the Similarity Threshold**: Modify the `threshold` parameter in `main.py` to change the similarity threshold.

- **Updating the List of Names**: Modify the `names.yaml` file in the `data` directory to update the list of names.

## Dependencies

- [Streamlit](https://www.streamlit.io/)
- [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy)
- [PyYAML](https://pyyaml.org/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
