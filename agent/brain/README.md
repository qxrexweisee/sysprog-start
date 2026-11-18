# Мозг агента (Python)

`brain.py` загружает ядро через `ctypes`, по расписанию вызывает его функции и решает, что считать нарушением.
Первая версия появляется на паре 3. Какие файлы и в какой главе появляются здесь — в [`agent/README.md`](../README.md).

| Файл | Что в нём |
|---|---|
| `brain.py` | описание структуры `CoreInfo`, загрузка `sentry_core.dll`, вызов `core_get_info`, формирование JSON-события `agent_started` и отправка POST в n8n |

Для Windows сначала соберите библиотеку из папки `agent/core`:

```bat
cl /nologo /W4 /LD core_info.c /Fe:sentry_core.dll
```

Затем из папки `agent/brain` запустите:

```bat
python brain.py
```

Чтобы отправить сообщение в n8n, передайте URL вебхука:

```bat
python brain.py http://localhost:5678/webhook-test/agent
```

Для опубликованного сценария используйте боевой адрес без `-test`:

```bat
python brain.py http://localhost:5678/webhook/agent
```

Библиотека должна лежать в `agent/core` рядом с папкой `brain`. Файл библиотеки не коммитится — он собирается локально на каждом компьютере.
