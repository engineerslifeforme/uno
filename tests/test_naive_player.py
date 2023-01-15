""" Tests for naive player """

from auto_uno.player import NaivePlayer
from auto_uno.cards import NumberCard, WildDrawFourCard, Color

def test_select_card():
    blue_one = NumberCard(number=1, color=Color.BLUE)
    player = NaivePlayer([blue_one])
    blue_two = NumberCard(number=2, color=Color.BLUE)
    assert(player.select_card(blue_two) == blue_one)
    assert(len(player.hand) == 0)

    player.hand.append(blue_one)
    green_two = NumberCard(number=2, color=Color.GREEN)
    assert(player.select_card(green_two) is None)

    wild = WildDrawFourCard()
    player.hand = [
        wild,
        blue_one,
    ]
    assert(player.select_card(blue_two) == blue_one)
    player.hand.append(blue_one)
    assert(player.select_card(green_two) == wild)
    assert(wild.color == Color.BLUE)