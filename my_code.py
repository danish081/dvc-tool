import pandas as pd
import os

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

df.head()
# Create directory if it does not exist
os.makedirs("data", exist_ok=True)

# # Save CSV file inside the folder
file_path = os.path.join("data", "people.csv")
df.to_csv(file_path, index=False)

# print(f"File saved at: {file_path}")
