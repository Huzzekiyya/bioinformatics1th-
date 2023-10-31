import os
import pandas as pd
import matplotlib.pyplot as plt

# Define the folder path where your CSV files are located
folder_path = r"C:\Users\anechyporenko\Desktop\Measurments\Huzze\PPG_IBI\Stress"


# Get a list of CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]

# Iterate through each CSV file and list all column names
for csv_file in csv_files:
    # Construct the full path to the CSV file
    csv_path = os.path.join(folder_path, csv_file)

    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_path, delimiter='\t', skiprows=[0, 2])

    # Print the list of column names
    print(f"Column names in {csv_file}:")
    for column_name in df.columns:
        print(column_name)


# Print the values in the "Shimmer__PPG_IBI_CAL" column
print("Values in 'Shimmer__PPG_IBI_CAL' column:")
print(df["Shimmer__PPG_IBI_CAL"])



# Assuming you have loaded your CSV into a DataFrame named df
# Extract the values from the "Shimmer__PPG_IBI_CAL" column
ibi_data = df["Shimmer__PPG_IBI_CAL"]

# Create a range of x-values (assuming a simple linear progression)
x_values = range(len(ibi_data))

# Plot the data
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.plot(x_values, ibi_data, label="Shimmer__PPG_IBI_CAL")
plt.xlabel("Sample Index")
plt.ylabel("Values")
plt.title("Shimmer__PPG_IBI_CAL Data")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
