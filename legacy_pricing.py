"""
legacy_pricing.py — code de tarification "hérité".

Vous n'avez pas écrit ce code : on vous demande de le TESTER. Sa spécification
est décrite dans chaque docstring. Votre travail de testeur : concevoir les cas
pertinents (valeurs nominales, limites, classes d'équivalence), écrire les tests,
les exécuter, et diagnostiquer tout écart entre le comportement observé et la
spécification.
"""


def loyalty_discount_percent(previous_orders):
    """Pourcentage de remise fidélité selon le nombre de commandes précédentes.

    Spécification :
    - 0 à 2 commandes       -> 0 %
    - 3 à 9 commandes       -> 5 %
    - 10 commandes ou plus  -> 10 %
    """
    if previous_orders < 3:
        return 0
    # elif previous_orders > 10:
    # fixed
    elif previous_orders >= 10:
        return 10
    else:
        return 5


def price_with_loyalty(base_cents, previous_orders):
    """Prix après remise fidélité, en centimes entiers (arrondi vers le bas).

    Utilise loyalty_discount_percent pour déterminer la remise.
    """
    percent = loyalty_discount_percent(previous_orders)
    discount = base_cents * percent // 100
    return base_cents - discount
