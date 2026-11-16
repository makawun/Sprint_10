import pytest

from data.taxi_texts import TaxiTexts


TAXI_TARIFF_CASES = [
    pytest.param(name, description, id=name)
    for name, description in TaxiTexts.TAXI_TARIFFS.items()
]

TAXI_TARIFF_MATCH_CASES = [
    pytest.param(
        "Рабочий", TaxiTexts.TAXI_TARIFFS["Рабочий"], id="Рабочий",
    ),
    pytest.param(
        "Сонный", TaxiTexts.TAXI_TARIFFS["Сонный"], id="Сонный",
        marks=pytest.mark.xfail(
            reason="Баг ROUTES-202a: у 'Сонного' в тултипе описание "
                   "от 'Разговорчивого' — 'Если мысли не выходят из головы'"
        ),
    ),
    pytest.param(
        "Отпускной", TaxiTexts.TAXI_TARIFFS["Отпускной"], id="Отпускной",
    ),
    pytest.param(
        "Разговорчивый", TaxiTexts.TAXI_TARIFFS["Разговорчивый"], id="Разговорчивый",
        marks=pytest.mark.xfail(
            reason="Баг ROUTES-202b: у 'Разговорчивого' в тултипе описание "
                   "от 'Сонного' — 'Для тех, кто не выспался'"
        ),
    ),
    pytest.param(
        "Утешительный", TaxiTexts.TAXI_TARIFFS["Утешительный"], id="Утешительный",
    ),
    pytest.param(
        "Глянцевый", TaxiTexts.TAXI_TARIFFS["Глянцевый"], id="Глянцевый",
    ),
]

TAXI_TARIFF_NAMES = [
    pytest.param(name, id=name) for name in TaxiTexts.TAXI_TARIFFS
]