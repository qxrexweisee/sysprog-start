
import os
import time
import psutil

process = psutil.Process(os.getpid())
memory_blocks = []

STEP_MB = 10
STEPS = 15
INTERVAL = 5

print("=" * 50)
print("ТЕСТ ПОСТЕПЕННОГО РОСТА ПАМЯТИ")
print("=" * 50)
print(f"PID тестовой программы: {os.getpid()}")

try:
    for step in range(1, STEPS + 1):
        # Выделяем очередные 10 МБ
        block = bytearray(STEP_MB * 1024 * 1024)

        # Записываем данные в страницы памяти
        for i in range(0, len(block), 4096):
            block[i] = 1

        memory_blocks.append(block)

        ram = process.memory_info().rss / (1024 * 1024)

        print(
            f"Шаг {step}/{STEPS} | "
            f"Выделено: {step * STEP_MB} MB | "
            f"RAM процесса: {ram:.2f} MB"
        )

        time.sleep(INTERVAL)

    print("\nВыделение памяти завершено.")
    print("Удерживаем память ещё 20 секунд...")
    time.sleep(20)

except KeyboardInterrupt:
    print("\nТест остановлен пользователем.")

finally:
    memory_blocks.clear()
    print("Тест завершён.")
