"""
Exercices Bloc 1 & 3 — voir J3_exercices_eleves.md.
Lancez : pytest test_pricing.py -v
"""
from booking import ticket_price, line_total, apply_promo, order_total

# À vous d'écrire les tests.

def test_ticket_price() :

    assert ticket_price("vip") == 7500
    assert ticket_price("standard") == 3500
    assert ticket_price("early_bird") == 2495

    # assert ticket_price("gollum") is ValueError