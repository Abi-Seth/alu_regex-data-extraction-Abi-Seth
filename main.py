import re

patterns = {
    "email": r"\b[a-zA-Z0-9._%+-]+@(?:[a-zA-Z0-9.-]+\.)+[a-zA-Z]{2,}\b",
    "url": r"https?://[^\s/$.?#].[^\s]*",
    "phone": r"\b(?:\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}\b",
    "credit_card": r"\b(?:\d{4}[-.\s]?){3}\d{4}\b",
    "time": r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b",
    "currency": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?",
    "html_tag": r"</?[a-zA-Z][^>]*>",
    "hashtag": r"#\w+"
}

def extract_data(patterns, text):
    for label, regex in patterns.items():
        matches = re.findall(regex, text)
        print(f"\n{label.upper()} matches:")
        if matches:
            for match in matches:
                print("-", match)
        else:
            print("No matches found.")

with open('test-data.txt', 'r', encoding='utf-8') as file:
    sample_data = file.read()

extract_data(patterns, sample_data)
