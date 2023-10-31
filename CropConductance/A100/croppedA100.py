import os
import pandas as pd

# Define the folder path where your CSV files are located
folder_path = "C:/Users/anechyporenko/Desktop/Measurments/Huzze/Cropped Conductance/A100"

# Get a list of CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]

# Assuming 'Shimmer_D630_GSR_Skin_Conductance_CAL' is the column name
signal_name = 'Shimmer_D630_GSR_Skin_Conductance_CAL'
for csv_file in csv_files:
    # Construct the full path to the CSV file
    csv_path = os.path.join(folder_path, csv_file)

    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_path, delimiter='\t', skiprows=[0, 2])

    # Crop the data
    cropped_data = df[[signal_name]].iloc[:8000]

    # Create a subfolder named 'CropConductance' if it doesn't exist
    os.makedirs("CropConductance", exist_ok=True)

    # Construct the output file name
    output_filename = os.path.join("CropConductance", csv_file)

    # Save the cropped data to a new CSV file
    cropped_data.to_csv(output_filename, index=False)

    print(f"Saved cropped data for {csv_file} to {output_filename}")