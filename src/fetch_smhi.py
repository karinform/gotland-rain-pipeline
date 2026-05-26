import requests
import pandas as pd

stations = {
    "Fårösund Ar A": 78550,
    "Visby Flygplats": 78400,
    "Östergarnsholm A": 78280,
    "Hoburg A": 68560
}

all_data = []

for station_name, station_id in stations.items():
    url = f"https://opendata-download-metobs.smhi.se/api/version/latest/parameter/7/station/{station_id}/period/latest-hour/data.json"

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Skipping {station_name} ({station_id}) - status {response.status_code}")
        continue

    data = response.json()

    for row in data["value"]:
        row["station_id"] = station_id
        row["station_name"] = station_name
        row["parameter"] = data["parameter"]["name"]
        row["unit"] = data["parameter"]["unit"]

        all_data.append(row)

df = pd.DataFrame(all_data)

df["date"] = pd.to_datetime(df["date"], unit="ms")
df["value"] = df["value"].astype(float)

print(df)

df.to_csv("gotland_rainfall.csv", index=False)

print("CSV file created: gotland_rainfall.csv")