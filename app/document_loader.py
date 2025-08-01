import fitz 

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts all text from a PDF file using PyMuPDF.
    
    Args:
        pdf_path (str): Local path to the PDF file.

    Returns:
        str: Full extracted text.
    """
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text
