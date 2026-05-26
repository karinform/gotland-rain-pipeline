import json
from datetime import datetime
from pathlib import Path
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

load_dotenv()


def save_raw_json(data):
    raw_dir = Path("data/raw")
    raw_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = raw_dir / f"smhi_gotland_rainfall_raw_{timestamp}.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    return file_path


def upload_to_azure(local_file_path):
    connection_string = os.getenv("AZURE_CONNECTION_STRING")

    parts = dict(
        item.split("=", 1)
        for item in connection_string.split(";")
        if "=" in item
    )

    account_name = parts["AccountName"]
    account_key = parts["AccountKey"]

    account_url = f"https://{account_name}.blob.core.windows.net"

    blob_service_client = BlobServiceClient(
        account_url=account_url,
        credential=account_key
    )

    blob_client = blob_service_client.get_blob_client(
        container="raw",
        blob=Path(local_file_path).name
    )

    with open(local_file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

    print(f"Uploaded to Azure Blob Storage: {Path(local_file_path).name}")