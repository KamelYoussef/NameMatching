from difflib import SequenceMatcher

def find_closest_matches(input_name, name_list):
    matches = [{'name': name, 'similarity': calculate_similarity(input_name.lower(), name.lower())} for name in name_list]
    return sorted(matches, key=lambda x: x['similarity'], reverse=True)

def calculate_similarity(a, b):
    return round(SequenceMatcher(None, a, b).ratio() * 100)
