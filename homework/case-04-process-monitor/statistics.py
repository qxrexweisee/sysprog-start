
import csv
from collections import defaultdict
from pathlib import Path


CSV_FILE = Path(__file__).resolve().parent / "data" / "history.csv"


def analyze_history():
    """Анализирует историю использования ресурсов."""

    if not CSV_FILE.exists():
        print("Файл истории не найден.")
        return

    processes = defaultdict(list)

    with open(CSV_FILE, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            processes[row["process_key"]].append(row)

    if not processes:
        print("История пуста.")
        return

    print("=" * 90)
    print("                  АНАЛИЗ ИСТОРИИ ПРОЦЕССОВ")
    print("=" * 90)

    print(f"Всего экземпляров процессов в истории: {len(processes)}")

    results = []

    for process_key, records in processes.items():
        records.sort(key=lambda r: r["timestamp"])

        first = records[0]
        last = records[-1]

        first_memory = float(first["memory_mb"])
        last_memory = float(last["memory_mb"])

        average_memory = sum(
            float(r["memory_mb"]) for r in records
        ) / len(records)

        average_cpu = sum(
            float(r["cpu_percent"]) for r in records
        ) / len(records)

        results.append({
            "name": last["name"],
            "pid": last["pid"],
            "key": process_key,
            "samples": len(records),
            "first_memory": first_memory,
            "last_memory": last_memory,
            "delta": last_memory - first_memory,
            "average_memory": average_memory,
            "average_cpu": average_cpu
        })

    # Сначала процессы с наибольшим увеличением RAM
    results.sort(key=lambda p: p["delta"], reverse=True)

    print("\nПРОЦЕССЫ С НАИБОЛЬШИМ РОСТОМ RAM:")
    print("-" * 90)

    for p in results[:20]:
        print(
            f"{p['name'][:22]:<23} "
            f"PID: {p['pid']:<7} "
            f"Измерений: {p['samples']:<5} "
            f"RAM: {p['first_memory']:.2f} -> "
            f"{p['last_memory']:.2f} MB "
            f"(+{p['delta']:.2f} MB)"
        )

    print("\nПРОЦЕССЫ С НЕСКОЛЬКИМИ ЭКЗЕМПЛЯРАМИ В ИСТОРИИ:")
    print("-" * 90)

    by_name = defaultdict(set)

    for p in results:
        by_name[p["name"]].add(p["key"])

    for name, instances in sorted(by_name.items()):
        if len(instances) > 1:
            print(f"{name}: {len(instances)} разных экземпляров")

    print("\nАНАЛИЗ ЗАВЕРШЁН.")


if __name__ == "__main__":
    analyze_history()
