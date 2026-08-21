# AI Trading Agent

AI-агент для поиска лидов, подбора китайских поставщиков и подготовки
коммерческих предложений для B2B-импорта в ОАЭ.

## Архитектура

Проект следует принципам Domain-Driven Design и слоистой (clean)
архитектуры:

- `app/domain` — сущности, агрегаты, value objects и доменные сервисы.
  Без зависимостей от внешнего мира.
- `app/application` — сценарии использования (use cases), интерфейсы
  портов (репозитории, LLM, поиск) и оркестрация агентов.
- `app/infrastructure` — реализации портов: LLM-клиент (Claude),
  веб-поиск, база данных, кэш, очереди сообщений, email.
- `app/presentation` — точки входа: HTTP API и CLI.

## Установка

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -e .
```

## Запуск

```powershell
python -m app.main
```

## Тесты

```powershell
pytest
```

## Документация

- `docs/architecture` — архитектура и модель предметной области.
- `docs/business` — рыночное исследование, лиды, поставщики, outreach.
- `docs/ai` — описание агентов, инструментов, промптов и guardrails.
