# Sprint_10
# Sprint_n — автотесты для сервиса «Яндекс.Маршруты»

Проект автотестов на **Python + Selenium + Pytest + Allure** для учебного сервиса
[«Яндекс.Маршруты»](https://qa-routes.education-services.ru/).

## 📋 Что проверяется

| Функциональность | Тестовый модуль |
|---|---|
| Отрисовка маршрута на карте | `tests/test_route_display.py` |
| Блок выбора маршрута и типы передвижения | `tests/test_route_selection_block.py` |
| Подготовка к заказу такси (тарифы, тултипы) | `tests/test_taxi_preparation.py` |
| Заказ тарифа Такси + полный флоу | `tests/test_taxi_order.py` |

## 🛠 Стек

- **Python 3.11+**
- **Selenium 4.x** (драйвер подтягивается автоматически через Selenium Manager)
- **Pytest 8.x**
- **Allure-pytest** — отчёты о прогоне
- **Google Chrome** (тесты запускаются в `--headless=new`)

## 📂 Структура проекта

```text
Sprint_n/
├── conftest.py             # фикстуры
├── helper.py               # вспомогательные функции
├── requirements.txt
├── README.md
├── data/                   # тестовые данные
│   ├── addresses.py        # адреса
│   ├── route_texts.py      # тексты блока маршрута
│   ├── taxi_texts.py       # тарифы и описания из ТЗ
│   ├── taxi_cases.py       # параметризация
│   └── urls.py             # URL сервиса
├── locators/               # локаторы по страницам
│   ├── added_address_page_locators.py
│   ├── confirm_order_page_locators.py
│   ├── main_page_locators.py
│   ├── taxi_page_locators.py
│   └── waiting_taxi_page_locators.py
├── pages/                  # Page Object
│   ├── base_page.py        # обёртки над Selenium API
│   ├── main_page.py        # главная: ввод адресов
│   ├── added_address_page.py  # блок маршрута
│   ├── taxi_page.py        # форма заказа такси
│   ├── waiting_taxi_page.py   # окно «Поиск машины»
│   └── confirm_order_page.py  # окно совершенного заказа
└── tests/                  # тесты
    ├── test_route_display.py
    ├── test_route_selection_block.py
    ├── test_taxi_preparation.py
    └── test_taxi_order.py
```



## 🧩 Особенности проекта

### `@pytest.mark.xfail` для известных багов
Помечается `xfail` с описанием и номером задачи:

