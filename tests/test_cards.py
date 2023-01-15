""" Test Card behaviors """

from auto_uno.cards import (
    NumberCard,
    ReverseCard,
    SkipCard,
    DrawTwoCard,
    WildCard,
    WildDrawFourCard,
    Color,
)

def test_allowed():
    number_card = NumberCard(number=1, color=Color.BLUE)
    assert(number_card.allowed(NumberCard(number=1, color=Color.GREEN)))
    assert(number_card.allowed(NumberCard(number=2, color=Color.BLUE)))
    for CardType in [ReverseCard, SkipCard, DrawTwoCard]:
        assert(number_card.allowed(CardType(color=Color.BLUE)))
    
    for WildCardType in [WildCard, WildDrawFourCard]:
        wild_card = WildCardType()
        wild_card.color = Color.BLUE
        assert(number_card.allowed(wild_card))