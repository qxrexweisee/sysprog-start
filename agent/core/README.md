# Ядро агента (C)

Ядро собирается в динамическую библиотеку: `sentry_core.dll` в Windows, `libsentry_core.dylib` в macOS,
`libsentry_core.so` в Linux. Первая функция появляется на паре 2. Какие файлы и в какой главе появляются здесь — в [`agent/README.md`](../README.md).

| Файл | Что в нём |
|---|---|
| `core.h` | структура `core_info` и объявление экспортируемой функции `core_get_info` |
| `core_info.c` | получение PID, числа процессоров, размера страницы памяти и имени компьютера |
| `show_info.c` | проверочная программа: вызывает `core_get_info` и печатает поля структуры |

Сборка и проверка в Windows из этой папки (x64 Native Tools Command Prompt):

```bat
cl /nologo /W4 show_info.c core_info.c && show_info.exe
```

Сборка динамической библиотеки для Python (глава 1.2):

```bat
cl /nologo /W4 /LD core_info.c /Fe:sentry_core.dll
```

Собранные `.exe`, `.obj`, `.dll`, `.lib` и `.exp` в репозиторий не добавляются: они создаются локально из исходников.
