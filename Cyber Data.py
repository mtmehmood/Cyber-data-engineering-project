import pandas as pd

# Step 1: Load the datasets
server1_path = r"C:\Users\tahir\Documents\Mine\Mine New\Jaat\Jahanzeb\server1_dataset.csv"
server2_path = r"C:\Users\tahir\Documents\Mine\Mine New\Jaat\Jahanzeb\server2_dataset.csv"

df1 = pd.read_csv(server1_path)
df2 = pd.read_csv(server2_path)

# Step 2: Compare using email as the unique identifier
key_column = 'Email'

# Matching
matching = pd.merge(df1, df2, on=key_column, suffixes=('_Server1', '_Server2'))

# Records only in Server1
only_in_server1 = df1[~df1[key_column].isin(df2[key_column])]

# Records only in Server2
only_in_server2 = df2[~df2[key_column].isin(df1[key_column])]

# Step 3: Save the results (optional)
matching.to_csv("matching_records.csv", index=False)
only_in_server1.to_csv("only_in_server1.csv", index=False)
only_in_server2.to_csv("only_in_server2.csv", index=False)

# Step 4: Print preview
print("✅ Matching Records:")
print(matching[['Name_Server1', 'Email']])
print("\n❌ Only in Server1:")
print(only_in_server1[['Name', 'Email']])
print("\n❌ Only in Server2:")
print(only_in_server2[['Name', 'Email']])
