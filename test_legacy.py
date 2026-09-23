"""
Exercice Bloc 2 — Code hérité (voir énoncé).
Lisez la spécification dans legacy_pricing.py, concevez vos cas, écrivez vos
tests, lancez-les, et diagnostiquez tout écart avec la spécification.
Lancez : pytest test_legacy.py -v
"""
from legacy_pricing import loyalty_discount_percent, price_with_loyalty
from pytest import raises
# À vous d'écrire les tests.

def test_loyalty_discount_percent():
    assert loyalty_discount_percent(0) == 0

    assert loyalty_discount_percent(2) == 0
    assert loyalty_discount_percent(3) == 5
    assert loyalty_discount_percent(9) == 5
    assert loyalty_discount_percent(8) == 5

    # 10 commandes ou plus  -> 10 % 
    # -> inclusif
    assert loyalty_discount_percent(10) == 10 
    assert loyalty_discount_percent(11) == 10

    with raises(ValueError) as e :
        loyalty_discount_percent(-1)
        assert e is ValueError

def test_price_with_loyalty():
   
   assert price_with_loyalty(100, 2) == 100
   assert price_with_loyalty(100, 3) == 100-(100*.05)
   assert price_with_loyalty(100, 8) == 100-(100*.05)
   assert price_with_loyalty(100, 9) == 100-(100*.05)
   assert price_with_loyalty(100, 10) == 100-(100*.1)