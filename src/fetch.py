import requests


STATIONS = {
    "Fårösund Ar A": 78550,
    "Visby Flygplats": 78400,
    "Östergarnsholm A": 78280,
    "Hoburg A": 68560,
}


def fetch_smhi_data():
    all_data = []

    for station_name, station_id in STATIONS.items():
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

    return all_data