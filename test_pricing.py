"""
Exercices Bloc 1 & 3 — voir J3_exercices_eleves.md.
Lancez : pytest test_pricing.py -v
"""
from booking import ticket_price, line_total, apply_promo, order_total
from pytest import raises

# À vous d'écrire les tests.

def test_ticket_price() :
    assert ticket_price("vip") == 7500
    assert ticket_price("standard") == 3500
    assert ticket_price("early_bird") == 2495

def test_ticket_price_bad_cat() :
    #throw if bad category
    with raises(ValueError) as e :
        ticket_price("gollum")
        assert "Catégorie de billet inconnue" in str(e)

def test_line_total() :

    assert line_total("early_bird", 2) == 2495*2
    assert line_total("vip", 10) == 7500*10
    assert line_total("standard", 1) == 3500*1

def test_line_total_bad_qty() :

    with raises(ValueError) as e :
        line_total("vip", -1)
        assert e is ValueError and"La quantité doit être strictement positive" in str(e)

def test_line_total_bad_qty2() :

    with raises(ValueError) as e :
        line_total("vip", 0)
        assert e is ValueError and"La quantité doit être strictement positive" in str(e)

def test_line_total_bad_cat() :

    with raises(ValueError) as e :
        ticket_price("gollum")
        assert e is ValueError and "Catégorie de billet inconnue" in str(e)

def test_apply_promo_invalid() :

    p_percentInvalid1 = {
        "percent_off": 0,
    }
    p_percentInvalid2 = {
        "percent_off": 101,
    }

    pr = {
        "code": str, 
        "percent_off": int, 
        "active": bool,
        "max_uses": int, 
        "used_count": int
    }

    with raises(ValueError) as e :
        apply_promo(100, p_percentInvalid1)
        assert e is ValueError and "remise invalide" in str(e)

    with raises(ValueError) as e :
        apply_promo(100, p_percentInvalid2)
        assert e is ValueError and "remise invalide" in str(e)


def test_apply_promo_inactive() :
    p_inactif = {
        "active": False,
    }
    with raises(ValueError) as e :
        apply_promo(100, p_inactif)
        assert e is ValueError and "Code promo inactif" in str(e)

def test_apply_promo_epuise() :
    p_epuise = {
        "max_uses": 10, 
        "used_count": 10
    }
    with raises(ValueError) as e :
        apply_promo(100, p_epuise)
        assert e is ValueError and "épuisé" in str(e)

def test_apply_promo_valids() :
    p_percentValid1 = {
        "percent_off": 50,
    }
    p_percentValid2 = {
        "percent_off": 100,
    }
    assert apply_promo(100, None) == 100
    assert apply_promo(100, p_percentValid1) == 100 - (100*.5)
    assert apply_promo(100, p_percentValid2) == 0

def test_order_total():
    orders = [{
        "category" : "vip",
        "quantity" : 6
    }]
    assert order_total(orders, None) == 7500 * 6