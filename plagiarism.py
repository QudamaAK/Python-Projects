import spacy
from docx import Document

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

def read_docx(file_path):
    doc = Document(file_path)
    return ' '.join([para.text for para in doc.paragraphs])

def calculate_similarity(text1, text2):
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    return doc1.similarity(doc2)

# Replace 'file1.docx' and 'file2.docx' with the paths to your Word files
file1_path = 'D:\Football.docx'
file2_path = 'D:\Cricket.docx'

text1 = read_docx(file1_path)
text2 = read_docx(file2_path)

similarity_score = calculate_similarity(text1, text2)

print(f"Similarity score: {similarity_score:.2f}")