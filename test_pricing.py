"""
Exercices Bloc 1 & 3 — voir J3_exercices_eleves.md.
Lancez : pytest test_pricing.py -v
"""
from booking import ticket_price, line_total, apply_promo, order_total
from booking import MAX_TICKETS_PER_ORDER
import pytest
from pytest import raises

# À vous d'écrire les tests.

def test_ticket_price() :
    assert ticket_price("vip") == 7500
    assert ticket_price("standard") == 3500
    assert ticket_price("early_bird") == 2495

def test_ticket_price_bad_cat() :
    #throw if bad category
    with raises(ValueError, match="Catégorie de billet inconnue") as e :
        ticket_price("gollum")


@pytest.mark.parametrize(
        "cat, qty, exp",
        [
            ("early_bird", 2, 2495*2),
            ("standard", 1, 3500*1), 
            ("vip", 10, 7500*10), 
        ]
)
def test_line_total(cat, qty, exp) :
    assert line_total(cat, qty) == exp
    # assert line_total("early_bird", 2) == 2495*2
    # assert line_total("vip", 10) == 7500*10
    # assert line_total("standard", 1) == 3500*1

def test_line_total_bad_qty() :
    with raises(ValueError, match="La quantité doit être strictement positive") as e :
        line_total("vip", -1)

def test_line_total_bad_qty2() :
    with raises(ValueError, match="La quantité doit être strictement positive") as e :
        line_total("vip", 0)

def test_line_total_bad_cat() :
    with raises(ValueError, match="Catégorie de billet inconnue") as e :
        ticket_price("gollum")

def test_apply_promo_invalid() :
    p_percentInvalid1 = {
        "active" : True,
        "max_uses": 10, 
        "used_count": 1,
        "percent_off": 0,
    }
    p_percentInvalid2 = {
        "active" : True,
        "max_uses": 10, 
        "used_count": 1,
        "percent_off": 101,
    }

    with raises(ValueError, match="remise invalide") :
        apply_promo(100, p_percentInvalid1)

    with raises(ValueError, match="remise invalide") :
        apply_promo(100, p_percentInvalid2)

def test_apply_promo_inactive() :
    p_inactif = {
        "active": False,
    }
    with raises(ValueError, match="promo inactif") :
        apply_promo(100, p_inactif)

def test_apply_promo_epuise() :
    p_epuise = {
        "active" : True,
        "max_uses": 10, 
        "used_count": 1,
        "percent_off": 0,
        "max_uses": 10, 
        "used_count": 10
    }
    with raises(ValueError, match="épuisé") :
        apply_promo(100, p_epuise)

def test_apply_promo_valids() :
    p_percentValid1 = {
        "active" : True,
        "max_uses": 10, 
        "used_count": 1,
        "percent_off": 50,
    }
    p_percentValid2 = {
        "active" : True,
        "max_uses": 10, 
        "used_count": 1,
        "percent_off": 100,
    }
    assert apply_promo(100, None) == 100
    assert apply_promo(100, p_percentValid1) == 100 - (100*.5)
    assert apply_promo(100, p_percentValid2) == 0

@pytest.mark.parametrize(
        "cat, qty, promo, exp, e, eMsg", 
        [
            ("vip", 1, None, 7500, None, ""),
            ("vip", 6, None, 7500*6, None, ""),
            ("vip", 0, None, 7500*6, ValueError, "au moins un billet"),
            ("vip", 7, None, 7500*6, ValueError, f"Maximum {MAX_TICKETS_PER_ORDER} billets par commande")
        ], 
        ids=["1 ticket","6 tickets", "no ticket","7 tickets!"]
)
def test_order_total_quantities(cat, qty, promo, exp, e, eMsg):
    orders = [{
        "category" : cat,
        "quantity" : qty
    }]

    if e is not None :
        with raises(e, match=eMsg):
            order_total(orders, promo)
    else :
        assert order_total(orders, promo) == exp

# def test_order_total_notickets():
#     orders = [{
#         "category" : "vip",
#         "quantity" : 0
#     }]
#     with raises(ValueError, match="au moins un billet") :
#         order_total(orders, None)

# def test_order_total_toomanytickets():
#     orders = [{
#         "category" : "vip",
#         "quantity" : 7
#     }]
#     with raises(ValueError, match=f"Maximum {MAX_TICKETS_PER_ORDER} billets par commande") :
#         order_total(orders, None)
