import pandas as pd
import os

#create a sample dataframe with column names
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30,56],
        'City': ['New York', 'Los Angeles', 'Chicago']
        }
df = pd.DataFrame(data)

# Adding new row to df from v2

# new_row_loc = {'Name': 'v2', 'Age':'20', 'City':'city1'}
# df.loc[len(df.index)] = new_row_loc

# Adding new row to df from v3
# df = pd.DataFrame(data)
# new_row_loc2 = {'Name': 'v3', 'Age':'30', 'City':'city1'}
# df.loc[len(df.index)] = new_row_loc2


#Ensure the "data" directory exist at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)

print("SCV file saved to {file_path}")