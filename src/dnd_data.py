import requests
import pandas as pd

base = "https://www.dnd5eapi.co/api/2024"

class_response = requests.get(f"{base}/classes")
classes = class_response.json()["results"]

class_data = []
for c in classes:
    index = c["index"]
    resp = requests.get(f"{base}/classes/{index}")
    data = resp.json()

    class_data.append(data)

classes_df = pd.DataFrame(class_data)
print(classes_df.columns)

print(classes_df[['name', 'proficiency_choices']])