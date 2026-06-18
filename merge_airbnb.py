import pandas as pd
import os

folder = r"C:\Users\pkati\Documents\Coding\Portfolio Projects\Airbnb"

all_dfs = []

for filename in os.listdir(folder):
    if filename.endswith(".csv"):
        parts = filename.replace(".csv", "").split("_")
        city = parts[0]
        day_type = parts[1]  # weekdays or weekends

        filepath = os.path.join(folder, filename)
        df = pd.read_csv(filepath)
        df = df.rename(columns={"Unnamed: 0": "id"})

        df["city"] = city
        df["day_type"] = day_type

        all_dfs.append(df)
        print(f"Loaded {filename} → city={city}, day_type={day_type}, rows={len(df)}")

merged = pd.concat(all_dfs, ignore_index=True)

output_path = os.path.join(folder, "airbnb_europe_merged.csv")
merged.to_csv(output_path, index=False)

print(f"\nDone! {len(merged)} total rows saved to airbnb_europe_merged.csv")