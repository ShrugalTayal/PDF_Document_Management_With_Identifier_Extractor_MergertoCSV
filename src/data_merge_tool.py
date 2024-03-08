import tkinter as tk
from tkinter import filedialog, simpledialog
import pandas as pd

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
    file_path = filedialog.askopenfilename(title=title, filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
    root.destroy()  # Close the Tkinter window
    return file_path

def load_file(file_path):
    """
    Load a CSV or Excel file into a DataFrame.
    
    Parameters:
        file_path (str): Path of the file to load.
        
    Returns:
        pandas.DataFrame: DataFrame containing the data from the file.
    """
    if not file_path:
        print("No file selected.")
        return None
    
    if file_path.endswith('.csv'):
        # Load CSV file into a DataFrame
        df = pd.read_csv(file_path)
        print("CSV DataFrame:")
    elif file_path.endswith('.xlsx'):
        # Load Excel file into a DataFrame
        df = pd.read_excel(file_path)
        print("Excel DataFrame:")
    else:
        print("Unsupported file format.")
        return None
    
    print(df)
    return df

def get_user_input(title, prompt):
    """
    Prompt the user for input using a dialog box.
    
    Parameters:
        title (str): Title of the dialog box.
        prompt (str): Prompt message for the user.
        
    Returns:
        str: User input.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    user_input = simpledialog.askstring(title, prompt)
    root.destroy()  # Close the Tkinter window
    return user_input

def get_columns_to_merge_on(title, prompt):
    """
    Prompt the user for a list of column names to merge on using a dialog box.
    
    Parameters:
        title (str): Title of the dialog box.
        prompt (str): Prompt message for the user.
        
    Returns:
        list: List of column names to merge on.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    user_input = simpledialog.askstring(title, prompt)
    root.destroy()  # Close the Tkinter window
    
    # Split the user input by commas and strip whitespace from each column name
    columns_to_merge_on = [column.strip() for column in user_input.split(',')]
    return columns_to_merge_on

def main():
    # Prompt the user to select a source file
    source_file_path = select_file_dialog("Select source file")

    # Load the selected source file
    source_df = load_file(source_file_path)

    # Prompt the user to select a target file
    target_file_path = select_file_dialog("Select target file")

    # Load the selected target file
    target_df = load_file(target_file_path)
    
    if source_df is not None and target_df is not None:
        # Prompt the user for the unique column
        unique_column = get_user_input("Unique Column", "Enter the name of the unique column:")

        # Prompt the user for the columns to merge on
        columns_to_merge_on = get_columns_to_merge_on("Columns to Merge On", "Enter column names separated by commas:")
        print(columns_to_merge_on)

        # Perform left join
        merged_df = pd.merge(target_df, source_df[columns_to_merge_on + [unique_column]], on=unique_column, how='left')

        # Save merged_df to a CSV file named target_file.csv
        merged_df.to_csv(target_file_path, index=False)

if __name__ == "__main__":
    main()