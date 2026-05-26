from fetch import fetch_smhi_data
from save_raw import save_raw_json, upload_to_azure


def main():
    print("Fetching SMHI data...")
    data = fetch_smhi_data()

    print(f"Fetched {len(data)} rows.")

    print("Saving raw JSON...")
    file_path = save_raw_json(data)

    print(f"Raw data saved locally: {file_path}")

    print("Uploading to Azure Blob Storage...")
    upload_to_azure(file_path)

    print("Pipeline finished successfully!")


if __name__ == "__main__":
    main()