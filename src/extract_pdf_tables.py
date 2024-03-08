import os
import tkinter as tk
from tkinter import filedialog
import tabula

def extract_tables_from_pdf(pdf_file_path):
    """
    Extract tables from a PDF file using tabula.
    
    Parameters:
        pdf_file_path (str): Path to the PDF file.
        
    Returns:
        list: List of DataFrames representing the extracted tables.
    """
    # Extract tables from the PDF using tabula
    tables = tabula.read_pdf(pdf_file_path, pages='all')
    return tables

def save_tables_as_csv(tables, pdf_file_name, output_dir):
    """
    Save extracted tables as CSV files.
    
    Parameters:
        tables (list): List of DataFrames representing the tables.
        pdf_file_name (str): Name of the PDF file.
        output_dir (str): Path to the directory where CSV files will be saved.
    """
    # Iterate over each table in the list
    for idx, table in enumerate(tables):
        # Define the CSV file name
        csv_file_name = f"{os.path.splitext(pdf_file_name)[0]}_table_{idx + 1}.csv"
        
        # Construct the full path to the CSV file in the output directory
        csv_file_path = os.path.join(output_dir, csv_file_name)
        
        # Save the table as a CSV file in the output directory
        table.to_csv(csv_file_path, index=False)
        
        print(f"Table {idx + 1} from '{pdf_file_name}' saved as '{csv_file_name}' in '{output_dir}'")

def select_folder_dialog(title="Select Folder"):
    """
    Open a folder dialog window and return the selected folder path.
    
    Parameters:
        title (str): Title of the folder dialog window.
        
    Returns:
        str: Folder path of the selected folder.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    folder_path = filedialog.askdirectory(title=title)
    root.destroy()  # Close the Tkinter window
    return folder_path

def select_file_dialog(title="Select File"):
    """
    Open a file dialog window and return the selected file path.
    
    Parameters:
        title (str): Title of the file dialog window.
        
    Returns:
        str: File path of the selected file.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title=title, filetypes=[("PDF Files", "*.pdf")])
    root.destroy()  # Close the Tkinter window
    return file_path

def main():
    # Prompt the user to select a folder containing PDF files
    pdf_folder_path = select_folder_dialog("Select folder containing PDF files")

    # Prompt the user to select a folder where CSV files will be saved
    csv_output_dir = select_folder_dialog("Select output folder for CSV files")

    if pdf_folder_path and csv_output_dir:
        # Get list of PDF files in the folder
        pdf_files = [f for f in os.listdir(pdf_folder_path) if f.endswith('.pdf')]

        # Iterate over each PDF file in the directory
        for pdf_file_name in pdf_files:
            # Construct the full path to the PDF file
            pdf_file_path = os.path.join(pdf_folder_path, pdf_file_name)

            # Extract tables from the PDF
            tables = extract_tables_from_pdf(pdf_file_path)

            # Save the extracted tables as CSV files
            save_tables_as_csv(tables, pdf_file_name, csv_output_dir)

if __name__ == "__main__":
    main()