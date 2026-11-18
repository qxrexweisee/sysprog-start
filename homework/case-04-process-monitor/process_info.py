
import psutil
import time
from datetime import datetime


def get_processes():
    """Получает информацию о процессах и их экземплярах."""

    processes = []
    active_processes = []

    # Получаем процессы и подготавливаем измерение CPU
    for process in psutil.process_iter():
        try:
            process.cpu_percent(interval=None)
            active_processes.append(process)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Ждём для измерения загрузки процессора
    time.sleep(1)

    for process in active_processes:
        try:
            pid = process.pid
            name = process.name()
            create_time = process.create_time()

            memory = process.memory_info().rss / (1024 * 1024)
            cpu = process.cpu_percent(interval=None)

            process_data = {
                'pid': pid,
                'name': name,

                # Время создания используется для идентификации
                'create_time': create_time,

                # Уникальный идентификатор экземпляра
                'process_key': f"{pid}_{create_time:.6f}",

                'start_time': datetime.fromtimestamp(
                    create_time
                ).strftime('%Y-%m-%d %H:%M:%S'),

                'cpu_percent': cpu,
                'memory_mb': round(memory, 2)
            }

            processes.append(process_data)

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            continue

    return processes
