import pandas as pd
import json

df = pd.read_csv(r"D:\Ishan\HackOn_ProCoder\Quiz app\Data\Countries.csv")


# Select required columns and drop missing values
df = df[['country_name', 'capital_city']].dropna()

# Convert to list of dictionaries
quiz_data = df.to_dict(orient="records")

# Save as JSON
with open("quiz_data.json", "w") as f:
    json.dump(quiz_data, f, indent=4)

print("Conversion successful! quiz_data.json created.")
