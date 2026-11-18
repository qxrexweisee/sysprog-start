
import time

from process_info import get_processes
from history import save_history


def run_monitor(interval=5):
    """Постоянный мониторинг процессов с отслеживанием их жизненного цикла."""

    print("=" * 65)
    print("             МОНИТОР ПРОЦЕССОВ ЗАПУЩЕН")
    print("=" * 65)

    print(f"Интервал измерения: {interval} секунд")
    print("Для остановки нажмите Ctrl+C")

    previous_processes = {}
    iteration = 0

    try:
        while True:
            iteration += 1

            print(f"\nИзмерение №{iteration}")

            processes = get_processes()
            current_processes = {
                p["process_key"]: p for p in processes
            }

            current_keys = set(current_processes)
            previous_keys = set(previous_processes)

            # Первый запуск: формируем начальный снимок
            if iteration == 1:
                print("Начальный снимок процессов получен.")

            else:
                # Новые экземпляры процессов
                started = current_keys - previous_keys

                # Завершившиеся экземпляры процессов
                stopped = previous_keys - current_keys

                for key in started:
                    p = current_processes[key]
                    print(
                        f"[НОВЫЙ ПРОЦЕСС] {p['name']} "
                        f"PID={p['pid']}"
                    )

                for key in stopped:
                    p = previous_processes[key]
                    print(
                        f"[ЗАВЕРШЕН] {p['name']} "
                        f"PID={p['pid']}"
                    )

            saved = save_history(processes)

            print(f"Обнаружено процессов: {len(processes)}")
            print(f"Сохранено записей: {saved}")

            top_processes = sorted(
                processes,
                key=lambda p: p["memory_mb"],
                reverse=True
            )[:5]

            print("\nТоп-5 процессов по RAM:")

            for p in top_processes:
                print(
                    f"{p['name']:<25} "
                    f"PID: {p['pid']:<7} "
                    f"RAM: {p['memory_mb']:.2f} MB"
                )

            previous_processes = current_processes

            print("-" * 65)
            time.sleep(interval)

    except KeyboardInterrupt:
        print("\nМониторинг остановлен.")
        print(f"Всего измерений: {iteration}")
        print("История сохранена в data/history.csv")


if __name__ == "__main__":
    run_monitor()
