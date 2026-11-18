
import csv
from datetime import datetime
from pathlib import Path


# Путь к файлу истории
CSV_FILE = Path(__file__).resolve().parent / "data" / "history.csv"

# Поля CSV-файла
FIELDS = [
    "timestamp",
    "pid",
    "name",
    "process_key",
    "create_time",
    "cpu_percent",
    "memory_mb"
]


def save_history(processes):
    """Сохраняет измерения процессов в CSV."""

    CSV_FILE.parent.mkdir(parents=True, exist_ok=True)

    file_exists = CSV_FILE.exists() and CSV_FILE.stat().st_size > 0

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(
        CSV_FILE,
        "a",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        writer = csv.DictWriter(file, fieldnames=FIELDS)

        if not file_exists:
            writer.writeheader()

        for process in processes:
            writer.writerow({
                "timestamp": timestamp,
                "pid": process["pid"],
                "name": process["name"],
                "process_key": process["process_key"],
                "create_time": process["create_time"],
                "cpu_percent": process["cpu_percent"],
                "memory_mb": process["memory_mb"]
            })

    return len(processes)
