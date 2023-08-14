import re

# Define regular expressions for PII and PHI
pii_pattern = re.compile(r'\b(?:\d{9}|\d{3}-\d{2}-\d{4}|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,})\b')
phi_pattern = re.compile(r'\b\d{10}\b')  # Example: Medical record number

# Open and read the text file
with open('large_text_file.txt', 'r') as file:
    for line in file:
        if pii_pattern.search(line):
            print("Found PII:", line.strip())
        if phi_pattern.search(line):
            print("Found PHI:", line.strip())

