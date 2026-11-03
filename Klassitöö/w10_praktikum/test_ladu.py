from ladu import hind_km_ga


def test_hind_22():
    assert hind_km_ga(10, 22) == 12.2


def test_hind_9():
    assert hind_km_ga(10, 9) == 10.9