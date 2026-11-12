from copy import deepcopy

import pytest

from src.order_report import build_order_report


@pytest.mark.parametrize(
    "items, quantity, total",
    [
        ([], 0, 0),
        ([{"price": 100, "quantity": 2}], 2, 400),
        ([{"price": 999, "quantity": 1}], 1, 1199),
        ([{"price": 1000, "quantity": 1}], 1, 1100),
        ([{"price": 1100, "quantity": 1}], 1, 1190),
        ([{"price": 1200, "quantity": 1}], 1, 1080),
        ([{"price": 300, "quantity": 2},
          {"price": 500, "quantity": 1}], 3, 1190),
        ([{"price": 5000, "quantity": 1,
           "active": False}], 0, 0),
        ([{"price": 500, "quantity": 0}], 0, 0),
    ],
)
def test_build_order_report_totals(items, quantity, total):
    report = build_order_report(items)
    assert report["quantity"] == quantity
    assert report["total"] == total


def test_build_order_report_text():
    items = [{"price": 100, "quantity": 2}]
    assert build_order_report(items) == {
        "quantity": 2,
        "total": 400,
        "text": "Гость: 2 шт.; к оплате 400.00",
    }


def test_build_order_report_preserves_input():
    items = [{"price": 100, "quantity": 2}]
    original = deepcopy(items)
    build_order_report(items)
    assert items == original


def test_build_order_report_keyword_arguments():
    report = build_order_report(items=[], customer_name="Анна")
    assert report["text"] == "Анна: 0 шт.; к оплате 0.00"
