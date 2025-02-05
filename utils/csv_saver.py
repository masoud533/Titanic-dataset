import os 
import pandas as pd

def Save_csv(df,folder_path, base_filename):
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, f"{base_filename}.csv")

    couter = 1

    while os.path.exists(file_path):
        file_path = os.path.join(folder_path, f"{base_filename}_{couter}.csv")
        couter += 1
    
    df.to_csv(file_path,index=False)
    print(f"DataFrame saved frome: {file_path}")