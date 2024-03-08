import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog, simpledialog

def load_single_csv_file(csv_file_path, custom_headers):
    """
    Load a single CSV file into a DataFrame.
    
    Parameters:
        csv_file_path (str): Path to the CSV file.
        custom_headers (list): List of custom headers provided by the user.
        
    Returns:
        pandas.DataFrame: DataFrame containing data from the CSV file.
    """
    # Load the CSV file into a DataFrame, skipping rows 0 and 1 for column names
    df = pd.read_csv(csv_file_path, header=[0, 1])

    # Concatenate row 0 and row 1 to create new column names
    new_columns = [f'{col1} {col2}' if col2 else col1 for col1, col2 in zip(df.columns.get_level_values(0), df.iloc[1])]
    
    # If custom headers are provided, replace the new column names
    if custom_headers:
        new_columns = custom_headers

    # Assign the new column names to the DataFrame
    df.columns = new_columns
    
    # Drop rows 0 and 1
    df = df.drop([0, 1])
    
    return df

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

def main():
    # Prompt the user to select the directory containing CSV files
    csv_input_dir = select_folder_dialog("Select directory containing CSV files")

    # Prompt the user to select the directory where transformed CSV files will be saved
    csv_output_dir = select_folder_dialog("Select output directory for transformed CSV files")

    if csv_input_dir and csv_output_dir:
        # Get list of CSV files in the folder
        csv_files = [f for f in os.listdir(csv_input_dir) if f.endswith('.csv')]

        # Iterate over each CSV file in the directory
        for csv_file_name in csv_files:
            # Construct the full path to the CSV file
            csv_file_path = os.path.join(csv_input_dir, csv_file_name)

            # Prompt the user to input custom headers
            custom_headers = simpledialog.askstring("Custom Headers", f"Enter custom headers for file '{csv_file_name}' separated by commas (leave blank to use default headers): ")

            # Load the CSV file
            df = load_single_csv_file(csv_file_path, custom_headers.split(',') if custom_headers else [])

            # Print the DataFrame
            print(f"Data from file '{csv_file_name}':")
            print(df)

            # Save the DataFrame as a CSV file in the output directory
            output_csv_file_path = os.path.join(csv_output_dir, csv_file_name)
            df.to_csv(output_csv_file_path, index=False)

            print(f"DataFrame saved as CSV at '{output_csv_file_path}'")

if __name__ == "__main__":
    main()