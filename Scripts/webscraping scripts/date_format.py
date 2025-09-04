import os
import pandas as pd

# Replace 'C:/Users/siddh/OneDrive/Desktop/Dissertation/Scripts/files to be uploaded/Boots/PL' with the actual path to your folder
folder_path = 'C:/Users/siddh/OneDrive/Desktop/Dissertation/Scripts/files to be uploaded/Boots/PL'

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):  # Assuming the files are in CSV format
        file_path = os.path.join(folder_path, filename)

        # Extract the date from the filename using a different approach
        date_str = filename.split('_PL_Output_')[1].split('.')[0]

        # Assuming the date format is '%Y-%m-%d'
        date_format = '%Y-%m-%d'

        try:
            date = pd.to_datetime(date_str, format=date_format)

            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv(file_path)

            # Add a new 'Date' column after the 'Sponsored' column
            df.insert(df.columns.get_loc('Sponsored') + 1, 'Date', date)

            # Save the modified DataFrame back to the file
            df.to_csv(file_path, index=False)

            print(f"Processed {filename} and added the 'Date' column.")
        except ValueError:
            print(f"Skipping {filename} due to date extraction error.")
