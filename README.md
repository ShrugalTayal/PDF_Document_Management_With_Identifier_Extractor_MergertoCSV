# PDF_Document_Management_With_Identifier_Extractor_MergertoCSV
 PDF Document Management With Identifier Extractor and Loader. This repository contains Python scripts for managing PDF documents efficiently. The scripts provide functionalities to extract unique identifiers from PDF files and organize them into a structured document management system. It includes updating extracted features to a CSV file based on predefined parameters. This tool streamlines the process of handling PDF documents and extracting relevant information for further analysis or processing.

### Instructions for Using Python Scripts

#### Script 1: PDF File Selection and Processing

- **Description**: This script allows users to select a PDF file, extracts information from the PDF, and performs operations based on the extracted data.
- **Libraries Used**: `os`, `tkinter`, `PyPDF2`
- **Functionality**:
  - It presents a dialog window for selecting a PDF file.
  - Extracts the number of pages in the PDF and text from the first page.
  - Additional operations on the PDF can be added as needed.
- **Usage**:
  1. Run the script.
  2. Select a PDF file using the dialog window.
  3. The script extracts information from the selected PDF file.

#### Script 2: PDF Table Extraction and CSV Conversion

- **Description**: This script extracts tables from PDF files using tabula and saves them as CSV files.
- **Libraries Used**: `os`, `tabula`
- **Functionality**:
  - It allows users to select a folder containing PDF files and an output folder for saving CSV files.
  - Extracts tables from each PDF file in the selected folder.
  - Saves the extracted tables as CSV files in the specified output folder.
- **Usage**:
  1. Run the script.
  2. Select a folder containing PDF files and an output folder for CSV files.
  3. The script extracts tables from each PDF file and saves them as CSV files in the output folder.

#### Script 3: CSV File Processing with Custom Headers

- **Description**: This script loads CSV files, allows users to input custom headers, and saves transformed CSV files.
- **Libraries Used**: `os`, `pandas`, `tkinter`
- **Functionality**:
  - It prompts the user to select a directory containing CSV files and an output directory for transformed CSV files.
  - Users can input custom headers for each CSV file.
  - Loads each CSV file, replaces column names with custom headers (if provided), and saves the transformed CSV files.
- **Usage**:
  1. Run the script.
  2. Select a directory containing CSV files and an output directory for transformed CSV files.
  3. Input custom headers (optional) for each CSV file when prompted.

#### Script 4: DataFrame Merge with User Input

- **Description**: This script performs a left join on two DataFrames based on user-defined columns.
- **Libraries Used**: `os`, `pandas`, `tkinter`
- **Functionality**:
  - It prompts the user to select source and target CSV files.
  - Users define a unique column and columns to merge on.
  - Performs a left join on the DataFrames and saves the result as a CSV file.
- **Usage**:
  1. Run the script.
  2. Select source and target CSV files using the dialog window.
  3. Define a unique column and columns to merge on when prompted.

### Instructions for Running Scripts

- Ensure you have Python installed on your system.
- Install required libraries using `pip install requirements.txt`.
- Run each script using Python interpreter.
- Follow the on-screen instructions and provide necessary inputs through the UI dialog windows.
- View the printed outputs and check generated CSV files as per the script functionalities.