import os
import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader

def select_file_dialog(title="Select PDF File"):
    """
    Open a file dialog window and return the selected PDF file path.
    
    Parameters:
        title (str): Title of the file dialog window.
        
    Returns:
        str: File path of the selected PDF file.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title=title, filetypes=[("PDF Files", "*.pdf")])
    root.destroy()  # Close the Tkinter window
    return file_path

def main():
    # Prompt the user to select a PDF file
    pdf_file_path = select_file_dialog("Select PDF File")

    if pdf_file_path:
        with open(pdf_file_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            
            # Access information from the PDF
            num_pages = len(pdf_reader.pages)
            print(f"Number of pages in '{os.path.basename(pdf_file_path)}': {num_pages}")
            
            # Example: Extract text from the first page
            first_page_text = pdf_reader.pages[0].extract_text()
            print(f"Text from the first page of '{os.path.basename(pdf_file_path)}': {first_page_text}")
            
            # You can perform more operations on the pdf_reader object as needed

if __name__ == "__main__":
    main()