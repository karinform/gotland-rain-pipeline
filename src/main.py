from fetch import fetch_smhi_data
from save_raw import save_raw_json


def main():
    print("Fetching SMHI data...")
    data = fetch_smhi_data()

    print(f"Fetched {len(data)} rows.")

    print("Saving raw JSON...")
    file_path = save_raw_json(data)

    print(f"Done. Raw data saved to: {file_path}")


if __name__ == "__main__":
    main()