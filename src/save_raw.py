import json
from datetime import datetime
from pathlib import Path


def save_raw_json(data):
    raw_dir = Path("data/raw")
    raw_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = raw_dir / f"smhi_gotland_rainfall_raw_{timestamp}.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    return file_path