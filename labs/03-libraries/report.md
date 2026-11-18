# ЛР 3. Библиотеки программы

Система: **Windows 10 x64 · MSVC 19.50 · Python 3.14 x64**

## Библиотеки файла

Программа напечатала: `libs.exe: sqrt(2) = 1.414214`

Команда для списка библиотек файла: `dumpbin /nologo /dependents libs.exe`

Библиотеки libs: `KERNEL32.dll`.

Почему в списке нет отдельной математической библиотеки: MSVC использует статическую компоновку необходимых компонентов математической библиотеки, поэтому отдельная DLL для `sqrt()` не отображается.

Где лежит интерпретатор Python: `C:\Users\Пользователь\AppData\Local\Programs\Python\Python314\python.exe`. Динамическая библиотека интерпретатора: `python314.dll`.

## Библиотеки процесса

PID Python: **13380**

Библиотек в процессе до `ctypes.CDLL`: **29**, после: **30**.

Загруженная библиотека: `winsqlite3.dll` (полный путь: `C:\Windows\System32\winsqlite3.dll`).

Функция `sqlite3_libversion()` вернула: **`b'3.53.4'`**.

Не получилось: первоначальный запуск `dumpbin` для Python.exe через cmd не сработал из-за кириллицы в пути. Повторный запуск через Python `subprocess` выполнился успешно.

## Снимки экрана

1. `screenshots/01_build_run.png` — сборка и запуск.
2. `screenshots/02_file_libraries.png` — библиотеки файла libs.
3. `screenshots/03_python_libraries.png` — библиотеки Python.
4. `screenshots/04_python_pid.png` — PID Python.
5. `screenshots/05_libraries_before.png` — библиотеки до ctypes.
6. `screenshots/06_library_loaded.png` — загрузка DLL и вызов функции.
7. `screenshots/07_libraries_after.png` — библиотеки после ctypes.
